#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import unittest

from tests.checks import CheckSchema
from tests.utils import generalizedTest


class TestSchema(unittest.TestCase):
    """Check metadata JSON against the consortium JSON schema."""

    def test_main(self):
        """Run the schema check against all repository examples."""
        generalizedTest(CheckSchema)
