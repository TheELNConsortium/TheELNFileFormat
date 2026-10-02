"""Validation using the PyPI ``rocrate`` package."""
from .base import BaseCheck


class CheckPypiRocrate(BaseCheck):
    """Check that the PyPI ``rocrate`` package can parse the RO-Crate."""

    label = 'Pypi RO-Crate'
    loggingLabel = 'pypi_rocrate'
    requiresRootDirectory = True
    requiresMetadataJson = False

    def check(self, _elnFile):
        from rocrate.rocrate import ROCrate
        crate = ROCrate(self.rootDirectory)
        crate.get_entities()
        return True, ''
