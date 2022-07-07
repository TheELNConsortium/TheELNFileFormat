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
|  Resource Description | description              |

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
            "description": "Group of records(as folders) that are part of the collection in Kadi4Mat.",
            "hasPart":[
                {
                    "@id": "./Characterization-of-a-Sample/"
                },
                {
                    "@id":"./Generated-files-during-experiment/"
                },
                {
                    "@id" :"./Instrument-used-in-experiment/"
                },
                {
                    "@id":"./Scripts-used-in-the-experiment/"
                }
            ]
        },
        {
            "@id":"./Characterization-of-a-Sample/",
            "@type": "Dataset",
            "name": "A record with an example characterization experiment.",
            "hasPart":[
                {
                    "@id":"./Characterization-of-a-Sample/characterization-of-a-sample.json"
                },
                {
                    "@id": "./Characterization-of-a-Sample/characterization-of-a-sample.pdf"
                }
                
            ]
        },
        {
            "@id":"./Characterization-of-a-Sample/characterization-of-a-sample.json",
            "@type": "File",
            "description": "JSON export.",
            "encodingFormat": "application/json"
        },
        {
            "@id":"./Characterization-of-a-Sample/characterization-of-a-sample.pdf",
            "@type": "File",
            "description": "PDF export.",
            "encodingFormat": "application/pdf"
        },
        {
            "@id":"./Generated-files-during-experiment/",
            "@type": "Dataset",
            "name": "Some example files generated during the experiment.",
            "hasPart": [
                {
                    "@id":"./Generated-files-during-experiment/Test_experiment.csv"
                }
            ]
        },
        {
            "@id":"./Generated-files-during-experiment/Test_experiment.csv",
            "@type": "File",
            "encodingFormat": "text/csv",
            "sha256": "0e2d934f40d7fdc2863c3434027d5ddf83225beac9af5b716a63420c7050d2c0"
        },
        {
            "@id":"./Instrument-used-in-experiment/",
            "@type": "Dataset",
            "name": "Instrument related information.",
            "description": "Related files attached in the current record.",
            "hasPart":[
                {
                    "@id" : "./Instrument-used-in-experiment/zeiss_gemini_360_microscope.jpeg"
                },
                {
                    "@id": "./Instrument-used-in-experiment/Product-flyer_GeminiSEM_360.pdf"
                }
            ]
        },
        {
            "@id" : "./Instrument-used-in-experiment/zeiss_gemini_360_microscope.jpeg",
            "@type": "File",
            "name": "Zeiss GeminiSEM 360",
            "encodingFormat": "image/jpeg",
            "sha256": "ba8b6d49daccf711dbf715df9f83fb311aaa1a319b5735ce2a0a5761f61a029d"
        },
        {
            "@id": "./Instrument-used-in-experiment/Product-flyer_GeminiSEM_360.pdf",
            "@type":"File",
            "name": "Product Flyer",
            "description": "Detailed information about the technical specifications of Zeiss GeminiSEM 360.",
            "encodingFormat": "application/pdf",
            "sha256": "e073424647390ad772eb724112cdad8167961a98ae3a5e4c47c4f3a1cbc32c9d"
        },
        {
            "@id":"./Scripts-used-in-the-experiment/",
            "@type": "Dataset",
            "name": "Scripts used in the experiment.",
            "hasPart":[
                {
                    "@id": "./Scripts-used-in-the-experiment/test_script.py"
                }
            ]
        },
        {
            "@id": "./Scripts-used-in-the-experiment/test_script.py",
            "@type": "File",
            "encodingFormat": "text/x-python",
            "sha256": "d768da9010dc334c86d9a936a872dc5c5c2f496072e0d90d349540326799453b"
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
            "description": "A single record in Kadi4Mat.",
            "hasPart":[
                {
                    "@id": "./sample-record/"
                }
                
            ]
        },
        {
            "@id": "./sample-record/",
            "@type": "Dataset",
            "name": "sample-record",
            "author": {
                "@type": "Person",
                "familyName": "Mustermann",
                "givenName": "Max"
            },
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
            "name": "example.csv",
            "description": "Some example CSV file saved in a record.",
            "encodingFormat": "text/csv",
            "contentSize": "151",
            "sha256": "96d583afd10a85fd1c1a8c5fab1af52a0bc515f769377b2253fc16883646dd70"
        },
        {
            "@id": "./sample-record/example.txt",
            "@type": "File",
            "name": "example.txt",
            "description": "Some example Text file saved in a record.",
            "encodingFormat": "text/plain",
            "contentSize": "93",
            "sha256": "6648775a9dbb1a493d67849c703b2f493bff94a6b4bab1348bd55d64e8894460"
        },
        {
            "@id": "./sample-record/sample-record.json",
            "@type": "File",
            "name": "sample-record.json",
            "description": "JSON Export",
            "encodingFormat": "application/json"
        },
        {
            "@id": "./sample-record/sample-record.pdf",
            "@type": "File",
            "name": "sample-record.pdf",
            "description": "PDF Export",
            "encodingFormat": "application/pdf"
        },
        {
            "@id": "./sample-record/sample-record.png",
            "@type": "File",
            "name": "sample-record.png",
            "description": "QR Export",
            "encodingFormat": "image/png"
        }
        
    ]
}
```