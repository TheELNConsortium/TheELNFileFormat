# Kadi4Mat

### Basic Components of Kadi4Mat

**Records**, contain data and connect it with corresponding metadata. The data of a record can consist of an arbitrary number of different files, all sharing the same metadata, as well as metadata only.

**Collections**, represents simple, logical groupings of multiple records.

### Structure of the current Kadi4Mat example

**records-example.eln** is an archive of a single record in Kadi4Mat with some example files.

**collections-example.eln** is an archive of a group of multiple records with some example files in each record. Each record is represented as a folder in this archive.

# Kadi4Mat examples

## Concepts used

Files `{record_identifier}.json`, and `{record_identifier}.ttl` are the JSON export and RDF (Turtle) export of the record respectively, that are added to the archive during export. It contains the corresponding metadata specific to the record.

The actual content of the Record (i.e., Files) is stored in a separate folder `files` to prevent issues if a file with same name as JSON export file exists.

The `author` property represents the creator of either File, Link, or Record in Kadi4Mat.

In Kadi4Mat, the generic metadata can be organized using nested types(along with primitive data-types). The following nested value types are available:

- **Dictionary**: A nested value that combines multiple metadata entries under a single key. In the example below, `Instrument.manufacturer` is a dictionary containing `manufacturerName` as a nested key.

- **List**: A nested value similar to dictionaries, but without keys for the values. In the example below, `Instrument.Detector` is a list where each item is an entry without a key, referenced by its index.

The nodes representing generic metadata in `variableMeasured` array have the following properties:

- `propertyID`: The name of the property. For nested entries, it indicates the flattened nested entry with `dot(.)` as separator for keys. For list type entries, the index of the list item is appended after the separator. For example:
  - `Instrument.name`: Refers to the `name` key under the `Instrument` dictionary.
  - `Instrument.Detector.0`: Refers to the first item (with index 0) in the `Detector` list within `Instrument` dictionary.
- `value`: The actual value of the generic metadata entry.
- `additionalType`: The data type of the value.
- `identifier`: An IRI specifying an existing term that the metadata should represent.

The following table is the mapping of Kadi4Mat concepts to the base metadata standard of RO-Crate specification (i.e., **schema.org**)

| Kadi4Mat concepts    | JSON property            |
| -------------------- | ------------------------ |
| JSON export          | {record_identifier}.json |
| RDF (Turtle) export  | {record_identifier}.ttl  |
| File name            | name                     |
| File Size            | contentSize              |
| File MIME Type       | encodingFormat           |
| File ID              | identifier               |
| tags                 | keywords                 |
| Resource Title       | name                     |
| Resource Identifier  | identifier               |
| Resource Description | description              |
| Creator              | author                   |
| Generic Metadata     | variableMeasured         |

### collections-example.eln

```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "dateCreated": "2024-11-19T13:44:29.875084+00:00",
      "sdPublisher": {
        "@id": "https://kadi.iam.kit.edu"
      },
      "version": "1.1.2"
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "datePublished": "2024-11-19",
      "description": "An RO-Crate exported from Kadi4Mat following the ELN file format specification.",
      "hasPart": [
        {
          "@id": "./characterization-of-a-sample/"
        },
        {
          "@id": "./instrument-used-in-experiment/"
        },
        {
          "@id": "./scripts-used-in-the-experiment/"
        },
        {
          "@id": "./generated-files-during-experiment/"
        }
      ],
      "license": "For license information, please refer to the individual dataset nodes, if applicable.",
      "name": "collections-example"
    },
    {
      "@id": "https://kadi.iam.kit.edu",
      "@type": "Organization",
      "description": "A generic and open source virtual research environment.",
      "name": "Kadi4Mat",
      "url": "https://kadi.iam.kit.edu"
    },
    {
      "@id": "http://localhost:5000/records/49#description",
      "@type": "TextObject",
      "encodingFormat": "text/markdown",
      "text": "Some information about the instrument used in a process and other metadata like owner of the instrument etc."
    },
    {
      "@id": "http://localhost:5000/users/34",
      "@type": "Person",
      "name": "Manideep"
    },
    {
      "@id": "http://localhost:5000/records/49#extras-Characterization%20type",
      "@type": "PropertyValue",
      "propertyID": "Characterization type",
      "value": "SEM"
    },
    {
      "@id": "http://localhost:5000/records/49#extras-Characterization%20result%20file(s)",
      "@type": "PropertyValue",
      "propertyID": "Characterization result file(s)",
      "value": false
    },
    {
      "@id": "http://localhost:5000/records/49#extras-Measurement.Device",
      "@type": "PropertyValue",
      "propertyID": "Measurement.Device",
      "value": "PPMS-14"
    },
    {
      "@id": "./characterization-of-a-sample/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:46:38.317387+00:00",
      "dateModified": "2024-09-23T10:28:10.526780+00:00",
      "description": {
        "@id": "http://localhost:5000/records/49#description"
      },
      "hasPart": [
        {
          "@id": "./characterization-of-a-sample/characterization-of-a-sample.json"
        },
        {
          "@id": "./characterization-of-a-sample/characterization-of-a-sample.ttl"
        },
        {
          "@id": "./characterization-of-a-sample/files/asa.txt"
        }
      ],
      "identifier": "characterization-of-a-sample",
      "keywords": "characterization, mechanical properties",
      "name": "Characterization of a Sample",
      "variableMeasured": [
        {
          "@id": "http://localhost:5000/records/49#extras-Characterization%20type"
        },
        {
          "@id": "http://localhost:5000/records/49#extras-Characterization%20result%20file(s)"
        },
        {
          "@id": "http://localhost:5000/records/49#extras-Measurement.Device"
        }
      ]
    },
    {
      "@id": "./characterization-of-a-sample/characterization-of-a-sample.json",
      "@type": "File",
      "contentSize": "6685",
      "dateCreated": "2024-11-19T13:44:30.006566+00:00",
      "encodingFormat": "application/json",
      "name": "characterization-of-a-sample.json"
    },
    {
      "@id": "./characterization-of-a-sample/characterization-of-a-sample.ttl",
      "@type": "File",
      "contentSize": "2494",
      "dateCreated": "2024-11-19T13:44:30.006632+00:00",
      "encodingFormat": "text/turtle",
      "name": "characterization-of-a-sample.ttl"
    },
    {
      "@id": "http://localhost:5000/records/49/files/7d15b95c-6fd8-4556-8beb-6225f0bfff83#description",
      "@type": "TextObject",
      "encodingFormat": "text/markdown",
      "text": "sample file description"
    },
    {
      "@id": "./characterization-of-a-sample/files/asa.txt",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "3",
      "dateCreated": "2024-09-23T10:27:34.267189+00:00",
      "dateModified": "2024-09-23T10:28:10.532544+00:00",
      "description": {
        "@id": "http://localhost:5000/records/49/files/7d15b95c-6fd8-4556-8beb-6225f0bfff83#description"
      },
      "encodingFormat": "text/plain",
      "identifier": "7d15b95c-6fd8-4556-8beb-6225f0bfff83",
      "name": "asa.txt"
    },
    {
      "@id": "http://localhost:5000/records/51#description",
      "@type": "TextObject",
      "encodingFormat": "text/markdown",
      "text": "Instrument used in the experiment."
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Instrument.Settings.beam%20spot%20size",
      "@type": "PropertyValue",
      "propertyID": "Instrument.Settings.beam spot size",
      "unitText": "mm",
      "value": 1.2
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Instrument.Detector.0",
      "@type": "PropertyValue",
      "propertyID": "Instrument.Detector.0",
      "value": "EDT"
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Instrument.Detector.1",
      "@type": "PropertyValue",
      "propertyID": "Instrument.Detector.1",
      "value": "CDEM"
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Technical%20Data.Emitter",
      "@type": "PropertyValue",
      "propertyID": "Technical Data.Emitter",
      "value": "X-FEG"
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Technical%20Data.Vacuum%20system",
      "@type": "PropertyValue",
      "propertyID": "Technical Data.Vacuum system",
      "value": "oil-free"
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Software.PC%20Operating%20system",
      "@type": "PropertyValue",
      "propertyID": "Software.PC Operating system",
      "value": "Windows 7"
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Software.Analysis%20software.0",
      "@type": "PropertyValue",
      "propertyID": "Software.Analysis software.0",
      "value": "Velox"
    },
    {
      "@id": "http://localhost:5000/records/51#extras-Software.Analysis%20software.1",
      "@type": "PropertyValue",
      "propertyID": "Software.Analysis software.1",
      "value": "Velox EELS and EDS"
    },
    {
      "@id": "./instrument-used-in-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:50:07.621285+00:00",
      "dateModified": "2024-07-10T10:16:03.718253+00:00",
      "description": {
        "@id": "http://localhost:5000/records/51#description"
      },
      "hasPart": [
        {
          "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json"
        },
        {
          "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.ttl"
        },
        {
          "@id": "./instrument-used-in-experiment/files/Product-flyer_GeminiSEM_360.pdf"
        },
        {
          "@id": "./instrument-used-in-experiment/files/zeiss_gemini_360_microscope.jpeg"
        }
      ],
      "identifier": "instrument-used-in-experiment",
      "keywords": "high-resolution electron microscopy, instrument",
      "name": "Instrument used in experiment",
      "variableMeasured": [
        {
          "@id": "http://localhost:5000/records/51#extras-Instrument.Settings.beam%20spot%20size"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Instrument.Detector.0"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Instrument.Detector.1"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Technical%20Data.Emitter"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Technical%20Data.Vacuum%20system"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Software.PC%20Operating%20system"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Software.Analysis%20software.0"
        },
        {
          "@id": "http://localhost:5000/records/51#extras-Software.Analysis%20software.1"
        }
      ]
    },
    {
      "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json",
      "@type": "File",
      "contentSize": "5963",
      "dateCreated": "2024-11-19T13:44:30.114434+00:00",
      "encodingFormat": "application/json",
      "name": "instrument-used-in-experiment.json"
    },
    {
      "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.ttl",
      "@type": "File",
      "contentSize": "3016",
      "dateCreated": "2024-11-19T13:44:30.114477+00:00",
      "encodingFormat": "text/turtle",
      "name": "instrument-used-in-experiment.ttl"
    },
    {
      "@id": "./instrument-used-in-experiment/files/Product-flyer_GeminiSEM_360.pdf",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "2415711",
      "dateCreated": "2022-10-10T10:51:32.028390+00:00",
      "dateModified": "2022-10-10T10:51:32.051089+00:00",
      "encodingFormat": "application/pdf",
      "identifier": "936cc52e-5b8c-4baa-bcc6-570763c39123",
      "name": "Product-flyer_GeminiSEM_360.pdf"
    },
    {
      "@id": "./instrument-used-in-experiment/files/zeiss_gemini_360_microscope.jpeg",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "37414",
      "dateCreated": "2022-10-10T10:51:31.689397+00:00",
      "dateModified": "2022-10-10T10:51:31.715504+00:00",
      "encodingFormat": "image/jpeg",
      "identifier": "f4b5df90-062d-4a68-adac-9dd533777333",
      "name": "zeiss_gemini_360_microscope.jpeg"
    },
    {
      "@id": "./scripts-used-in-the-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:19:46.195177+00:00",
      "dateModified": "2023-09-04T14:54:31.034009+00:00",
      "hasPart": [
        {
          "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json"
        },
        {
          "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.ttl"
        },
        {
          "@id": "./scripts-used-in-the-experiment/files/test_script.py"
        }
      ],
      "identifier": "scripts-used-in-the-experiment",
      "keywords": "python, script",
      "name": "Scripts used in the experiment"
    },
    {
      "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json",
      "@type": "File",
      "contentSize": "3896",
      "dateCreated": "2024-11-19T13:44:30.243866+00:00",
      "encodingFormat": "application/json",
      "name": "scripts-used-in-the-experiment.json"
    },
    {
      "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.ttl",
      "@type": "File",
      "contentSize": "2030",
      "dateCreated": "2024-11-19T13:44:30.243927+00:00",
      "encodingFormat": "text/turtle",
      "name": "scripts-used-in-the-experiment.ttl"
    },
    {
      "@id": "./scripts-used-in-the-experiment/files/test_script.py",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "55",
      "dateCreated": "2022-10-10T10:20:00.504951+00:00",
      "dateModified": "2022-10-10T10:20:00.542591+00:00",
      "encodingFormat": "text/x-python",
      "identifier": "3e303b47-4087-4557-b825-bd29f81975b9",
      "name": "test_script.py"
    },
    {
      "@id": "./generated-files-during-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:48:28.007926+00:00",
      "dateModified": "2022-10-10T10:49:21.987613+00:00",
      "hasPart": [
        {
          "@id": "./generated-files-during-experiment/generated-files-during-experiment.json"
        },
        {
          "@id": "./generated-files-during-experiment/generated-files-during-experiment.ttl"
        },
        {
          "@id": "./generated-files-during-experiment/files/Test_experiment.csv"
        }
      ],
      "identifier": "generated-files-during-experiment",
      "keywords": "measurements",
      "name": "Generated files during experiment"
    },
    {
      "@id": "./generated-files-during-experiment/generated-files-during-experiment.json",
      "@type": "File",
      "contentSize": "929",
      "dateCreated": "2024-11-19T13:44:30.315045+00:00",
      "encodingFormat": "application/json",
      "name": "generated-files-during-experiment.json"
    },
    {
      "@id": "./generated-files-during-experiment/generated-files-during-experiment.ttl",
      "@type": "File",
      "contentSize": "1197",
      "dateCreated": "2024-11-19T13:44:30.315108+00:00",
      "encodingFormat": "text/turtle",
      "name": "generated-files-during-experiment.ttl"
    },
    {
      "@id": "./generated-files-during-experiment/files/Test_experiment.csv",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "87",
      "dateCreated": "2022-10-10T10:49:21.959310+00:00",
      "dateModified": "2022-10-10T10:49:21.997803+00:00",
      "encodingFormat": "text/csv",
      "identifier": "c1767022-a604-4de4-8bd5-0472f361967e",
      "name": "Test_experiment.csv"
    }
  ]
}
```

### records-example.eln

```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "dateCreated": "2024-11-19T13:44:35.476888+00:00",
      "sdPublisher": {
        "@id": "https://kadi.iam.kit.edu"
      },
      "version": "1.1.2"
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "datePublished": "2024-11-19",
      "description": "An RO-Crate exported from Kadi4Mat following the ELN file format specification.",
      "hasPart": [
        {
          "@id": "./records-example/"
        }
      ],
      "license": "For license information, please refer to the individual dataset nodes, if applicable.",
      "name": "records-example"
    },
    {
      "@id": "https://kadi.iam.kit.edu",
      "@type": "Organization",
      "description": "A generic and open source virtual research environment.",
      "name": "Kadi4Mat",
      "url": "https://kadi.iam.kit.edu"
    },
    {
      "@id": "http://localhost:5000/records/47#description",
      "@type": "TextObject",
      "encodingFormat": "text/markdown",
      "text": "This is a sample record."
    },
    {
      "@id": "http://localhost:5000/users/34",
      "@type": "Person",
      "name": "Manideep"
    },
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "@type": "CreativeWork",
      "identifier": "CC-BY-4.0",
      "name": "Creative Commons Attribution 4.0",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
      "@id": "http://localhost:5000/records/47#extras-type",
      "@type": "PropertyValue",
      "propertyID": "type",
      "value": "Measurement"
    },
    {
      "@id": "http://localhost:5000/records/47#extras-actor.givenName",
      "@type": "PropertyValue",
      "propertyID": "actor.givenName",
      "value": "Max"
    },
    {
      "@id": "http://localhost:5000/records/47#extras-actor.familyName",
      "@type": "PropertyValue",
      "propertyID": "actor.familyName",
      "value": "Mustermann"
    },
    {
      "@id": "http://localhost:5000/records/47#extras-Tools%20Used.0",
      "@type": "PropertyValue",
      "propertyID": "Tools Used.0",
      "value": "Universal Specimen holder"
    },
    {
      "@id": "http://localhost:5000/records/47#extras-Tools%20Used.1",
      "@type": "PropertyValue",
      "propertyID": "Tools Used.1",
      "value": "Flat specimen holder"
    },
    {
      "@id": "http://localhost:5000/records/47#extras-start%20date%20of%20experiment",
      "@type": "PropertyValue",
      "propertyID": "start date of experiment",
      "value": "2024-08-05T22:00:00+00:00"
    },
    {
      "@id": "./records-example/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:06:11.191752+00:00",
      "dateModified": "2024-08-21T11:43:17.626965+00:00",
      "description": {
        "@id": "http://localhost:5000/records/47#description"
      },
      "hasPart": [
        {
          "@id": "./records-example/records-example.json"
        },
        {
          "@id": "./records-example/records-example.ttl"
        },
        {
          "@id": "./records-example/files/example.csv"
        },
        {
          "@id": "./records-example/files/example.txt"
        }
      ],
      "identifier": "records-example",
      "keywords": "sample",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "records-example",
      "variableMeasured": [
        {
          "@id": "http://localhost:5000/records/47#extras-type"
        },
        {
          "@id": "http://localhost:5000/records/47#extras-actor.givenName"
        },
        {
          "@id": "http://localhost:5000/records/47#extras-actor.familyName"
        },
        {
          "@id": "http://localhost:5000/records/47#extras-Tools%20Used.0"
        },
        {
          "@id": "http://localhost:5000/records/47#extras-Tools%20Used.1"
        },
        {
          "@id": "http://localhost:5000/records/47#extras-start%20date%20of%20experiment"
        }
      ]
    },
    {
      "@id": "./records-example/records-example.json",
      "@type": "File",
      "contentSize": "3216",
      "dateCreated": "2024-11-19T13:44:35.590159+00:00",
      "encodingFormat": "application/json",
      "name": "records-example.json"
    },
    {
      "@id": "./records-example/records-example.ttl",
      "@type": "File",
      "contentSize": "2704",
      "dateCreated": "2024-11-19T13:44:35.590233+00:00",
      "encodingFormat": "text/turtle",
      "name": "records-example.ttl"
    },
    {
      "@id": "./records-example/files/example.csv",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "151",
      "dateCreated": "2022-10-10T10:06:54.806927+00:00",
      "dateModified": "2022-10-10T10:06:54.833108+00:00",
      "encodingFormat": "text/csv",
      "identifier": "ff576b4c-96e3-4bef-aaed-1b15da52a0b1",
      "name": "example.csv"
    },
    {
      "@id": "./records-example/files/example.txt",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "93",
      "dateCreated": "2022-10-10T10:06:54.567576+00:00",
      "dateModified": "2022-10-10T10:06:54.608407+00:00",
      "encodingFormat": "text/plain",
      "identifier": "78f16581-4b1f-45fc-b91d-837a057567ca",
      "name": "example.txt"
    }
  ]
}
```
