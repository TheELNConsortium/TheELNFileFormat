#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import os
import json
import unittest
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED
from zipfile import Path as ZPath
from zipfile import ZipFile
from rocrate.rocrate import ROCrate

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
            for name in files:
                if not name.endswith('.eln'):
                  continue
                fileName = os.path.join(root, name)
                print(f'\n\nTry to parse: {fileName}')
                with ZipFile(fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                    p = ZPath(elnFile)
                    dirName = sorted(p.iterdir())[0]
                    try:
                        dirpath = Path(tempfile.mkdtemp())
                        elnFile.extractall(dirpath)
                        temppath= dirpath.joinpath(dirName.name)
                        crate = ROCrate(temppath)
                        for e in crate.get_entities():
                            print(f'  {e.id}: {e.type}')
                        if fileName not in logJson:
                            logJson[fileName] = {'pypi_rocrate':True}
                        else:
                            logJson[fileName] = logJson[fileName] | {'pypi_rocrate':True}
                    except Exception:
                        print("  *****  ERROR: Could not parse content of this file!!  *****")
                        if fileName not in logJson:
                            logJson[fileName] = {'pypi_rocrate':False}
                        else:
                            logJson[fileName] = logJson[fileName] | {'pypi_rocrate':False}
                        success = False
        json.dump(logJson, open('tests/logging.json', 'w'))
        assert success
