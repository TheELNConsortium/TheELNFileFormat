#!/usr/bin/python3
"""  This tests against rules that we as the ELN consortium set for ourselves """
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from tests.checks import CheckParamMetadataJson
from tests.utils import generalizedTest


class TestParamMetadataJson(unittest.TestCase):
    """Check consortium-specific metadata rules not covered by RO-Crate."""


    def test_main(self):
        """Run the metadata-convention check against all repository examples."""
        generalizedTest(CheckParamMetadataJson)


    def test_array_types_are_checked(self):
        """Dataset and File rules also apply when @type is an array."""
        cases = [
            ("dataset.eln", "data/", ["Dataset", "Message"]),
            ("file.eln", "data.txt", ["File", "DigitalDocument"]),
        ]
        with tempfile.TemporaryDirectory() as directory:
            for filename, entity_id, entity_type in cases:
                with self.subTest(entity_type=entity_type):
                    path = Path(directory) / filename
                    metadata = {
                        "@context": "https://w3id.org/ro/crate/1.1/context",
                        "@graph": [
                            {
                                "@id": "ro-crate-metadata.json",
                                "@type": "CreativeWork",
                                "about": {"@id": "./"},
                                "conformsTo": {"@id": "https://w3id.org/ro/crate/1.1"},
                                "version": "1.0",
                                "sdPublisher": {"@id": "#publisher"},
                            },
                            {
                                "@id": "./",
                                "@type": "Dataset",
                                "name": "Test crate",
                                "hasPart": [{"@id": entity_id}],
                            },
                            {"@id": entity_id, "@type": entity_type},
                            {
                                "@id": "#publisher",
                                "@type": "Organization",
                                "name": "Test publisher",
                            },
                        ],
                    }
                    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
                        archive.writestr("test.eln/ro-crate-metadata.json", json.dumps(metadata))
                    success, _ = CheckParamMetadataJson(path).run()
                    self.assertFalse(success)
