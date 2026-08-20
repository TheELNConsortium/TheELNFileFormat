"""Shared helpers for example-wide check tests."""

import json
import os
from pathlib import Path


def generalizedTest(checkClass):
    """Run one check over every example that is included in CI."""
    logPath = Path('tests/logging.json')
    if logPath.exists():
        logJson = json.loads(logPath.read_text(encoding='utf-8'))
    else:
        logJson = {}

    elnFiles = []
    for root, _, files in os.walk('.'):
        if 'SKIP_CI' in files:
            continue
        elnFiles.extend(os.path.join(root, name) for name in files if name.endswith('.eln'))

    # Remove results for examples that no longer exist, while retaining
    # results already written by the other check classes.
    logJson = {fileName: logJson.get(fileName, {}) for fileName in elnFiles}

    success = True
    for fileName in elnFiles:
        print(f'\n\n{checkClass.label}: {fileName}')
        successI, log = checkClass(fileName).run()
        print(log)
        logJson[fileName][checkClass.loggingLabel] = successI
        success = success and successI

    logPath.write_text(json.dumps(logJson), encoding='utf-8')
    print('=' * 100)
    assert success
