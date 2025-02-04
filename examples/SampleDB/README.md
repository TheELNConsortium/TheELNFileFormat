# SampleDB

- Code: https://github.com/sciapp/sampledb
- Documentation: https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/

# Export Structure

Each export contains one or more SampleDB objects, identified by their ID, with each object containing one or more versions and an arbitrary number of files. For each object version, the internal data and schema JSON represenation is written out to `data.json` and `schema.json` files. For each object, the JSON representation of internal file data and comment data is written to `files.json` and `comments.json`.

- `ro-crate-metadata.json`
- `objects/`
  - `<object_id>/`
    - `version/`
      - `<version_id>`
        - `data.json`
        - `schema.json`
    - `files/`
      - `<file_id>/`
        - `<file_name>`
    - `files.json`
    - `comments.json`

## Concepts used

| SampleDB concepts            | JSON property     | JSON object    |
|------------------------------|-------------------|----------------|
| object                       | hasPart           | ./             |
| object name                  | name              | object         |
| object creation time         | dateCreated       | object         |
| object modification time     | dateModified      | object         |
| object url                   | url               | object         |
| object creator               | author            | object         |
| object metadata              | variableMeasured  | object         |
| object tags                  | keywords          | object         |
| object references            | mentions          | object         |
| object ID                    | identifier        | object         |
| action type                  | genre             | object         |
| comments                     | comment           | object         |
| files                        | hasPart           | object         |
| object version               | hasPart           | object         |
| object version data          | hasPart           | object version |
| object version schema        | hasPart           | object version |
| object version creation time | dateCreated       | object version |
| object version creator       | author            | object version |
| object version url           | url               | object version |
| comment author               | author            | comment        |
| comment creation time        | dateCreated       | comment        |
| comment content              | text              | comment        |
| file name                    | name              | file           |
| file uploader                | author            | file           |
| file upload time             | dateCreated       | file           |

## SampleDB examples

### sampledb_export.eln
```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@type": "CreativeWork",
      "@id": "ro-crate-metadata.json",
      "description": "RO-Crate Metadata File Descriptor",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "sdPublisher": {
        "@id": "SampleDB"
      },
      "version": "1.1",
      "dateCreated": "2025-02-04T08:08:05.270274"
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "SampleDB .eln export",
      "description": "SampleDB .eln export generated for user #2 for objects #1, #7",
      "license": {
        "@id": "./license"
      },
      "datePublished": "2025-02-04T08:08:05.270274",
      "hasPart": [
        {
          "@id": "./objects/7/"
        },
        {
          "@id": "./objects/1/"
        }
      ]
    },
    {
      "@type": "Organization",
      "@id": "SampleDB",
      "name": "SampleDB",
      "logo": "https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/_static/img/logo.svg",
      "slogan": "SampleDB is a web-based electronic lab notebook with a focus on sample and measurement metadata.",
      "url": "https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/"
    },
    {
      "@id": "./license",
      "@type": "CreativeWork",
      "name": "No License",
      "description": "This .eln file does not include a license."
    },
    {
      "value": "Measurement",
      "@type": "PropertyValue",
      "@id": "./objects/7/properties/name",
      "propertyID": "name",
      "name": "Object Name"
    },
    {
      "value": "./objects/1/",
      "@type": "PropertyValue",
      "@id": "./objects/7/properties/sample",
      "propertyID": "sample",
      "name": "Sample"
    },
    {
      "value": "This is a test.\nThis **is** a *second* line.\n\nThis line follows an empty line.",
      "@type": "PropertyValue",
      "@id": "./objects/7/properties/comment",
      "propertyID": "comment",
      "name": "Comment"
    },
    {
      "value": "2025-02-04T08:01:07.000000",
      "@type": "PropertyValue",
      "@id": "./objects/7/properties/datetime",
      "propertyID": "datetime",
      "name": "Measurement Date/Time"
    },
    {
      "@id": "./objects/7/",
      "@type": "Dataset",
      "identifier": "7",
      "name": "Measurement",
      "description": "Object #7",
      "dateCreated": "2025-02-04T08:01:07.545532",
      "dateModified": "2025-02-04T08:01:07.545532",
      "author": {
        "@id": "./users/3"
      },
      "creator": {
        "@id": "./users/3"
      },
      "url": "http://localhost:5000/objects/7",
      "variableMeasured": [
        {
          "@id": "./objects/7/properties/name"
        },
        {
          "@id": "./objects/7/properties/sample"
        },
        {
          "@id": "./objects/7/properties/comment"
        },
        {
          "@id": "./objects/7/properties/datetime"
        }
      ],
      "mentions": {
        "@id": "./objects/1/"
      },
      "comment": [],
      "isBasedOn": {
        "@id": "./objects/7/versions/0/"
      },
      "hasPart": [
        {
          "@id": "./objects/7/versions/0/"
        },
        {
          "@id": "./objects/7/files.json"
        }
      ],
      "genre": "measurement",
      "keywords": "example_tag, other_tag, tag3"
    },
    {
      "value": "Measurement",
      "@type": "PropertyValue",
      "@id": "./objects/7/versions/0/properties/name",
      "propertyID": "name",
      "name": "Object Name"
    },
    {
      "value": "./objects/1/",
      "@type": "PropertyValue",
      "@id": "./objects/7/versions/0/properties/sample",
      "propertyID": "sample",
      "name": "Sample"
    },
    {
      "value": "This is a test.\nThis **is** a *second* line.\n\nThis line follows an empty line.",
      "@type": "PropertyValue",
      "@id": "./objects/7/versions/0/properties/comment",
      "propertyID": "comment",
      "name": "Comment"
    },
    {
      "value": "2025-02-04T08:01:07.000000",
      "@type": "PropertyValue",
      "@id": "./objects/7/versions/0/properties/datetime",
      "propertyID": "datetime",
      "name": "Measurement Date/Time"
    },
    {
      "@id": "./objects/7/versions/0/",
      "@type": "Dataset",
      "name": "Measurement",
      "description": "Object #7 version #0",
      "dateCreated": "2025-02-04T08:01:07.545532",
      "creator": {
        "@id": "./users/3"
      },
      "author": {
        "@id": "./users/3"
      },
      "url": "http://localhost:5000/objects/7/versions/0",
      "variableMeasured": [
        {
          "@id": "./objects/7/versions/0/properties/name"
        },
        {
          "@id": "./objects/7/versions/0/properties/sample"
        },
        {
          "@id": "./objects/7/versions/0/properties/comment"
        },
        {
          "@id": "./objects/7/versions/0/properties/datetime"
        }
      ],
      "hasPart": [
        {
          "@id": "./objects/7/versions/0/schema.json"
        },
        {
          "@id": "./objects/7/versions/0/data.json"
        }
      ]
    },
    {
      "@id": "./objects/7/versions/0/schema.json",
      "@type": "File",
      "description": "Schema for Object #7 version #0",
      "name": "schema.json",
      "encodingFormat": "application/json",
      "contentSize": "784",
      "sha256": "17dbb2aba3461cba3031823aaf3a8def73405a0606bb19b8d690cd0870b80ac7"
    },
    {
      "@id": "./objects/7/versions/0/data.json",
      "@type": "File",
      "description": "Data for Object #7 version #0",
      "name": "data.json",
      "encodingFormat": "application/json",
      "contentSize": "551",
      "sha256": "0c9c90898b2b97ca8deabf889fac32a34d7336e66484037075ba77b82b2cd320"
    },
    {
      "@id": "./objects/7/files.json",
      "@type": "File",
      "description": "Data about files for Object #7",
      "name": "files.json",
      "encodingFormat": "application/json",
      "contentSize": "2",
      "sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
    },
    {
      "value": "OMBE-1",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/name",
      "propertyID": "name",
      "name": "Sample Name"
    },
    {
      "value": "2017-02-24T11:56:00.000000",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/created",
      "propertyID": "created",
      "name": "Creation Datetime"
    },
    {
      "value": false,
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/checkbox",
      "propertyID": "checkbox",
      "name": "Checkbox"
    },
    {
      "value": "Option B",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/dropdown",
      "propertyID": "dropdown",
      "name": "Dropdown"
    },
    {
      "value": "GaAs",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/substrate",
      "propertyID": "substrate",
      "name": "Substrate"
    },
    {
      "value": "Seed Layer",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.films.0.name",
      "propertyID": "multilayer.0.films.0.name",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Fe",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.films.0.elements.0.name",
      "propertyID": "multilayer.0.films.0.elements.0.name",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.09999999999999999,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.films.0.elements.0.rate",
      "propertyID": "multilayer.0.films.0.elements.0.rate",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 5.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.films.0.thickness",
      "propertyID": "multilayer.0.films.0.thickness",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.films.0.oxygen_flow",
      "propertyID": "multilayer.0.films.0.oxygen_flow",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 129.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.films.0.substrate_temperature",
      "propertyID": "multilayer.0.films.0.substrate_temperature",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 1.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.0.repetitions",
      "propertyID": "multilayer.0.repetitions",
      "name": "Multilayers \u2192 0 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "value": "Buffer Layer",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.films.0.name",
      "propertyID": "multilayer.1.films.0.name",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Ag",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.films.0.elements.0.name",
      "propertyID": "multilayer.1.films.0.elements.0.name",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 1.0,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.films.0.elements.0.rate",
      "propertyID": "multilayer.1.films.0.elements.0.rate",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 1500.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.films.0.thickness",
      "propertyID": "multilayer.1.films.0.thickness",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.films.0.oxygen_flow",
      "propertyID": "multilayer.1.films.0.oxygen_flow",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 129.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.films.0.substrate_temperature",
      "propertyID": "multilayer.1.films.0.substrate_temperature",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 1.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.1.repetitions",
      "propertyID": "multilayer.1.repetitions",
      "name": "Multilayers \u2192 1 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "value": "Pd",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.0.name",
      "propertyID": "multilayer.2.films.0.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Pd",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.0.elements.0.name",
      "propertyID": "multilayer.2.films.0.elements.0.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.01,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.0.elements.0.rate",
      "propertyID": "multilayer.2.films.0.elements.0.rate",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 150.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.0.thickness",
      "propertyID": "multilayer.2.films.0.thickness",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.0.oxygen_flow",
      "propertyID": "multilayer.2.films.0.oxygen_flow",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 99.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.0.substrate_temperature",
      "propertyID": "multilayer.2.films.0.substrate_temperature",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": "Fe",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.1.name",
      "propertyID": "multilayer.2.films.1.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Film Name"
    },
    {
      "value": "Fe",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.1.elements.0.name",
      "propertyID": "multilayer.2.films.1.elements.0.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.049999999999999996,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.1.elements.0.rate",
      "propertyID": "multilayer.2.films.1.elements.0.rate",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 10.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.1.thickness",
      "propertyID": "multilayer.2.films.1.thickness",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.1.oxygen_flow",
      "propertyID": "multilayer.2.films.1.oxygen_flow",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Oxygen Flow"
    },
    {
      "value": 129.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.films.1.substrate_temperature",
      "propertyID": "multilayer.2.films.1.substrate_temperature",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 10.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.2.repetitions",
      "propertyID": "multilayer.2.repetitions",
      "name": "Multilayers \u2192 2 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "value": "Pd Layer",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.films.0.name",
      "propertyID": "multilayer.3.films.0.name",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Pd",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.films.0.elements.0.name",
      "propertyID": "multilayer.3.films.0.elements.0.name",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.09999999999999999,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.films.0.elements.0.rate",
      "propertyID": "multilayer.3.films.0.elements.0.rate",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 150.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.films.0.thickness",
      "propertyID": "multilayer.3.films.0.thickness",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.films.0.oxygen_flow",
      "propertyID": "multilayer.3.films.0.oxygen_flow",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 99.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.films.0.substrate_temperature",
      "propertyID": "multilayer.3.films.0.substrate_temperature",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 1.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/properties/multilayer.3.repetitions",
      "propertyID": "multilayer.3.repetitions",
      "name": "Multilayers \u2192 3 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "@id": "./objects/1/",
      "@type": "Dataset",
      "identifier": "1",
      "name": "OMBE-1",
      "description": "Object #1",
      "dateCreated": "2025-02-04T08:01:06.965224",
      "dateModified": "2025-02-04T08:01:06.965224",
      "author": {
        "@id": "./users/2"
      },
      "creator": {
        "@id": "./users/2"
      },
      "url": "http://localhost:5000/objects/1",
      "variableMeasured": [
        {
          "@id": "./objects/1/properties/name"
        },
        {
          "@id": "./objects/1/properties/created"
        },
        {
          "@id": "./objects/1/properties/checkbox"
        },
        {
          "@id": "./objects/1/properties/dropdown"
        },
        {
          "@id": "./objects/1/properties/substrate"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.films.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.films.0.thickness"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/properties/multilayer.0.repetitions"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.films.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.films.0.thickness"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/properties/multilayer.1.repetitions"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.0.thickness"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.1.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.1.elements.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.1.elements.0.rate"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.1.thickness"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.1.oxygen_flow"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.films.1.substrate_temperature"
        },
        {
          "@id": "./objects/1/properties/multilayer.2.repetitions"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.films.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.films.0.thickness"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/properties/multilayer.3.repetitions"
        }
      ],
      "comment": [
        {
          "@id": "./objects/1/comments/1"
        },
        {
          "@id": "./objects/1/comments/2"
        }
      ],
      "isBasedOn": {
        "@id": "./objects/1/versions/0/"
      },
      "hasPart": [
        {
          "@id": "./objects/1/versions/0/"
        },
        {
          "@id": "./objects/1/files.json"
        },
        {
          "@id": "./objects/1/files/0/example.txt"
        },
        {
          "@id": "./objects/1/files/1/demo.png"
        }
      ],
      "genre": "sample"
    },
    {
      "value": "OMBE-1",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/name",
      "propertyID": "name",
      "name": "Sample Name"
    },
    {
      "value": "2017-02-24T11:56:00.000000",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/created",
      "propertyID": "created",
      "name": "Creation Datetime"
    },
    {
      "value": false,
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/checkbox",
      "propertyID": "checkbox",
      "name": "Checkbox"
    },
    {
      "value": "Option B",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/dropdown",
      "propertyID": "dropdown",
      "name": "Dropdown"
    },
    {
      "value": "GaAs",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/substrate",
      "propertyID": "substrate",
      "name": "Substrate"
    },
    {
      "value": "Seed Layer",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.name",
      "propertyID": "multilayer.0.films.0.name",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Fe",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.elements.0.name",
      "propertyID": "multilayer.0.films.0.elements.0.name",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.09999999999999999,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.elements.0.rate",
      "propertyID": "multilayer.0.films.0.elements.0.rate",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 5.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.thickness",
      "propertyID": "multilayer.0.films.0.thickness",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.oxygen_flow",
      "propertyID": "multilayer.0.films.0.oxygen_flow",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 129.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.substrate_temperature",
      "propertyID": "multilayer.0.films.0.substrate_temperature",
      "name": "Multilayers \u2192 0 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 1.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.0.repetitions",
      "propertyID": "multilayer.0.repetitions",
      "name": "Multilayers \u2192 0 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "value": "Buffer Layer",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.name",
      "propertyID": "multilayer.1.films.0.name",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Ag",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.elements.0.name",
      "propertyID": "multilayer.1.films.0.elements.0.name",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 1.0,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.elements.0.rate",
      "propertyID": "multilayer.1.films.0.elements.0.rate",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 1500.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.thickness",
      "propertyID": "multilayer.1.films.0.thickness",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.oxygen_flow",
      "propertyID": "multilayer.1.films.0.oxygen_flow",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 129.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.substrate_temperature",
      "propertyID": "multilayer.1.films.0.substrate_temperature",
      "name": "Multilayers \u2192 1 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 1.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.1.repetitions",
      "propertyID": "multilayer.1.repetitions",
      "name": "Multilayers \u2192 1 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "value": "Pd",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.name",
      "propertyID": "multilayer.2.films.0.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Pd",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.elements.0.name",
      "propertyID": "multilayer.2.films.0.elements.0.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.01,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.elements.0.rate",
      "propertyID": "multilayer.2.films.0.elements.0.rate",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 150.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.thickness",
      "propertyID": "multilayer.2.films.0.thickness",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.oxygen_flow",
      "propertyID": "multilayer.2.films.0.oxygen_flow",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 99.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.substrate_temperature",
      "propertyID": "multilayer.2.films.0.substrate_temperature",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": "Fe",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.name",
      "propertyID": "multilayer.2.films.1.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Film Name"
    },
    {
      "value": "Fe",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.elements.0.name",
      "propertyID": "multilayer.2.films.1.elements.0.name",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.049999999999999996,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.elements.0.rate",
      "propertyID": "multilayer.2.films.1.elements.0.rate",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 10.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.thickness",
      "propertyID": "multilayer.2.films.1.thickness",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.oxygen_flow",
      "propertyID": "multilayer.2.films.1.oxygen_flow",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Oxygen Flow"
    },
    {
      "value": 129.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.substrate_temperature",
      "propertyID": "multilayer.2.films.1.substrate_temperature",
      "name": "Multilayers \u2192 2 \u2192 Films \u2192 1 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 10.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.2.repetitions",
      "propertyID": "multilayer.2.repetitions",
      "name": "Multilayers \u2192 2 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "value": "Pd Layer",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.name",
      "propertyID": "multilayer.3.films.0.name",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Film Name"
    },
    {
      "value": "Pd",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.elements.0.name",
      "propertyID": "multilayer.3.films.0.elements.0.name",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Element Name"
    },
    {
      "value": 0.09999999999999999,
      "unitText": "\u00c5/s",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.elements.0.rate",
      "propertyID": "multilayer.3.films.0.elements.0.rate",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Elements \u2192 0 \u2192 Rate"
    },
    {
      "value": 150.0,
      "unitText": "\u00c5",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.thickness",
      "propertyID": "multilayer.3.films.0.thickness",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Film Thickness",
      "unitCode": "A11"
    },
    {
      "value": 0.0,
      "unitText": "sccm",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.oxygen_flow",
      "propertyID": "multilayer.3.films.0.oxygen_flow",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Oxygen Flow"
    },
    {
      "value": 99.99999999999997,
      "unitText": "degC",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.substrate_temperature",
      "propertyID": "multilayer.3.films.0.substrate_temperature",
      "name": "Multilayers \u2192 3 \u2192 Films \u2192 0 \u2192 Substrate Temperature",
      "unitCode": "CEL"
    },
    {
      "value": 1.0,
      "unitText": "1",
      "@type": "PropertyValue",
      "@id": "./objects/1/versions/0/properties/multilayer.3.repetitions",
      "propertyID": "multilayer.3.repetitions",
      "name": "Multilayers \u2192 3 \u2192 Film Layer Repetitions",
      "unitCode": "C62"
    },
    {
      "@id": "./objects/1/versions/0/",
      "@type": "Dataset",
      "name": "OMBE-1",
      "description": "Object #1 version #0",
      "dateCreated": "2025-02-04T08:01:06.965224",
      "creator": {
        "@id": "./users/2"
      },
      "author": {
        "@id": "./users/2"
      },
      "url": "http://localhost:5000/objects/1/versions/0",
      "variableMeasured": [
        {
          "@id": "./objects/1/versions/0/properties/name"
        },
        {
          "@id": "./objects/1/versions/0/properties/created"
        },
        {
          "@id": "./objects/1/versions/0/properties/checkbox"
        },
        {
          "@id": "./objects/1/versions/0/properties/dropdown"
        },
        {
          "@id": "./objects/1/versions/0/properties/substrate"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.thickness"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.0.repetitions"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.thickness"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.1.repetitions"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.thickness"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.elements.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.elements.0.rate"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.thickness"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.oxygen_flow"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.films.1.substrate_temperature"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.2.repetitions"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.elements.0.name"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.elements.0.rate"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.thickness"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.oxygen_flow"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.films.0.substrate_temperature"
        },
        {
          "@id": "./objects/1/versions/0/properties/multilayer.3.repetitions"
        }
      ],
      "hasPart": [
        {
          "@id": "./objects/1/versions/0/schema.json"
        },
        {
          "@id": "./objects/1/versions/0/data.json"
        }
      ]
    },
    {
      "@id": "./objects/1/versions/0/schema.json",
      "@type": "File",
      "description": "Schema for Object #1 version #0",
      "name": "schema.json",
      "encodingFormat": "application/json",
      "contentSize": "4073",
      "sha256": "d97ffc5d8d8a04059512b6559bb5f2199646642ef10436d9b910a3f47313015b"
    },
    {
      "@id": "./objects/1/versions/0/data.json",
      "@type": "File",
      "description": "Data for Object #1 version #0",
      "name": "data.json",
      "encodingFormat": "application/json",
      "contentSize": "7695",
      "sha256": "79a4238305f0be9d92b059e7f6001b931f5c9eeda531dd39cf376ae501e7e171"
    },
    {
      "@id": "./objects/1/comments/1",
      "@type": "Comment",
      "parentItem": {
        "@id": "./objects/1/"
      },
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2025-02-04T08:01:07.075820",
      "text": "This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. \nThis comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. \n\nThis comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. "
    },
    {
      "@id": "./objects/1/comments/2",
      "@type": "Comment",
      "parentItem": {
        "@id": "./objects/1/"
      },
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2025-02-04T08:01:07.087748",
      "text": "This is another, shorter comment"
    },
    {
      "@id": "./objects/1/files.json",
      "@type": "File",
      "description": "Data about files for Object #1",
      "name": "files.json",
      "encodingFormat": "application/json",
      "contentSize": "763",
      "sha256": "f370ef736f0ce114d4b0fdd762c6edd96ba107de7baef795b74df60cf5ba5cdd"
    },
    {
      "@id": "./objects/1/files/0/example.txt",
      "@type": "File",
      "name": "example.txt",
      "description": "File #0 for Object #1",
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2025-02-04T08:01:07.102037",
      "encodingFormat": "text/plain",
      "contentSize": "17",
      "contentUrl": "http://localhost:5000/objects/1/files/0",
      "sha256": "9f722959a023c02a3ba0fafdba81aded642d6610eff5dca32dce35132e16b6c5"
    },
    {
      "@id": "./objects/1/files/1/demo.png",
      "@type": "File",
      "name": "demo.png",
      "description": "File #1 for Object #1",
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2025-02-04T08:01:07.117063",
      "encodingFormat": "image/png",
      "contentSize": "9952",
      "contentUrl": "http://localhost:5000/objects/1/files/1",
      "sha256": "9cef78156ceee44ca84b813b79d7f26afba9307aaa00da40d28a6aa2e623496b"
    },
    {
      "@id": "./users/3",
      "@type": "Person",
      "name": "Basic User",
      "url": "http://localhost:5000/users/3"
    },
    {
      "@id": "./users/2",
      "@type": "Person",
      "name": "Instrument Scientist",
      "url": "http://localhost:5000/users/2"
    }
  ]
}
```
