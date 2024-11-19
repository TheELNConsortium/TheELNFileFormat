#!/usr/bin/python3
""" Convert a logging.json to a readme file """
from pathlib import Path
import json
import unittest

COLUMNS = ['pypi_rocrate','validator','schema','params_metadata_json']
HEADER  = "## Results of verification\nautomatically created\n\n"


class Test_2(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        if Path('tests/logging.json').exists():
            logJson = json.load(open('tests/logging.json'))
            print(f'Test results\n{json.dumps(logJson, indent=2)}')
            with open('tests/logging.md', 'w') as output:
                output.write(HEADER)
                output.write(f'| software | file name | {" | ".join(COLUMNS)} |\n')
                output.write(f'| -------- | --------- | {" | ".join(["-----------" for _ in COLUMNS])} |\n')
                for filename, result in logJson.items():
                    software = filename.split('/')[2]
                    individualFileName = filename.split('/')[3]
                    if len(individualFileName)>30:
                        individualFileName=individualFileName[:24]+'...eln'
                    resultStr   = ' | '.join([':white_check_mark:' if result[col] else ':x:' for col in COLUMNS])
                    output.write(f'| {software} | {individualFileName} | {resultStr} |\n')
                output.write("\n\nDefinition of tests\n")
                output.write("- **pypi_rocrate**: tests if eln-file can be opened by pypi's rocrate; if eln file can be easily opened by that library.\n")
                output.write("- **validator**: tests if the ro-crate conventions fulfilled using pypi's roc-validator.\n")
                output.write("- **schema**: tests if the conventions of the ELN-consortium are fulfilled using a schema description.\n")
                output.write("- **params_metadata_json**: tests if the conventions of the ELN-consortium are fulfilled, aka parameters exist and are consistent with convention.\n")
                output.close()
            print('Created logging markdown')
        else:
            print('Did not create logging markdown')
