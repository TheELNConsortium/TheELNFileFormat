"""ELN validation check classes."""

from .archive_structure import CheckArchiveStructure, PREVIEW_FILE
from .base import BaseCheck
from .param_metadata_json import CheckParamMetadataJson
from .pypi_rocrate import CheckPypiRocrate
from .schema import CheckSchema
from .validator import CheckValidator

ALL_TESTS = (
    CheckArchiveStructure,
    CheckParamMetadataJson,
    CheckSchema,
    CheckValidator,
    CheckPypiRocrate,
)
