#!/usr/bin/env python3
import json
import shutil
import sys
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
        if item['@id'] in ['ro-crate-metadata.json', './']:
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
    rocrateNode = [i for i in graph if i["@id"] == "ro-crate-metadata.json"][0]
    output = 'ro-crate-metadata.json\n'
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
        )  # TODO_P2 first child should get elnName and version
    return output


if __name__ == '__main__':
    cwd = Path('.')
    readme = cwd.joinpath(README_FILE)
    # start by deleting the old one so we don't append to it
    readme.unlink(missing_ok=True)
    # copy the template (header) if it exists
    if cwd.joinpath(TEMPLATE_FILE).is_file():
        shutil.copy(TEMPLATE_FILE, README_FILE)

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
                if len(sys.argv) > 1 and sys.argv[1] == 'simple':
                    output = simplify(metadata)
                elif len(sys.argv) > 1 and sys.argv[1] == 'tree':
                    output = tree(metadata)
                else:
                    output = json.dumps(metadata, indent=2)
                outfile.write(f'```\n {output}\n```\n')
    outfile.close()
