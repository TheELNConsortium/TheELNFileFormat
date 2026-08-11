# BenchLineage

## Information

* Repository: https://github.com/CAOShurong/benchlineage
* Documentation: https://caoshurong.github.io/benchlineage/
* Package: https://pypi.org/project/benchlineage/
* License: MIT
* Generator version: 0.3.0

The archive in this directory was generated from BenchLineage's deterministic
electrical-engineering demonstration. Every person, instrument, serial number,
calibration certificate, and measurement in it is synthetic. It demonstrates
the exchange mapping and does not claim a real experiment or successful import
by any third-party ELN product.

## Reproduce the archive

```bash
pipx run --spec benchlineage==0.3.0 benchlineage demo benchlineage-demo --seed 20260804
pipx run --spec benchlineage==0.3.0 benchlineage export-eln benchlineage-demo --output benchlineage-0.3.0-demo.eln
pipx run --spec benchlineage==0.3.0 benchlineage verify-eln benchlineage-0.3.0-demo.eln
```

## Concepts used

| BenchLineage concept | RO-Crate / Schema.org representation |
|---|---|
| sealed workspace | root `Dataset` and experiment `Dataset` |
| preserved workspace file | `File` reachable through `hasPart` |
| study intent and protocol | `CreativeWork` |
| instrument identity | `IndividualProduct` |
| calibration record | `CreativeWork` whose `about` is the instrument |
| experimental run | `CreateAction` linking person, study, instruments, and raw results |
| derived analysis | `CreateAction` linking source files, result, and software |
| workspace owner and run operator | `Person` |
| content-addressed seal | SHA-256 `identifier`, with the original seal file preserved |

