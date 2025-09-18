#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import unittest
from pathlib import Path
from checks import checkPypiRocrate

def generalizedTest(checkFunction, label):
    """
    generalized test function to reduce code duplication

    Args:
        checkFunction: function to be tested
        label: label to be used in logging.json
    """
    if Path('tests/logging.json').exists():
        logJson = json.load(open('tests/logging.json'))
    else:
        logJson = {}
    success = True
    for root, _, files in os.walk(".", topdown=False):
        if 'SKIP_CI' in files:
            continue
        for name in files:
            if not name.endswith('.eln'):
                continue
            fileName = os.path.join(root, name)
            print(f'\n\nTest 00: {fileName}')
            successI, log = checkFunction(fileName)
            print(log)
            if fileName not in logJson:
                logJson[fileName] = {label:successI}
            else:
                logJson[fileName] = logJson[fileName] | {label:successI}
            success = success and successI
    json.dump(logJson, open('tests/logging.json', 'w'))
    assert success


class Test_1(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        generalizedTest(checkPypiRocrate, 'pypi_rocrate')
