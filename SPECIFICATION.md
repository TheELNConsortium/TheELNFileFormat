# Specification for the ELN file format

## Generalities

This format is an open format, licensed under the [MIT](./LICENSE) license and specified by the present document.

The file is a ZIP archive, so it MUST follow the standard ZIP specifications and be readable by all zip utilities.

The contents of the archive MAY be encrypted, as with any ZIP archive.

An up to date version of this document can be accessed at: https://github.com/TheELNConsortium/eln-file-format

This archive format is basically a zipped RO-Crate, with a `.eln` file extension.

## Structure of the archive

Inside a .eln file, there MUST be a folder that will contain the rest of the data. The name of the folder SHOULD be the same as the archive name. This folder at root prevents issues when opening the file as a zip file and getting archived files extracted in the current directory, possibly overwriting other files, and probably polluting the current directory. There MUST be only one folder at the root of the archive.

Inside that root folder, there MUST be a file named `ro-crate-metadata.json`. This file follows the [RO-Crate 1.1+ Specification](https://w3id.org/ro/crate/1.1).

The rest of the archive is composed of 0 or more folders that each describe one experiment or coherent set of data. Thus, the ELN archive can accomodate one or several experimental set of data.

Example for file: some-data.eln

~~~yaml
some-data.eln:
  - ro-crate-metadata.json
  - experimentA/:
    - index.json
    - image.tif
    - measurements.csv
    - paper.pdf
  - experimentB/:
    - content.txt
    - image-overexposed.tif
    - results.xlsx
    - subfolder-with-data/:
      - some-data.bin
      - some-data2.bin
~~~

## Examples

See the [examples folder](./examples).

See also the [RO-Crate website](https://www.researchobject.org/ro-crate/1.1/data-entities.html#example-linking-to-a-file-and-folders).
