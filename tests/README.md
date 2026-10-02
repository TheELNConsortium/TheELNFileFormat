# Check an ELN file

Run all checks on one archive from the repository root:

```bash
python tests/run_checks.py path/to/file.eln
```

Omit the filename to be prompted for it. Add `--no-recommend` to validate only REQUIRED, not RECOMMENDED, RO-Crate rules and to hide warnings. The exit code is 0 when all checks pass, 1 when a check fails and 2 when the file is not found.

---

# ELN File Format Specification Hierarchy

The ELN file format is built on:
1. **[RO-Crate 1.2](https://w3id.org/ro/crate/1.2)** - Base specification
2. **[SPECIFICATION.md](../SPECIFICATION.md)** - ELN-specific extensions and refinements
3. **This document** - Additional clarifications

The tests distinguish three versions: `1.1` (RO-Crate 1.1), `1.2` (RO-Crate 1.2 without an ELN version) and `1.2+20260923` (RO-Crate 1.2 with ELN version 1.2+20260923). The clarifications below are checked only for `1.2+20260923`.

The ELN version is declared in the root Dataset's `conformsTo`, next to the RO-Crate version:

```json
{
  "@id": "./",
  "@type": "Dataset",
  "conformsTo": [
    { "@id": "https://w3id.org/ro/crate/1.2" },
    { "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+20260923" }
  ]
}
```

Without that URI, the RO-Crate version in the metadata descriptor's `conformsTo` decides between `1.1` and `1.2` (`tests/checks/versions.py`). The archive structure, metadata and schema checks run only on `1.2+20260923`; the validator and PyPI rocrate checks run on all versions. A file whose version cannot be read gets all checks.

---

## Additional Clarifications

### description vs text

Property  |     Definition
--------- | --------------------
description |   Concise, human-readable metadata describing the entity's purpose, scope, or role. Use on any entity type. Must not contain the full record body. Should be plain text string.
text       |    Inline textual content of the entity itself. Use only on CreativeWork subclasses (including Dataset, File). Should be the full content.
comment    |    List of references via `@id` to separate top-level `Comment` nodes whose content is in `text`. Must be a list even for a single comment.

**Rules:**
- If description and body are present, they must have different roles: summary vs full content
- Do not use `text` on Person, Organization, PropertyValue, or other non-CreativeWork entities
- For large documents, represent as a File and reference it rather than embedding in `text`

**Example:**
```json
{
  "@type": "Dataset",
  "description": "Temperature-dependence experiment on amylase activity",
  "text": "<h1>Method</h1><p>…full experiment record…</p>"
}
```

---

### identifier vs url vs contentUrl

Property | Definition | Example
-------- | ---------- | -------
identifier | Identifier assigned by the ELN, UUID, or DOI. For a Person, the ORCID URI is the `@id`, not the `identifier` | `"exp-uuid-123"` or `"10.5281/zenodo.123"`
url | Web page about the object that a person can visit | `https://github.com/user/repo/blob/main/file.md`
contentUrl | Direct location of downloadable bytes (mainly for File) | `https://raw.githubusercontent.com/user/repo/main/file.md`

---

### author

**Format:** Must reference Person or Organization entities using `@id`. Plain strings like "Donald Duck and Goofy Dog" are not permitted.

**Single author:**
```json
"author": {"@id": "./person/123"}
```

**Multiple authors:**
```json
"author": [{"@id": "./person/123"}, {"@id": "./person/456"}]
```

---

### @type

All entries must be defined in the JSON-LD context. This is enforced by rocrate-validator, not by the consortium checks.
