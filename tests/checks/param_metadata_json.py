"""Validation of consortium-specific RO-Crate metadata conventions."""

import re
from collections import Counter
from urllib.parse import unquote, urlparse

from .base import BaseCheck, METADATA_FILE


class CheckParamMetadataJson(BaseCheck):
    """Check consortium-specific metadata conventions."""

    label = 'Parameters metadata json'
    loggingLabel = 'params_metadata_json'
    requiresRootDirectory = True
    requiresMetadataJson = True
    versions = ('1.2+20260923',)
    ROCRATE_NODE_SUGGESTED = ['version', 'sdPublisher']
    DATASET_SUGGESTED = ['author', 'mentions', 'dateCreated', 'dateModified', 'identifier',
                         'text', 'keywords',]
    FILE_SUGGESTED = ['sha256', 'encodingFormat', 'contentSize', 'description']
    NO_TEXT_TYPES = {'Person', 'Organization', 'PropertyValue'}

    def processNode(self, nodesByID, nodeID):
        """Recursively validate one node and its ``hasPart`` children."""
        success = True
        log = ''
        node = nodesByID[nodeID]

        nodeTypes = node['@type']
        if isinstance(nodeTypes, str):
            nodeTypes = [nodeTypes]
        elif not isinstance(nodeTypes, list):
            nodeTypes = []
        if 'Dataset' in nodeTypes:
            for key in self.DATASET_SUGGESTED:
                if key not in node:
                    log += f'**WARNING in dataset: "{key}" not in @id={node["@id"]}\n'
        elif 'File' in nodeTypes:
            for key in self.FILE_SUGGESTED:
                if key not in node:
                    log += f'**WARNING in file: "{key}" not in @id={node["@id"]}\n'
        if any(not str(value).strip() for value in node.values()):
            log += f'**WARNING: {nodeID} contains empty values in the key-value pairs\n'
        if isinstance(node.get('keywords', ''), list):
            log += f'**ERROR: {nodeID} contains an array of keywords. Use comma or space separated string\n'
            success = False
        for child in node.get('hasPart', []):
            childSuccess, childLog = self.processNode(nodesByID, child['@id'])
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
                isinstance(node.get('@type'), str)     #@type is a str
                or (
                    isinstance(node.get('@type'), list)#or @type is nonzero list of str
                    and node['@type']
                    and all(isinstance(nodeType, str) for nodeType in node['@type'])
                )
            )
            for node in graph
        ):
            return False, '**ERROR: RO-Crate metadata contains an invalid graph node\n'

        # test duplicated nodes
        nodeIDs = [node['@id'] for node in graph]
        if duplicateNodeIDs := [nodeID for nodeID, count in Counter(nodeIDs).items() if count > 1]:
            duplicates = ', '.join(repr(nodeID) for nodeID in duplicateNodeIDs)
            return False, f'**ERROR: RO-Crate metadata contains duplicate node IDs: {duplicates}\n'
        nodesByID = {node['@id']: node for node in graph}

        metadataNodes = [node for node in graph if node['@id'] == METADATA_FILE]
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
        if publisher is not None:
            if not isinstance(publisher, dict) or '@id' not in publisher:
                return False, '**ERROR: sdPublisher must reference an Organization or Person entity via @id\n'
            publisherID = publisher['@id']
            if publisherID not in nodeIDs:
                return False, '**ERROR: sdPublisher references non-existent entity\n'
            if publisherNodes := [node for node in graph if node['@id'] == publisherID]:
                publisherType = publisherNodes[0].get('@type')
                if isinstance(publisherType, str):
                    publisherType = [publisherType]
                if not {'Organization', 'Person'} & set(publisherType):
                    return False, '**ERROR: sdPublisher must reference an Organization or Person entity\n'

        for key in self.ROCRATE_NODE_SUGGESTED:
            if key not in metadataNodes[0]:
                log += f'**WARNING: "{key}" not in @id={METADATA_FILE}\n'

        mainNode = rootNodes[0]
        if 'hasPart' not in mainNode:
            log += '**WARNING: RO-Crate root node has no hasPart; nothing to import\n'
        for part in mainNode.get('hasPart', []):
            nodeSuccess, nodeLog = self.processNode(nodesByID, part['@id'])
            success = nodeSuccess and success
            log += nodeLog

        entitySuccess, entityLog = self.checkEntities(graph, mainNode)
        success = entitySuccess and success
        log += entityLog
        return success, log


    def checkEntities(self, graph, rootNode):
        """Check the rules of SPECIFICATION.md that apply to single entities."""
        success = True
        log = ''
        types = {node['@id']: nodeTypes(node) for node in graph}

        def error(message):
            nonlocal success, log
            success = False
            log += f'**ERROR: {message}\n'

        for node in graph:
            nodeID = node['@id']
            # author: @id reference(s) to Person or Organization
            if 'author' in node:
                authorIDs = references(node['author'])
                if authorIDs is None:
                    error(f'{nodeID}: author must be @id reference(s), not strings or embedded objects')
                for authorID in authorIDs or []:
                    if not {'Person', 'Organization'} & set(types.get(authorID, [])):
                        error(f'{nodeID}: author {authorID!r} must reference a Person or Organization node')
            # text only on CreativeWork subclasses
            if 'text' in node and self.NO_TEXT_TYPES & set(types[nodeID]):
                error(f'{nodeID}: text must not be used on {", ".join(sorted(self.NO_TEXT_TYPES & set(types[nodeID])))}')
            # comment: list of @id references to top-level Comment nodes
            if 'comment' in node:
                commentIDs = references(node['comment']) if isinstance(node['comment'], list) else None
                if commentIDs is None:
                    error(f'{nodeID}: comment must be a list of @id references to top-level Comment nodes')
                for commentID in commentIDs or []:
                    if 'Comment' not in types.get(commentID, []):
                        error(f'{nodeID}: comment {commentID!r} must reference a Comment node')
            # field formats
            if 'contentSize' in node and not (isinstance(node['contentSize'], str)
                                              and re.fullmatch(r'\d+', node['contentSize'])):
                error(f'{nodeID}: contentSize must be a string with the number of bytes, without units')
            if 'additionalType' in node and references(node['additionalType']) is None:
                error(f'{nodeID}: additionalType must be {{"@id": IRI}} or a list of those')
            for key in ('url', 'contentUrl'):
                if key in node and not (isinstance(node[key], str)
                                        and urlparse(node[key]).scheme and urlparse(node[key]).netloc):
                    log += f'**WARNING: {nodeID}: {key} SHOULD be an absolute URL\n'
            if 'PropertyValue' in types[nodeID]:
                for key in ('propertyID', 'value'):
                    if key not in node:
                        log += f'**WARNING: {nodeID}: PropertyValue SHOULD have {key}\n'
            # physical directories are Datasets, files are Files
            if nodeID not in ('./', METADATA_FILE) and not urlparse(nodeID).scheme and not nodeID.startswith('#'):
                relative = nodeID.removeprefix('./')
                path = next((self.rootDirectory/candidate for candidate in (relative, unquote(relative))
                             if (self.rootDirectory/candidate).exists()), None)
                if path is not None and path.is_dir() and 'Dataset' not in types[nodeID]:
                    error(f'{nodeID}: directories must have @type Dataset')
                if path is not None and path.is_file() and 'File' not in types[nodeID]:
                    error(f'{nodeID}: files must have @type File')
        return success, log


def nodeTypes(node):
    """Return the ``@type`` of a node as a list."""
    types = node.get('@type', [])
    return [types] if isinstance(types, str) else types


def references(value):
    """Return the ``@id`` values of one reference or a list of references, or None if malformed.

    A reference is an object with only ``@id``; anything else (strings, embedded objects) is malformed.
    """
    items = value if isinstance(value, list) else [value]
    if not all(isinstance(item, dict) and set(item) == {'@id'} and isinstance(item['@id'], str)
               for item in items):
        return None
    return [item['@id'] for item in items]
