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
| eLabFTW extra fields (project, version, hash, progress, software) | `PropertyValue` `elabftw_metadata` (JSON), referenced from `variableMeasured` |
| evidence tables (CSV), printable dossier (HTML), evidence JSON, signed snapshots, checksum list, Excel workbook | `File` nodes with `sha256`, `contentSize`, `encodingFormat`, `description` |
| exporting user | `author` → `Person` |
| exporting workspace | root `publisher` → `Organization`; the author's `affiliation` |
| software | `sdPublisher` → `Organization` |
| conformance | root `conformsTo` → RO-Crate 1.2 and ELN 1.2+20260923 `Profile` entities |

`scientific_evidence.canonical.json` is the evidence in canonical byte form: `sha256sum` of that one file reproduces the evidence hash recorded in the metadata and in every signature. Empty evidence tables are listed in `SHA256SUMS.txt` but not attached.

The example was produced from the public demo dataset (a cosmetics emulsifier replacement, no real formulas): one model-recommended batch of five candidates with bench results entered, a three-replicate confirmation run, and one signed approval; the discovery and confirmation gates pass. The crate is a flattened JSON-LD graph on RO-Crate 1.2 declaring ELN 1.2+20260923. It imports into eLabFTW as one experiment with 17 attachments; the extra-fields panel needs the importer to resolve `variableMeasured` references for crates without eLabFTW's internal `version` marker (fix proposed upstream in elabftw/elabftw#7517).

## Examples

### cosmetics-peg-emulsifier-replacement-demo_qualification_dossier_v1.eln
```json
{
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.2"
      },
      "version": "1.0",
      "dateCreated": "2026-10-03T00:19:24+00:00",
      "sdPublisher": {
        "@id": "https://github.com/TM289012/reformulation-assurance"
      }
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Cosmetics: PEG emulsifier replacement (demo): qualification dossier v1 (Reformulation Assurance)",
      "description": "Qualification evidence for 'Cosmetics: PEG emulsifier replacement (demo)' exported from Reformulation Assurance v0.12.6 as one notebook entry with attached evidence files. Empty evidence tables are listed in SHA256SUMS.txt but not attached: approval_policies.csv, assignments.csv, comments.csv, robustness_runs.csv.",
      "datePublished": "2026-10-03T00:19:24+00:00",
      "publisher": {
        "@id": "#workspace-ae3e9e5a-29a1-489a-85ba-2e900563c6bf"
      },
      "license": {
        "@id": "#license"
      },
      "conformsTo": [
        {
          "@id": "https://w3id.org/ro/crate/1.2"
        },
        {
          "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+20260923"
        }
      ],
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
          "@id": "./dossier-v1/signed_evidence_snapshots/discovery_d7c1e283394d.json"
        }
      ]
    },
    {
      "@id": "https://w3id.org/ro/crate/1.2",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "RO-Crate 1.2 Specification"
    },
    {
      "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+20260923",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "ELN-File Format 1.2+20260923 Specification"
    },
    {
      "@id": "https://github.com/TM289012/reformulation-assurance",
      "@type": "Organization",
      "name": "Reformulation Assurance",
      "description": "The open-source workbench that produced this archive (v0.12.6).",
      "url": "https://github.com/TM289012/reformulation-assurance"
    },
    {
      "@id": "#workspace-ae3e9e5a-29a1-489a-85ba-2e900563c6bf",
      "@type": "Organization",
      "name": "Public Demo Lab",
      "description": "The workspace (laboratory, team or course section) that owns the evidence in this archive."
    },
    {
      "@id": "#license",
      "@type": "CreativeWork",
      "name": "All rights reserved by the exporting workspace",
      "description": "The evidence in this archive belongs to the workspace that exported it. No licence is granted by the export itself; the owner may attach one when sharing the archive."
    },
    {
      "@id": "#author-e5a05f79-0e49-42ab-aa4c-812c1868a827",
      "@type": "Person",
      "name": "Demo Explorer",
      "affiliation": {
        "@id": "#workspace-ae3e9e5a-29a1-489a-85ba-2e900563c6bf"
      },
      "givenName": "Demo",
      "familyName": "Explorer",
      "email": "demo@example.com"
    },
    {
      "@id": "./dossier-v1/",
      "@type": "Dataset",
      "name": "Cosmetics: PEG emulsifier replacement (demo): qualification dossier v1",
      "description": "Qualification dossier v1 for 'Cosmetics: PEG emulsifier replacement (demo)': gates, approvals, calibration and the evidence hash, with the evidence files attached.",
      "identifier": "66d880b8-01e4-42c0-9065-3cf922e07874",
      "genre": "experiment",
      "author": {
        "@id": "#author-e5a05f79-0e49-42ab-aa4c-812c1868a827"
      },
      "dateCreated": "2026-10-03T00:19:24+00:00",
      "dateModified": "2026-10-03T00:19:24+00:00",
      "temporal": "2026-10-03T00:19:24+00:00",
      "text": "<h1>Qualification dossier v1: Cosmetics: PEG emulsifier replacement (demo)</h1><p>Replace a discontinued PEG emulsifier in an oil-in-water lotion. 88 historical lots including 7 failed emulsions. Shared sandbox: run the model, create batches, sign approvals \u2014 data resets periodically.</p><p>Generated 2026-10-03T00:19:24+00:00 by Demo Explorer with Reformulation Assurance v0.12.6.</p><p><strong>Qualification progress:</strong> 35% &nbsp; <strong>All gates passed:</strong> No &nbsp; <strong>Best robust probability:</strong> n/a</p><p><strong>Scientific evidence SHA-256:</strong> <code>d7c1e283394da47df30e5ef9c435f79c5b17889b8e8acae93b8ad1ffd9afd2b8</code></p><p><em>Decision-support record: this entry documents software evidence and approvals. It does not replace chemical-safety review, regulatory review, a validated quality system, or final release authority.</em></p><h2>Qualification gates</h2><table class=\"dataframe evidence-table\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>stage</th>\n      <th>completed</th>\n      <th>compliant</th>\n      <th>success_rate</th>\n      <th>passing_replicate_groups</th>\n      <th>best_robust_probability</th>\n      <th>completion</th>\n      <th>gate_passed</th>\n      <th>status</th>\n      <th>remaining_requirements</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discovery</td>\n      <td>5</td>\n      <td>4</td>\n      <td>80%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>100%</td>\n      <td>True</td>\n      <td>Passed</td>\n      <td>All configured gates passed</td>\n    </tr>\n    <tr>\n      <td>confirmation</td>\n      <td>3</td>\n      <td>3</td>\n      <td>100%</td>\n      <td>1</td>\n      <td>None</td>\n      <td>100%</td>\n      <td>True</td>\n      <td>Passed</td>\n      <td>All configured gates passed</td>\n    </tr>\n    <tr>\n      <td>process_window</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 4 more completed experiment(s); Needs 3 more compliant result(s); Success rate 0% is below 75%; Best robustness result none is below 80%</td>\n    </tr>\n    <tr>\n      <td>raw_material</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 3 more completed experiment(s); Needs 3 more compliant result(s); Success rate 0% is below 80%</td>\n    </tr>\n    <tr>\n      <td>stability</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 1 more completed experiment(s); Needs 1 more compliant result(s); Success rate 0% is below 100%</td>\n    </tr>\n    <tr>\n      <td>pilot</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 1 more completed experiment(s); Needs 1 more compliant result(s); Success rate 0% is below 100%</td>\n    </tr>\n  </tbody>\n</table><h2>Approvals and signatures</h2><table class=\"dataframe evidence-table\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>stage</th>\n      <th>status</th>\n      <th>signer_name</th>\n      <th>signer_role</th>\n      <th>signed_at</th>\n      <th>matches_this_evidence</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discovery</td>\n      <td>signed</td>\n      <td>Demo Explorer</td>\n      <td>owner</td>\n      <td>2026-10-03T00:19:23+00:00</td>\n      <td>True</td>\n    </tr>\n  </tbody>\n</table><h2>Attached files</h2><ul><li><code>SHA256SUMS.txt</code> (1654 bytes, sha256 a748bec071bc7f74\u2026)</li><li><code>approvals.csv</code> (475 bytes, sha256 a37c955dbf4024fa\u2026)</li><li><code>audit_trail.csv</code> (3323 bytes, sha256 349a17609d9c2f2d\u2026)</li><li><code>calibration_formulation_observations.csv</code> (2684 bytes, sha256 f3a96bdfb3826ec8\u2026)</li><li><code>calibration_formulation_response_summary.csv</code> (338 bytes, sha256 7bf4e617157772c3\u2026)</li><li><code>calibration_run_observations.csv</code> (4276 bytes, sha256 ad6d5630c953b272\u2026)</li><li><code>calibration_run_response_summary.csv</code> (345 bytes, sha256 c80f6090a6569665\u2026)</li><li><code>cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx</code> (41416 bytes, sha256 5e667b99603f7fc3\u2026)</li><li><code>experiments.csv</code> (39894 bytes, sha256 e2f3c8041f51a933\u2026)</li><li><code>manifest.json</code> (810 bytes, sha256 1e1940588f5759db\u2026)</li><li><code>qualification_dossier.html</code> (94355 bytes, sha256 5e84b2428ff4c39f\u2026)</li><li><code>qualification_gates.csv</code> (898 bytes, sha256 41e5db72fd772f3c\u2026)</li><li><code>recommendation_batches.csv</code> (445 bytes, sha256 ccc12461871a7bfa\u2026)</li><li><code>replicate_summary.csv</code> (1929 bytes, sha256 3d4f661649b79843\u2026)</li><li><code>scientific_evidence.canonical.json</code> (140840 bytes, sha256 d7c1e283394da47d\u2026)</li><li><code>scientific_evidence.json</code> (188963 bytes, sha256 b55709d3ea458e85\u2026)</li><li><code>signed_evidence_snapshots/discovery_d7c1e283394d.json</code> (140840 bytes, sha256 d7c1e283394da47d\u2026)</li></ul><p>The full printable dossier is attached as <code>qualification_dossier.html</code>. <code>scientific_evidence.canonical.json</code> holds the complete evidence as canonical bytes: its sha256sum is the evidence hash above.</p>",
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
          "@id": "./dossier-v1/signed_evidence_snapshots/discovery_d7c1e283394d.json"
        }
      ],
      "variableMeasured": [
        {
          "@id": "#elabftw-metadata"
        },
        {
          "@id": "#scientific-evidence-sha256"
        },
        {
          "@id": "#dossier-version"
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
      "sha256": "a748bec071bc7f74c05064f21fefbd00db6dadbf7a7da84cc6b21c4ac65fecb3",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/approvals.csv",
      "@type": "File",
      "name": "approvals.csv",
      "description": "Signed approvals (evidence hash per signature).",
      "encodingFormat": "text/csv",
      "contentSize": "475",
      "sha256": "a37c955dbf4024fa5a2bf957c1880c35e82450561c4efb314019cc9339e4cab5",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/audit_trail.csv",
      "@type": "File",
      "name": "audit_trail.csv",
      "description": "Audit trail of every recorded event.",
      "encodingFormat": "text/csv",
      "contentSize": "3323",
      "sha256": "349a17609d9c2f2d33aea42b31ec32b0e4187b96ee80892430ab1d974152a2d5",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_formulation_observations.csv",
      "@type": "File",
      "name": "calibration_formulation_observations.csv",
      "description": "Formulation-level calibration observations.",
      "encodingFormat": "text/csv",
      "contentSize": "2684",
      "sha256": "f3a96bdfb3826ec8b55298bf39d621b32a8ca849bc7a566aa6e060f2e46e57a6",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_formulation_response_summary.csv",
      "@type": "File",
      "name": "calibration_formulation_response_summary.csv",
      "description": "Formulation-level prospective calibration summary.",
      "encodingFormat": "text/csv",
      "contentSize": "338",
      "sha256": "7bf4e617157772c3b5a6797a68cd6f028e290517cdbfb936daf0fbb5ec3e6fa2",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_run_observations.csv",
      "@type": "File",
      "name": "calibration_run_observations.csv",
      "description": "Run-level calibration observations.",
      "encodingFormat": "text/csv",
      "contentSize": "4276",
      "sha256": "ad6d5630c953b27251192161e390e6def001933699080c853d05d680f60bf5f9",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_run_response_summary.csv",
      "@type": "File",
      "name": "calibration_run_response_summary.csv",
      "description": "Run-level prospective calibration summary.",
      "encodingFormat": "text/csv",
      "contentSize": "345",
      "sha256": "c80f6090a656966566af5a8ff0e91b84406c54d8472d42b52e55e2c3c847421d",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx",
      "@type": "File",
      "name": "cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx",
      "description": "Excel workbook: every evidence table as a tab, evidence hash on the cover sheet.",
      "encodingFormat": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "contentSize": "41416",
      "sha256": "5e667b99603f7fc31778ada95b6c816b5db1adc93a964e17ffc66ce890421b0e",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/experiments.csv",
      "@type": "File",
      "name": "experiments.csv",
      "description": "Every experiment with recipe, responses and pass/fail status.",
      "encodingFormat": "text/csv",
      "contentSize": "39894",
      "sha256": "e2f3c8041f51a93324d7673e01b8148a8b8de0b329c3824f181cc754c3aae08c",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/manifest.json",
      "@type": "File",
      "name": "manifest.json",
      "description": "Dossier manifest: version, evidence hash, generating user, disclaimer.",
      "encodingFormat": "application/json",
      "contentSize": "810",
      "sha256": "1e1940588f5759db0514b0d42aa53a8132cc3410172cb75c8b2e869812ab686d",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/qualification_dossier.html",
      "@type": "File",
      "name": "qualification_dossier.html",
      "description": "Printable qualification dossier (the full report).",
      "encodingFormat": "text/html",
      "contentSize": "94355",
      "sha256": "5e84b2428ff4c39fcc40ea4787845cd97855131963bae781f6e5ef95294d9d3b",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/qualification_gates.csv",
      "@type": "File",
      "name": "qualification_gates.csv",
      "description": "Stage-by-stage qualification gate progress.",
      "encodingFormat": "text/csv",
      "contentSize": "898",
      "sha256": "41e5db72fd772f3c18d5ac198936eabd258f26fe838081b791772a0d3a61da16",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/recommendation_batches.csv",
      "@type": "File",
      "name": "recommendation_batches.csv",
      "description": "Recommendation batches and their approval state.",
      "encodingFormat": "text/csv",
      "contentSize": "445",
      "sha256": "ccc12461871a7bfa2038d0f29fc4701a701131e63b9603ff38d5483a34cae180",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/replicate_summary.csv",
      "@type": "File",
      "name": "replicate_summary.csv",
      "description": "Replicate groups: consistency screen, CV and gate status.",
      "encodingFormat": "text/csv",
      "contentSize": "1929",
      "sha256": "3d4f661649b7984398018a8fe17490dcd9d30c86b547f326b1e145047cf49bb7",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/scientific_evidence.canonical.json",
      "@type": "File",
      "name": "scientific_evidence.canonical.json",
      "description": "The same evidence as canonical bytes: sha256sum of this file IS the evidence hash.",
      "encodingFormat": "application/json",
      "contentSize": "140840",
      "sha256": "d7c1e283394da47df30e5ef9c435f79c5b17889b8e8acae93b8ad1ffd9afd2b8",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/scientific_evidence.json",
      "@type": "File",
      "name": "scientific_evidence.json",
      "description": "Complete scientific evidence as readable JSON.",
      "encodingFormat": "application/json",
      "contentSize": "188963",
      "sha256": "b55709d3ea458e85668c6070367ae73e03b9afbdc0a80e0b01c5348dec002fd9",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "./dossier-v1/signed_evidence_snapshots/discovery_d7c1e283394d.json",
      "@type": "File",
      "name": "discovery_d7c1e283394d.json",
      "description": "Evidence snapshot frozen at signing; re-hashing it reproduces the hash recorded with the signature.",
      "encodingFormat": "application/json",
      "contentSize": "140840",
      "sha256": "d7c1e283394da47df30e5ef9c435f79c5b17889b8e8acae93b8ad1ffd9afd2b8",
      "dateCreated": "2026-10-03T00:19:24+00:00"
    },
    {
      "@id": "#elabftw-metadata",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "name": "eLabFTW extra fields",
      "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Reformulation Assurance\"}]}, \"extra_fields\": {\"All gates passed\": {\"group_id\": 1, \"position\": 6, \"readonly\": true, \"type\": \"checkbox\", \"value\": \"\"}, \"Best robust probability\": {\"group_id\": 1, \"position\": 7, \"readonly\": true, \"type\": \"text\", \"value\": \"n/a\"}, \"Disclaimer\": {\"group_id\": 1, \"position\": 12, \"readonly\": true, \"type\": \"text\", \"value\": \"Prototype decision-support evidence; not a validated regulated quality system.\"}, \"Dossier id\": {\"group_id\": 1, \"position\": 2, \"readonly\": true, \"type\": \"text\", \"value\": \"66d880b8-01e4-42c0-9065-3cf922e07874\"}, \"Dossier version\": {\"group_id\": 1, \"position\": 3, \"readonly\": true, \"type\": \"number\", \"value\": \"1\"}, \"Generated at (UTC)\": {\"group_id\": 1, \"position\": 8, \"readonly\": true, \"type\": \"text\", \"value\": \"2026-10-03T00:19:24+00:00\"}, \"Generated by\": {\"group_id\": 1, \"position\": 9, \"readonly\": true, \"type\": \"text\", \"value\": \"Demo Explorer\"}, \"Project\": {\"group_id\": 1, \"position\": 0, \"readonly\": true, \"type\": \"text\", \"value\": \"Cosmetics: PEG emulsifier replacement (demo)\"}, \"Project id\": {\"group_id\": 1, \"position\": 1, \"readonly\": true, \"type\": \"text\", \"value\": \"96886997-c8c7-4639-83e8-b9736e40aa84\"}, \"Qualification progress (%)\": {\"group_id\": 1, \"position\": 5, \"readonly\": true, \"type\": \"number\", \"value\": \"35\"}, \"Scientific evidence SHA-256\": {\"group_id\": 1, \"position\": 4, \"readonly\": true, \"type\": \"text\", \"value\": \"d7c1e283394da47df30e5ef9c435f79c5b17889b8e8acae93b8ad1ffd9afd2b8\"}, \"Software\": {\"group_id\": 1, \"position\": 10, \"readonly\": true, \"type\": \"text\", \"value\": \"Reformulation Assurance v0.12.6\"}, \"Software URL\": {\"group_id\": 1, \"position\": 11, \"readonly\": true, \"type\": \"url\", \"value\": \"https://github.com/TM289012/reformulation-assurance\"}}}"
    },
    {
      "@id": "#scientific-evidence-sha256",
      "@type": "PropertyValue",
      "propertyID": "scientific_evidence_sha256",
      "name": "Scientific evidence SHA-256",
      "value": "d7c1e283394da47df30e5ef9c435f79c5b17889b8e8acae93b8ad1ffd9afd2b8"
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
