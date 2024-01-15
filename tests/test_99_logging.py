#!/usr/bin/python3
""" Convert a logging.json to a readme file """
from pathlib import Path
import json
import unittest

class Test_2(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        columns = ['params_metadata_json', 'pypi_rocrate']
        header  = "## Results of verification\nautomatically created\n\n"
        if Path('tests/logging.json').exists():
            logJson = json.load(open('tests/logging.json'))
            output = open('tests/logging.md', 'w')
            output.write(header)
            output.write(f'| software | file name | {" | ".join(columns)} |\n')
            output.write(f'| -------- | --------- | {" | ".join(["-----------" for _ in columns])} |\n')
            for filename, result in logJson.items():
                software = filename.split('/')[2]
                indFileName = filename.split('/')[3]
                resultStr   = ' | '.join([':white_check_mark:' if result[col] else ':x:' for col in columns])
                output.write(f'| {software} | {indFileName} | {resultStr} |\n')
            output.close()
            print('Created logging markdown')
        else:
            print('Did not create logging markdown')
