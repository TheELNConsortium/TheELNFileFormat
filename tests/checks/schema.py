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
            log += f'- {error.message}\n'
            success = False
        return success, log
