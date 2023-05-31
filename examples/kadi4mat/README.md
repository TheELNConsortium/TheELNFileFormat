# Kadi4Mat

### Basic Components of Kadi4Mat

**Records**, contain data and connect it with corresponding metadata. The data of a record can consist of an arbitrary number of different files, all sharing the same metadata, as well as metadata only.

**Collections**, represents simple, logical groupings of multiple records.

### Structure of the current Kadi4Mat example

**records-example.eln** is an archive of a single record in Kadi4Mat with some example files.

**collections-example.eln** is an archive of a group of multiple records with some example files in each record. Each record is represented as a folder in this archive.

# Kadi4Mat examples

## Concepts used

Files `{record_identifier}.json`, and  `{record_identifier}.ttl` are JSON export and RDF (Turtle) export of the record respectively. It contains the corresponding metadata specific to the record.

The actual content of the Record (i.e., Files) is stored in a separate folder `files` to prevent issues if a file with same name as JSON export file exists.

The `author` property represents the creator of either File, Link, or Record in Kadi4Mat.

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
| Resource Description | text                     |
| Creator              | author                   |

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
      "dateCreated": "2023-05-31T11:02:55.963946+00:00",
      "sdPublisher": {
        "@id": "https://kadi.iam.kit.edu"
      },
      "version": "1.0"
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./characterization-of-a-sample/"
        },
        {
          "@id": "./instrument-used-in-experiment/"
        },
        {
          "@id": "./generated-files-during-experiment/"
        },
        {
          "@id": "./scripts-used-in-the-experiment/"
        }
      ]
    },
    {
      "@id": "https://kadi.iam.kit.edu",
      "@type": "Organization",
      "description": "An open source software for managing research data.",
      "name": "Kadi4Mat",
      "url": "https://kadi.iam.kit.edu"
    },
    {
      "@id": "http://localhost:5000/users/34",
      "@type": "Person",
      "email": "test@gmail.com",
      "identifier": "jmanideep",
      "name": "Manideep"
    },
    {
      "@id": "http://localhost:5000/users/31",
      "@type": "Person",
      "email": "example@gmail.com",
      "identifier": "max_mustermann",
      "name": "Max Mustermann"
    },
    {
      "@id": "./characterization-of-a-sample/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:46:38.317387+00:00",
      "dateModified": "2023-05-31T10:02:44.517359+00:00",
      "hasPart": [
        {
          "@id": "./characterization-of-a-sample/characterization-of-a-sample.json"
        },
        {
          "@id": "./characterization-of-a-sample/characterization-of-a-sample.ttl"
        }
      ],
      "identifier": "characterization-of-a-sample",
      "keywords": ["characterization", "mechanical properties"],
      "name": "Characterization of a Sample",
      "text": "Some information about the instrument used in a process and other metadata like owner of the instrument etc."
    },
    {
      "@id": "./characterization-of-a-sample/characterization-of-a-sample.json",
      "@type": "File",
      "contentSize": "5342",
      "dateCreated": "2023-05-31T11:02:56.315575+00:00",
      "description": "JSON export of characterization-of-a-sample.",
      "encodingFormat": "application/json",
      "name": "characterization-of-a-sample.json"
    },
    {
      "@id": "./characterization-of-a-sample/characterization-of-a-sample.ttl",
      "@type": "File",
      "contentSize": "1729",
      "dateCreated": "2023-05-31T11:02:56.315628+00:00",
      "description": "RDF (Turtle) export of characterization-of-a-sample.",
      "encodingFormat": "text/turtle",
      "name": "characterization-of-a-sample.ttl"
    },
    {
      "@id": "./instrument-used-in-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:50:07.621285+00:00",
      "dateModified": "2022-10-10T10:55:33.784943+00:00",
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
      "keywords": ["high-resolution electron microscopy", "instrument"],
      "name": "Instrument used in experiment",
      "text": ""
    },
    {
      "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json",
      "@type": "File",
      "contentSize": "5644",
      "dateCreated": "2023-05-31T11:02:56.517565+00:00",
      "description": "JSON export of instrument-used-in-experiment.",
      "encodingFormat": "application/json",
      "name": "instrument-used-in-experiment.json"
    },
    {
      "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.ttl",
      "@type": "File",
      "contentSize": "2403",
      "dateCreated": "2023-05-31T11:02:56.517616+00:00",
      "description": "RDF (Turtle) export of instrument-used-in-experiment.",
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
      "name": "Product-flyer_GeminiSEM_360.pdf",
      "text": ""
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
      "name": "zeiss_gemini_360_microscope.jpeg",
      "text": ""
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
      "keywords": ["measurements"],
      "name": "Generated files during experiment",
      "text": ""
    },
    {
      "@id": "./generated-files-during-experiment/generated-files-during-experiment.json",
      "@type": "File",
      "contentSize": "2144",
      "dateCreated": "2023-05-31T11:02:56.647354+00:00",
      "description": "JSON export of generated-files-during-experiment.",
      "encodingFormat": "application/json",
      "name": "generated-files-during-experiment.json"
    },
    {
      "@id": "./generated-files-during-experiment/generated-files-during-experiment.ttl",
      "@type": "File",
      "contentSize": "1325",
      "dateCreated": "2023-05-31T11:02:56.647424+00:00",
      "description": "RDF (Turtle) export of generated-files-during-experiment.",
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
      "name": "Test_experiment.csv",
      "text": ""
    },
    {
      "@id": "./scripts-used-in-the-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:19:46.195177+00:00",
      "dateModified": "2022-10-10T10:20:00.536466+00:00",
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
      "keywords": ["python", "script"],
      "name": "Scripts used in the experiment",
      "text": ""
    },
    {
      "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json",
      "@type": "File",
      "contentSize": "2146",
      "dateCreated": "2023-05-31T11:02:56.788743+00:00",
      "description": "JSON export of scripts-used-in-the-experiment.",
      "encodingFormat": "application/json",
      "name": "scripts-used-in-the-experiment.json"
    },
    {
      "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.ttl",
      "@type": "File",
      "contentSize": "1331",
      "dateCreated": "2023-05-31T11:02:56.788800+00:00",
      "description": "RDF (Turtle) export of scripts-used-in-the-experiment.",
      "encodingFormat": "text/turtle",
      "name": "scripts-used-in-the-experiment.ttl"
    },
    {
      "@id": "./scripts-used-in-the-experiment/files/test_script.py",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/31"
      },
      "contentSize": "55",
      "dateCreated": "2022-10-10T10:20:00.504951+00:00",
      "dateModified": "2022-10-10T10:20:00.542591+00:00",
      "encodingFormat": "text/x-python",
      "identifier": "3e303b47-4087-4557-b825-bd29f81975b9",
      "name": "test_script.py",
      "text": ""
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
      "dateCreated": "2022-10-10T10:14:48.549179+00:00",
      "sdPublisher": {
        "@id": "https://kadi.iam.kit.edu"
      },
      "version": "1.0"
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./sample-record/"
        }
      ]
    },
    {
      "@id": "https://kadi.iam.kit.edu",
      "@type": "Organization",
      "description": "An open source software for managing research data.",
      "name": "Kadi4Mat",
      "url": "https://kadi.iam.kit.edu"
    },
    {
      "@id": "http://localhost:5000/users/34",
      "@type": "Person",
      "email": "test@gmail.com",
      "identifier": "jmanideep",
      "name": "Manideep"
    },
    {
      "@id": "http://localhost:5000/users/31",
      "@type": "Person",
      "email": "example@gmail.com",
      "identifier": "max_mustermann",
      "name": "Max Mustermann"
    },
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "@type": "CreativeWork",
      "identifier": "CC-BY-4.0",
      "name": "Creative Commons Attribution 4.0",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
      "@id": "./sample-record/",
      "@type": "Dataset",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "dateCreated": "2022-10-10T10:06:11.191752+00:00",
      "dateModified": "2022-10-10T10:08:51.554677+00:00",
      "hasPart": [
        {
          "@id": "./sample-record/sample-record.json"
        },
        {
          "@id": "./sample-record/sample-record.ttl"
        },
        {
          "@id": "./sample-record/files/example.csv"
        },
        {
          "@id": "./sample-record/files/example.txt"
        }
      ],
      "identifier": "sample-record",
      "keywords": ["characterization", "experiment"],
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Sample Record",
      "text": ""
    },
    {
      "@id": "./sample-record/sample-record.json",
      "@type": "File",
      "contentSize": "2117",
      "description": "JSON export of sample-record.",
      "encodingFormat": "application/json",
      "name": "sample-record.json"
    },
    {
      "@id": "./sample-record/sample-record.json",
      "@type": "File",
      "contentSize": "2117",
      "description": "JSON export of sample-record.",
      "encodingFormat": "application/json",
      "name": "sample-record.json"
    },
    {
      "@id": "./sample-record/sample-record.ttl",
      "@type": "File",
      "contentSize": "2447",
      "description": "RDF (Turtle) export of sample-record.",
      "encodingFormat": "text/plain",
      "name": "sample-record.ttl"
    },
    {
      "@id": "./sample-record/files/example.csv",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/34"
      },
      "contentSize": "151",
      "encodingFormat": "text/csv",
      "identifier": "ff576b4c-96e3-4bef-aaed-1b15da52a0b1",
      "name": "example.csv",
      "text": ""
    },
    {
      "@id": "./sample-record/files/example.txt",
      "@type": "File",
      "author": {
        "@id": "http://localhost:5000/users/31"
      },
      "contentSize": "93",
      "encodingFormat": "text/plain",
      "identifier": "78f16581-4b1f-45fc-b91d-837a057567ca",
      "name": "example.txt",
      "text": ""
    }
  ]
}
```
