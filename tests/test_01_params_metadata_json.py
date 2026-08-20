#!/usr/bin/python3
"""  This tests against rules that we as the ELN consortium set for ourselves """
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from tests.checks import CheckParamMetadataJson
from tests.utils import generalizedTest


def validMetadata():
    """Return the smallest metadata document accepted by this check."""
    return {
        '@context': 'https://w3id.org/ro/crate/1.1/context',
        '@graph': [
            {
                '@id': 'ro-crate-metadata.json',
                '@type': 'CreativeWork',
                'about': {'@id': './'},
                'version': '1.0',
                'sdPublisher': {'@id': '#publisher'},
            },
            {
                '@id': './',
                '@type': 'Dataset',
                'name': 'Test crate',
                'hasPart': [],
            },
            {
                '@id': '#publisher',
                '@type': 'Organization',
                'name': 'Test publisher',
            },
        ],
    }


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
        print('\nFalse-Flag Test: should report two ERRORs:')
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

    def test_rejects_pasta_graph_preflight_failures(self):
        """Reject malformed graph structures required by the PASTA importer."""
        cases = []

        metadata = validMetadata()
        metadata['@graph'] = {}
        cases.append(('non-array graph', metadata))

        metadata = validMetadata()
        metadata['@graph'][2] = {'@id': '#publisher', '@type': 1}
        cases.append(('invalid graph node type', metadata))

        metadata = validMetadata()
        metadata['@graph'][2]['@id'] = './'
        cases.append(('duplicate node IDs', metadata))

        metadata = validMetadata()
        metadata['@graph'][2]['@type'] = []
        cases.append(('empty type list', metadata))

        metadata = validMetadata()
        metadata['@graph'].pop(1)
        cases.append(('missing root node', metadata))

        metadata = validMetadata()
        metadata['@graph'].append({
            '@id': 'other/ro-crate-metadata.json', '@type': 'CreativeWork',
        })
        cases.append(('ambiguous metadata descriptor', metadata))

        metadata = validMetadata()
        metadata['@graph'][2]['hasPart'] = [{'@id': 'missing'}]
        cases.append(('unresolved unreachable child', metadata))

        metadata = validMetadata()
        metadata['@graph'][1]['hasPart'] = [{'not-id': 'missing'}]
        cases.append(('malformed child reference', metadata))

        metadata = validMetadata()
        metadata['@graph'][0]['sdPublisher'] = 'publisher'
        cases.append(('non-object publisher', metadata))

        metadata = validMetadata()
        metadata['@graph'][0]['sdPublisher'] = {'@id': '#missing'}
        cases.append(('unresolved publisher', metadata))

        metadata = validMetadata()
        metadata['@graph'][1].pop('hasPart')
        cases.append(('missing root hasPart', metadata))

        with tempfile.TemporaryDirectory() as directory:
            for index, (description, metadata) in enumerate(cases):
                with self.subTest(description=description):
                    path = Path(directory) / f'preflight-{index}.eln'
                    with ZipFile(path, 'w', compression=ZIP_DEFLATED) as archive:
                        archive.writestr(
                            'test.eln/ro-crate-metadata.json',
                            json.dumps(deepcopy(metadata)),
                        )
                    success, log = CheckParamMetadataJson(path).run()
                    self.assertFalse(success)
                    if description == 'duplicate node IDs':
                        self.assertIn("duplicate node IDs: './'", log)
