# Kadi4Mat

### Basic Components of Kadi4Mat

**Records**, contain data and connect it with corresponding metadata. The data of a record can consist of an arbitrary number of different files, all sharing the same metadata, as well as metadata only.

**Collections**, represents simple, logical groupings of multiple records.

### Structure of the current Kadi4Mat example

**records-example.eln** is an archive of a single record in Kadi4Mat with some example files.

**collections-example.eln** is an archive of a group of multiple records with some example files in each record. Each record is represented as a folder in this archive.

# Kadi4Mat examples

## Concepts used

A file `{record_identifier}.json` is a JSON export of the record and is added to the archive during export. It contains the corresponding metadata specific to the record.

The following table is the mapping of Kadi4Mat concepts to the base metadata standard of RO-Crate specification (i.e., **schema.org**)

|  Kadi4Mat concepts    |  JSON property           |
|-----------------------|--------------------------|
|  JSON export          | {record_identifier}.json |
|  File name            | name                     |
|  File Size            | contentSize              |
|  File MIME Type       | encodingFormat           |
|  File ID              | identifier               |
|  tags                 | keywords                 |
|  Resource Title       | name                     |
|  Resource Identifier  | identifier               |
|  Resource Description | text                     |

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
            "conformsTo":{
                "@id": "https://w3id.org/ro/crate/1.1"
            },
            "schemaVersion": "https://w3id.org/ro/crate/1.1",
            "sdPublisher":{
                "@type": "Organization",
                "name": "Kadi4Mat",
                "description": "An open source software for managing research data.",
                "logo": "https://kadi.iam-cms.kit.edu/static/images/kadi.png",
                "url": "https://kadi4mat.iam-cms.kit.edu"
            },
            "version": "1.0"
        },
        {
            "@id":"./",
            "@type": [
                "Dataset"
            ],
            "hasPart":[
                {
                    "@id": "./characterization-of-a-sample/"
                },
                {
                    "@id":"./generated-files-during-experiment/"
                },
                {
                    "@id" :"./instrument-used-in-experiment/"
                },
                {
                    "@id":"./scripts-used-in-the-experiment/"
                }
            ]
        },
        {
            "@id":"./characterization-of-a-sample/",
            "@type": "Dataset",
            "identifier": "characterization-of-a-sample",
            "keywords":[
                "characterization",
                "mechanical properties"
              ],
            "name": "Characterization of a Sample",
            "text": "Some information about the instrument used in a process and other metadata like owner of the instrument etc.",
            "hasPart":[
                {
                    "@id":"./characterization-of-a-sample/characterization-of-a-sample.json"
                },
                {
                    "@id": "./characterization-of-a-sample/characterization-of-a-sample.pdf"
                }
               
            ]
        },
        {
            "@id":"./characterization-of-a-sample/characterization-of-a-sample.json",
            "@type": "File",
            "description": "JSON export.",
            "encodingFormat": "application/json",
            "name": "characterization-of-a-sample.json"
        },
        {
            "@id":"./characterization-of-a-sample/characterization-of-a-sample.pdf",
            "@type": "File",
            "description": "PDF export.",
            "encodingFormat": "application/pdf",
            "name": "characterization-of-a-sample.pdf"
        },
        {
            "@id":"./generated-files-during-experiment/",
            "@type": "Dataset",
            "identifier": "generated-files-during-experiment",
            "keywords": [
                "measurements"
            ],
            "name": "Generated files during experiment",
            "text": "Some example files generated during the experiment.",
            "hasPart": [
                {
                    "@id":"./generated-files-during-experiment/Test_experiment.csv"
                },
                {
                    "@id":"./generated-files-during-experiment/generated-files-during-experiment.json"
                }
            ]
        },
        {
            "@id":"./generated-files-during-experiment/Test_experiment.csv",
            "@type": "File",
            "encodingFormat": "text/csv",
            "contentSize": "87",
            "identifier": "688f6cf2-4a51-4fa1-8b07-db77ddcd9f74",
            "name": "Test_experiment.csv"
        },
        {
            "@id":"../generated-files-during-experiment/generated-files-during-experiment.json",
            "@type": "File",
            "description": "JSON export.",
            "encodingFormat": "application/json",
            "name": "generated-files-during-experiment.json"
        },
        {
            "@id":"./instrument-used-in-experiment/",
            "@type": "Dataset",
            "identifier": "instrument-used-in-experiment",
            "keywords":[
                "high-resolution electron microscopy",
                "instrument"
              ],
            "name": "Instrument used in experiment",
            "text": "Information related to the instrument used in the experiment.",
            "hasPart":[
                {
                    "@id" : "./instrument-used-in-experiment/zeiss_gemini_360_microscope.jpeg"
                },
                {
                    "@id": "./instrument-used-in-experiment/Product-flyer_GeminiSEM_360.pdf"
                },
                {
                    "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json"
                }
            ]
        },
        {
            "@id" : "./instrument-used-in-experiment/zeiss_gemini_360_microscope.jpeg",
            "@type": "File",
            "contentSize": "37414",
            "encodingFormat": "image/jpeg",
            "identifier": "fa134da2-71d2-4ac5-ad8b-00f4c7e2cdad",
            "name": "zeiss_gemini_360_microscope.jpeg"
        },
        {
            "@id": "./instrument-used-in-experiment/Product-flyer_GeminiSEM_360.pdf",
            "@type":"File",
            "contentSize": "2415711",
            "encodingFormat": "application/pdf",
            "identifier": "68396f45-dd7e-464f-9ead-2135af92bee8",
            "name": "Product-flyer_GeminiSEM_360.pdf"
        },
        {
            "@id": "./instrument-used-in-experiment/instrument-used-in-experiment.json",
            "@type": "File",
            "description": "JSON export.",
            "encodingFormat": "application/json",
            "name": "instrument-used-in-experiment.json"
        },
        {
            "@id":"./scripts-used-in-the-experiment/",
            "@type": "Dataset",
            "identifier": "scripts-used-in-the-experiment",
            "keywords": [
                "script",
                "python"
            ],
            "name": "Scripts used in the experiment",
            "hasPart":[
                {
                    "@id": "./scripts-used-in-the-experiment/test_script.py"
                },
                {
                    "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json"
                }
            ]
        },
        {
            "@id": "./scripts-used-in-the-experiment/test_script.py",
            "@type": "File",
            "contentSize": "55",
            "encodingFormat": "text/x-python",
            "identifier": "923d7189-81a5-4e31-9517-efb619226a11",
            "name": "test_script.py"
        },
        {
            "@id": "./scripts-used-in-the-experiment/scripts-used-in-the-experiment.json",
            "@type": "File",
            "description": "JSON export.",
            "encodingFormat": "application/json",
            "name": "scripts-used-in-the-experiment.json"
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
            "conformsTo":{
                "@id": "https://w3id.org/ro/crate/1.1"
            },
            "dateCreated": "2022-06-08T08:34:39.996698+00:00",
            "schemaVersion": "https://w3id.org/ro/crate/1.1",
            "sdPublisher":{
                "@type": "Organization",
                "name": "Kadi4Mat",
                "description": "An open source software for managing research data.",
                "logo": "https://kadi.iam-cms.kit.edu/static/images/kadi.png",
                "url": "https://kadi4mat.iam-cms.kit.edu"
            },
            "version": "1.0"
        },
        {
            "@id":"./",
            "@type": [
                "Dataset"
            ],
            "hasPart":[
                {
                    "@id": "./sample-record/"
                }
            ]
        },
        {
            "@id": "./sample-record/",
            "@type": "Dataset",
            "author": {
                "@type": "Person",
                "familyName": "Mustermann",
                "givenName": "Max"
            },
            "identifier" :"sample-record",
            "keywords": [
                "characterization",
                "experiment"
              ],
            "name": "Sample Record",
            "text": "A single record in Kadi4Mat.",
            "hasPart":[
                {
                    "@id": "./sample-record/example.csv"
                },
                {
                    "@id": "./sample-record/example.txt"
                },
                {
                    "@id": "./sample-record/sample-record.json"
                },
                {
                    "@id": "./sample-record/sample-record.pdf"
                },
                {
                    "@id": "./sample-record/sample-record.png"
                }
            ]
        },
        {
            "@id": "./sample-record/example.csv",
            "@type": "File",
            "contentSize": "151",
            "encodingFormat": "text/csv",
            "identifier": "1049f570-2525-4ee9-b502-0a678e555c88",
            "name": "example.csv"
        },
        {
            "@id": "./sample-record/example.txt",
            "@type": "File",
            "contentSize": "93",
            "encodingFormat": "text/plain",
            "identifier": "29ef5432-220c-4643-8e69-32bda6c4436f",
            "name": "example.txt"
        },
        {
            "@id": "./sample-record/sample-record.json",
            "@type": "File",
            "description": "JSON Export",
            "encodingFormat": "application/json",
            "name": "sample-record.json"
        },
        {
            "@id": "./sample-record/sample-record.pdf",
            "@type": "File",
            "description": "PDF Export",
            "encodingFormat": "application/pdf",
            "name": "sample-record.pdf"
        },
        {
            "@id": "./sample-record/sample-record.png",
            "@type": "File",
            "description": "QR Export",
            "encodingFormat": "image/png",
            "name": "sample-record.png"
        }
    ]
}
```
