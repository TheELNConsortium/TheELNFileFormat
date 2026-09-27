"""Validation of the outer .eln ZIP archive layout."""
import base64
import binascii
import re
from pathlib import Path, PurePosixPath

from .base import BaseCheck, METADATA_FILE

PREVIEW_FILE = 'ro-crate-preview.html'
SIGNATURE_FILE = f'{METADATA_FILE}.minisig'
KEYS_URL = re.compile(r'https://[^/\s]+/\.well-known/keys\.json')


class CheckArchiveStructure(BaseCheck):
    """Check that an .eln ZIP contains exactly one root folder."""

    label = 'Archive structure'
    loggingLabel = 'archive_structure'
    requiresRootDirectory = False
    requiresMetadataJson = False
    versions = ('1.2+202609',)
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
            log += f'**ERROR: .eln archive entries must be stored inside the root folder: {entries}\n'
            success = False
        if len(rootFolders) != 1:
            folders = ', '.join(repr(path) for path in sorted(rootFolders))
            log += f'**ERROR: .eln archive must contain exactly one root folder; found {len(rootFolders)}: {folders}\n'
            success = False
        if success and not any(PurePosixPath(entry.filename).name == PREVIEW_FILE for entry in archiveInfo):
            log += f'**INFO: .eln archive does not contain {PREVIEW_FILE}; the preview is optional\n'
        if success:
            rootFolder = rootFolders.pop()
            archiveName = Path(str(self.fileName)).name
            if rootFolder not in (Path(archiveName).stem, archiveName):
                log += (f'**WARNING: root folder {rootFolder!r} SHOULD have the same name as the archive '
                        f'{archiveName!r}\n')
            signatureSuccess, signatureLog = self.checkSignature(elnFile, rootFolder)
            success = signatureSuccess and success
            log += signatureLog
        return success, log


    @staticmethod
    def checkSignature(elnFile, rootFolder):
        """Check the format of an optional minisign signature file; no cryptographic verification."""
        entry = next((entry for entry in elnFile.infolist()
                      if entry.filename == f'{rootFolder}/{SIGNATURE_FILE}'), None)
        if entry is None:
            return True, ''
        if entry.flag_bits & 0x1:
            return True, f'**INFO: {SIGNATURE_FILE} is encrypted and was not checked\n'
        error = f'**ERROR: {SIGNATURE_FILE} is not a valid minisign signature file: '
        try:
            lines = elnFile.read(entry).decode('utf-8').splitlines()
        except UnicodeDecodeError:
            return False, error + 'not UTF-8 text\n'
        if len(lines) < 4:
            return False, error + 'expected 4 lines\n'
        try:
            signature = base64.b64decode(lines[1], validate=True)
            globalSignature = base64.b64decode(lines[3], validate=True)
        except binascii.Error:
            return False, error + 'line 2 or 4 is not base64\n'
        if not lines[0].startswith('untrusted comment: '):
            return False, error + 'line 1 must start with "untrusted comment: "\n'
        if len(signature) != 74 or signature[:2] not in (b'Ed', b'ED'):
            return False, error + 'line 2 is not an Ed25519 signature\n'
        if not lines[2].startswith('trusted comment: '):
            return False, error + 'line 3 must start with "trusted comment: "\n'
        if len(globalSignature) != 64:
            return False, error + 'line 4 is not a global signature\n'
        trustedComment = lines[2].removeprefix('trusted comment: ').strip()
        if not KEYS_URL.fullmatch(trustedComment):
            return True, (f'**WARNING: the trusted comment of {SIGNATURE_FILE} SHOULD be a URL like '
                          f'https://<domain>/.well-known/keys.json, found {trustedComment!r}\n')
        return True, ''

