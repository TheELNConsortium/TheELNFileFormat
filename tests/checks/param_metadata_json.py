"""Validation of consortium-specific RO-Crate metadata conventions."""

from .base import BaseCheck, METADATA_FILE


class CheckParamMetadataJson(BaseCheck):
    """Check consortium-specific metadata conventions."""

    label = 'Parameters metadata json'
    loggingLabel = 'params_metadata_json'
    requiresRootDirectory = True
    requiresMetadataJson = True
    ROCRATE_NOTE_MANDATORY = ['version', 'sdPublisher']
    DATASET_MANDATORY = ['name']
    DATASET_SUGGESTED = [
        'author', 'mentions', 'dateCreated', 'dateModified', 'identifier',
        'text', 'keywords',
    ]
    FILE_MANDATORY = ['name']
    FILE_SUGGESTED = ['sha256', 'encodingFormat', 'contentSize', 'description']
    OUTPUT_INFO = False
    OUTPUT_COUNTS = False

    def processNode(self, graph, nodeID):
        """Recursively validate one node and its ``hasPart`` children."""
        success = True
        nodes = [node for node in graph if node.get('@id') == nodeID]
        if len(nodes) != 1:
            print('**ERROR: all entries must only occur once in crate. check:', nodeID)
            return False
        node = nodes[0]
        if '@type' not in node:
            print('**ERROR: all nodes must have @type. check:', nodeID)
            return False

        nodeTypes = node['@type']
        if isinstance(nodeTypes, str):
            nodeTypes = [nodeTypes]
        elif not isinstance(nodeTypes, list):
            nodeTypes = []
        if 'Dataset' in nodeTypes:
            for key in self.DATASET_MANDATORY:
                if key not in node:
                    print(f'**ERROR in dataset: "{key}" not in @id={node["@id"]}')
                    success = False
            for key in self.DATASET_SUGGESTED:
                if key not in node and self.OUTPUT_INFO:
                    print(f'**INFO for dataset: "{key}" not in @id={node["@id"]}')
        elif 'File' in nodeTypes:
            for key in self.FILE_MANDATORY:
                if key not in node:
                    print(f'**ERROR in file: "{key}" not in @id={node["@id"]}')
                    success = False
            for key in self.FILE_SUGGESTED:
                if key not in node and self.OUTPUT_INFO:
                    print(f'**INFO for file: "{key}" not in @id={node["@id"]}')
        if any(not str(value).strip() for value in node.values()):
            print(f'**WARNING: {nodeID} contains empty values in the key-value pairs')
        if isinstance(node.get('keywords', ''), list):
            print(f'**ERROR: {nodeID} contains an array of keywords. Use comma or space separated string')
            success = False
        for child in node.get('hasPart', []):
            success = self.processNode(graph, child['@id']) and success
        return success

    def check(self, _elnFile):
        graph = self.metadataJson['@graph']
        log = ''
        success = True

        roCrateNodes = [node for node in graph if node['@id'] == METADATA_FILE]
        if len(roCrateNodes) == 1:
            for key in self.ROCRATE_NOTE_MANDATORY:
                if key not in roCrateNodes[0]:
                    log += f'**ERROR: "{key}" not in @id={METADATA_FILE}'
                    success = False
        else:
            log += f'**ERROR: @id={METADATA_FILE} does not uniquely exist '
            success = False

        mainNode = [node for node in graph if node['@id'] == './'][0]
        for part in mainNode['hasPart']:
            success = self.processNode(graph, part['@id']) and success

        if self.OUTPUT_COUNTS:
            knownKeys = (
                self.DATASET_MANDATORY + self.DATASET_SUGGESTED
                + self.FILE_MANDATORY + self.FILE_SUGGESTED + ['@id', '@type']
            )
            counts = {}
            for node in graph:
                if node['@id'] not in ['./', METADATA_FILE]:
                    for key in node:
                        counts[key] = counts.get(key, 0) + 1
            log += '===== Counts (* unspecified)'
            for count, key in sorted((value, key) for key, value in counts.items()):
                prefix = '   ' if key in knownKeys else ' * '
                log += f'{prefix}{key:15}: {count}'
        return success, log
