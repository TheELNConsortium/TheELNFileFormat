# Make an .eln file 1.2+202609 compliant

These steps take an existing .eln export, fix the code that generates `ro-crate-metadata.json` to RO-Crate 1.2 and ELN version `1.2+202609`, and check the result with `tests/run_checks.py`. All commands run from the root of this repository and use [uv](https://docs.astral.sh/uv/).

## 1. Install the test dependencies

```bash
uv sync --group test
```

## 2. Export an .eln from your ELN

Export an .eln file with your ELN. You re-run this export after every code change in step 3, so keep the command at hand:

```bash
<export-eln-command>
```

## 3. Update the context and the specification versions

Edit the exporter code that writes the `ro-crate-metadata.json`, in particular the metadata descriptor and the root Dataset `./`:

- Use the RO-Crate 1.2 context:

  ```json
  "@context": "https://w3id.org/ro/crate/1.2/context"
  ```

- The metadata descriptor declares RO-Crate 1.2:

  ```json
  {
    "@id": "ro-crate-metadata.json",
    "@type": "CreativeWork",
    "about": { "@id": "./" },
    "conformsTo": { "@id": "https://w3id.org/ro/crate/1.2" }
  }
  ```

- The root Dataset declares RO-Crate 1.2 and the ELN version:

  ```json
  {
    "@id": "./",
    "@type": "Dataset",
    "conformsTo": [
      { "@id": "https://w3id.org/ro/crate/1.2" },
      { "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609" }
    ]
  }
  ```

- Add these two nodes to the `@graph`:

  ```json
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
  }
  ```

## 4. Run the checks

Start with the REQUIRED rules only. `--no-recommend` skips RECOMMENDED RO-Crate rules and hides warnings and info lines:

```bash
uv run python tests/run_checks.py --no-recommend <path-to-.eln>
```

The first output line shows the version the checks assume. It must read `Identified version: 1.2+202609`. If it shows `1.1` or `1.2`, the root Dataset's `conformsTo` is wrong (step 3).

When everything passes, run again without the flag to see the RECOMMENDED rules and warnings. Any RECOMMENDED issue makes the Validator check fail and the exit code 1:

```bash
uv run python tests/run_checks.py <path-to-.eln>
```

The exit code is 0 when all checks pass, 1 when a check fails and 2 when the file is not found. Repeat steps 2 to 4 until the run with `--no-recommend` passes, then work through the RECOMMENDED issues of the second run.

## 5. Common issues

**REQUIRED (the check fails):**

- **Not flattened** (`ro-crate-1.2_2.3`): every entity is a separate node in the top-level `@graph`. Other nodes reference it only with `{"@id": "..."}`, never by embedding the whole object.
- **Metadata descriptor or root incomplete**: `ro-crate-metadata.json` must be a `CreativeWork` with `about` and `conformsTo`; the root Dataset's `@id` must be `./`.
- **author**: must be `{"@id": ...}` reference(s) to Person or Organization nodes, not a string like `"Donald Duck and Goofy Dog"`.
- **Field formats**: `contentSize` is a string with the number of bytes and no units (`"247"`); `keywords` is one comma-separated string, not an array; `comment` is a list of `@id` references to `Comment` nodes (`[{"@id": "..."}]`, even for one comment).
- **Types**: directories in the archive must have `@type` `Dataset`, files `File`.
- **Schema** (`tests/schema.json`): `identifier` is a string and `hasPart` is always an array, even with a single entry.
- **Archive structure**: exactly one root folder, with every file inside it.

**RECOMMENDED (shown without `--no-recommend`):**

- **Local IDs** (`ro-crate-1.2_41.1`): contextual entities such as Person, Organization or PropertyValue use an `@id` starting with `#` (e.g. `#alice`) or an absolute URI.
- **Persons and organizations** (`ro-crate-1.2_89.0`, `ro-crate-1.2_87.0`): use the ORCID or ROR URI as `@id` when one is available.
- **Names** (`ro-crate-1.2_75.1`): give every contextual entity a `name`.
- **License** (`ro-crate-1.2_81.1`, `ro-crate-1.2_81.2`, `ro-crate-1.2_82.0`, `ro-crate-1.2_83.0`): reference the license with `{"@id": "<license URL>"}` and add a `CreativeWork` node for it with `name` and `description`.
- **Identifiers as PropertyValue** (`ro-crate-1.2_53.0`): the consortium schema requires `identifier` to be a string, so ignore this recommendation.

## Need help?

If a check fails and you do not know why, open an [issue](https://github.com/TheELNConsortium/TheELNFileFormat/issues) or a [discussion](https://github.com/TheELNConsortium/TheELNFileFormat/discussions). Include the output of `run_checks.py` and, if possible, the `ro-crate-metadata.json`. We are happy to help.
