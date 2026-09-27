# Reformulation Assurance example

[Repository](https://github.com/TM289012/reformulation-assurance) · export only

## Overview

Reformulation Assurance is an open-source, local-first workbench for ingredient-replacement projects in formulated products (coatings, cosmetics, adhesives, anything mixed to a specification). It suggests the next experiments from a lab's batch history, tracks results through staged qualification gates, and binds sign-offs to a SHA-256 hash of the frozen evidence.

The `.eln` export files one project's qualification dossier into a lab notebook as **one experiment entry** with the evidence attached:

| Reformulation Assurance concept | JSON property |
|---|---|
| project dossier (one per export) | root `hasPart` → one `Dataset` with `genre: experiment` |
| dossier summary (gates, approvals, evidence hash) | `text` (HTML) |
| dossier id, version | `identifier`, `PropertyValue` `dossier_version` |
| evidence hash | `PropertyValue` `scientific_evidence_sha256` |
| eLabFTW extra fields (project, version, hash, progress, software) | `PropertyValue` `elabftw_metadata` (JSON, inline in `variableMeasured`) |
| evidence tables (CSV), printable dossier (HTML), evidence JSON, signed snapshots, checksum list, Excel workbook | `File` nodes with `sha256`, `contentSize`, `encodingFormat`, `description` |
| exporting user | `author` → `Person` |
| software | `sdPublisher` → `Organization` |

`scientific_evidence.canonical.json` is the evidence in canonical byte form: `sha256sum` of that one file reproduces the evidence hash recorded in the metadata and in every signature. Empty evidence tables are listed in `SHA256SUMS.txt` but not attached.

The example was produced from the public demo dataset (a cosmetics emulsifier replacement, no real formulas): one model-recommended batch of five candidates with bench results entered, a three-replicate confirmation run, and one signed approval; the discovery and confirmation gates pass. It imports into eLabFTW as one experiment with 17 attachments and the extra-fields panel populated.

## Examples

### cosmetics-peg-emulsifier-replacement-demo_qualification_dossier_v1.eln
```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
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
      "version": "1.0",
      "dateCreated": "2026-09-27T06:21:46+00:00",
      "sdPublisher": {
        "@id": "https://github.com/TM289012/reformulation-assurance"
      }
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Cosmetics: PEG emulsifier replacement (demo): qualification dossier v1 (Reformulation Assurance)",
      "description": "Qualification evidence for 'Cosmetics: PEG emulsifier replacement (demo)' exported from Reformulation Assurance v0.12.1 as one notebook entry with attached evidence files. Empty evidence tables are listed in SHA256SUMS.txt but not attached: approval_policies.csv, assignments.csv, comments.csv, robustness_runs.csv.",
      "datePublished": "2026-09-27T06:21:46+00:00",
      "hasPart": [
        {
          "@id": "./dossier-v1/"
        },
        {
          "@id": "./dossier-v1/SHA256SUMS.txt"
        },
        {
          "@id": "./dossier-v1/approvals.csv"
        },
        {
          "@id": "./dossier-v1/audit_trail.csv"
        },
        {
          "@id": "./dossier-v1/calibration_formulation_observations.csv"
        },
        {
          "@id": "./dossier-v1/calibration_formulation_response_summary.csv"
        },
        {
          "@id": "./dossier-v1/calibration_run_observations.csv"
        },
        {
          "@id": "./dossier-v1/calibration_run_response_summary.csv"
        },
        {
          "@id": "./dossier-v1/cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx"
        },
        {
          "@id": "./dossier-v1/experiments.csv"
        },
        {
          "@id": "./dossier-v1/manifest.json"
        },
        {
          "@id": "./dossier-v1/qualification_dossier.html"
        },
        {
          "@id": "./dossier-v1/qualification_gates.csv"
        },
        {
          "@id": "./dossier-v1/recommendation_batches.csv"
        },
        {
          "@id": "./dossier-v1/replicate_summary.csv"
        },
        {
          "@id": "./dossier-v1/scientific_evidence.canonical.json"
        },
        {
          "@id": "./dossier-v1/scientific_evidence.json"
        },
        {
          "@id": "./dossier-v1/signed_evidence_snapshots/discovery_618dbe66870f.json"
        }
      ]
    },
    {
      "@id": "https://github.com/TM289012/reformulation-assurance",
      "@type": "Organization",
      "name": "Reformulation Assurance",
      "url": "https://github.com/TM289012/reformulation-assurance"
    },
    {
      "@id": "./author/edb62bfc-2b57-41a4-82e0-546620a45f11",
      "@type": "Person",
      "name": "Demo Explorer",
      "givenName": "Demo",
      "familyName": "Explorer",
      "email": "demo@example.com"
    },
    {
      "@id": "./dossier-v1/",
      "@type": "Dataset",
      "name": "Cosmetics: PEG emulsifier replacement (demo): qualification dossier v1",
      "identifier": "351873b7-5f75-4a80-9b49-fcf498f0ab9f",
      "genre": "experiment",
      "author": {
        "@id": "./author/edb62bfc-2b57-41a4-82e0-546620a45f11"
      },
      "dateCreated": "2026-09-27T06:21:46+00:00",
      "dateModified": "2026-09-27T06:21:46+00:00",
      "temporal": "2026-09-27T06:21:46+00:00",
      "text": "<h1>Qualification dossier v1: Cosmetics: PEG emulsifier replacement (demo)</h1><p>Replace a discontinued PEG emulsifier in an oil-in-water lotion. 88 historical lots including 7 failed emulsions. Shared sandbox: run the model, create batches, sign approvals \u2014 data resets periodically.</p><p>Generated 2026-09-27T06:21:46+00:00 by Demo Explorer with Reformulation Assurance v0.12.1.</p><p><strong>Qualification progress:</strong> 35% &nbsp; <strong>All gates passed:</strong> No &nbsp; <strong>Best robust probability:</strong> n/a</p><p><strong>Scientific evidence SHA-256:</strong> <code>618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884</code></p><p><em>Decision-support record: this entry documents software evidence and approvals. It does not replace chemical-safety review, regulatory review, a validated quality system, or final release authority.</em></p><h2>Qualification gates</h2><table class=\"dataframe evidence-table\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>stage</th>\n      <th>completed</th>\n      <th>compliant</th>\n      <th>success_rate</th>\n      <th>passing_replicate_groups</th>\n      <th>best_robust_probability</th>\n      <th>completion</th>\n      <th>gate_passed</th>\n      <th>status</th>\n      <th>remaining_requirements</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discovery</td>\n      <td>5</td>\n      <td>4</td>\n      <td>80%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>100%</td>\n      <td>True</td>\n      <td>Passed</td>\n      <td>All configured gates passed</td>\n    </tr>\n    <tr>\n      <td>confirmation</td>\n      <td>3</td>\n      <td>3</td>\n      <td>100%</td>\n      <td>1</td>\n      <td>None</td>\n      <td>100%</td>\n      <td>True</td>\n      <td>Passed</td>\n      <td>All configured gates passed</td>\n    </tr>\n    <tr>\n      <td>process_window</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 4 more completed experiment(s); Needs 3 more compliant result(s); Success rate 0% is below 75%; Best robustness result none is below 80%</td>\n    </tr>\n    <tr>\n      <td>raw_material</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 3 more completed experiment(s); Needs 3 more compliant result(s); Success rate 0% is below 80%</td>\n    </tr>\n    <tr>\n      <td>stability</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 1 more completed experiment(s); Needs 1 more compliant result(s); Success rate 0% is below 100%</td>\n    </tr>\n    <tr>\n      <td>pilot</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 1 more completed experiment(s); Needs 1 more compliant result(s); Success rate 0% is below 100%</td>\n    </tr>\n  </tbody>\n</table><h2>Approvals and signatures</h2><table class=\"dataframe evidence-table\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>stage</th>\n      <th>status</th>\n      <th>signer_name</th>\n      <th>signer_role</th>\n      <th>signed_at</th>\n      <th>matches_this_evidence</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discovery</td>\n      <td>signed</td>\n      <td>Demo Explorer</td>\n      <td>owner</td>\n      <td>2026-09-27T06:21:45+00:00</td>\n      <td>True</td>\n    </tr>\n  </tbody>\n</table><h2>Attached files</h2><ul><li><code>SHA256SUMS.txt</code> (1654 bytes, sha256 82d15e447d5269f6\u2026)</li><li><code>approvals.csv</code> (475 bytes, sha256 4861fd2b415c6ec0\u2026)</li><li><code>audit_trail.csv</code> (3664 bytes, sha256 2eba448c1979935e\u2026)</li><li><code>calibration_formulation_observations.csv</code> (2676 bytes, sha256 7321d058171acb5a\u2026)</li><li><code>calibration_formulation_response_summary.csv</code> (340 bytes, sha256 6695062e465cf201\u2026)</li><li><code>calibration_run_observations.csv</code> (2676 bytes, sha256 7321d058171acb5a\u2026)</li><li><code>calibration_run_response_summary.csv</code> (340 bytes, sha256 6695062e465cf201\u2026)</li><li><code>cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx</code> (40609 bytes, sha256 3a22245f419f742b\u2026)</li><li><code>experiments.csv</code> (36315 bytes, sha256 1a4cfcbacb40eb81\u2026)</li><li><code>manifest.json</code> (810 bytes, sha256 efa76bfb69aabcfe\u2026)</li><li><code>qualification_dossier.html</code> (91395 bytes, sha256 29602ff31a57ea62\u2026)</li><li><code>qualification_gates.csv</code> (898 bytes, sha256 41e5db72fd772f3c\u2026)</li><li><code>recommendation_batches.csv</code> (687 bytes, sha256 7c22f911db3f84bc\u2026)</li><li><code>replicate_summary.csv</code> (1649 bytes, sha256 d62379015c86c1a2\u2026)</li><li><code>scientific_evidence.canonical.json</code> (132091 bytes, sha256 618dbe66870f989b\u2026)</li><li><code>scientific_evidence.json</code> (176943 bytes, sha256 cb8a1158dc2b26d9\u2026)</li><li><code>signed_evidence_snapshots/discovery_618dbe66870f.json</code> (132091 bytes, sha256 618dbe66870f989b\u2026)</li></ul><p>The full printable dossier is attached as <code>qualification_dossier.html</code>. <code>scientific_evidence.canonical.json</code> holds the complete evidence as canonical bytes: its sha256sum is the evidence hash above.</p>",
      "keywords": "reformulation assurance, qualification dossier, formulation",
      "url": "https://github.com/TM289012/reformulation-assurance",
      "hasPart": [
        {
          "@id": "./dossier-v1/SHA256SUMS.txt"
        },
        {
          "@id": "./dossier-v1/approvals.csv"
        },
        {
          "@id": "./dossier-v1/audit_trail.csv"
        },
        {
          "@id": "./dossier-v1/calibration_formulation_observations.csv"
        },
        {
          "@id": "./dossier-v1/calibration_formulation_response_summary.csv"
        },
        {
          "@id": "./dossier-v1/calibration_run_observations.csv"
        },
        {
          "@id": "./dossier-v1/calibration_run_response_summary.csv"
        },
        {
          "@id": "./dossier-v1/cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx"
        },
        {
          "@id": "./dossier-v1/experiments.csv"
        },
        {
          "@id": "./dossier-v1/manifest.json"
        },
        {
          "@id": "./dossier-v1/qualification_dossier.html"
        },
        {
          "@id": "./dossier-v1/qualification_gates.csv"
        },
        {
          "@id": "./dossier-v1/recommendation_batches.csv"
        },
        {
          "@id": "./dossier-v1/replicate_summary.csv"
        },
        {
          "@id": "./dossier-v1/scientific_evidence.canonical.json"
        },
        {
          "@id": "./dossier-v1/scientific_evidence.json"
        },
        {
          "@id": "./dossier-v1/signed_evidence_snapshots/discovery_618dbe66870f.json"
        }
      ],
      "variableMeasured": [
        {
          "@id": "#elabftw-metadata",
          "@type": "PropertyValue",
          "propertyID": "elabftw_metadata",
          "name": "eLabFTW extra fields",
          "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Reformulation Assurance\"}]}, \"extra_fields\": {\"All gates passed\": {\"group_id\": 1, \"position\": 6, \"readonly\": true, \"type\": \"checkbox\", \"value\": \"\"}, \"Best robust probability\": {\"group_id\": 1, \"position\": 7, \"readonly\": true, \"type\": \"text\", \"value\": \"n/a\"}, \"Disclaimer\": {\"group_id\": 1, \"position\": 12, \"readonly\": true, \"type\": \"text\", \"value\": \"Prototype decision-support evidence; not a validated regulated quality system.\"}, \"Dossier id\": {\"group_id\": 1, \"position\": 2, \"readonly\": true, \"type\": \"text\", \"value\": \"351873b7-5f75-4a80-9b49-fcf498f0ab9f\"}, \"Dossier version\": {\"group_id\": 1, \"position\": 3, \"readonly\": true, \"type\": \"number\", \"value\": \"1\"}, \"Generated at (UTC)\": {\"group_id\": 1, \"position\": 8, \"readonly\": true, \"type\": \"text\", \"value\": \"2026-09-27T06:21:46+00:00\"}, \"Generated by\": {\"group_id\": 1, \"position\": 9, \"readonly\": true, \"type\": \"text\", \"value\": \"Demo Explorer\"}, \"Project\": {\"group_id\": 1, \"position\": 0, \"readonly\": true, \"type\": \"text\", \"value\": \"Cosmetics: PEG emulsifier replacement (demo)\"}, \"Project id\": {\"group_id\": 1, \"position\": 1, \"readonly\": true, \"type\": \"text\", \"value\": \"1416bb7b-e4c3-431d-a261-e6f36b723d1c\"}, \"Qualification progress (%)\": {\"group_id\": 1, \"position\": 5, \"readonly\": true, \"type\": \"number\", \"value\": \"35\"}, \"Scientific evidence SHA-256\": {\"group_id\": 1, \"position\": 4, \"readonly\": true, \"type\": \"text\", \"value\": \"618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884\"}, \"Software\": {\"group_id\": 1, \"position\": 10, \"readonly\": true, \"type\": \"text\", \"value\": \"Reformulation Assurance v0.12.1\"}, \"Software URL\": {\"group_id\": 1, \"position\": 11, \"readonly\": true, \"type\": \"url\", \"value\": \"https://github.com/TM289012/reformulation-assurance\"}}}"
        },
        {
          "@id": "#scientific-evidence-sha256",
          "@type": "PropertyValue",
          "propertyID": "scientific_evidence_sha256",
          "name": "Scientific evidence SHA-256",
          "value": "618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884"
        },
        {
          "@id": "#dossier-version",
          "@type": "PropertyValue",
          "propertyID": "dossier_version",
          "name": "Dossier version",
          "value": "1"
        }
      ]
    },
    {
      "@id": "./dossier-v1/SHA256SUMS.txt",
      "@type": "File",
      "name": "SHA256SUMS.txt",
      "description": "SHA-256 of every file in the dossier package.",
      "encodingFormat": "text/plain",
      "contentSize": "1654",
      "sha256": "82d15e447d5269f6dfad0b1d1bc539e116e6b42bbc82996bb84e78e5ec1ca4db",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/approvals.csv",
      "@type": "File",
      "name": "approvals.csv",
      "description": "Signed approvals (evidence hash per signature).",
      "encodingFormat": "text/csv",
      "contentSize": "475",
      "sha256": "4861fd2b415c6ec03e4680cefac62b6c5adde17428eb729a3c24e2ccf34df0e5",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/audit_trail.csv",
      "@type": "File",
      "name": "audit_trail.csv",
      "description": "Audit trail of every recorded event.",
      "encodingFormat": "text/csv",
      "contentSize": "3664",
      "sha256": "2eba448c1979935e71366394fad16acefed4a84edc3e71a79f5ed137081ea4e3",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_formulation_observations.csv",
      "@type": "File",
      "name": "calibration_formulation_observations.csv",
      "description": "Formulation-level calibration observations.",
      "encodingFormat": "text/csv",
      "contentSize": "2676",
      "sha256": "7321d058171acb5a364972380cbbeda8bfea4838bcc8c97ab7b189da71ad38b9",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_formulation_response_summary.csv",
      "@type": "File",
      "name": "calibration_formulation_response_summary.csv",
      "description": "Formulation-level prospective calibration summary.",
      "encodingFormat": "text/csv",
      "contentSize": "340",
      "sha256": "6695062e465cf201b60a08649b6161522b1dbe5a6e9bb2bb17fee5bc3d47ec24",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_run_observations.csv",
      "@type": "File",
      "name": "calibration_run_observations.csv",
      "description": "Run-level calibration observations.",
      "encodingFormat": "text/csv",
      "contentSize": "2676",
      "sha256": "7321d058171acb5a364972380cbbeda8bfea4838bcc8c97ab7b189da71ad38b9",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_run_response_summary.csv",
      "@type": "File",
      "name": "calibration_run_response_summary.csv",
      "description": "Run-level prospective calibration summary.",
      "encodingFormat": "text/csv",
      "contentSize": "340",
      "sha256": "6695062e465cf201b60a08649b6161522b1dbe5a6e9bb2bb17fee5bc3d47ec24",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx",
      "@type": "File",
      "name": "cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx",
      "description": "Excel workbook: every evidence table as a tab, evidence hash on the cover sheet.",
      "encodingFormat": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "contentSize": "40609",
      "sha256": "3a22245f419f742b5fc3695fa02ac28c66c1c4db41f32a0da2c6a5cdb1df24da",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/experiments.csv",
      "@type": "File",
      "name": "experiments.csv",
      "description": "Every experiment with recipe, responses and pass/fail status.",
      "encodingFormat": "text/csv",
      "contentSize": "36315",
      "sha256": "1a4cfcbacb40eb81a70e42c5b678c3b12a7cf44ebb72198d620459faa6d13066",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/manifest.json",
      "@type": "File",
      "name": "manifest.json",
      "description": "Dossier manifest: version, evidence hash, generating user, disclaimer.",
      "encodingFormat": "application/json",
      "contentSize": "810",
      "sha256": "efa76bfb69aabcfe661055533cdbb1cbcc289c4844c6b33e64750a569beed20e",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/qualification_dossier.html",
      "@type": "File",
      "name": "qualification_dossier.html",
      "description": "Printable qualification dossier (the full report).",
      "encodingFormat": "text/html",
      "contentSize": "91395",
      "sha256": "29602ff31a57ea6230476e3d4ef32308a868e1546bf38aeaf46e7d8016c43d9b",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/qualification_gates.csv",
      "@type": "File",
      "name": "qualification_gates.csv",
      "description": "Stage-by-stage qualification gate progress.",
      "encodingFormat": "text/csv",
      "contentSize": "898",
      "sha256": "41e5db72fd772f3c18d5ac198936eabd258f26fe838081b791772a0d3a61da16",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/recommendation_batches.csv",
      "@type": "File",
      "name": "recommendation_batches.csv",
      "description": "Recommendation batches and their approval state.",
      "encodingFormat": "text/csv",
      "contentSize": "687",
      "sha256": "7c22f911db3f84bce5a45780513b2758cfc6a02f19e235c41f4dd4c7e67aa794",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/replicate_summary.csv",
      "@type": "File",
      "name": "replicate_summary.csv",
      "description": "Replicate groups: consistency screen, CV and gate status.",
      "encodingFormat": "text/csv",
      "contentSize": "1649",
      "sha256": "d62379015c86c1a2e26c556f822d8728145adaeb968f455812f7621716bf2b1f",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/scientific_evidence.canonical.json",
      "@type": "File",
      "name": "scientific_evidence.canonical.json",
      "description": "The same evidence as canonical bytes: sha256sum of this file IS the evidence hash.",
      "encodingFormat": "application/json",
      "contentSize": "132091",
      "sha256": "618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/scientific_evidence.json",
      "@type": "File",
      "name": "scientific_evidence.json",
      "description": "Complete scientific evidence as readable JSON.",
      "encodingFormat": "application/json",
      "contentSize": "176943",
      "sha256": "cb8a1158dc2b26d9c636e085a7d21b09d3365a4d3ee581e726696bd821f3cf69",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "./dossier-v1/signed_evidence_snapshots/discovery_618dbe66870f.json",
      "@type": "File",
      "name": "discovery_618dbe66870f.json",
      "description": "Evidence snapshot frozen at signing; re-hashing it reproduces the hash recorded with the signature.",
      "encodingFormat": "application/json",
      "contentSize": "132091",
      "sha256": "618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884",
      "dateCreated": "2026-09-27T06:21:46+00:00"
    },
    {
      "@id": "#elabftw-metadata",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "name": "eLabFTW extra fields",
      "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Reformulation Assurance\"}]}, \"extra_fields\": {\"All gates passed\": {\"group_id\": 1, \"position\": 6, \"readonly\": true, \"type\": \"checkbox\", \"value\": \"\"}, \"Best robust probability\": {\"group_id\": 1, \"position\": 7, \"readonly\": true, \"type\": \"text\", \"value\": \"n/a\"}, \"Disclaimer\": {\"group_id\": 1, \"position\": 12, \"readonly\": true, \"type\": \"text\", \"value\": \"Prototype decision-support evidence; not a validated regulated quality system.\"}, \"Dossier id\": {\"group_id\": 1, \"position\": 2, \"readonly\": true, \"type\": \"text\", \"value\": \"351873b7-5f75-4a80-9b49-fcf498f0ab9f\"}, \"Dossier version\": {\"group_id\": 1, \"position\": 3, \"readonly\": true, \"type\": \"number\", \"value\": \"1\"}, \"Generated at (UTC)\": {\"group_id\": 1, \"position\": 8, \"readonly\": true, \"type\": \"text\", \"value\": \"2026-09-27T06:21:46+00:00\"}, \"Generated by\": {\"group_id\": 1, \"position\": 9, \"readonly\": true, \"type\": \"text\", \"value\": \"Demo Explorer\"}, \"Project\": {\"group_id\": 1, \"position\": 0, \"readonly\": true, \"type\": \"text\", \"value\": \"Cosmetics: PEG emulsifier replacement (demo)\"}, \"Project id\": {\"group_id\": 1, \"position\": 1, \"readonly\": true, \"type\": \"text\", \"value\": \"1416bb7b-e4c3-431d-a261-e6f36b723d1c\"}, \"Qualification progress (%)\": {\"group_id\": 1, \"position\": 5, \"readonly\": true, \"type\": \"number\", \"value\": \"35\"}, \"Scientific evidence SHA-256\": {\"group_id\": 1, \"position\": 4, \"readonly\": true, \"type\": \"text\", \"value\": \"618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884\"}, \"Software\": {\"group_id\": 1, \"position\": 10, \"readonly\": true, \"type\": \"text\", \"value\": \"Reformulation Assurance v0.12.1\"}, \"Software URL\": {\"group_id\": 1, \"position\": 11, \"readonly\": true, \"type\": \"url\", \"value\": \"https://github.com/TM289012/reformulation-assurance\"}}}"
    },
    {
      "@id": "#scientific-evidence-sha256",
      "@type": "PropertyValue",
      "propertyID": "scientific_evidence_sha256",
      "name": "Scientific evidence SHA-256",
      "value": "618dbe66870f989bc8a1bf3b66b3ed313409a13872ccdfd317fdb6617ab02884"
    },
    {
      "@id": "#dossier-version",
      "@type": "PropertyValue",
      "propertyID": "dossier_version",
      "name": "Dossier version",
      "value": "1"
    }
  ]
}
```
