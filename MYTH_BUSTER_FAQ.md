# Myth buster FAQ

We regularly encounter recurring, incorrect criticisms of .eln. These points have previously been addressed, yet they continue to resurface.

**Myth 1: .eln does not allow semantic annotation**<br>
This is incorrect. .eln enables semantic annotation by allowing each entry to include an identifier that can reference an external semantic definition (for example, an ontology PURL). This mechanism supports explicit linking to controlled vocabularies and ontologies, facilitating interoperable, machine-readable semantics.

**Myth 2: .eln does not allow for profile validation**<br>
Not true. At its core, .eln is built around a JSON‑LD representation that can be validated against JSON Schema using a wide range of existing tools. Example files are validated as part of the publishing workflow, and stricter or custom validation profiles can be implemented for specific use cases when required.