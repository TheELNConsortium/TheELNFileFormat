"""Validation against the ELN consortium JSON schema."""

import json
from pathlib import Path

from .base import BaseCheck


class CheckSchema(BaseCheck):
    """Check metadata JSON against the consortium JSON schema."""

    label = 'Schema'
    loggingLabel = 'schema'
    requiresRootDirectory = True
    requiresMetadataJson = True

    def check(self, _elnFile):
        from jsonschema import Draft202012Validator

        schemaPath = Path(__file__).parent.parent/'schema.json'
        schema     = json.loads(schemaPath.read_text(encoding='utf-8'))
        validator  = Draft202012Validator(schema=schema)
        validator.check_schema(schema=schema)
        success = True
        log = ''
        metadataContent = self.metadataJson
        for error in sorted(validator.iter_errors(metadataContent), key=str):
            path = list(error.absolute_path)
            location = 'Metadata'
            if path[:1] == ['@graph'] and len(path) >= 2 and isinstance(path[1], int):
                node = metadataContent['@graph'][path[1]]
                nodeID = node.get('@id', f'graph entry {path[1]}')
                location = f'Node {nodeID!r}'
                path = path[2:]
            if path:
                propertyPath = ''.join(f'[{part}]' if isinstance(part, int) else f'.{part}'
                    for part in path).lstrip('.')
                location += f', property {propertyPath!r}'
            log += f'- {location}: {error.message}\n'
            success = False
        return success, log
