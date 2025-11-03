**Gold‑standard example**

This gold‑standard sibling triplet consists of an ELN
file, a JSON‑LD file, and a Turtle file. The example was created from the data
for CRR‑25894 on chemotion‑repository.org.

- **The JSON‑LD and Turtle files are equivalent:** the Turtle file was generated
  from the JSON‑LD representation using rdflib.
- **All data contained in the JSON‑LD/Turtle files are also present in the ELN file:** minor format conversions are summarized below.
- **Binary and raw data contained in the ELN file are NOT included in the JSON‑LD or Turtle files.**

**Therefore, the ELN file fully supersedes the JSON‑LD/Turtle files in terms of content** as also evident from the size although the json-ld file is packed less  dense.

## Format conversion: JSON‑LD → ELN file

1.  Create an empty folder and add the data files to it.
2.  Ensure that every node has an `@id`. If a node lacks an identifier, create
    one using the pattern `@type_@name`.
3.  Flatten hierarchical dictionaries into a list of nodes, using `@id` values
    to represent links.
4.  Add the manifest nodes and include them in the node list.
5.  Remove duplicate nodes.
6.  Adjust dataset `@id` values to reflect the file locations of the
    corresponding data sets:
  - Add an additional file node to the node list for each data file. Each file
    node must include `@id`, `@type`, `@name`, and `sha256`.
  - Use the instrument information from `dataset-description.txt` as
    supplemental metadata for the dataset.
  - Link the additional data files via `hasPart` both in the dataset node and in
    the root `./` node.
7.  Restructure the root node:
  - Set `@id` to `./` and `@type` to `Dataset`.
  - Add all datasets and files under the root node using `hasPart`.
8.  Rename protected keys:
  - `author` → `authors`
  - `keywords` → `keywordLists`
  - Remove the protected `about` key if it only links back to the root node.

## Original data

Source: CRR‑25894 from [chemotion‑repository.net](https://www.chemotion-repository.net/home/publications/collections/4916).

The JSON‑LD files were downloaded manually and merged by copying the Analysis
branches into the main Reaction tree to produce a single master JSON‑LD file.
The files used include:

- `JSON-LD_Reaction_7354-20251031....json`
- `JSON-LD_Analysis_674242-20251031....json`
- `JSON-LD_Analysis_674244-20251031....json`
- `JSON-LD_Analysis_674246-20251031....json`
- `JSON-LD_Analysis_674248-20251031....json`

The master JSON‑LD file was converted to a Turtle file. A heuristic
verification schema (`goldStandardShapes.ttl`) was created, and all files were
validated against it.

