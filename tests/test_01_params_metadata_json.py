#!/usr/bin/python3
"""  This tests against rules that we as the ELN consortium set for ourselves """
import unittest
from checks import checkParamMetadataJson
from test_00_pypi_rocrate import generalizedTest

class Test_2(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        generalizedTest(checkParamMetadataJson, 'params_metadata_json')
