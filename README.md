# ELN file format (.eln)

## Description

The ELN file format is an archive format for exchange of experimental results and data.

This file format can be created and read by software such as Electronic Laboratory Notebooks.

## Specification

The file format is specified in the [SPECIFICATION.md](./SPECIFICATION.md) file. It follows the [RO-Crate](https://www.researchobject.org/ro-crate/) specification and bundles the files into a ZIP archive.

The `.eln` file/extension is an accepted and recognized media type (previously known as MIME type), see IANA assignment:
https://www.iana.org/assignments/media-types/application/vnd.eln+zip

## Origin

This file format was created for the needs of better interoperability between ELN software. So editors of these software decided it would be useful for users to have an archive format that can be easily understood by several ELNs.

## Status

Generally working with some quirks here and there.

## Known implementations

| Implementation                                    | .eln import | .eln export  | Example |
| ------------------------------------------------- | ----------- | ------------ | ------------ |
| [eLabFTW](https://www.elabftw.net)                | ✅ | ✅ | [elabftw](https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/elabftw)   |
| [Kadi4Mat](https://kadi.iam.kit.edu/)             | ✅ | ✅ | [kadi4mat](https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/kadi4mat) |
| [Pasta](https://github.com/PASTA-ELN/pasta-eln)   | ✅ | ✅ | [PASTA](https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/PASTA)       |
| [SampleDB](https://github.com/sciapp/sampledb)    | ✅ | ✅ | [SampleDB](https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/SampleDB) |
| [Rspace](https://www.researchspace.com/)          | ✅ | ✅ | [RSpace](https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/RSpace)     |
| [NOMAD](https://nomad-lab.eu)                     | ✅ |    | |

 
