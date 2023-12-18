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
      "dateCreated": "2023-12-18T08:21:19.471161+00:00",
      "sdPublisher": {
        "@id": "https://kadi.iam.kit.edu"
      },
      "version": "1.0"
    },
    {
      "@id": "./",
      "@type": ["Dataset"],
      "hasPart": [
        {
          "@id": "./scripts-used-in-the-experiment/"
        },
        {
          "@id": "./instrument-used-in-experiment/"
        },
        {
          "@id": "./generated-files-during-experiment/"
        },
        {
          "@id": "./characterization-of-a-sample/"
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
      "@id": "https://orcid.org/0000-0002-3495-9100",
      "@type": "Person",
      "name": "Manideep Jayavarapu"
    },
    {
      "@id": "https://kadi4mat.iam-cms.kit.edu/records/11672#other-at",
      "@type": "CreativeWork",
      "identifier": "other-at",
      "name": "Other (Attribution)"
    },
    {
      "@id": "./scripts-used-in-the-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "dateCreated": "2022-07-08T07:29:06.319759+00:00",
      "dateModified": "2023-09-04T13:29:32.724539+00:00",
      "hasPart": [
        {
          "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json"
        },
        {
          "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.ttl"
        },
        {
          "@id": "./scripts-used-in-the-experiment/files/test_script.py"
        },
        {
          "@id": "./scripts-used-in-the-experiment/files/301122-cag-13001-nano-silver-ink-annealed-flower-a.json"
        }
      ],
      "identifier": "scripts-used-in-the-experiment",
      "keywords": "python, script",
      "license": {
        "@id": "https://kadi4mat.iam-cms.kit.edu/records/11672#other-at"
      },
      "name": "Scripts used in the experiment",
      "text": ""
    },
    {
      "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json",
      "@type": "File",
      "contentSize": "9968",
      "dateCreated": "2023-12-18T08:21:19.687398+00:00",
      "description": "JSON export of scripts-used-in-the-experiment.",
      "encodingFormat": "application/json",
      "name": "scripts-used-in-the-experiment.json"
    },
    {
      "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.ttl",
      "@type": "File",
      "contentSize": "2857",
      "dateCreated": "2023-12-18T08:21:19.689579+00:00",
      "description": "RDF (Turtle) export of scripts-used-in-the-experiment.",
      "encodingFormat": "text/turtle",
      "name": "scripts-used-in-the-experiment.ttl"
    },
    {
      "@id": "./scripts-used-in-the-experiment/files/test_script.py",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "55",
      "dateCreated": "2022-07-08T07:29:50.914076+00:00",
      "dateModified": "2022-12-05T15:45:11.669968+00:00",
      "encodingFormat": "text/x-python",
      "identifier": "923d7189-81a5-4e31-9517-efb619226a11",
      "name": "test_script.py",
      "text": "A sample python file."
    },
    {
      "@id": "./scripts-used-in-the-experiment/files/301122-cag-13001-nano-silver-ink-annealed-flower-a.json",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "37493",
      "dateCreated": "2022-12-05T14:31:27.522031+00:00",
      "dateModified": "2022-12-05T14:31:27.692988+00:00",
      "encodingFormat": "application/json",
      "identifier": "aaab0261-4fbe-4270-bfd7-d68b9c83df02",
      "name": "301122-cag-13001-nano-silver-ink-annealed-flower-a.json",
      "text": ""
    },
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "@type": "CreativeWork",
      "identifier": "CC-BY-4.0",
      "name": "Creative Commons Attribution 4.0",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
      "@id": "./instrument-used-in-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "dateCreated": "2022-06-01T08:26:42.763612+00:00",
      "dateModified": "2023-09-04T13:29:32.675449+00:00",
      "hasPart": [
        {
          "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json"
        },
        {
          "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.ttl"
        },
        {
          "@id": "./instrument-used-in-experiment/files/zeiss_gemini_360_microscope.jpeg"
        },
        {
          "@id": "./instrument-used-in-experiment/files/Product-flyer_GeminiSEM_360.pdf"
        }
      ],
      "identifier": "instrument-used-in-experiment",
      "keywords": "high-resolution electron microscopy, instrument",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Instrument-used-in-experiment",
      "text": ""
    },
    {
      "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json",
      "@type": "File",
      "contentSize": "10871",
      "dateCreated": "2023-12-18T08:21:19.900682+00:00",
      "description": "JSON export of instrument-used-in-experiment.",
      "encodingFormat": "application/json",
      "name": "instrument-used-in-experiment.json"
    },
    {
      "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.ttl",
      "@type": "File",
      "contentSize": "3521",
      "dateCreated": "2023-12-18T08:21:19.900729+00:00",
      "description": "RDF (Turtle) export of instrument-used-in-experiment.",
      "encodingFormat": "text/turtle",
      "name": "instrument-used-in-experiment.ttl"
    },
    {
      "@id": "./instrument-used-in-experiment/files/zeiss_gemini_360_microscope.jpeg",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "37414",
      "dateCreated": "2022-06-01T08:26:51.331083+00:00",
      "dateModified": "2023-06-14T12:35:45.738816+00:00",
      "encodingFormat": "image/jpeg",
      "identifier": "fa134da2-71d2-4ac5-ad8b-00f4c7e2cdad",
      "name": "zeiss_gemini_360_microscope.jpeg",
      "text": "Microscope file"
    },
    {
      "@id": "./instrument-used-in-experiment/files/Product-flyer_GeminiSEM_360.pdf",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "2415711",
      "dateCreated": "2022-06-01T08:26:50.896099+00:00",
      "dateModified": "2022-06-01T08:26:51.013059+00:00",
      "encodingFormat": "application/pdf",
      "identifier": "68396f45-dd7e-464f-9ead-2135af92bee8",
      "name": "Product-flyer_GeminiSEM_360.pdf",
      "text": ""
    },
    {
      "@id": "./generated-files-during-experiment/",
      "@type": "Dataset",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "dateCreated": "2022-06-01T08:24:03.115590+00:00",
      "dateModified": "2023-09-04T13:29:32.621928+00:00",
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
      "name": "Generated files during experiment",
      "text": ""
    },
    {
      "@id": "./generated-files-during-experiment/generated-files-during-experiment.json",
      "@type": "File",
      "contentSize": "4678",
      "dateCreated": "2023-12-18T08:21:20.050136+00:00",
      "description": "JSON export of generated-files-during-experiment.",
      "encodingFormat": "application/json",
      "name": "generated-files-during-experiment.json"
    },
    {
      "@id": "./generated-files-during-experiment/generated-files-during-experiment.ttl",
      "@type": "File",
      "contentSize": "1903",
      "dateCreated": "2023-12-18T08:21:20.050203+00:00",
      "description": "RDF (Turtle) export of generated-files-during-experiment.",
      "encodingFormat": "text/turtle",
      "name": "generated-files-during-experiment.ttl"
    },
    {
      "@id": "./generated-files-during-experiment/files/Test_experiment.csv",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "87",
      "dateCreated": "2022-06-01T08:24:20.096041+00:00",
      "dateModified": "2022-07-08T07:06:32.277413+00:00",
      "encodingFormat": "text/csv",
      "identifier": "688f6cf2-4a51-4fa1-8b07-db77ddcd9f74",
      "name": "Test_experiment.csv",
      "text": ""
    },
    {
      "@id": "./characterization-of-a-sample/",
      "@type": "Dataset",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "dateCreated": "2022-05-30T11:09:35.212226+00:00",
      "dateModified": "2023-09-04T13:29:32.557353+00:00",
      "hasPart": [
        {
          "@id": "./characterization-of-a-sample/characterization-of-a-sample.json"
        },
        {
          "@id": "./characterization-of-a-sample/characterization-of-a-sample.ttl"
        }
      ],
      "identifier": "characterization-of-a-sample",
      "keywords": "characterization, mechanical properties",
      "name": "Characterization of a Sample",
      "text": "Some information about the instrument used in a process and other metadata like owner of the instrument etc."
    },
    {
      "@id": "./characterization-of-a-sample/characterization-of-a-sample.json",
      "@type": "File",
      "contentSize": "11979",
      "dateCreated": "2023-12-18T08:21:20.204465+00:00",
      "description": "JSON export of characterization-of-a-sample.",
      "encodingFormat": "application/json",
      "name": "characterization-of-a-sample.json"
    },
    {
      "@id": "./characterization-of-a-sample/characterization-of-a-sample.ttl",
      "@type": "File",
      "contentSize": "3083",
      "dateCreated": "2023-12-18T08:21:20.204516+00:00",
      "description": "RDF (Turtle) export of characterization-of-a-sample.",
      "encodingFormat": "text/turtle",
      "name": "characterization-of-a-sample.ttl"
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
      "dateCreated": "2023-12-18T08:22:17.681025+00:00",
      "sdPublisher": {
        "@id": "https://kadi.iam.kit.edu"
      },
      "version": "1.0"
    },
    {
      "@id": "./",
      "@type": ["Dataset"],
      "hasPart": [
        {
          "@id": "./records-example/"
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
      "@id": "https://orcid.org/0000-0002-3495-9100",
      "@type": "Person",
      "name": "Manideep Jayavarapu"
    },
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "@type": "CreativeWork",
      "identifier": "CC-BY-4.0",
      "name": "Creative Commons Attribution 4.0",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    },
    {
      "@id": "./records-example/",
      "@type": "Dataset",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "dateCreated": "2022-06-08T08:34:39.996698+00:00",
      "dateModified": "2023-12-18T08:22:07.596157+00:00",
      "hasPart": [
        {
          "@id": "./records-example/records-example.json"
        },
        {
          "@id": "./records-example/records-example.ttl"
        },
        {
          "@id": "./records-example/files/example.txt"
        },
        {
          "@id": "./records-example/files/example.csv"
        }
      ],
      "identifier": "records-example",
      "keywords": "characterization, experiment",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "records-example",
      "text": ""
    },
    {
      "@id": "./records-example/records-example.json",
      "@type": "File",
      "contentSize": "4632",
      "dateCreated": "2023-12-18T08:22:17.886292+00:00",
      "description": "JSON export of records-example.",
      "encodingFormat": "application/json",
      "name": "records-example.json"
    },
    {
      "@id": "./records-example/records-example.ttl",
      "@type": "File",
      "contentSize": "2447",
      "dateCreated": "2023-12-18T08:22:17.888900+00:00",
      "description": "RDF (Turtle) export of records-example.",
      "encodingFormat": "text/turtle",
      "name": "records-example.ttl"
    },
    {
      "@id": "./records-example/files/example.txt",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "93",
      "dateCreated": "2022-06-15T08:54:35.406311+00:00",
      "dateModified": "2022-06-15T08:58:03.198999+00:00",
      "encodingFormat": "text/plain",
      "identifier": "29ef5432-220c-4643-8e69-32bda6c4436f",
      "name": "example.txt",
      "text": ""
    },
    {
      "@id": "./records-example/files/example.csv",
      "@type": "File",
      "author": {
        "@id": "https://orcid.org/0000-0002-3495-9100"
      },
      "contentSize": "151",
      "dateCreated": "2022-06-08T12:34:26.278248+00:00",
      "dateModified": "2022-06-08T12:34:26.448668+00:00",
      "encodingFormat": "text/csv",
      "identifier": "1049f570-2525-4ee9-b502-0a678e555c88",
      "name": "example.csv",
      "text": ""
    }
  ]
}
```
