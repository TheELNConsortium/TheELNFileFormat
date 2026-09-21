"""Validation of the outer .eln ZIP archive layout."""
from pathlib import PurePosixPath

from .base import BaseCheck

PREVIEW_FILE = 'ro-crate-preview.html'


class CheckArchiveStructure(BaseCheck):
    """Check that an .eln ZIP contains exactly one root folder."""

    label = 'Archive structure'
    loggingLabel = 'archive_structure'
    requiresRootDirectory = False
    requiresMetadataJson = False
    MAX_ARCHIVE_MEMBERS = 10_000
    MAX_ARCHIVE_BYTES = 4 * 1024**3
    RESOURCE_LIMIT_PRESETS = {'permissive', 'sensible'}

    def __init__(self, fileName, resourceLimits='sensible'):
        """Create an archive-layout check with a resource-limit preset."""
        super().__init__(fileName)
        if resourceLimits not in self.RESOURCE_LIMIT_PRESETS:
            raise ValueError(f'resourceLimits must be one of {sorted(self.RESOURCE_LIMIT_PRESETS)}')
        self.resourceLimits = resourceLimits

    def check(self, elnFile):
        archiveInfo = elnFile.infolist()
        entriesOutsideRoot = set()
        rootFolders = set()
        for entry in archiveInfo:
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
        success = True
        if self.resourceLimits == 'sensible':
            if len(archiveInfo) > self.MAX_ARCHIVE_MEMBERS:
                log += (f'**ERROR: .eln archive contains more than {self.MAX_ARCHIVE_MEMBERS} members\n')
                success = False
            archiveBytes = sum(entry.file_size for entry in archiveInfo)
            if archiveBytes > self.MAX_ARCHIVE_BYTES:
                log += (f'**ERROR: .eln archive expands beyond {self.MAX_ARCHIVE_BYTES} bytes\n')
                success = False
        if entriesOutsideRoot:
            entries = ', '.join(repr(path) for path in sorted(entriesOutsideRoot))
            log += (
                '**ERROR: .eln archive entries must be stored inside the root '
                f'folder: {entries}\n'
            )
            success = False
        if len(rootFolders) != 1:
            folders = ', '.join(repr(path) for path in sorted(rootFolders))
            log += (
                '**ERROR: .eln archive must contain exactly one root folder; '
                f'found {len(rootFolders)}: {folders}\n'
            )
            success = False
        if success and not any(
            PurePosixPath(entry.filename).name == PREVIEW_FILE
            for entry in archiveInfo
        ):
            log += f'**INFO: .eln archive does not contain {PREVIEW_FILE}; the preview is optional\n'
        return success, log
