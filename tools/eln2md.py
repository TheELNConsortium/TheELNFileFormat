#!/usr/bin/env python3
""" Append ro-crate-metadata.json to end of README.md """
import json
import shutil
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
        for subitem in [i for i in item]: # pylint: disable=unnecessary-comprehension
            if subitem not in ['@id', '@type', 'hasPart']:
                del item[subitem]
    return json.dumps(metadata, indent=2)


def tree(metadata):
    """
    use metadata to create hierarchical tree struction in ascii
    """
    def process_part(part, level):
        """
        recursive function call to process this node
        """
        prefix = '    ' * (level - 1) + '|-> '
        output = prefix + part['@id']
        # find next node to process
        new_node = [
            i for i in metadata['@graph'] if '@id' in i and i['@id'] == part['@id']
        ]
        if len(new_node) == 1:
            output += (
                ',  items: ' + str(len(new_node[0]) - 1) + ' \n'
            )  # -1 because @id is not counted
            subparts = new_node[0].pop('hasPart') if 'hasPart' in new_node[0] else []
            if len(subparts) > 0:  # don't do if no subparts: measurements, ...
                for subpart in subparts:
                    output += process_part(subpart, level + 1)
        else:
            output += (
                ',  items: ' + str(len(part) - 1) + '\n'
            )  # -1 because @id is not counted
        return output

    # main tree-function
    graph = metadata["@graph"]
    # find information from master node
    ro_crate_node = [i for i in graph if i["@id"] == METADATA_FILE][0]
    output = METADATA_FILE+'\n'
    if 'sdPublisher' in ro_crate_node:
        output += '  publisher: ' + ro_crate_node['sdPublisher']['name'] + '\n'
    if 'version' in ro_crate_node:
        output += '  version: ' + ro_crate_node['version'] + '\n'
    main_node = [i for i in graph if i["@id"] == "./"][0]
    output += './\n'
    # iteratively go through list
    for part in main_node['hasPart']:
        output += process_part(
            part, 1
        )
    return output


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(usage="eln2md.py [-d directory] [-f format]")
    argparser.add_argument('-d','--directory',
        help='directory path to use for parsing; defaults to .',
        default='.')
    argparser.add_argument('-f','--format',
        help='output format: "full", "short", "tree"; defaults to full',
        default='full')
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
                metadataContent = json.loads(metadataJsonFile.read_bytes())
                if args.format == 'full':
                    outputString = json.dumps(metadataContent, indent=2)
                elif args.format == 'short':
                    outputString = simplify(metadataContent)
                elif args.format == 'tree':
                    outputString = tree(metadataContent)
                else:
                    print("**ERROR: unknown format")
                outfile.write(f'```json\n {outputString}\n```\n')
    outfile.close()
