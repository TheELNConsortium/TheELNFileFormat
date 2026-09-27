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
| conformance | root `conformsTo` → RO-Crate 1.2 and ELN 1.2+202609 `Profile` entities |

`scientific_evidence.canonical.json` is the evidence in canonical byte form: `sha256sum` of that one file reproduces the evidence hash recorded in the metadata and in every signature. Empty evidence tables are listed in `SHA256SUMS.txt` but not attached.

The example was produced from the public demo dataset (a cosmetics emulsifier replacement, no real formulas): one model-recommended batch of five candidates with bench results entered, a three-replicate confirmation run, and one signed approval; the discovery and confirmation gates pass. The crate is a flattened JSON-LD graph on RO-Crate 1.2 declaring ELN 1.2+202609. It imports into eLabFTW as one experiment with 17 attachments; the extra-fields panel needs the importer to resolve `variableMeasured` references for crates without eLabFTW's internal `version` marker (reported upstream).

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
      "dateCreated": "2026-09-27T21:53:53+00:00",
      "sdPublisher": {
        "@id": "https://github.com/TM289012/reformulation-assurance"
      }
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Cosmetics: PEG emulsifier replacement (demo): qualification dossier v1 (Reformulation Assurance)",
      "description": "Qualification evidence for 'Cosmetics: PEG emulsifier replacement (demo)' exported from Reformulation Assurance v0.12.4 as one notebook entry with attached evidence files. Empty evidence tables are listed in SHA256SUMS.txt but not attached: approval_policies.csv, assignments.csv, comments.csv, robustness_runs.csv.",
      "datePublished": "2026-09-27T21:53:53+00:00",
      "publisher": {
        "@id": "#workspace-53002a18-b57c-4450-b2ea-d4c2f31dd414"
      },
      "license": {
        "@id": "#license"
      },
      "conformsTo": [
        {
          "@id": "https://w3id.org/ro/crate/1.2"
        },
        {
          "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609"
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
          "@id": "./dossier-v1/signed_evidence_snapshots/discovery_856f12ed7d60.json"
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
      "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "ELN-File Format 1.2+202609 Specification"
    },
    {
      "@id": "https://github.com/TM289012/reformulation-assurance",
      "@type": "Organization",
      "name": "Reformulation Assurance",
      "description": "The open-source workbench that produced this archive (v0.12.4).",
      "url": "https://github.com/TM289012/reformulation-assurance"
    },
    {
      "@id": "#workspace-53002a18-b57c-4450-b2ea-d4c2f31dd414",
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
      "@id": "#author-4863c8b7-7f09-4a23-8d37-84412e7dc72d",
      "@type": "Person",
      "name": "Demo Explorer",
      "affiliation": {
        "@id": "#workspace-53002a18-b57c-4450-b2ea-d4c2f31dd414"
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
      "identifier": "bdcde038-c16a-463c-bd90-3fb930f89528",
      "genre": "experiment",
      "author": {
        "@id": "#author-4863c8b7-7f09-4a23-8d37-84412e7dc72d"
      },
      "dateCreated": "2026-09-27T21:53:53+00:00",
      "dateModified": "2026-09-27T21:53:53+00:00",
      "temporal": "2026-09-27T21:53:53+00:00",
      "text": "<h1>Qualification dossier v1: Cosmetics: PEG emulsifier replacement (demo)</h1><p>Replace a discontinued PEG emulsifier in an oil-in-water lotion. 88 historical lots including 7 failed emulsions. Shared sandbox: run the model, create batches, sign approvals \u2014 data resets periodically.</p><p>Generated 2026-09-27T21:53:53+00:00 by Demo Explorer with Reformulation Assurance v0.12.4.</p><p><strong>Qualification progress:</strong> 35% &nbsp; <strong>All gates passed:</strong> No &nbsp; <strong>Best robust probability:</strong> n/a</p><p><strong>Scientific evidence SHA-256:</strong> <code>856f12ed7d606e65c207cab1f617f17cd121790ae729afea1f7421516a278666</code></p><p><em>Decision-support record: this entry documents software evidence and approvals. It does not replace chemical-safety review, regulatory review, a validated quality system, or final release authority.</em></p><h2>Qualification gates</h2><table class=\"dataframe evidence-table\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>stage</th>\n      <th>completed</th>\n      <th>compliant</th>\n      <th>success_rate</th>\n      <th>passing_replicate_groups</th>\n      <th>best_robust_probability</th>\n      <th>completion</th>\n      <th>gate_passed</th>\n      <th>status</th>\n      <th>remaining_requirements</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discovery</td>\n      <td>5</td>\n      <td>4</td>\n      <td>80%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>100%</td>\n      <td>True</td>\n      <td>Passed</td>\n      <td>All configured gates passed</td>\n    </tr>\n    <tr>\n      <td>confirmation</td>\n      <td>3</td>\n      <td>3</td>\n      <td>100%</td>\n      <td>1</td>\n      <td>None</td>\n      <td>100%</td>\n      <td>True</td>\n      <td>Passed</td>\n      <td>All configured gates passed</td>\n    </tr>\n    <tr>\n      <td>process_window</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 4 more completed experiment(s); Needs 3 more compliant result(s); Success rate 0% is below 75%; Best robustness result none is below 80%</td>\n    </tr>\n    <tr>\n      <td>raw_material</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 3 more completed experiment(s); Needs 3 more compliant result(s); Success rate 0% is below 80%</td>\n    </tr>\n    <tr>\n      <td>stability</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 1 more completed experiment(s); Needs 1 more compliant result(s); Success rate 0% is below 100%</td>\n    </tr>\n    <tr>\n      <td>pilot</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0%</td>\n      <td>0</td>\n      <td>None</td>\n      <td>0%</td>\n      <td>False</td>\n      <td>Not started</td>\n      <td>Needs 1 more completed experiment(s); Needs 1 more compliant result(s); Success rate 0% is below 100%</td>\n    </tr>\n  </tbody>\n</table><h2>Approvals and signatures</h2><table class=\"dataframe evidence-table\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>stage</th>\n      <th>status</th>\n      <th>signer_name</th>\n      <th>signer_role</th>\n      <th>signed_at</th>\n      <th>matches_this_evidence</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discovery</td>\n      <td>signed</td>\n      <td>Demo Explorer</td>\n      <td>owner</td>\n      <td>2026-09-27T21:53:53+00:00</td>\n      <td>True</td>\n    </tr>\n  </tbody>\n</table><h2>Attached files</h2><ul><li><code>SHA256SUMS.txt</code> (1654 bytes, sha256 2aac821aac9b3a0b\u2026)</li><li><code>approvals.csv</code> (475 bytes, sha256 7041998afa35da20\u2026)</li><li><code>audit_trail.csv</code> (3664 bytes, sha256 45733278a25fd6f8\u2026)</li><li><code>calibration_formulation_observations.csv</code> (2674 bytes, sha256 672b78e5c13ba41f\u2026)</li><li><code>calibration_formulation_response_summary.csv</code> (340 bytes, sha256 6695062e465cf201\u2026)</li><li><code>calibration_run_observations.csv</code> (2674 bytes, sha256 672b78e5c13ba41f\u2026)</li><li><code>calibration_run_response_summary.csv</code> (340 bytes, sha256 6695062e465cf201\u2026)</li><li><code>cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx</code> (40600 bytes, sha256 734c4227b5b00e2f\u2026)</li><li><code>experiments.csv</code> (36318 bytes, sha256 02a27592f61dffd8\u2026)</li><li><code>manifest.json</code> (810 bytes, sha256 6247aaf640ed04e5\u2026)</li><li><code>qualification_dossier.html</code> (91398 bytes, sha256 dc9d4910d1d1fab2\u2026)</li><li><code>qualification_gates.csv</code> (898 bytes, sha256 41e5db72fd772f3c\u2026)</li><li><code>recommendation_batches.csv</code> (687 bytes, sha256 47f37f79aec91910\u2026)</li><li><code>replicate_summary.csv</code> (1649 bytes, sha256 d62379015c86c1a2\u2026)</li><li><code>scientific_evidence.canonical.json</code> (132096 bytes, sha256 856f12ed7d606e65\u2026)</li><li><code>scientific_evidence.json</code> (176948 bytes, sha256 dfdbc35938aa19e2\u2026)</li><li><code>signed_evidence_snapshots/discovery_856f12ed7d60.json</code> (132096 bytes, sha256 856f12ed7d606e65\u2026)</li></ul><p>The full printable dossier is attached as <code>qualification_dossier.html</code>. <code>scientific_evidence.canonical.json</code> holds the complete evidence as canonical bytes: its sha256sum is the evidence hash above.</p>",
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
          "@id": "./dossier-v1/signed_evidence_snapshots/discovery_856f12ed7d60.json"
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
      "sha256": "2aac821aac9b3a0b0d00470808c3e7837f63f87ef3751d5c8be48b3e704ccc23",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/approvals.csv",
      "@type": "File",
      "name": "approvals.csv",
      "description": "Signed approvals (evidence hash per signature).",
      "encodingFormat": "text/csv",
      "contentSize": "475",
      "sha256": "7041998afa35da20a20ee1c8f079645eb2aee4374b8aa971c5f07b288b77f086",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/audit_trail.csv",
      "@type": "File",
      "name": "audit_trail.csv",
      "description": "Audit trail of every recorded event.",
      "encodingFormat": "text/csv",
      "contentSize": "3664",
      "sha256": "45733278a25fd6f8362eb63dca9206cff8cac51998efcac25a7ead2d62694cb6",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_formulation_observations.csv",
      "@type": "File",
      "name": "calibration_formulation_observations.csv",
      "description": "Formulation-level calibration observations.",
      "encodingFormat": "text/csv",
      "contentSize": "2674",
      "sha256": "672b78e5c13ba41f8edb14ac244af7705f2d598e66950959d18bd4739d35bd12",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_formulation_response_summary.csv",
      "@type": "File",
      "name": "calibration_formulation_response_summary.csv",
      "description": "Formulation-level prospective calibration summary.",
      "encodingFormat": "text/csv",
      "contentSize": "340",
      "sha256": "6695062e465cf201b60a08649b6161522b1dbe5a6e9bb2bb17fee5bc3d47ec24",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_run_observations.csv",
      "@type": "File",
      "name": "calibration_run_observations.csv",
      "description": "Run-level calibration observations.",
      "encodingFormat": "text/csv",
      "contentSize": "2674",
      "sha256": "672b78e5c13ba41f8edb14ac244af7705f2d598e66950959d18bd4739d35bd12",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/calibration_run_response_summary.csv",
      "@type": "File",
      "name": "calibration_run_response_summary.csv",
      "description": "Run-level prospective calibration summary.",
      "encodingFormat": "text/csv",
      "contentSize": "340",
      "sha256": "6695062e465cf201b60a08649b6161522b1dbe5a6e9bb2bb17fee5bc3d47ec24",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx",
      "@type": "File",
      "name": "cosmetics-peg-emulsifier-replacement-demo_workbench_export.xlsx",
      "description": "Excel workbook: every evidence table as a tab, evidence hash on the cover sheet.",
      "encodingFormat": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "contentSize": "40600",
      "sha256": "734c4227b5b00e2fb76d95ce9178f092cabf24013af29c31546e75166682886a",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/experiments.csv",
      "@type": "File",
      "name": "experiments.csv",
      "description": "Every experiment with recipe, responses and pass/fail status.",
      "encodingFormat": "text/csv",
      "contentSize": "36318",
      "sha256": "02a27592f61dffd8b092128509f9472cf4fa1516a3be5b5160bd239b3049de2f",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/manifest.json",
      "@type": "File",
      "name": "manifest.json",
      "description": "Dossier manifest: version, evidence hash, generating user, disclaimer.",
      "encodingFormat": "application/json",
      "contentSize": "810",
      "sha256": "6247aaf640ed04e506b196923c7b0f200f86437b1d970bcad8206c8db8d39f4f",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/qualification_dossier.html",
      "@type": "File",
      "name": "qualification_dossier.html",
      "description": "Printable qualification dossier (the full report).",
      "encodingFormat": "text/html",
      "contentSize": "91398",
      "sha256": "dc9d4910d1d1fab21b4755fa5bbd92fe17a49187ae95c5b05e25e614e5bf5bb0",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/qualification_gates.csv",
      "@type": "File",
      "name": "qualification_gates.csv",
      "description": "Stage-by-stage qualification gate progress.",
      "encodingFormat": "text/csv",
      "contentSize": "898",
      "sha256": "41e5db72fd772f3c18d5ac198936eabd258f26fe838081b791772a0d3a61da16",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/recommendation_batches.csv",
      "@type": "File",
      "name": "recommendation_batches.csv",
      "description": "Recommendation batches and their approval state.",
      "encodingFormat": "text/csv",
      "contentSize": "687",
      "sha256": "47f37f79aec91910d128d9635d559e77f4667c8466be60bfe6e00de24c600e3f",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/replicate_summary.csv",
      "@type": "File",
      "name": "replicate_summary.csv",
      "description": "Replicate groups: consistency screen, CV and gate status.",
      "encodingFormat": "text/csv",
      "contentSize": "1649",
      "sha256": "d62379015c86c1a2e26c556f822d8728145adaeb968f455812f7621716bf2b1f",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/scientific_evidence.canonical.json",
      "@type": "File",
      "name": "scientific_evidence.canonical.json",
      "description": "The same evidence as canonical bytes: sha256sum of this file IS the evidence hash.",
      "encodingFormat": "application/json",
      "contentSize": "132096",
      "sha256": "856f12ed7d606e65c207cab1f617f17cd121790ae729afea1f7421516a278666",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/scientific_evidence.json",
      "@type": "File",
      "name": "scientific_evidence.json",
      "description": "Complete scientific evidence as readable JSON.",
      "encodingFormat": "application/json",
      "contentSize": "176948",
      "sha256": "dfdbc35938aa19e2fb215418d534c2319c3c251b0f8f598dc3b46057f9218151",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "./dossier-v1/signed_evidence_snapshots/discovery_856f12ed7d60.json",
      "@type": "File",
      "name": "discovery_856f12ed7d60.json",
      "description": "Evidence snapshot frozen at signing; re-hashing it reproduces the hash recorded with the signature.",
      "encodingFormat": "application/json",
      "contentSize": "132096",
      "sha256": "856f12ed7d606e65c207cab1f617f17cd121790ae729afea1f7421516a278666",
      "dateCreated": "2026-09-27T21:53:53+00:00"
    },
    {
      "@id": "#elabftw-metadata",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "name": "eLabFTW extra fields",
      "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Reformulation Assurance\"}]}, \"extra_fields\": {\"All gates passed\": {\"group_id\": 1, \"position\": 6, \"readonly\": true, \"type\": \"checkbox\", \"value\": \"\"}, \"Best robust probability\": {\"group_id\": 1, \"position\": 7, \"readonly\": true, \"type\": \"text\", \"value\": \"n/a\"}, \"Disclaimer\": {\"group_id\": 1, \"position\": 12, \"readonly\": true, \"type\": \"text\", \"value\": \"Prototype decision-support evidence; not a validated regulated quality system.\"}, \"Dossier id\": {\"group_id\": 1, \"position\": 2, \"readonly\": true, \"type\": \"text\", \"value\": \"bdcde038-c16a-463c-bd90-3fb930f89528\"}, \"Dossier version\": {\"group_id\": 1, \"position\": 3, \"readonly\": true, \"type\": \"number\", \"value\": \"1\"}, \"Generated at (UTC)\": {\"group_id\": 1, \"position\": 8, \"readonly\": true, \"type\": \"text\", \"value\": \"2026-09-27T21:53:53+00:00\"}, \"Generated by\": {\"group_id\": 1, \"position\": 9, \"readonly\": true, \"type\": \"text\", \"value\": \"Demo Explorer\"}, \"Project\": {\"group_id\": 1, \"position\": 0, \"readonly\": true, \"type\": \"text\", \"value\": \"Cosmetics: PEG emulsifier replacement (demo)\"}, \"Project id\": {\"group_id\": 1, \"position\": 1, \"readonly\": true, \"type\": \"text\", \"value\": \"02bee293-423b-44ac-b53f-e1bad2d02bce\"}, \"Qualification progress (%)\": {\"group_id\": 1, \"position\": 5, \"readonly\": true, \"type\": \"number\", \"value\": \"35\"}, \"Scientific evidence SHA-256\": {\"group_id\": 1, \"position\": 4, \"readonly\": true, \"type\": \"text\", \"value\": \"856f12ed7d606e65c207cab1f617f17cd121790ae729afea1f7421516a278666\"}, \"Software\": {\"group_id\": 1, \"position\": 10, \"readonly\": true, \"type\": \"text\", \"value\": \"Reformulation Assurance v0.12.4\"}, \"Software URL\": {\"group_id\": 1, \"position\": 11, \"readonly\": true, \"type\": \"url\", \"value\": \"https://github.com/TM289012/reformulation-assurance\"}}}"
    },
    {
      "@id": "#scientific-evidence-sha256",
      "@type": "PropertyValue",
      "propertyID": "scientific_evidence_sha256",
      "name": "Scientific evidence SHA-256",
      "value": "856f12ed7d606e65c207cab1f617f17cd121790ae729afea1f7421516a278666"
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
