#!/usr/bin/python3
"""
Validate if rocrate of pypi can open and parse it. This is a test if we follow general ro-crate guidelines.
https://pypi.org/project/rocrate/
"""
import unittest

from tests.checks import CheckValidator
from tests.utils import generalizedTest


class TestValidator(unittest.TestCase):
    """Check each example with the RO-Crate validator."""

    def test_main(self):
        """Run the RO-Crate validator against all repository examples."""
        generalizedTest(CheckValidator)
