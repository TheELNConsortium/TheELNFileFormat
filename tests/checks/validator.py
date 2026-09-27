"""Validation using ``rocrate-validator``."""

from pathlib import Path

from .base import BaseCheck
from .versions import RO_CRATE_PROFILES, getVersion


class CheckValidator(BaseCheck):
    """Check the extracted RO-Crate with ``rocrate-validator``."""

    label = 'Validator'
    loggingLabel = 'validator'
    requiresRootDirectory = True
    requiresMetadataJson = True

    def __init__(self, fileName: str | Path, includeRecommended: bool = False) -> None:
        """Initialize the validator check.

        Args:
            fileName: Path to the ELN archive to validate.
            includeRecommended: Whether to validate recommended RO-Crate rules too.
        """
        super().__init__(fileName)
        self.includeRecommended = includeRecommended


    def check(self, _elnFile: object) -> tuple[bool, str]:
        """Validate the extracted RO-Crate.

        Args:
            _elnFile: Open ELN archive, unused after extraction.

        Returns:
            Whether validation passed and its diagnostic log.
        """
        version = getVersion(self.metadataJson)
        if version not in RO_CRATE_PROFILES:
            return False, (
                f'{self.fileName} is not valid\n'
                'The metadata must declare RO-Crate version 1.1 or 1.2, or ELN version '
                '1.2+202609, in conformsTo\n'
            )

        from rocrate_validator import models, services

        log = ''
        success = True
        settings = services.ValidationSettings(
            rocrate_uri=self.rootDirectory,
            profile_identifier=RO_CRATE_PROFILES[version],
            requirement_severity=(models.Severity.RECOMMENDED
                if self.includeRecommended else models.Severity.REQUIRED))
        result = services.validate(settings)
        # format issues
        if result.has_issues():
            log += f'{self.fileName} is not valid\n'
            for issue in result.get_issues():
                log += (
                    f'Version: {version} '
                    f'Detected issue of severity {issue.severity.name} with check '
                    f'"{issue.check.identifier}": {issue.message}\n'
                )
            success = False
        return success, log
