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


### benchlineage-0.3.0-demo.eln
```json
{
  "@context": [
    "https://w3id.org/ro/crate/1.1/context",
    {
      "sha256": "https://the.elnconsortium.org/specification/#sha256"
    }
  ],
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "dateCreated": "2026-08-04T08:00:00+00:00",
      "sdPublisher": {
        "@id": "https://github.com/CAOShurong/benchlineage"
      },
      "version": "1.0"
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "author": {
        "@id": "#person-7e1a506b2e984e7b"
      },
      "dateCreated": "2026-08-04T07:59:00+00:00",
      "dateModified": "2026-08-04T08:00:00+00:00",
      "datePublished": "2026-08-04T08:00:00+00:00",
      "description": "An ELN Consortium exchange archive exported by BenchLineage.",
      "hasPart": [
        {
          "@id": "./workspace/"
        }
      ],
      "identifier": "sha256:db35e8d479450fb39f336cc48688a45fe050e9d95e1e9e42a348f175d901198d",
      "license": "No data license was declared; contact the workspace author before reuse.",
      "name": "Power-conversion and RC-filter characterization"
    },
    {
      "@id": "./workspace/",
      "@type": "Dataset",
      "author": {
        "@id": "#person-7e1a506b2e984e7b"
      },
      "dateCreated": "2026-08-04T07:59:00+00:00",
      "dateModified": "2026-08-04T08:00:00+00:00",
      "description": "Sealed experimental evidence exported from a BenchLineage workspace.",
      "hasPart": [
        {
          "@id": "./workspace/analysis/buck-load-001.json"
        },
        {
          "@id": "./workspace/analysis/rc-baseline-001.json"
        },
        {
          "@id": "./workspace/analysis/rc-swap-002.json"
        },
        {
          "@id": "./workspace/benchlineage.json"
        },
        {
          "@id": "./workspace/calibrations/cal-dmm-01-2026.json"
        },
        {
          "@id": "./workspace/calibrations/cal-scope-01-2026.json"
        },
        {
          "@id": "./workspace/calibrations/cal-source-01-2026.json"
        },
        {
          "@id": "./workspace/data/raw/buck-load-sweep.csv"
        },
        {
          "@id": "./workspace/data/raw/rc-baseline.csv"
        },
        {
          "@id": "./workspace/data/raw/rc-resistor-swap.csv"
        },
        {
          "@id": "./workspace/instruments/dmm-01.json"
        },
        {
          "@id": "./workspace/instruments/scope-01.json"
        },
        {
          "@id": "./workspace/instruments/source-01.json"
        },
        {
          "@id": "./workspace/reports/demo-report.html"
        },
        {
          "@id": "./workspace/runs/buck-load-001.json"
        },
        {
          "@id": "./workspace/runs/rc-baseline-001.json"
        },
        {
          "@id": "./workspace/runs/rc-swap-002.json"
        },
        {
          "@id": "./workspace/seals/seal-2026-08-04T080000-0000.json"
        },
        {
          "@id": "./workspace/studies/buck-efficiency.json"
        },
        {
          "@id": "./workspace/studies/rc-filter.json"
        }
      ],
      "identifier": "sha256:db35e8d479450fb39f336cc48688a45fe050e9d95e1e9e42a348f175d901198d",
      "keywords": "analog, efficiency, filter, frequency-response, load-sweep, metrology, power-electronics",
      "mentions": [
        {
          "@id": "#instrument-dmm-01"
        },
        {
          "@id": "#instrument-scope-01"
        },
        {
          "@id": "#instrument-source-01"
        },
        {
          "@id": "#study-buck-efficiency"
        },
        {
          "@id": "#study-rc-filter"
        },
        {
          "@id": "#calibration-cal-dmm-01-2026"
        },
        {
          "@id": "#calibration-cal-scope-01-2026"
        },
        {
          "@id": "#calibration-cal-source-01-2026"
        },
        {
          "@id": "#run-buck-load-001"
        },
        {
          "@id": "#run-rc-baseline-001"
        },
        {
          "@id": "#run-rc-swap-002"
        },
        {
          "@id": "https://pypi.org/project/benchlineage/"
        },
        {
          "@id": "#analysis-buck-load-001"
        },
        {
          "@id": "#analysis-rc-baseline-001"
        },
        {
          "@id": "#analysis-rc-swap-002"
        },
        {
          "@id": "#person-7e1a506b2e984e7b"
        }
      ],
      "name": "Power-conversion and RC-filter characterization",
      "text": "<p>BenchLineage workspace containing 2 studies and 3 experimental runs. The archive preserves the original records, raw files, analyses, reports, and content-addressed seals.</p>"
    },
    {
      "@id": "https://github.com/CAOShurong/benchlineage",
      "@type": "Organization",
      "name": "BenchLineage",
      "url": "https://github.com/CAOShurong/benchlineage"
    },
    {
      "@id": "./workspace/analysis/buck-load-001.json",
      "@type": "File",
      "contentSize": "3859",
      "description": "Derived analysis record with explicit source-file lineage.",
      "encodingFormat": "application/json",
      "name": "buck-load-001.json",
      "sha256": "786e6645c7d5d7fb4b6f0e0ec1dcca3b03806727aa7eb6dd44c386a60fa0518e"
    },
    {
      "@id": "./workspace/analysis/rc-baseline-001.json",
      "@type": "File",
      "contentSize": "8690",
      "description": "Derived analysis record with explicit source-file lineage.",
      "encodingFormat": "application/json",
      "name": "rc-baseline-001.json",
      "sha256": "55a26591684c018f15e804449dc5870609b535ce7c7d52bdab0e48d5a94ea899"
    },
    {
      "@id": "./workspace/analysis/rc-swap-002.json",
      "@type": "File",
      "contentSize": "8698",
      "description": "Derived analysis record with explicit source-file lineage.",
      "encodingFormat": "application/json",
      "name": "rc-swap-002.json",
      "sha256": "c8a49af848d2a4a36fefb3ac9c536cf952132d83c8ff0ebac46132364cf6c159"
    },
    {
      "@id": "./workspace/benchlineage.json",
      "@type": "File",
      "contentSize": "404",
      "description": "File preserved from the BenchLineage workspace.",
      "encodingFormat": "application/json",
      "name": "benchlineage.json",
      "sha256": "45440da0e6d606fee44a63843c744556aec05bab9df109c9e7cfab3ae6849dd3"
    },
    {
      "@id": "./workspace/calibrations/cal-dmm-01-2026.json",
      "@type": "File",
      "contentSize": "373",
      "description": "Instrument calibration record.",
      "encodingFormat": "application/json",
      "name": "cal-dmm-01-2026.json",
      "sha256": "59bf35001aba40f43b45900d8584324e883f2b13dd886f2f97eb03f95d4a35f5"
    },
    {
      "@id": "./workspace/calibrations/cal-scope-01-2026.json",
      "@type": "File",
      "contentSize": "379",
      "description": "Instrument calibration record.",
      "encodingFormat": "application/json",
      "name": "cal-scope-01-2026.json",
      "sha256": "3b2a0702e00ed0cbe1b9e949b7973268318ddd12d0dad0ffc033c38a9c15ee5d"
    },
    {
      "@id": "./workspace/calibrations/cal-source-01-2026.json",
      "@type": "File",
      "contentSize": "382",
      "description": "Instrument calibration record.",
      "encodingFormat": "application/json",
      "name": "cal-source-01-2026.json",
      "sha256": "bf5028f10c74e0d80ed73363386644e55114f3e7ef39dbd68c15a93836b92bc6"
    },
    {
      "@id": "./workspace/data/raw/buck-load-sweep.csv",
      "@type": "File",
      "contentSize": "456",
      "description": "Raw evidence recorded by the BenchLineage workspace.",
      "encodingFormat": "text/csv",
      "name": "buck-load-sweep.csv",
      "sha256": "94adcd45d83a1a836b64182f41270bb1a6e31e0121ade82084cc7780a9e070f1"
    },
    {
      "@id": "./workspace/data/raw/rc-baseline.csv",
      "@type": "File",
      "contentSize": "1693",
      "description": "Raw evidence recorded by the BenchLineage workspace.",
      "encodingFormat": "text/csv",
      "name": "rc-baseline.csv",
      "sha256": "4266851a5cdaf4fd8cb30110c1a7de7ec19c3bc5ccd7e5b721973e7858e63a83"
    },
    {
      "@id": "./workspace/data/raw/rc-resistor-swap.csv",
      "@type": "File",
      "contentSize": "1699",
      "description": "Raw evidence recorded by the BenchLineage workspace.",
      "encodingFormat": "text/csv",
      "name": "rc-resistor-swap.csv",
      "sha256": "17608ebc141b71dbb79bc954b4826f2746a9375b8f26d96e3d56cd7e479dd9cf"
    },
    {
      "@id": "./workspace/instruments/dmm-01.json",
      "@type": "File",
      "contentSize": "333",
      "description": "Instrument identity record.",
      "encodingFormat": "application/json",
      "name": "dmm-01.json",
      "sha256": "a41557a2d2170db06b84170f695ac5cec77e9b9497ffb3d74f0efd7946ae40a5"
    },
    {
      "@id": "./workspace/instruments/scope-01.json",
      "@type": "File",
      "contentSize": "332",
      "description": "Instrument identity record.",
      "encodingFormat": "application/json",
      "name": "scope-01.json",
      "sha256": "8337dfb996cfb8c1555dfc0823c101ce4e5039b0d77a336195dd425182cf980f"
    },
    {
      "@id": "./workspace/instruments/source-01.json",
      "@type": "File",
      "contentSize": "350",
      "description": "Instrument identity record.",
      "encodingFormat": "application/json",
      "name": "source-01.json",
      "sha256": "f796b33e5f4ddac03c133d3537b3e91f906a15661bcba42022912fa0b1be46f2"
    },
    {
      "@id": "./workspace/reports/demo-report.html",
      "@type": "File",
      "contentSize": "45772",
      "description": "Self-contained human-readable evidence report.",
      "encodingFormat": "text/html",
      "name": "demo-report.html",
      "sha256": "91643fee76f5fa36c9b72b3a385c2aa25bea704282cdd34d4423d705bc7cedf0"
    },
    {
      "@id": "./workspace/runs/buck-load-001.json",
      "@type": "File",
      "contentSize": "512",
      "description": "Experimental run record.",
      "encodingFormat": "application/json",
      "name": "buck-load-001.json",
      "sha256": "f1fca5c644688a366ea4f10e3407dc358eae5ee11f8eb778c0569b409c44730f"
    },
    {
      "@id": "./workspace/runs/rc-baseline-001.json",
      "@type": "File",
      "contentSize": "530",
      "description": "Experimental run record.",
      "encodingFormat": "application/json",
      "name": "rc-baseline-001.json",
      "sha256": "7739745561dc08544192c5f31a7da02524fc9e814466a5b1b607a77d80561fb6"
    },
    {
      "@id": "./workspace/runs/rc-swap-002.json",
      "@type": "File",
      "contentSize": "592",
      "description": "Experimental run record.",
      "encodingFormat": "application/json",
      "name": "rc-swap-002.json",
      "sha256": "33a6101c6745e77f4563620d254b8fc1ac91cf542054b6505b88eea994c76f61"
    },
    {
      "@id": "./workspace/seals/seal-2026-08-04T080000-0000.json",
      "@type": "File",
      "contentSize": "3400",
      "description": "Content-addressed BenchLineage evidence seal.",
      "encodingFormat": "application/json",
      "name": "seal-2026-08-04T080000-0000.json",
      "sha256": "11d8f22c548edff7950c5805c86268c17cc80ddfa48df9fd9778c7beb4286060"
    },
    {
      "@id": "./workspace/studies/buck-efficiency.json",
      "@type": "File",
      "contentSize": "558",
      "description": "Study intent and protocol record.",
      "encodingFormat": "application/json",
      "name": "buck-efficiency.json",
      "sha256": "7e411b8f6398da3f2104e44609b4434920155b5559fd9fb78b5c10b37306ef60"
    },
    {
      "@id": "./workspace/studies/rc-filter.json",
      "@type": "File",
      "contentSize": "591",
      "description": "Study intent and protocol record.",
      "encodingFormat": "application/json",
      "name": "rc-filter.json",
      "sha256": "57dfb43bc61b148e0ba40efc70590530c0d68ba6ac6a223d61ec3e6aa4827d61"
    },
    {
      "@id": "#instrument-dmm-01",
      "@type": "IndividualProduct",
      "description": "Synthetic identity used only in the public demonstration.",
      "identifier": "dmm-01",
      "manufacturer": "Acme Metrology",
      "model": "CountPro 6.5",
      "name": "Acme Metrology CountPro 6.5",
      "productID": "EE-DEMO-002",
      "serialNumber": "SYN-DMM-0017"
    },
    {
      "@id": "#instrument-scope-01",
      "@type": "IndividualProduct",
      "description": "Synthetic identity used only in the public demonstration.",
      "identifier": "scope-01",
      "manufacturer": "Acme Metrology",
      "model": "WaveView 2000",
      "name": "Acme Metrology WaveView 2000",
      "productID": "EE-DEMO-001",
      "serialNumber": "SYN-SCOPE-0042"
    },
    {
      "@id": "#instrument-source-01",
      "@type": "IndividualProduct",
      "description": "Synthetic identity used only in the public demonstration.",
      "identifier": "source-01",
      "manufacturer": "Acme Metrology",
      "model": "SourceBox 80",
      "name": "Acme Metrology SourceBox 80",
      "productID": "EE-DEMO-003",
      "serialNumber": "SYN-SRC-0009"
    },
    {
      "@id": "#study-buck-efficiency",
      "@type": "CreativeWork",
      "abstract": "Efficiency rises at light-to-moderate load and then plateaus below 95%.",
      "dateCreated": "2026-08-04T07:59:00+00:00",
      "description": "Measure conversion efficiency and locate its observed peak across resistive loads.",
      "identifier": "buck-efficiency",
      "keywords": "efficiency, load-sweep, power-electronics",
      "name": "Buck-converter load sweep",
      "text": "Apply 12 V DC. Sweep ten resistive loads, wait for thermal stabilization, then record input/output voltage and current."
    },
    {
      "@id": "#study-rc-filter",
      "@type": "CreativeWork",
      "abstract": "The measured cutoff follows 1/(2\u03c0RC) within the expanded uncertainty.",
      "dateCreated": "2026-08-04T07:59:00+00:00",
      "description": "Estimate the -3 dB cutoff and quantify the effect of a resistor substitution.",
      "identifier": "rc-filter",
      "keywords": "analog, filter, frequency-response, metrology",
      "name": "First-order RC low-pass characterization",
      "text": "Apply a 1 V sine sweep from 20 Hz to 100 kHz. Record input amplitude, output amplitude, and phase at 41 logarithmically spaced frequencies."
    },
    {
      "@id": "#calibration-cal-dmm-01-2026",
      "@type": "CreativeWork",
      "about": {
        "@id": "#instrument-dmm-01"
      },
      "dateCreated": "2026-01-15T09:00:00+00:00",
      "expires": "2027-01-15T09:00:00+00:00",
      "identifier": "SYNTHETIC-CERT-DMM-01",
      "name": "Calibration cal-dmm-01-2026",
      "text": "Certificate SYNTHETIC-CERT-DMM-01; status valid; standard uncertainty 0.0008 V; coverage factor 2.0; valid from 2026-01-15T09:00:00+00:00 through 2027-01-15T09:00:00+00:00."
    },
    {
      "@id": "#calibration-cal-scope-01-2026",
      "@type": "CreativeWork",
      "about": {
        "@id": "#instrument-scope-01"
      },
      "dateCreated": "2026-01-15T09:00:00+00:00",
      "expires": "2027-01-15T09:00:00+00:00",
      "identifier": "SYNTHETIC-CERT-SCOPE-01",
      "name": "Calibration cal-scope-01-2026",
      "text": "Certificate SYNTHETIC-CERT-SCOPE-01; status valid; standard uncertainty 0.0025 V; coverage factor 2.0; valid from 2026-01-15T09:00:00+00:00 through 2027-01-15T09:00:00+00:00."
    },
    {
      "@id": "#calibration-cal-source-01-2026",
      "@type": "CreativeWork",
      "about": {
        "@id": "#instrument-source-01"
      },
      "dateCreated": "2026-01-15T09:00:00+00:00",
      "expires": "2027-01-15T09:00:00+00:00",
      "identifier": "SYNTHETIC-CERT-SOURCE-01",
      "name": "Calibration cal-source-01-2026",
      "text": "Certificate SYNTHETIC-CERT-SOURCE-01; status valid; standard uncertainty 0.0015 V; coverage factor 2.0; valid from 2026-01-15T09:00:00+00:00 through 2027-01-15T09:00:00+00:00."
    },
    {
      "@id": "#run-buck-load-001",
      "@type": "CreateAction",
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      },
      "agent": {
        "@id": "#person-7e1a506b2e984e7b"
      },
      "description": "Conditions: {\"ambient_temperature_degC\":24.1,\"input_setpoint_v\":12.0}. Synthetic demonstration data; no physical measurement claim.",
      "endTime": "2026-08-04T07:59:00+00:00",
      "instrument": [
        {
          "@id": "#instrument-dmm-01"
        },
        {
          "@id": "#instrument-source-01"
        }
      ],
      "name": "Experimental run buck-load-001",
      "object": {
        "@id": "#study-buck-efficiency"
      },
      "result": {
        "@id": "./workspace/data/raw/buck-load-sweep.csv"
      },
      "startTime": "2026-08-05T06:00:00+00:00"
    },
    {
      "@id": "#run-rc-baseline-001",
      "@type": "CreateAction",
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      },
      "agent": {
        "@id": "#person-7e1a506b2e984e7b"
      },
      "description": "Conditions: {\"ambient_temperature_degC\":23.4,\"nominal_c_f\":1e-08,\"nominal_r_ohm\":10000}. Synthetic demonstration data; no physical measurement claim.",
      "endTime": "2026-08-04T07:59:00+00:00",
      "instrument": [
        {
          "@id": "#instrument-scope-01"
        },
        {
          "@id": "#instrument-source-01"
        }
      ],
      "name": "Experimental run rc-baseline-001",
      "object": {
        "@id": "#study-rc-filter"
      },
      "result": {
        "@id": "./workspace/data/raw/rc-baseline.csv"
      },
      "startTime": "2026-08-04T06:00:00+00:00"
    },
    {
      "@id": "#run-rc-swap-002",
      "@type": "CreateAction",
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      },
      "agent": {
        "@id": "#person-7e1a506b2e984e7b"
      },
      "description": "Conditions: {\"ambient_temperature_degC\":23.8,\"nominal_c_f\":1e-08,\"nominal_r_ohm\":12000}. Deviations: Resistor changed from 10 kohm to 12 kohm by design.. Synthetic demonstration data; no physical measurement claim.",
      "endTime": "2026-08-04T07:59:00+00:00",
      "instrument": [
        {
          "@id": "#instrument-scope-01"
        },
        {
          "@id": "#instrument-source-01"
        }
      ],
      "name": "Experimental run rc-swap-002",
      "object": {
        "@id": "#study-rc-filter"
      },
      "result": {
        "@id": "./workspace/data/raw/rc-resistor-swap.csv"
      },
      "startTime": "2026-08-04T08:00:00+00:00"
    },
    {
      "@id": "https://pypi.org/project/benchlineage/",
      "@type": "SoftwareApplication",
      "name": "BenchLineage",
      "url": "https://github.com/CAOShurong/benchlineage",
      "version": "0.3.0"
    },
    {
      "@id": "#analysis-buck-load-001",
      "@type": "CreateAction",
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      },
      "description": "Derived analysis linked to run buck-load-001.",
      "endTime": "2026-08-04T07:59:00+00:00",
      "instrument": {
        "@id": "https://pypi.org/project/benchlineage/"
      },
      "name": "BenchLineage analysis for buck-load-001",
      "object": {
        "@id": "./workspace/data/raw/buck-load-sweep.csv"
      },
      "result": {
        "@id": "./workspace/analysis/buck-load-001.json"
      }
    },
    {
      "@id": "#analysis-rc-baseline-001",
      "@type": "CreateAction",
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      },
      "description": "Derived analysis linked to run rc-baseline-001.",
      "endTime": "2026-08-04T07:59:00+00:00",
      "instrument": {
        "@id": "https://pypi.org/project/benchlineage/"
      },
      "name": "BenchLineage analysis for rc-baseline-001",
      "object": {
        "@id": "./workspace/data/raw/rc-baseline.csv"
      },
      "result": {
        "@id": "./workspace/analysis/rc-baseline-001.json"
      }
    },
    {
      "@id": "#analysis-rc-swap-002",
      "@type": "CreateAction",
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      },
      "description": "Derived analysis linked to run rc-swap-002.",
      "endTime": "2026-08-04T07:59:00+00:00",
      "instrument": {
        "@id": "https://pypi.org/project/benchlineage/"
      },
      "name": "BenchLineage analysis for rc-swap-002",
      "object": {
        "@id": "./workspace/data/raw/rc-resistor-swap.csv"
      },
      "result": {
        "@id": "./workspace/analysis/rc-swap-002.json"
      }
    },
    {
      "@id": "#person-7e1a506b2e984e7b",
      "@type": "Person",
      "name": "Shurong Cao"
    }
  ]
}
```
