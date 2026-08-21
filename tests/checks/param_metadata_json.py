"""Validation of consortium-specific RO-Crate metadata conventions."""

from collections import Counter

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
        log = ''
        nodes = [node for node in graph if node.get('@id') == nodeID]
        if len(nodes) != 1:
            log += f'**ERROR: all entries must only occur once in crate. check: {nodeID}\n'
            return False, log
        node = nodes[0]
        if '@type' not in node:
            log += f'**ERROR: all nodes must have @type. check: {nodeID}\n'
            return False, log

        nodeTypes = node['@type']
        if isinstance(nodeTypes, str):
            nodeTypes = [nodeTypes]
        elif not isinstance(nodeTypes, list):
            nodeTypes = []
        if 'Dataset' in nodeTypes:
            for key in self.DATASET_MANDATORY:
                if key not in node:
                    log += f'**ERROR in dataset: "{key}" not in @id={node["@id"]}\n'
                    success = False
            for key in self.DATASET_SUGGESTED:
                if key not in node and self.OUTPUT_INFO:
                    log += f'**INFO for dataset: "{key}" not in @id={node["@id"]}\n'
        elif 'File' in nodeTypes:
            for key in self.FILE_MANDATORY:
                if key not in node:
                    log += f'**ERROR in file: "{key}" not in @id={node["@id"]}\n'
                    success = False
            for key in self.FILE_SUGGESTED:
                if key not in node and self.OUTPUT_INFO:
                    log += f'**INFO for file: "{key}" not in @id={node["@id"]}\n'
        if any(not str(value).strip() for value in node.values()):
            log += f'**WARNING: {nodeID} contains empty values in the key-value pairs\n'
        if isinstance(node.get('keywords', ''), list):
            log += f'**ERROR: {nodeID} contains an array of keywords. Use comma or space separated string\n'
            success = False
        for child in node.get('hasPart', []):
            childSuccess, childLog = self.processNode(graph, child['@id'])
            success = childSuccess and success
            log += childLog
        return success, log

    def check(self, _elnFile):
        graph = self.metadataJson['@graph']
        log = ''
        success = True
        if not isinstance(graph, list):
            return False, '**ERROR: RO-Crate metadata @graph must be an array\n'
        if not all(
            isinstance(node, dict)
            and isinstance(node.get('@id'), str)
            and (
                isinstance(node.get('@type'), str)
                or (
                    isinstance(node.get('@type'), list)
                    and node['@type']
                    and all(isinstance(nodeType, str) for nodeType in node['@type'])
                )
            )
            for node in graph
        ):
            return False, '**ERROR: RO-Crate metadata contains an invalid graph node\n'

        nodeIDs = [node['@id'] for node in graph]
        duplicateNodeIDs = [nodeID for nodeID, count in Counter(nodeIDs).items() if count > 1]
        if duplicateNodeIDs:
            duplicates = ', '.join(repr(nodeID) for nodeID in duplicateNodeIDs)
            return False, f'**ERROR: RO-Crate metadata contains duplicate node IDs: {duplicates}\n'

        metadataNodes = [node for node in graph if node['@id'].endswith(METADATA_FILE)]
        rootNodes = [node for node in graph if node['@id'] == './']
        if len(metadataNodes) != 1 or len(rootNodes) != 1:
            return False, '**ERROR: RO-Crate metadata descriptor or root node is missing or ambiguous\n'

        for node in graph:
            children = node.get('hasPart', [])
            if not isinstance(children, list) or any(
                not isinstance(child, dict)
                or not isinstance(child.get('@id'), str)
                or child['@id'] not in nodeIDs
                for child in children
            ):
                return False, f'**ERROR: RO-Crate node {node["@id"]} has invalid hasPart references\n'

        publisher = metadataNodes[0].get('sdPublisher')
        if publisher is not None and (
            not isinstance(publisher, dict)
            or ('name' not in publisher and publisher.get('@id') not in nodeIDs)
        ):
            return False, '**ERROR: RO-Crate publisher metadata is invalid\n'

        roCrateNodes = [node for node in graph if node['@id'] == METADATA_FILE]
        if len(roCrateNodes) == 1:
            for key in self.ROCRATE_NOTE_MANDATORY:
                if key not in roCrateNodes[0]:
                    log += f'**ERROR: "{key}" not in @id={METADATA_FILE}\n'
                    success = False
        else:
            log += f'**ERROR: @id={METADATA_FILE} does not uniquely exist\n'
            success = False

        mainNode = rootNodes[0]
        if 'hasPart' not in mainNode:
            return False, '**ERROR: RO-Crate root node requires hasPart\n'
        for part in mainNode['hasPart']:
            nodeSuccess, nodeLog = self.processNode(graph, part['@id'])
            success = nodeSuccess and success
            log += nodeLog

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
