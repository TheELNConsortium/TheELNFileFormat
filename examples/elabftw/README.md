# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

## Concepts used

Here is a correspondance between concepts in eLabFTW and how they are translated in the metadata json file in the archive:

| eLabFTW concepts    | JSON property          |
|---------------------|------------------------|
| body (main content) | text                   |
| category            | about                  |
| comments            | comment                |
| content_type        | encodingFormat         |
| created_at          | dateCreated            |
| custom_id           | alternateName          |
| elabid              | identifier             |
| entity type         | genre                  |
| links               | mentions               |
| metadata            | variableMeasured       |
| modified_at         | dateModified           |
| owner               | author                 |
| rating              | aggregateRating        |
| status              | creativeWorkStatus     |
| steps               | step                   |
| tags                | keywords               |
| title               | name                   |


### export.eln
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
      "dateCreated": "2024-06-15T16:00:23+02:00",
      "sdPublisher": {
        "@id": "#publisher"
      },
      "version": "1.0"
    },
    {
      "@id": "#publisher",
      "@type": "Organization",
      "areaServed": "Laniakea Supercluster",
      "name": "eLabFTW",
      "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
      "slogan": "A free and open source electronic lab notebook.",
      "url": "https://www.elabftw.net",
      "parentOrganization": {
        "@type": "Organization",
        "name": "Deltablot",
        "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
        "slogan": "Open Source software for research labs.",
        "url": "https://www.deltablot.com"
      }
    },
    {
      "@id": "#ro-crate_created",
      "@type": "CreateAction",
      "object": {
        "@id": "./"
      },
      "name": "RO-Crate created",
      "endTime": "2024-06-15T16:00:23+02:00",
      "instrument": {
        "@id": "https://www.elabftw.net"
      },
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      }
    },
    {
      "@id": "https://www.elabftw.net",
      "@type": "SoftwareApplication",
      "name": "eLabFTW",
      "version": "5.1.0",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "./Project-CASIMIR - Markdown-experiment - ce78d5e4/example.pdf",
      "@type": "File",
      "name": "example.pdf",
      "alternateName": "eb/ebbd7f68548d2e52bc7ae937f43f2f87706c11cbe69d96365a303f1b0d607e8a7da613d4c4962202e8e117dca4a51d86a4b47e6b83976c07fe2d4911ad045e6e.pdf",
      "contentSize": 116369,
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1"
    },
    {
      "@id": "./Project-CASIMIR - Markdown-experiment - ce78d5e4/example.png",
      "@type": "File",
      "name": "example.png",
      "alternateName": "e0/e021d9f1278e5e289e6c75a70e78dd717b5ae58b17282c65b89daa2c173298d195a8ff86a9f0f3eb36198b3f2712d315f595de49d3d4cda43cf0c8ff3f44356e.png",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "#category-Project CASIMIR",
      "@type": "Thing",
      "name": "Project CASIMIR"
    },
    {
      "@id": "./Project-CASIMIR - Markdown-experiment - ce78d5e4/",
      "@type": "Dataset",
      "author": {
        "@id": "person://797dd58d4ee3e5e9c6cc81c28ee2cd60d408a48bded24131581f98fa7de0b141?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T23:24:55+02:00",
      "dateModified": "2024-06-15T15:56:36+02:00",
      "name": "Markdown experiment",
      "encodingFormat": "text/markdown",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=298",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CASIMIR"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      }
    },
    {
      "@id": "comment://2024-06-15T15%3A49%3A49%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2024-06-15T15:49:49+02:00",
      "text": "this is a comment",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CASIMIR - Experiment-with-an-image-in-the-text - 2c00e9a2/haproxy3-stats-reload.png",
      "@type": "File",
      "name": "haproxy3-stats-reload.png",
      "alternateName": "cf/cfc36b71003a82ccb366a7a3694dba3972eab46002f61384f3c5437885f6944ec15189f8a5596b1cffd07c2a565c7beb9094cd1b8e0ac371b937777defd87f6b.png",
      "contentSize": 30301,
      "sha256": "2f7944084e994fff29c372ca2111796f3603463636aba8e2f656cb69f071f523"
    },
    {
      "@id": "#category-Project CASIMIR",
      "@type": "Thing",
      "name": "Project CASIMIR"
    },
    {
      "@id": "./Project-CASIMIR - Experiment-with-an-image-in-the-text - 2c00e9a2/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-14T18:13:33+02:00",
      "dateModified": "2024-06-15T15:51:40+02:00",
      "name": "Experiment with an image in the text",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=301",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CASIMIR"
      },
      "variableMeasured": null,
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "creativeWorkStatus": "finished",
          "temporal": "2024-06-15T15:51:40+02:00",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "step 1"
            }
          ]
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "creativeWorkStatus": "finished",
          "temporal": "2024-06-15T15:51:40+02:00",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "step 2"
            }
          ]
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "creativeWorkStatus": "unfinished",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "step 3"
            }
          ]
        }
      ]
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 734dad66/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:24+02:00",
      "dateModified": "2024-06-10T22:48:24+02:00",
      "name": "Gold master experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=289",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group 1\"}, {\"id\": 2, \"name\": \"Group 2\"}, {\"id\": 3, \"name\": \"Last group\"}]}, \"extra_fields\": {\"Number\": {\"type\": \"number\", \"unit\": \"\", \"units\": [], \"value\": \"\", \"group_id\": 2, \"description\": \"no units\"}, \"Type URL\": {\"type\": \"url\", \"value\": \"https://www.elabftw.net\", \"group_id\": 2, \"readonly\": true, \"description\": \"a link (readonly)\"}, \"Just time\": {\"type\": \"time\", \"value\": \"17:00\", \"group_id\": 2, \"description\": \"tea time\"}, \"Some date\": {\"type\": \"date\", \"value\": \"2024-07-14\", \"group_id\": 2, \"description\": \"is a date\"}, \"Type user\": {\"type\": \"users\", \"value\": 1, \"group_id\": 3, \"description\": \"this is a link to a user\"}, \"A checkbox\": {\"type\": \"checkbox\", \"value\": \"on\", \"group_id\": 2, \"description\": \"is checked\"}, \"Email input\": {\"type\": \"email\", \"value\": \"louis@example.com\", \"group_id\": 2, \"description\": \"type email\"}, \"Date and time\": {\"type\": \"datetime-local\", \"value\": \"2024-07-14T13:37\", \"group_id\": 2, \"description\": \"datetime description\"}, \"Radio buttons\": {\"type\": \"radio\", \"value\": \"Oui\", \"options\": [\"Oui\", \"Non\", \"Peut-\u00eatre\"], \"group_id\": 1, \"description\": \"radio description\"}, \"Type resource\": {\"type\": \"items\", \"value\": 208, \"group_id\": 3, \"description\": \"This is a link to a resource\"}, \"A dropdown menu\": {\"type\": \"select\", \"value\": \"Choice 1\", \"options\": [\"Choice 1\", \"Choice 2\", \"Choice 3\"], \"group_id\": 1, \"description\": \"Single select\"}, \"Text input name\": {\"type\": \"text\", \"value\": \"some text\", \"group_id\": 1, \"readonly\": true, \"required\": true, \"description\": \"type text + all attributes\", \"blank_value_on_duplicate\": true}, \"Type experiment\": {\"type\": \"experiments\", \"value\": 373, \"group_id\": 3, \"description\": \"This is a link to an experiment\"}, \"Number with units\": {\"type\": \"number\", \"unit\": \"mM\", \"units\": [\"mM\", \"\u03bcM\", \"nM\"], \"value\": \"\", \"group_id\": 2, \"description\": \"this one has units\"}, \"Unchecked checkbox\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 2, \"description\": \"this one is not checked\"}, \"Multi dropdown menu\": {\"type\": \"select\", \"value\": \"Option 1\", \"options\": [\"Option 1\", \"Option 2\", \"Option 3\"], \"group_id\": 1, \"description\": \"Allows multiple selection\", \"allow_multi_values\": true}}}"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Number",
          "valueReference": "number",
          "value": "",
          "description": "no units"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Type URL",
          "valueReference": "url",
          "value": "https://www.elabftw.net",
          "description": "a link (readonly)"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Just time",
          "valueReference": "time",
          "value": "17:00",
          "description": "tea time"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Some date",
          "valueReference": "date",
          "value": "2024-07-14",
          "description": "is a date"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Type user",
          "valueReference": "users",
          "value": 1,
          "description": "this is a link to a user"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "A checkbox",
          "valueReference": "checkbox",
          "value": "on",
          "description": "is checked"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Email input",
          "valueReference": "email",
          "value": "louis@example.com",
          "description": "type email"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Date and time",
          "valueReference": "datetime-local",
          "value": "2024-07-14T13:37",
          "description": "datetime description"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Radio buttons",
          "valueReference": "radio",
          "value": "Oui",
          "description": "radio description"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Type resource",
          "valueReference": "items",
          "value": 208,
          "description": "This is a link to a resource"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "A dropdown menu",
          "valueReference": "select",
          "value": "Choice 1",
          "description": "Single select"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Text input name",
          "valueReference": "text",
          "value": "some text",
          "description": "type text + all attributes"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Type experiment",
          "valueReference": "experiments",
          "value": 373,
          "description": "This is a link to an experiment"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Number with units",
          "valueReference": "number",
          "value": "",
          "description": "this one has units",
          "unitText": "mM"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Unchecked checkbox",
          "valueReference": "checkbox",
          "value": "",
          "description": "this one is not checked"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Multi dropdown menu",
          "valueReference": "select",
          "value": "Option 1",
          "description": "Allows multiple selection"
        }
      ]
    },
    {
      "@id": "#category-Antibody",
      "@type": "Thing",
      "name": "Antibody"
    },
    {
      "@id": "./Antibody - Anti-GAPDH - 49d9d070/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "name": "Anti-GAPDH",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=174",
      "genre": "resource",
      "about": {
        "@id": "#category-Antibody"
      },
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"text\", \"value\": \"Rabbit\"}, \"Isotype\": {\"type\": \"text\", \"value\": \"IgG\"}, \"Dilution for IF\": {\"type\": \"text\", \"value\": \"1:1000\"}, \"Dilution for WB\": {\"type\": \"text\", \"value\": \"1:5000\"}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"-20\u00b0C\", \"options\": [\"+4\u00b0C\", \"-20\u00b0C\", \"-80\u00b0C\"]}}}"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Host",
          "valueReference": "text",
          "value": "Rabbit"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Isotype",
          "valueReference": "text",
          "value": "IgG"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Dilution for IF",
          "valueReference": "text",
          "value": "1:1000"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Dilution for WB",
          "valueReference": "text",
          "value": "1:5000"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "-20\u00b0C"
        }
      ]
    },
    {
      "@id": "#category-Chemical compound",
      "@type": "Thing",
      "name": "Chemical compound"
    },
    {
      "@id": "./Chemical-compound - Potassium-chloride-KCl - 9ca2ca08/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "name": "Potassium chloride - KCl",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=164",
      "genre": "resource",
      "about": {
        "@id": "#category-Chemical compound"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-Yeast",
      "@type": "Thing",
      "name": "Yeast"
    },
    {
      "@id": "./Yeast - JK9-3d - 42b153ea/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "name": "JK9-3d",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=171",
      "genre": "resource",
      "about": {
        "@id": "#category-Yeast"
      },
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Genotype\": {\"type\": \"text\", \"value\": \"MATa his3\u0394200 leu2\u03941 trp1\u039463 ura3\u039452\"}, \"Plasmids\": {\"type\": \"text\", \"value\": \"pRS416\"}, \"Temperature\": {\"type\": \"text\", \"value\": \"30\u00b0C\"}}}"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Genotype",
          "valueReference": "text",
          "value": "MATa his3\u0394200 leu2\u03941 trp1\u039463 ura3\u039452"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Plasmids",
          "valueReference": "text",
          "value": "pRS416"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Temperature",
          "valueReference": "text",
          "value": "30\u00b0C"
        }
      ]
    },
    {
      "@id": "#category-Production",
      "@type": "Thing",
      "name": "Production"
    },
    {
      "@id": "./Production - With-links-to-resources-and-experiments - c1fefd66/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:25+02:00",
      "dateModified": "2024-06-15T15:53:24+02:00",
      "name": "With links to resources and experiments",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=297",
      "genre": "experiment",
      "about": {
        "@id": "#category-Production"
      }
    },
    {
      "@id": "./simple-experiment-nothing-extra - af674ffe/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-15T15:11:18+02:00",
      "dateModified": "2024-06-15T15:48:53+02:00",
      "name": "simple experiment : nothing extra",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=302",
      "genre": "experiment"
    },
    {
      "@id": "#category-R&D",
      "@type": "Thing",
      "name": "R&D"
    },
    {
      "@id": "./RD - Rerum-nisi-eligendi-libero - 2402131b/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:25+02:00",
      "dateModified": "2024-06-10T22:48:25+02:00",
      "name": "Rerum nisi eligendi libero.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=296",
      "genre": "experiment",
      "about": {
        "@id": "#category-R&D"
      }
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 046cb409/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:24+02:00",
      "dateModified": "2024-06-10T22:48:24+02:00",
      "name": "Test the grouped extra fields",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=292",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"elabftw\": {\"display_main_text\": false, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group with id 1, first position\"}, {\"id\": 2, \"name\": \"Group with id 2, second position\"}, {\"id\": 3, \"name\": \"Group with id 3, third position\"}]}, \"extra_fields\": {\"Has group_id 3 as number\": {\"type\": \"text\", \"value\": \"\", \"group_id\": 3}, \"Has group_id 3 as string\": {\"type\": \"text\", \"value\": \"\", \"group_id\": \"3\"}, \"Has no group_id property\": {\"type\": \"text\", \"value\": \"\"}, \"Group_id 1 and position 1\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 1, \"position\": 1, \"description\": \"This is a checkbox custom input\"}, \"Group_id 2 and position 1\": {\"type\": \"url\", \"value\": \"\", \"group_id\": 2, \"position\": 1}, \"Group_id 2 and position 2\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\", \"group_id\": 2, \"position\": 2}, \"Group_id 2 and position 3\": {\"type\": \"url\", \"value\": \"\", \"group_id\": 2, \"position\": 3}, \"Another one without group_id property\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"this element has no group property defined\"}, \"Has group_id that is not in elabftw.groups\": {\"type\": \"text\", \"value\": \"I am lost!\", \"group_id\": \"19\"}}}"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Has group_id 3 as number",
          "valueReference": "text",
          "value": ""
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Has group_id 3 as string",
          "valueReference": "text",
          "value": ""
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Has no group_id property",
          "valueReference": "text",
          "value": ""
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Group_id 1 and position 1",
          "valueReference": "checkbox",
          "value": "",
          "description": "This is a checkbox custom input"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Group_id 2 and position 1",
          "valueReference": "url",
          "value": ""
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Group_id 2 and position 2",
          "valueReference": "url",
          "value": "https://datalake.example.com/experiments/3921"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Group_id 2 and position 3",
          "valueReference": "url",
          "value": ""
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Another one without group_id property",
          "valueReference": "select",
          "value": "Some choice",
          "description": "this element has no group property defined"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Has group_id that is not in elabftw.groups",
          "valueReference": "text",
          "value": "I am lost!"
        }
      ]
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - An-example-experiment - 19797cbf/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:24+02:00",
      "dateModified": "2024-06-10T22:48:24+02:00",
      "name": "An example experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=291",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - eafcde50/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:24+02:00",
      "dateModified": "2024-06-10T22:48:24+02:00",
      "name": "Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=290",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - f15f3515/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:24+02:00",
      "dateModified": "2024-06-10T22:48:24+02:00",
      "name": "Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=288",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - 79dc39c5/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-10T22:48:24+02:00",
      "dateModified": "2024-06-10T22:48:24+02:00",
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=287",
      "genre": "experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Project-CASIMIR - Markdown-experiment - ce78d5e4/"
        },
        {
          "@id": "./Production - With-links-to-resources-and-experiments - c1fefd66/"
        },
        {
          "@id": "./Project-CASIMIR - Experiment-with-an-image-in-the-text - 2c00e9a2/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 734dad66/"
        },
        {
          "@id": "./Antibody - Anti-GAPDH - 49d9d070/"
        },
        {
          "@id": "./Chemical-compound - Potassium-chloride-KCl - 9ca2ca08/"
        },
        {
          "@id": "./Yeast - JK9-3d - 42b153ea/"
        },
        {
          "@id": "./simple-experiment-nothing-extra - af674ffe/"
        },
        {
          "@id": "./RD - Rerum-nisi-eligendi-libero - 2402131b/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 046cb409/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - An-example-experiment - 19797cbf/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - eafcde50/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - f15f3515/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - 79dc39c5/"
        }
      ]
    },
    {
      "@id": "person://797dd58d4ee3e5e9c6cc81c28ee2cd60d408a48bded24131581f98fa7de0b141?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Kian",
      "familyName": "Daugherty",
      "email": "titi@yopmail.com"
    },
    {
      "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Toto",
      "familyName": "Le sysadmin",
      "email": "toto@yopmail.com"
    }
  ]
}
```
