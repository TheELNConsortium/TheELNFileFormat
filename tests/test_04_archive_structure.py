#!/usr/bin/python3
"""Validate the outer archive structure required by the .eln specification. Create good and bad archives and test them"""
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from tests.checks import CheckArchiveStructure
from tests.utils import generalizedTest


def write_test_archive(path, entries):
    """Write a small ZIP fixture with the given entry names."""
    with ZipFile(path, 'w', compression=ZIP_DEFLATED) as archive:
        for entry in entries:
            archive.writestr(entry, '' if entry.endswith('/') else '{}')


class TestArchiveStructure(unittest.TestCase):
    """Test the .eln single-root-folder requirement."""

    def test_main(self):
        """Run the archive-structure check against all repository examples."""
        generalizedTest(CheckArchiveStructure)

    def test_accepts_single_root_folder(self):
        """A directory entry is optional when every file has the same root."""
        cases = [
            ['crate/ro-crate-metadata.json', 'crate/data/value.txt'],
            ['crate/', 'crate/ro-crate-metadata.json'],
        ]
        with tempfile.TemporaryDirectory() as directory:
            for index, entries in enumerate(cases):
                with self.subTest(entries=entries):
                    path = Path(directory) / f'valid-{index}.eln'
                    write_test_archive(path, entries)
                    self.assertEqual(CheckArchiveStructure(path).run(), (True, ''))

    def test_rejects_root_level_file(self):
        """Files alongside the root folder violate the archive layout."""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'root-file.eln'
            write_test_archive(path, [
                'crate/ro-crate-metadata.json',
                'unexpected-root.txt',
            ])
            self.assertEqual(CheckArchiveStructure(path).run(), (
                False,
                '**ERROR: .eln archive entries must be stored inside the root '
                "folder: 'unexpected-root.txt'\n",
            ))

    def test_rejects_multiple_root_folders(self):
        """Two top-level folders are not a single .eln RO-Crate."""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'multiple-roots.eln'
            write_test_archive(path, [
                'first/ro-crate-metadata.json',
                'second/data.txt',
            ])
            self.assertEqual(CheckArchiveStructure(path).run(), (
                False,
                '**ERROR: .eln archive must contain exactly one root folder; '
                "found 2: 'first', 'second'\n",
            ))
