# FAQ | Frequently asked questions

We regularly encounter recurring, incorrect criticisms of the .eln file format. These points have previously been addressed, yet they continue to resurface.

**Myth 1: The .eln file format does not allow semantic annotation**<br>
This is incorrect. The .eln file format enables semantic annotation by allowing each entry to include an identifier that can reference an external semantic definition (for example, an ontology PURL). This mechanism supports explicit linking to controlled vocabularies and ontologies, facilitating interoperable, machine-readable semantics.

**Myth 2: The .eln file format does not allow for profile validation**<br>
This is not true. At its core, the .eln file format is built around a JSON‑LD representation that can be validated against JSON Schema using a wide range of existing tools. Example files are validated as part of the publishing workflow, and stricter or custom validation profiles can be implemented for specific use cases when required.