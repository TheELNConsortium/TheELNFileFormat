#!/usr/bin/python3
"""Test the upload flow used by the Streamlit checker application."""

import io
import os
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from tests.checks import (
    ALL_TESTS,
    BaseCheck,
    CheckValidator,
)


def findExampleEln():
    """Return the path of one .eln example shipped in this repository."""
    for root, _, files in os.walk('.', topdown=False):
        if 'SKIP_CI' in files:
            continue
        for name in sorted(files):
            if name.endswith('.eln'):
                return Path(root)/name
    raise unittest.SkipTest('no .eln example available in this checkout')


class TestUploadedFileAsPath(unittest.TestCase):
    """Test materializing an in-memory upload as a real file."""

    def test_reads_bytes_from_several_sources(self):
        """bytes, BytesIO and a plain file handle all yield the same payload."""
        payload = b'not-a-real-zip'
        with tempfile.TemporaryDirectory() as directory:
            handlePath = Path(directory)/'payload.eln'
            handlePath.write_bytes(payload)
            with open(handlePath, 'rb') as handle:
                sources = [payload, io.BytesIO(payload), handle]
                for source in sources:
                    with self.subTest(source=type(source).__name__):
                        self.assertEqual(BaseCheck.readUploadedBytes(source), payload)

    def test_writes_and_removes_temporary_file(self):
        """The upload exists on disk inside the block and is gone after it."""
        payload = b'temporary'
        with BaseCheck.uploadedFileAsPath(io.BytesIO(payload), 'demo.eln') as elnPath:
            self.assertTrue(elnPath.is_file())
            self.assertEqual(elnPath.name, 'demo.eln')
            self.assertEqual(elnPath.read_bytes(), payload)
            leaked = elnPath
        self.assertFalse(leaked.exists())

    def test_uses_only_the_basename_of_the_upload(self):
        """A directory component in the upload name cannot escape the sandbox."""
        with BaseCheck.uploadedFileAsPath(b'x', '../../evil.eln') as elnPath:
            self.assertEqual(elnPath.name, 'evil.eln')
            self.assertEqual(elnPath.parent.name, 'upload')


class TestRunChecks(unittest.TestCase):
    """Test the BaseCheck batch entry point for paths and uploads."""

    def test_validator_rejects_raw_bytes_without_the_bridge(self):
        """Raw bytes need the bridge before a child check can read them."""
        example = findExampleEln()
        success, _ = CheckValidator(example.read_bytes()).run()
        self.assertFalse(success)

    def test_valid_upload_passes_all_checks(self):
        """A valid .eln uploaded as bytes passes every check."""
        example = findExampleEln()
        results = BaseCheck.runChecks(io.BytesIO(example.read_bytes()), ALL_TESTS, example.name)
        for label, success, _log in results:
            with self.subTest(check=label):
                self.assertTrue(success, f'{label} failed on a valid example')

    def test_corrupt_upload_is_reported_not_raised(self):
        """A corrupt upload yields failing checks instead of breaking the page."""
        results = BaseCheck.runChecks(b'this is not a zip file', ALL_TESTS, 'broken.eln')
        self.assertTrue(all(not success for _label, success, _log in results))
        self.assertTrue(all(log for _label, _success, log in results))

    def test_all_results_returned_in_order(self):
        """The batch runner returns one result per check in ALL_TESTS order."""
        example = findExampleEln()
        payload = io.BytesIO(example.read_bytes())
        uploaded = BaseCheck.runChecks(payload, ALL_TESTS, example.name)
        self.assertEqual(
            [label for label, _, _ in uploaded],
            [checkClass.label for checkClass in ALL_TESTS],
        )
        fromPath = BaseCheck.runChecks(example, ALL_TESTS)
        self.assertEqual(
            [label for label, _, _ in fromPath],
            [checkClass.label for checkClass in ALL_TESTS],
        )
        for (uLabel, uSuccess, _), (pLabel, pSuccess, _) in zip(uploaded, fromPath):
            with self.subTest(check=uLabel):
                self.assertEqual(uLabel, pLabel)
                self.assertEqual(uSuccess, pSuccess)

    def test_upload_and_path_produce_matching_verdicts(self):
        """An uploaded example produces the same verdicts as the file on disk."""
        example = findExampleEln()
        uploaded = BaseCheck.runChecks(io.BytesIO(example.read_bytes()), ALL_TESTS, example.name)
        for label, success, _log in uploaded:
            with self.subTest(check=label):
                checkClass = next(
                    candidate for candidate in ALL_TESTS if candidate.label == label
                )
                onDisk, _ = checkClass(example).run()
                self.assertEqual(success, onDisk)

    def test_archive_without_metadata_is_reported_not_raised(self):
        """A readable ZIP that is not an RO-Crate also fails cleanly."""
        buffer = io.BytesIO()
        with ZipFile(buffer, 'w', compression=ZIP_DEFLATED) as archive:
            archive.writestr('crate/readme.txt', 'no metadata here')
        results = BaseCheck.runChecks(buffer.getvalue(), ALL_TESTS, 'empty.eln')
        verdicts = {label: success for label, success, _log in results}
        self.assertTrue(verdicts['Archive structure'])
        self.assertFalse(verdicts['Parameters metadata json'])
