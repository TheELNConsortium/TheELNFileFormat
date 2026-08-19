#!/usr/bin/python3
"""Validate the upload bridge that lets a web front end reuse these checks."""
import io
import os
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from checks import (
    ALL_CHECKS,
    checkValidator,
    readUploadedBytes,
    runChecks,
    uploadedFileAsPath,
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
                        self.assertEqual(readUploadedBytes(source), payload)

    def test_writes_and_removes_temporary_file(self):
        """The upload exists on disk inside the block and is gone after it."""
        payload = b'temporary'
        with uploadedFileAsPath(io.BytesIO(payload), 'demo.eln') as elnPath:
            self.assertTrue(elnPath.is_file())
            self.assertEqual(elnPath.name, 'demo.eln')
            self.assertEqual(elnPath.read_bytes(), payload)
            leaked = elnPath
        self.assertFalse(leaked.exists())

    def test_uses_only_the_basename_of_the_upload(self):
        """A directory component in the upload name cannot escape the sandbox."""
        with uploadedFileAsPath(b'x', '../../evil.eln') as elnPath:
            self.assertEqual(elnPath.name, 'evil.eln')
            self.assertEqual(elnPath.parent.name, 'upload')


class TestRunChecks(unittest.TestCase):
    """Test the unified runChecks entry point for both paths and uploads."""

    def test_validator_rejects_an_upload_object_without_the_bridge(self):
        """checkValidator needs a real path, which is why the bridge exists."""
        example = findExampleEln()
        with self.assertRaises(TypeError):
            checkValidator(io.BytesIO(example.read_bytes()))

    def test_valid_upload_passes_all_checks(self):
        """A valid .eln uploaded as bytes passes every check."""
        example = findExampleEln()
        results = runChecks(io.BytesIO(example.read_bytes()), example.name)
        for label, success, _log in results:
            with self.subTest(check=label):
                self.assertTrue(success, f'{label} failed on a valid example')

    def test_corrupt_upload_is_reported_not_raised(self):
        """A corrupt upload yields failing checks instead of breaking the page."""
        results = runChecks(b'this is not a zip file', 'broken.eln')
        self.assertTrue(all(not success for _label, success, _log in results))
        self.assertTrue(all(log for _label, _success, log in results))

    def test_all_results_returned_in_order(self):
        """runChecks returns exactly one result per check, in ALL_CHECKS order."""
        example = findExampleEln()
        payload = io.BytesIO(example.read_bytes())
        uploaded = runChecks(payload, example.name)
        self.assertEqual(
            [label for label, _, _ in uploaded],
            [label for label, _ in ALL_CHECKS],
        )
        fromPath = runChecks(example)
        self.assertEqual(
            [label for label, _, _ in fromPath],
            [label for label, _ in ALL_CHECKS],
        )
        for (uLabel, uSuccess, _), (pLabel, pSuccess, _) in zip(uploaded, fromPath):
            with self.subTest(check=uLabel):
                self.assertEqual(uLabel, pLabel)
                self.assertEqual(uSuccess, pSuccess)

    def test_upload_and_path_produce_matching_verdicts(self):
        """An uploaded example produces the same verdicts as the file on disk."""
        example = findExampleEln()
        uploaded = runChecks(io.BytesIO(example.read_bytes()), example.name)
        for label, success, _log in uploaded:
            with self.subTest(check=label):
                onDisk, _ = dict(ALL_CHECKS)[label](example)
                self.assertEqual(success, onDisk)

    def test_archive_without_metadata_is_reported_not_raised(self):
        """A readable ZIP that is not an RO-Crate also fails cleanly."""
        buffer = io.BytesIO()
        with ZipFile(buffer, 'w', compression=ZIP_DEFLATED) as archive:
            archive.writestr('crate/readme.txt', 'no metadata here')
        results = runChecks(buffer.getvalue(), 'empty.eln')
        verdicts = {label: success for label, success, _log in results}
        self.assertTrue(verdicts['Archive structure'])
        self.assertFalse(verdicts['Parameters metadata json'])
