# AI4Green

## Information

* Repo: https://github.com/AI4Green/AI4Green
* Website: https://ai4green.app/

### Structure of the AI4Green example

Key parts of the reaction dataset are:
- The text field which renders the summary table in HTML
- Automatically generated .RDF (reaction data file) attachment and any additional file attachments

## Concepts used

Here is a correspondance between concepts in AI4Green and how they are translated in the metadata json file in the archive:

| AI4Green concepts | JSON property          |
|-------------------|------------------------|
| summary_table     | text                   ||
| comment           | comment                |
| mimetype          | encodingFormat         |
| time_of_creation  | dateCreated            ||
| time_of_update    | dateModified           |
| author            | author                 ||
| name              | name                   |
