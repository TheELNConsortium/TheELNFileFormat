"""Validation using ``rocrate-validator``."""

from .base import BaseCheck
from .versions import getDeclaredVersions


class CheckValidator(BaseCheck):
    """Check the extracted RO-Crate with ``rocrate-validator``."""

    label = 'Validator'
    loggingLabel = 'validator'
    requiresRootDirectory = True
    requiresMetadataJson = True
    SUPPORTED_RO_CRATE_VERSIONS = {'1.1', '1.2'}

    def check(self, _elnFile):
        roCrateVersion = getDeclaredVersions(self.metadataJson).roCrate
        if roCrateVersion not in self.SUPPORTED_RO_CRATE_VERSIONS:
            return False, (
                f'{self.fileName} is not valid\n'
                'The metadata descriptor must declare RO-Crate version 1.1 or 1.2 '
                'in conformsTo\n'
            )

        from rocrate_validator import models, services

        log = ''
        success = True
        settings = services.ValidationSettings(
            rocrate_uri=self.rootDirectory,
            profile_identifier=f'ro-crate-{roCrateVersion}',
            requirement_severity=models.Severity.REQUIRED,
        )
        result = services.validate(settings)
        if result.has_issues():
            log += f'{self.fileName} is not valid\n'
            for issue in result.get_issues():
                log += (
                    f'Detected issue of severity {issue.severity.name} with check '
                    f'"{issue.check.identifier}": {issue.message}\n'
                )
            success = False
        return success, log
