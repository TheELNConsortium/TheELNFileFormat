#!/usr/bin/python3
"""  This tests against rules that we as the ELN consortium set for ourselves """
import os
import json
from pathlib import Path
import unittest
from checks import checkParamMetadataJson

LABEL = 'params_metadata_json'

class Test_2(unittest.TestCase):
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
        success = True
        for root, _, files in os.walk(".", topdown=False):
            if '_skip_CI_' in files:
                continue
            for name in files:
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nTest 01: {fileName}')
                successI, log = checkParamMetadataJson(fileName)
                print(log)
                if fileName not in logJson:
                    logJson[fileName] = {LABEL:successI}
                else:
                    logJson[fileName] = logJson[fileName] | {LABEL:successI}
                success = success and successI
        print('\n\nSuccess:', success)
        json.dump(logJson, open('tests/logging.json', 'w'))
        assert success  #if this fails on your local test, great. It is a summary such that github actions report correctly
