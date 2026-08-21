"""Read the version declarations from an ELN RO-Crate metadata document."""

from dataclasses import dataclass

METADATA_FILE = 'ro-crate-metadata.json'
RO_CRATE_PROFILE_PREFIX = 'https://w3id.org/ro/crate/'
ELN_FORMAT_PROFILE_PREFIX = 'https://w3id.org/eln/file-format/'
EXPORTER_PROPERTY = 'eln:exportedBy'


@dataclass(frozen=True)
class DeclaredVersions:
    """Versions declared by an exported .eln archive.

    A value is ``None`` when the corresponding declaration is absent or uses
    an unrecognised profile URI.
    """
    roCrate: str | None
    elnFormat: str | None
    exporter: str | None


def _identifiers(value):
    """Yield JSON-LD identifiers from one reference or a list of references."""
    if isinstance(value, list):
        for item in value:
            yield from _identifiers(item)
    elif isinstance(value, dict) and isinstance(value.get('@id'), str):
        yield value['@id']
    elif isinstance(value, str):
        yield value


def _versionFromProfiles(profiles, prefix):
    """Return the first version suffix for a profile URI prefix."""
    for profile in profiles:
        if profile.startswith(prefix):
            version = profile.removeprefix(prefix).strip('/')
            if version:
                return version
    return None


def getDeclaredVersions(metadataJson):
    """Return declared RO-Crate, ELN-format, and exporter versions.

    The metadata descriptor declares RO-Crate and ELN-format profiles through
    ``conformsTo``.  The ELN profile defines ``eln:exportedBy`` as a reference
    to a ``SoftwareApplication`` node with a ``softwareVersion`` property.
    """
    graph = metadataJson.get('@graph', [])
    descriptor = next(
        (node for node in graph if node.get('@id') == METADATA_FILE),
        {},
    )
    profiles = list(_identifiers(descriptor.get('conformsTo')))
    exporterReferences = list(_identifiers(descriptor.get(EXPORTER_PROPERTY)))
    exporterNode = next(
        (node for node in graph if node.get('@id') in exporterReferences),
        {},
    )
    exporterVersion = exporterNode.get('softwareVersion')
    if not isinstance(exporterVersion, str):
        exporterVersion = None
    return DeclaredVersions(
        roCrate=_versionFromProfiles(profiles, RO_CRATE_PROFILE_PREFIX),
        elnFormat=_versionFromProfiles(profiles, ELN_FORMAT_PROFILE_PREFIX),
        exporter=exporterVersion,
    )
