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
