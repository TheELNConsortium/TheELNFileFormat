#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
import rocrate_validator
from rocrate_validator.errors import ValidationError
import rocrate_validator.services as rvs

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
        if Path('tests/logging.json').exists():
            logJson = json.load(open('tests/logging.json'))
        else:
            logJson = {}

        for root, _, files in os.walk(".", topdown=False):
            for name in files:
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nTry to parse: {fileName}')
                with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                    dirpath = Path(tempfile.mkdtemp())/Path(fileName).parent.name
                    dirpath.mkdir(parents=True, exist_ok=True)
                    elnFile.extractall(dirpath)
                    rocrate_dir= [i for i in dirpath.iterdir() if i.is_dir()][0]
                    result = rvs.validate({
                        "profiles_path": rocrate_validator.utils.get_profiles_path(),
                        "profile_identifier": "ro-crate",
                        "requirement_severity": rocrate_validator.models.Severity.REQUIRED.name,
                        "requirement_severity_only": False,
                        "inherit_profiles": True,
                        "verbose": True,
                        "data_path": rocrate_dir,
                        "ontology_path": None,
                        "abort_on_first": False
                        })
                    result_dict = result.to_dict()
                    if result_dict['issues'] == [] and result_dict['passed']:
                        success = True
                    else:
                        print(f'{fileName} is not valid')
                        print(result_dict)
                        success = False
                logJson[fileName] = logJson.get(fileName,{}) | {LABEL: success}
            json.dump(logJson, open('tests/logging.json', 'w'))
        assert success
