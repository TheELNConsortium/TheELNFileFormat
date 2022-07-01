#!/usr/bin/env python3
import json
import shutil
import sys
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import Path as ZPath
from zipfile import ZipFile

README_FILE = 'README.md'
TEMPLATE_FILE = 'README_template.md'
METADATA_FILE = 'ro-crate-metadata.json'


def simplify(metadata):
    """
    simplify metadata by removing everything except @id, @type, hasPart
    """
    for item in metadata['@graph']:
        if item['@id'] in [METADATA_FILE, './']:
            continue
        for subitem in [i for i in item]:
            if subitem not in ['@id', '@type', 'hasPart']:
                del item[subitem]
    return json.dumps(metadata, indent=2)


def tree(metadata):
    def processPart(part, level):
        """
        recursive function call to process this node
        """
        prefix = '    ' * (level - 1) + '|-> '
        output = prefix + part['@id']
        # find next node to process
        newNode = [
            i for i in metadata['@graph'] if '@id' in i and i['@id'] == part['@id']
        ]
        if len(newNode) == 1:
            output += (
                ',  items: ' + str(len(newNode[0]) - 1) + ' \n'
            )  # -1 because @id is not counted
            subparts = newNode[0].pop('hasPart') if 'hasPart' in newNode[0] else []
            if len(subparts) > 0:  # don't do if no subparts: measurements, ...
                for subpart in subparts:
                    output += processPart(subpart, level + 1)
        else:
            output += (
                ',  items: ' + str(len(part) - 1) + '\n'
            )  # -1 because @id is not counted
        return output

    # main tree-function
    graph = metadata["@graph"]
    # find information from master node
    rocrateNode = [i for i in graph if i["@id"] == METADATA_FILE][0]
    output = METADATA_FILE+'\n'
    if 'sdPublisher' in rocrateNode:
        output += '  publisher: ' + rocrateNode['sdPublisher']['name'] + '\n'
    if 'version' in rocrateNode:
        output += '  version: ' + rocrateNode['version'] + '\n'
    mainNode = [i for i in graph if i["@id"] == "./"][0]
    output += './\n'
    # iteratively go through list
    for part in mainNode['hasPart']:
        output += processPart(
            part, 1
        )
    return output


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(usage='''
eln2md.py [-d directory] [-f format]

with:
    -d --directory: directory path to use for parsing; defaults to '.'
    -f --format   : output format, possible choices 'full', 'short', 'tree'; defaults to 'full'
''')
    argparser.add_argument('-d','--directory', help='directory path to use for parsing', default='.')
    argparser.add_argument('-f','--format',    help='output format, possible choices "full", "short", "tree"', default='full')
    args = argparser.parse_args()

    cwd = Path(args.directory)
    readme = cwd.joinpath(README_FILE)
    # start by deleting the old one so we don't append to it
    readme.unlink(missing_ok=True)
    # copy the template (header) if it exists
    if cwd.joinpath(TEMPLATE_FILE).is_file():
        shutil.copy(cwd.joinpath(TEMPLATE_FILE), cwd.joinpath(README_FILE))

    outfile = readme.open('a')

    for fileName in cwd.glob('*.eln'):
        outfile.write(f'\n### {fileName}\n')
        with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
            # use the exposed Path from ziplib
            p = ZPath(elnFile)
            # there should be only one folder so we just consider the first one
            dirName = sorted(p.iterdir())[0]
            metadataJsonFile = dirName.joinpath(METADATA_FILE)
            if metadataJsonFile.is_file():
                print(f'Found metadata file: {metadataJsonFile}')
                metadata = json.loads(metadataJsonFile.read_bytes())
                if args.format == 'full':
                    output = json.dumps(metadata, indent=2)
                elif args.format == 'short':
                    output = simplify(metadata)
                elif args.format == 'tree':
                    output = tree(metadata)
                else:
                    print("**ERROR: unknown format")
                outfile.write(f'```\n {output}\n```\n')
    outfile.close()
