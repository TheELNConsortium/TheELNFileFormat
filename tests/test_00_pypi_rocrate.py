#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import unittest

from tests.checks import CheckPypiRocrate
from tests.utils import generalizedTest


class TestPypiRocrate(unittest.TestCase):
    """Check that each example can be opened by the PyPI rocrate package."""

    def test_main(self):
        """Run the PyPI RO-Crate check against all repository examples."""
        generalizedTest(CheckPypiRocrate)
