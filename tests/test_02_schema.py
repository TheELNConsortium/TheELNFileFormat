#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
from jsonschema import Draft202012Validator

LABEL = 'schema'
METADATA_FILE = 'ro-crate-metadata.json'

class Test_1(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        # log-file
        if Path('tests/logging.json').exists():
            logJson = json.load(open('tests/logging.json'))
        else:
            logJson = {}

        schema = json.load(open('tests/schema.json', 'r', encoding='utf-8'))
        validator = Draft202012Validator(schema=schema)
        validator.check_schema(schema=schema)
        success = True
        for root, _, files in os.walk(".", topdown=False):
            for name in files:
                successFile = True
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\nInspect: {name}')
                with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                    metadataJsonFile = [i for i in elnFile.namelist() if i.endswith(METADATA_FILE)][0]
                    metadataContent = json.loads(elnFile.read(metadataJsonFile))
                    for error in sorted(validator.iter_errors(metadataContent), key=str):
                        print(f'- {error.message}')
                        success = False
                        successFile = False
                logJson[fileName] = logJson.get(fileName,{}) | {LABEL: successFile}
        json.dump(logJson, open('tests/logging.json', 'w'))
        assert success
