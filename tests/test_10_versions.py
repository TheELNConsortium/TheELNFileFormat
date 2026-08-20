"""Tests for explicit RO-Crate, ELN-format, and exporter versions."""

import unittest

from tests.checks.versions import DeclaredVersions, getDeclaredVersions


class TestDeclaredVersions(unittest.TestCase):
    """Read version declarations without conflating their meanings."""

    def test_reads_all_three_declared_versions(self):
        metadata = {
            '@graph': [
                {
                    '@id': 'ro-crate-metadata.json',
                    'conformsTo': [
                        {'@id': 'https://w3id.org/ro/crate/1.2'},
                        {'@id': 'https://w3id.org/eln/file-format/1.0'},
                    ],
                    'eln:exportedBy': {'@id': '#exporter'},
                },
                {
                    '@id': '#exporter',
                    '@type': 'SoftwareApplication',
                    'softwareVersion': '4.2.1',
                },
            ]
        }
        self.assertEqual(
            getDeclaredVersions(metadata),
            DeclaredVersions(roCrate='1.2', elnFormat='1.0', exporter='4.2.1'),
        )

    def test_absent_declarations_are_not_inferred(self):
        metadata = {
            '@graph': [
                {
                    '@id': 'ro-crate-metadata.json',
                    'conformsTo': {'@id': 'https://w3id.org/ro/crate/1.1'},
                    'version': '99.0',
                }
            ]
        }
        self.assertEqual(
            getDeclaredVersions(metadata),
            DeclaredVersions(roCrate='1.1', elnFormat=None, exporter=None),
        )
