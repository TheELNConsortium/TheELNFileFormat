#!/usr/bin/env python3
""" Validate ro-crate-metadata.json """
import traceback
import json
import shutil
import argparse
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import Path as ZPath
from zipfile import ZipFile
import networkx as nx
import matplotlib.pyplot as plt
from rocrate.rocrate import ROCrate
from rocrate.model.entity import Entity
from rocrate.model.contextentity import ContextEntity

METADATA_FILE = 'ro-crate-metadata.json'


def process_part(part):
    """
    recursive function call to process this node

    Args:
      part: part in graph
    """
    # find next node to process
    if '@id' not in part:
        print('**ERROR: @id is not in node: ',part)
    new_node = [ i for i in graph if '@id' in i and i['@id'] == part['@id'] ]
    if len(new_node) != 1:
        print('**ERROR: all entries in hasPart should only occur once in crate. see:',part['@id'])
    else:
        if args.verbose:
            print('..',part['@id']+'  items: ' + str(len(new_node[0]) - 1))
        subparts = new_node[0].pop('hasPart') if 'hasPart' in new_node[0] else []
        if len(subparts) > 0:  # don't do if no subparts: measurements, ...
            for subpart in subparts:
                process_part(subpart)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(usage="eln2md.py [-d directory] [-v]")
    argparser.add_argument('-d','--directory',
        help='directory path to use for parsing; defaults to .',
        default='.')
    argparser.add_argument('-v', '--verbose', help='verbose output', action='store_true')
    argparser.add_argument('-l','--layout',
        help='create png-image with this layout. No output if None. Valid layouts: circular, '+\
             'kamada_kawai, random, spectral, spring, shell',
        default=None)
    args = argparser.parse_args()
    cwd = Path(args.directory)
    for fileName in cwd.glob('*.eln'):
        print(f'{fileName.name}')
        with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
            p = ZPath(elnFile)
            dirName = sorted(p.iterdir())[0]
            ## Part 1: https://pypi.org/project/rocrate/
            try:
                dirpath = Path(tempfile.mkdtemp())
                elnFile.extractall(dirpath)
                temppath= dirpath.joinpath(dirName.name)
                crate = ROCrate(temppath)
                g = nx.DiGraph()
                if args.verbose:
                    print('\nList content according to https://pypi.org/project/rocrate/')
                for e in crate.get_entities():
                    if args.verbose:
                        print(e.id, e.type)
                    parts = e.get("hasPart")
                    if not parts:
                        continue
                    if not isinstance(parts, list):
                        parts = [parts]
                    #https://github.com/ResearchObject/ro-crate-py/issues/131#issuecomment-1179064351
                    local = isinstance(e, ContextEntity)
                    for p in parts:
                        if isinstance(p, Entity):
                            g.add_edge(e.id[1:] if local else e.id, \
                                p.id)
                        elif isinstance(p, str):
                            g.add_edge(e.id[1:] if local else e.id,\
                                 p)
                if isinstance(args.layout, str):
                    if args.layout in ['circular', 'kamada_kawai', 'random', 'spectral', 'spring', 'shell']:
                        pos = getattr(nx, args.layout+'_layout')(g)
                        # pos = nx.circular_layout(g)
                        nx.draw(g, pos=pos)
                        nx.draw_networkx_labels(g, pos=pos, font_size=8)
                        plt.savefig(fileName.parent.joinpath(fileName.stem+'.png'))
                shutil.rmtree(dirpath)
            except:
                print("**ERROR: Could not parse content\n"+traceback.format_exc()+'\n\n')
            ## Part 2: Custom .eln validation
            if args.verbose:
                print('\nOutput due to custom validation')
            metadataJsonFile = dirName.joinpath(METADATA_FILE)
            metadataContent = json.loads(metadataJsonFile.read_bytes())
            graph = metadataContent["@graph"]
            # find information from master node
            ro_crate_node = [i for i in graph if i["@id"] == METADATA_FILE][0]
            if not 'sdPublisher' in ro_crate_node or not 'name' in ro_crate_node['sdPublisher']:
                print('**ERROR: sdPublisher is not fully defined.')
            if not 'version' in ro_crate_node:
                print('**ERROR: version is not fully defined.')
            main_node = [i for i in graph if i["@id"] == "./"][0]
            # iteratively go through list
            for partI in main_node['hasPart']:
                process_part(partI)
