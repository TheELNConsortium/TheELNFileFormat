#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import logging
import unittest
from pathlib import Path
from checks import checkValidator

LABEL = 'validator'

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
        success = True
        for root, _, files in os.walk(".", topdown=False):
            if '_skip_CI_' in files:
                continue
            for name in files:
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nTest 03: {fileName}')
                successI, log = checkValidator(fileName)
                print(log)
                if fileName not in logJson:
                    logJson[fileName] = {LABEL:successI}
                else:
                    logJson[fileName] = logJson[fileName] | {LABEL:successI}
                success = success and successI
            json.dump(logJson, open('tests/logging.json', 'w'))
        assert success
