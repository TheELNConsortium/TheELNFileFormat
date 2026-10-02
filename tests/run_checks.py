#!/usr/bin/env python3
"""Run all ELN checks for one archive."""

import argparse
import sys
from pathlib import Path

if __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tests.checks import ALL_TESTS, CheckValidator
from tests.checks.versions import getFileVersion


def main() -> int:
    """Run the command-line checker.

    Returns:
        Zero when all applicable checks pass, one when a check fails, two when the file is missing.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fileName', nargs='?', help='ELN archive to check')
    parser.add_argument('--no-recommend', action='store_true',
                        help='validate only REQUIRED, not RECOMMENDED, RO-Crate rules and hide warnings')
    arguments = parser.parse_args()
    includeRecommended = not arguments.no_recommend
    fileName = Path(arguments.fileName if arguments.fileName is not None else input('ELN filename: ').strip())
    if not fileName.is_file():
        print(f'ELN file not found: {fileName}')
        return 2
    version = getFileVersion(fileName)
    print(f'Identified version: {version if version else "unknown (all checks are run)"}')

    success = True
    for checkClass in ALL_TESTS:
        # determine if this test should be run, given the .eln file version
        if skipLog := checkClass.skipLog(fileName):
            print(f'\n{checkClass.label}: not run\n{skipLog}', end='')
            continue
        # check
        check = (checkClass(fileName, includeRecommended=includeRecommended)
                 if checkClass is CheckValidator else checkClass(fileName))
        checkSuccess, log = check.run()
        # clean output of Warning, etc if user wants that
        if not includeRecommended:
            log = ''.join(line for line in log.splitlines(keepends=True)
                          if not line.startswith(('**WARNING', '**INFO')))
        print(f'\n{checkClass.label}: {"passed" if checkSuccess else "failed"}')
        # prepare error-code
        if log:
            print(log, end='' if log.endswith('\n') else '\n')
        success = success and checkSuccess
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
