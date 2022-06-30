## Tools for eln crates

### eln2md | create README.md from eln crate's metadata.json
Usage from individual example directory:
- "eln2md.py" paste full ro-crate-metadata.json
- "eln2md.py simple" paste only @id and hasParts
- "eln2md.py tree" create tree representation
  - easiest to read
- a README_template.md can be used to define the header
- all .eln files are parsed sequentially

by Steffen Brinckmann