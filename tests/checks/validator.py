"""Validation using ``rocrate-validator``."""

from .base import BaseCheck


class CheckValidator(BaseCheck):
    """Check the extracted RO-Crate with ``rocrate-validator``."""

    label = 'Validator'
    loggingLabel = 'validator'
    requiresRootDirectory = True
    requiresMetadataJson = False

    def check(self, _elnFile):
        from rocrate_validator import models, services

        log = ''
        success = True
        settings = services.ValidationSettings(
            rocrate_uri=self.rootDirectory,
            profile_identifier='ro-crate-1.1',
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
