"""Shared archive setup and error handling for .eln checks."""

import json
import tempfile
import traceback
from contextlib import contextmanager
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

METADATA_FILE = 'ro-crate-metadata.json'


class BaseCheck:
    """Run one check against an open archive and extracted crate contents."""
    label = None
    loggingLabel = None
    requiresRootDirectory = False
    requiresMetadataJson = False

    def __init__(self, fileName):
        self.fileName = fileName
        self.rootDirectory: Path | None = None
        self.metadataJson: dict | None = None

    def run(self):
        """Prepare the archive, then delegate to the child-specific check."""
        try:
            with ZipFile(self.fileName, 'r', compression=ZIP_DEFLATED) as elnFile:
                with tempfile.TemporaryDirectory() as directory:
                    temporaryDirectory = Path(directory)
                    elnFile.extractall(temporaryDirectory)
                    rootDirectories = [
                        path for path in temporaryDirectory.iterdir()
                        if path.is_dir()
                    ]
                    if len(rootDirectories) == 1:
                        self.rootDirectory = rootDirectories[0]
                    if self.requiresRootDirectory and self.rootDirectory is None:
                        raise ValueError('The check requires exactly one root directory.')
                    if self.requiresMetadataJson:
                        if self.rootDirectory is None:
                            raise ValueError(f'The check requires {METADATA_FILE} in exactly one root directory.')
                        metadataJsonFile = self.rootDirectory/METADATA_FILE
                        if not metadataJsonFile.is_file():
                            raise ValueError(f'The check requires {METADATA_FILE} in the root directory.')
                        self.metadataJson = json.loads(metadataJsonFile.read_text(encoding='utf-8'))
                    return self.check(elnFile)
        except Exception:
            return False, self.errorLog()


    def check(self, elnFile):
        """Implement validation specific to this child check."""
        raise NotImplementedError


    def errorLog(self):
        """Return diagnostics for setup or validation errors."""
        return (
            '  *****  ERROR: this check could not run on the file  *****\n'
            + traceback.format_exc()
        )


    @staticmethod
    def readUploadedBytes(uploadedFile):
        """Read raw bytes from bytes or a file-like uploaded object."""
        if isinstance(uploadedFile, (bytes, bytearray)):
            return bytes(uploadedFile)
        if hasattr(uploadedFile, 'getvalue'):
            return uploadedFile.getvalue()
        if hasattr(uploadedFile, 'seek'):
            uploadedFile.seek(0)
        return uploadedFile.read()


    @classmethod
    @contextmanager
    def uploadedFileAsPath(cls, uploadedFile, fileName='uploaded.eln'):
        """Expose an uploaded .eln object as a temporary on-disk file."""
        payload = cls.readUploadedBytes(uploadedFile)
        with tempfile.TemporaryDirectory() as directory:
            elnPath = Path(directory)/'upload'/Path(fileName).name
            elnPath.parent.mkdir(parents=True, exist_ok=True)
            elnPath.write_bytes(payload)
            yield elnPath


    @classmethod
    @contextmanager
    def asPath(cls, source, fileName=None):
        """Yield a filesystem path for an existing file or uploaded object."""
        if isinstance(source, (str, Path)) and Path(source).is_file():
            yield Path(source)
        else:
            with cls.uploadedFileAsPath(source, fileName or 'uploaded.eln') as elnPath:
                yield elnPath


    @classmethod
    def runChecks(cls, source, checkClasses, fileName=None):
        """Run *checkClasses* against an on-disk or uploaded .eln object."""
        results = []
        with cls.asPath(source, fileName) as elnPath:
            for checkClass in checkClasses:
                success, log = checkClass(elnPath).run()
                results.append((checkClass.label, success, log))
        return results
