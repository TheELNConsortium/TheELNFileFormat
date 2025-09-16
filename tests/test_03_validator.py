#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import logging
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
from rocrate_validator import services, models

LABEL = 'validator'
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
        logging.getLogger('rdflib').setLevel(logging.ERROR) # get rid of verbose rdflib warnings, we concentrate on validator directly
        if Path('tests/logging.json').exists():
            logJson = json.load(open('tests/logging.json'))
        else:
            logJson = {}

        for root, _, files in os.walk(".", topdown=False):
            for name in files:
                if 'SKIP_CI' in files:
                    continue
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nTest 03: {fileName}')
                with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                    dirpath = Path(tempfile.mkdtemp())/Path(fileName).parent.name
                    dirpath.mkdir(parents=True, exist_ok=True)
                    elnFile.extractall(dirpath)
                    rocrate_dir= [i for i in dirpath.iterdir() if i.is_dir()][0]

                    # short stop-gap measure because the validator currently does not support the latest ro-crate version
                    with open(rocrate_dir/METADATA_FILE, 'r', encoding='utf-8') as f:
                        metadata = f.read()
                    metadata = metadata.replace('conformsTo":{"@id":"https:\/\/w3id.org\/ro\/crate\/1.2"}',
                                                'conformsTo":{"@id":"https:\/\/w3id.org\/ro\/crate\/1.1"}')
                    with open(rocrate_dir/METADATA_FILE, 'w', encoding='utf-8') as f:
                        f.write(metadata)

                    # start validation
                    settings = services.ValidationSettings(
                        rocrate_uri=rocrate_dir,
                        profile_identifier='ro-crate-1.1',
                        requirement_severity=models.Severity.REQUIRED,
                    )
                    result = services.validate(settings)
                    if not result.has_issues():
                        success = True
                    else:
                        print(f'{fileName} is not valid')
                        for issue in result.get_issues():
                            print(f"Detected issue of severity {issue.severity.name} with check \"{issue.check.identifier}\": {issue.message}")
                        success = False

                logJson[fileName] = logJson.get(fileName,{}) | {LABEL: success}
            json.dump(logJson, open('tests/logging.json', 'w'))
        assert success
