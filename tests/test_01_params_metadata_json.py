#!/usr/bin/python3
"""  This tests against rules that we as the ELN consortium set for ourselves """
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from checks import checkParamMetadataJson
from test_00_pypi_rocrate import generalizedTest


def write_test_eln(path, entity_id, entity_type):
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
            {"@id": "#publisher", "@type": "Organization", "name": "Test publisher"},
        ],
    }
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
        archive.writestr("test.eln/ro-crate-metadata.json", json.dumps(metadata))


class Test_2(unittest.TestCase):
    """
    derived class for this test
    """
    def test_main(self):
        """
        main function
        """
        generalizedTest(checkParamMetadataJson, 'params_metadata_json')

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
                    write_test_eln(path, entity_id, entity_type)
                    success, _ = checkParamMetadataJson(path)
                    self.assertFalse(success)
