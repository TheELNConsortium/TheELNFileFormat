#!/usr/bin/python3
""" Validate if rocrate of pypi can open and parse it https://pypi.org/project/rocrate/ """
import os
import json
import unittest
from zipfile import ZIP_DEFLATED
from zipfile import Path as ZPath
from zipfile import ZipFile

class Test_2(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        # global variables worth discussion
        ROCRATE_NOTE_MANDATORY = ['version','sdPublisher']
        DATASET_MANDATORY = ['name', 'dateCreated', 'dateModified', 'identifier', 'text', 'keywords']
        DATASET_INFO = ['author','mentions']
        FILE_MANDATORY = ['name']
        FILE_INFO = ['sha256', 'encodingFormat', 'contentSize', 'description']

        # runtime global variables
        METADATA_FILE = 'ro-crate-metadata.json'
        OUTPUT_INFO = True
        OUTPUT_COUNTS = True

        globalSuccess = 0
        def processNode(graph, nodeID):
            """
            recursive function call to process each node

            Args:
              graph: full graph
              nodeID: id of node in graph
            """
            nodes = [ i for i in graph if '@id' in i and i['@id'] == nodeID]
            if len(nodes)!=1:
                print('**ERROR: all entries must only occur once in crate. check:', nodeID)
                return
            node = nodes[0]
            global globalSuccess
            if '@type' not in node:
                print('**ERROR: all nodes must have @type. check:', nodeID)
            if node['@type'] == 'Dataset':
                for key in DATASET_MANDATORY:
                    if not key in node:
                        print(f'**ERROR in dataset: "{key}" not in @id={node["@id"]}')
                        globalSuccess = 1
                for key in DATASET_INFO:
                    if not key in node and OUTPUT_INFO:
                        print(f'**INFO for dataset: "{key}" not in @id={node["@id"]}')
            elif node['@type'] == 'File':
                for key in FILE_MANDATORY:
                    if not key in node:
                        print(f'**ERROR in file: "{key}" not in @id={node["@id"]}')
                        globalSuccess = 1
                for key in FILE_INFO:
                    if not key in node and OUTPUT_INFO:
                        print(f'**INFO for file: "{key}" not in @id={node["@id"]}')
            children = node.pop('hasPart') if 'hasPart' in node else []
            for child in children:
                processNode(graph, child['@id'])
            return

        for root, _, files in os.walk(".", topdown=False):
            for name in files:
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nParse: {fileName}')
                with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                    p = ZPath(elnFile)
                    dirName = sorted(p.iterdir())[0]
                    metadataJsonFile = dirName.joinpath(METADATA_FILE)
                    metadataContent = json.loads(metadataJsonFile.read_bytes())
                    graph = metadataContent["@graph"]
                    # find information from master node
                    ro_crate_nodes = [i for i in graph if i["@id"] == METADATA_FILE]
                    if len(ro_crate_nodes) == 1:
                        for key in ROCRATE_NOTE_MANDATORY:
                            if not key in ro_crate_nodes[0]:
                                print(f'**ERROR: "{key}" not in @id={METADATA_FILE}')
                    else:
                        print(f'**ERROR: @id={METADATA_FILE} does not uniquely exist ')
                    main_node = [i for i in graph if i["@id"] == "./"][0]

                    # iteratively go through graph
                    for partI in main_node['hasPart']:
                        processNode(graph, partI['@id'])

                    # count occurances of all keys
                    counts = {}
                    for node in graph:
                        if node['@id'] in ['./',METADATA_FILE]:
                            continue
                        for key in node.keys():
                            if key in counts:
                                counts[key] += 1
                            else:
                                counts[key] = 1

                    view = [ (v,k) for k,v in counts.items() ]
                    view.sort(reverse=True)
                    if OUTPUT_COUNTS:
                        print('===== Counts ======')
                        for v,k in view:
                            print(f'  {k:15}: {v}')
        print('\n\nSuccess:', globalSuccess)
        return globalSuccess
