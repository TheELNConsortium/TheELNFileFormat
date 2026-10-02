#!/usr/bin/python3
""" Convert a logging.json to a readme file """
from pathlib import Path
import json
import unittest

from tests.checks import ALL_TESTS
from tests.checks.versions import getFileVersion

COLUMNS = [check.loggingLabel for check in ALL_TESTS]
DEFINITIONS = {
    'archive_structure': 'tests whether the .eln has a single-root layout and, by default, sensible limits.',
    'params_metadata_json': 'tests the ELN-consortium metadata conventions and graph integrity.',
    'schema': 'tests the ELN-consortium conventions using a schema description.',
    'validator': 'tests the RO-Crate conventions using roc-validator.',
    'pypi_rocrate': 'tests whether the PyPI rocrate package can open the .eln file.',
}
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
            logJson = json.loads(Path('tests/logging.json').read_text(encoding='utf-8'))
            print(f'Test results\n{json.dumps(logJson, indent=2)}')
            with open('tests/logging.md', 'w') as output:
                output.write(HEADER)
                output.write(f'| software | file name | version | {" | ".join(COLUMNS)} |\n')
                output.write(f'| -------- | --------- | ------- | {" | ".join(["-----------" for _ in COLUMNS])} |\n')
                # loop over all items, sort by software (part1) then file name (part2)
                for filename, result in sorted(logJson.items(),
                                               key=lambda item: (Path(item[0]).parts[1], Path(item[0]).parts[2])):
                    software = Path(filename).parts[1]
                    individualFileName = Path(filename).parts[2]
                    if len(individualFileName)>30:
                        individualFileName=individualFileName[:24]+'...eln'
                    version = getFileVersion(filename) or 'unknown'
                    resultStr   = ' | '.join(['-'                  if col in result and result[col] is None else
                                              ':white_check_mark:' if col in result and result[col] else
                                              ':x:'
                                              for col in COLUMNS])
                    output.write(f'| {software} | {individualFileName} | {version} | {resultStr} |\n')
                output.write("\n\n'-': not run, the test only applies to other versions\n")
                output.write("\n'unknown': the version could not be read from ro-crate-metadata.json\n")
                output.write("\n\nDefinition of tests\n")
                for check in ALL_TESTS:
                    output.write(f'- **{check.loggingLabel}**: {DEFINITIONS[check.loggingLabel]}\n')
            print('Created logging markdown')
        else:
            print('Did not create logging markdown')
