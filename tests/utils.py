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

    success = True
    for root, _, files in os.walk('.'):
        if 'SKIP_CI' in files:
            continue
        for name in files:
            if not name.endswith('.eln'):
                continue
            fileName = os.path.join(root, name)
            print(f'\n\n{checkClass.label}: {fileName}')
            successI, log = checkClass(fileName).run()
            print(log)
            logJson.setdefault(fileName, {})[checkClass.loggingLabel] = successI
            success = success and successI

    logPath.write_text(json.dumps(logJson), encoding='utf-8')
    assert success
