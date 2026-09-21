#!/usr/bin/python3
"""Validate the outer archive structure required by the .eln specification. Create good and bad archives and test them"""
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
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
                    success, log = CheckArchiveStructure(path).run()
                    self.assertTrue(success)
                    self.assertIn('**INFO: .eln archive does not contain ro-crate-preview.html', log)

    def test_accepts_archive_with_preview_file(self):
        """An embedded preview is detected without adding a diagnostic."""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'with-preview.eln'
            write_test_archive(path, [
                'crate/ro-crate-metadata.json',
                'crate/ro-crate-preview.html',
            ])
            success, log = CheckArchiveStructure(path).run()
            self.assertTrue(success)
            self.assertNotIn('ro-crate-preview.html', log)

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

    def test_rejects_absolute_and_traversal_paths(self):
        """Absolute and parent-directory ZIP paths are outside the crate root."""
        with tempfile.TemporaryDirectory() as directory:
            for index, entry in enumerate(('/crate/file.txt', 'crate/../file.txt')):
                with self.subTest(entry=entry):
                    path = Path(directory) / f'unsafe-{index}.eln'
                    write_test_archive(path, ['crate/ro-crate-metadata.json', entry])
                    success, log = CheckArchiveStructure(path).run()
                    self.assertFalse(success)
                    self.assertIn('entries must be stored inside the root folder', log)

    def test_rejects_empty_archive(self):
        """An archive without members has no crate root directory."""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'empty.eln'
            write_test_archive(path, [])
            success, log = CheckArchiveStructure(path).run()
            self.assertFalse(success)
            self.assertIn('exactly one root folder', log)

    def test_sensible_limits_reject_large_member_count_and_size(self):
        """The default preset rejects ZIPs that exceed either resource cap."""
        class Archive:
            def __init__(self, entries):
                self.entries = entries

            def infolist(self):
                return self.entries

        def entry(name, size=0):
            return SimpleNamespace(filename=name, file_size=size, is_dir=lambda: False)

        memberArchive = Archive([entry(f'crate/{index}') for index in range(10_001)])
        success, log = CheckArchiveStructure('unused').check(memberArchive)
        self.assertFalse(success)
        self.assertIn('more than 10000 members', log)

        sizeArchive = Archive([entry('crate/file', 4 * 1024**3 + 1)])
        success, log = CheckArchiveStructure('unused').check(sizeArchive)
        self.assertFalse(success)
        self.assertIn('expands beyond', log)
