"""Read the version declaration from an ELN RO-Crate metadata document."""

import json
from pathlib import PurePosixPath
from zipfile import ZipFile

from .base import METADATA_FILE

RO_CRATE_PROFILE_PREFIX = 'https://w3id.org/ro/crate/'
ELN_SPEC_PROFILE_PREFIX = 'https://purl.archive.org/purl/elnconsortium/eln-spec/'
RO_CRATE_VERSIONS = ('1.1', '1.2')
ELN_SPEC_VERSIONS = ('1.2+202609',)
RO_CRATE_PROFILES = {'1.1': 'ro-crate-1.1', '1.2': 'ro-crate-1.2', '1.2+202609': 'ro-crate-1.2'}


def getVersion(metadataJson):
    """Return the declared version: ``1.1``, ``1.2``, ``1.2+202609`` or ``None``.

    The ELN version is declared in the root Dataset's ``conformsTo``; without it,
    the RO-Crate version in the metadata descriptor's ``conformsTo`` is returned.
    """
    graph = metadataJson.get('@graph', [])
    if not isinstance(graph, list):
        return None
    profiles = {}
    # get profile information in ./ and METADATA_FILE
    for nodeID in ('./', METADATA_FILE):
        node = next((node for node in graph if isinstance(node, dict) and node.get('@id') == nodeID), {})
        conformsTo = node.get('conformsTo', [])
        if not isinstance(conformsTo, list):
            conformsTo = [conformsTo]
        profiles[nodeID] = [item['@id'] if isinstance(item, dict) else item for item in conformsTo
                            if isinstance(item, str) or (isinstance(item, dict) and isinstance(item.get('@id'), str))]
    # use the one in ./
    for profile in profiles['./']:
        version = profile.removeprefix(ELN_SPEC_PROFILE_PREFIX)
        if profile.startswith(ELN_SPEC_PROFILE_PREFIX) and version in ELN_SPEC_VERSIONS:
            return version
    # fallback, to return RO-Crate 1.1 or RO-Crate 1.2...
    for profile in profiles[METADATA_FILE]:
        version = profile.removeprefix(RO_CRATE_PROFILE_PREFIX).strip('/')
        if profile.startswith(RO_CRATE_PROFILE_PREFIX) and version in RO_CRATE_VERSIONS:
            return version
    return None


def getFileVersion(fileName):
    """Return the declared version of an .eln file, or None if it cannot be read."""
    try:
        with ZipFile(fileName) as elnFile:
            names = [name for name in elnFile.namelist()
                     if PurePosixPath(name).parts[1:] == (METADATA_FILE,)]
            if len(names) != 1:
                return None
            return getVersion(json.loads(elnFile.read(names[0])))
    except Exception:
        return None
