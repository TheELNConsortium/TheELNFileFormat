#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import unittest, traceback
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile
from rocrate.rocrate import ROCrate

LABEL = 'pypi_rocrate'
verbose = False

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

        success = True
        for root, _, files in os.walk(".", topdown=False):
            if 'SKIP_CI' in files:
                continue
            for name in files:
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nTest 00: {fileName}')
                with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                    dirName = os.path.splitext(os.path.basename(fileName))[0]
                    try:
                        dirpath = Path(tempfile.mkdtemp())
                        elnFile.extractall(dirpath)
                        tempPath= [i for i in dirpath.iterdir() if i.is_dir()][0]
                        crate = ROCrate(tempPath)
                        for e in crate.get_entities():
                            if verbose:
                                print(f'  {e.id}: {e.type}')
                        if fileName not in logJson:
                            logJson[fileName] = {LABEL:True}
                        else:
                            logJson[fileName] = logJson[fileName] | {LABEL:True}
                    except Exception:
                        print("  *****  ERROR: Could not parse content of this file!!  *****")
                        print(f"  Temporary folder: ",tempPath)
                        print(traceback.format_exc())
                        if fileName not in logJson:
                            logJson[fileName] = {LABEL:False}
                        else:
                            logJson[fileName] = logJson[fileName] | {LABEL:False}
                        success = False
        json.dump(logJson, open('tests/logging.json', 'w'))
        assert success
