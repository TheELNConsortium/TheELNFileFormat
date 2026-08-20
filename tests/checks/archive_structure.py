"""Validation of the outer .eln ZIP archive layout."""
from pathlib import PurePosixPath

from .base import BaseCheck

class CheckArchiveStructure(BaseCheck):
    """Check that an .eln ZIP contains exactly one root folder."""

    label = 'Archive structure'
    loggingLabel = 'archive_structure'
    requiresRootDirectory = False
    requiresMetadataJson = False

    def check(self, elnFile):
        entriesOutsideRoot = set()
        rootFolders = set()
        for entry in elnFile.infolist():
            path = PurePosixPath(entry.filename)
            if (
                not path.parts
                or path.is_absolute()
                or '..' in path.parts
                or (len(path.parts) == 1 and not entry.is_dir())
            ):
                entriesOutsideRoot.add(entry.filename)
            else:
                rootFolders.add(path.parts[0])

        log = ''
        if entriesOutsideRoot:
            entries = ', '.join(repr(path) for path in sorted(entriesOutsideRoot))
            log += (
                '**ERROR: .eln archive entries must be stored inside the root '
                f'folder: {entries}\n'
            )
        if len(rootFolders) != 1:
            folders = ', '.join(repr(path) for path in sorted(rootFolders))
            log += (
                '**ERROR: .eln archive must contain exactly one root folder; '
                f'found {len(rootFolders)}: {folders}\n'
            )
        return not log, log
