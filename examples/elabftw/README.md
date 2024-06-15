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
      "dateCreated": "2024-06-15T16:12:15+02:00",
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
      "endTime": "2024-06-15T16:12:15+02:00",
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
      "creativeWorkStatus": "Project CASIMIR",
      "hasPart": [
        {
          "@id": "./Project-CASIMIR - Markdown-experiment - ce78d5e4/example.pdf"
        },
        {
          "@id": "./Project-CASIMIR - Markdown-experiment - ce78d5e4/example.png"
        }
      ],
      "identifier": "20240610-ce78d5e48ba7620f0e13fa2a6d4fa9bff6700557",
      "keywords": "molecular cloning,scientific literature,COVID-24,cell culture,markdown,eln-export",
      "text": "# This content is in markdown\n\n[a link](https://www.elabftw.net)\n\nAnd an embedded image:\n\n![image](app/download.php?name=example.png&amp;f=e0/e021d9f1278e5e289e6c75a70e78dd717b5ae58b17282c65b89daa2c173298d195a8ff86a9f0f3eb36198b3f2712d315f595de49d3d4cda43cf0c8ff3f44356e.png&amp;storage=1)\n",
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
      "alternateName": 312,
      "comment": [
        {
          "@id": "comment://2024-06-15T15%3A49%3A49%2B02%3A00"
        }
      ],
      "creativeWorkStatus": "Project CASIMIR",
      "hasPart": [
        {
          "@id": "./Project-CASIMIR - Experiment-with-an-image-in-the-text - 2c00e9a2/haproxy3-stats-reload.png"
        }
      ],
      "identifier": "20240614-2c00e9a21156c8b50b5dc251e2eca7509b0ff78a",
      "keywords": "with-image,with-customid,eln-export",
      "text": "<p>main <span style=\"text-decoration:underline;\">experiment</span> <strong>text</strong></p>\n<h1><span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\"><strong>which also contains an image!</strong></span></h1>\n<p><span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\"><strong><img src=\"app/download.php?name=haproxy3-stats-reload.png&amp;f=cf/cfc36b71003a82ccb366a7a3694dba3972eab46002f61384f3c5437885f6944ec15189f8a5596b1cffd07c2a565c7beb9094cd1b8e0ac371b937777defd87f6b.png&amp;storage=1\" alt=\"cfc36b71003a82ccb366a7a3694dba3972eab46002f61384f3c5437885f6944ec15189f8a5596b1cffd07c2a565c7beb9094cd1b8e0ac371b937777defd87f6b.png&amp;storage=1\"></strong></span></p>\n<p><span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\"><strong>After import, make sure the image appears above!</strong></span></p>",
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
      "creativeWorkStatus": "Project CRYPTO-COOL",
      "identifier": "20240610-734dad661f567f56d0c672fea0e047728f292f65",
      "keywords": "test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1,eln-export",
      "text": "<p>id:259</p><p>date:2025-01-03</p><p>body:Level 1 title\nLevel 2 title\nThe goal of this experiment is to have all attributes:\n\nall extra fields types\nlinks to experiments and items\nlinks from experiments and items\nstatus, category, tags and uploaded files\n\nHere is a table\n\n\n\nSomething\nin H2\nthe\n\n\ntable\n31321\nthere\n\n\n\nan emoji: \ud83e\udd2a\n\u221e \u2211\nAn image\n\nA link to elabftw.net.\n\u00a0\n</p><p>category:2</p><p>category_title:Project CRYPTO-COOL</p><p>category_color:08b329</p><p>status:2</p><p>status_title:Success</p><p>status_color:54AA08</p><p>custom_id:</p><p>elabid:20240610-af6df8588593f3a3189b8564a9105d4246c0011a</p><p>rating:0</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=259\">https://elab.local:3148/experiments.php?mode=view&amp;id=259</a></p>",
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
      "creativeWorkStatus": "Antibody",
      "identifier": "20240610-49d9d070a04a2afb390dfc57d25b98668d6082bb",
      "text": "<p>Anti-GAPDH is a polyclonal rabbit antibody used to detect the glyceraldehyde-3-phosphate dehydrogenase protein, a well-known housekeeping gene that is ubiquitously expressed in cells. This antibody is commonly used as a loading control in Western blotting and has been shown to work in a wide range of species including human, mouse, rat, and others. The antibody was generated by immunizing rabbits with purified GAPDH protein.</p>",
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
      "creativeWorkStatus": "Chemical compound",
      "identifier": "20240610-9ca2ca089b4854074337d85e30f3799b55a03395",
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
      "creativeWorkStatus": "Yeast",
      "identifier": "20240610-42b153ea593f10709b9677378b4d4b83fad88703",
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
      "creativeWorkStatus": "Production",
      "identifier": "20240610-c1fefd66d32720d791238034a679c531112738f5",
      "keywords": "hardness testing,molecular biology,cell culture,cell culture techniques,eln-export",
      "mentions": [
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
        }
      ],
      "text": "<p>main content</p>\n<p>\u00a0</p>",
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
      "genre": "experiment",
      "identifier": "20240615-af674ffe54cc9b513fdc0a7de7b4aff21cf91f8e",
      "keywords": "eln-export"
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
      "creativeWorkStatus": "R&D",
      "identifier": "20240610-2402131ba809c5cd2c23955eab6ff021246a32c9",
      "keywords": "molecular cloning,lab techniques,spectroscopy,experimental design,eln-export",
      "text": "<p>id:200</p><p>date:2021-12-04</p><p>body:She felt that this could not be denied, so she went on, looking anxiously about her. &#039;Oh, do let me help to undo it!&#039; &#039;I shall sit here,&#039; he said, turning to Alice, and she tried hard to whistle to it; but she could not remember ever having heard of uglifying!&#039; it exclaimed. &#039;You know what they&#039;re about!&#039; &#039;Read them,&#039; said the March Hare moved into the garden, called out &#039;The race is over!&#039; and they can&#039;t prove I did: there&#039;s no use in waiting by the time at the Footman&#039;s head: it just missed her. Alice caught the flamingo and brought it back, the fight was over, and both creatures hid their faces in their mouths. So they got settled down in an angry voice--the Rabbit&#039;s--&#039;Pat! Pat! Where are you?&#039; And then a great thistle, to keep herself from being broken. She hastily put down her flamingo, and began to repeat it, when a sharp hiss made her draw back in their mouths--and they&#039;re all over crumbs.&#039; &#039;You&#039;re wrong about the temper of your nose-- What made you so awfully clever?&#039; &#039;I have.</p><p>category:8</p><p>category_title:R&amp;D</p><p>category_color:c2136e</p><p>status:3</p><p>status_title:Need to be redone</p><p>status_color:C0C0C0</p><p>custom_id:</p><p>elabid:20240610-8709ac7daee351631ba3b1f01750352b4d2a6858</p><p>rating:0</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=200\">https://elab.local:3148/experiments.php?mode=view&amp;id=200</a></p>",
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
      "creativeWorkStatus": "Project CRYPTO-COOL",
      "identifier": "20240610-046cb40969bac1d6132107148d0e44762b4b18e3",
      "keywords": "dev,extra fields,eln-export",
      "text": "<p>id:256</p><p>date:2024-12-31</p><p>body:</p><p>category:2</p><p>category_title:Project CRYPTO-COOL</p><p>category_color:08b329</p><p>status:2</p><p>status_title:Success</p><p>status_color:54AA08</p><p>custom_id:</p><p>elabid:20240610-854e72d32638e17a9258c70a58b1902262baa47c</p><p>rating:0</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=256\">https://elab.local:3148/experiments.php?mode=view&amp;id=256</a></p>",
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
      "creativeWorkStatus": "Project CRYPTO-COOL",
      "identifier": "20240610-19797cbfb645d02602df2ade859314d73de615bf",
      "keywords": "example,demo,eln-export",
      "text": "<p>id:257</p><p>date:2025-01-01</p><p>body:This is the content of the experiment</p><p>category:2</p><p>category_title:Project CRYPTO-COOL</p><p>category_color:08b329</p><p>status:2</p><p>status_title:Success</p><p>status_color:54AA08</p><p>custom_id:</p><p>elabid:20240610-fc07130d293361d384b2425c5ec8512e454238ee</p><p>rating:0</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=257\">https://elab.local:3148/experiments.php?mode=view&amp;id=257</a></p>",
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
      "creativeWorkStatus": "Project CRYPTO-COOL",
      "identifier": "20240610-eafcde5026fcef10aba8fbfd7ff992a974b34071",
      "keywords": "transfection,biocell,RPE-1,eln-export",
      "text": "<p>id:258</p><p>date:2025-01-02</p><p>body:GoalTransfecting the plasmid p103\u039412-22 into the RPE-1 Actin-RFP cells and look at the death rate.</p><p>category:2</p><p>category_title:Project CRYPTO-COOL</p><p>category_color:08b329</p><p>status:2</p><p>status_title:Success</p><p>status_color:54AA08</p><p>custom_id:</p><p>elabid:20240610-c6bff418669b56a40f914c36e4bc871be7a210da</p><p>rating:0</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=258\">https://elab.local:3148/experiments.php?mode=view&amp;id=258</a></p>",
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
      "creativeWorkStatus": "Project CRYPTO-COOL",
      "identifier": "20240610-f15f3515fc6265e2d0152d1716d2b26f46802900",
      "keywords": "synthesis,antimicrobial,chemistry,eln-export",
      "text": "<p>id:260</p><p>date:2025-01-02</p><p>body:Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties\n\nThe emergence of drug-resistant bacterial strains has become a major public health concern, highlighting the need for the development of new antimicrobial agents. In this study, we aimed to synthesize a novel organic compound with potential antimicrobial activity.\n\nExperimental Design\n\nThe compound was synthesized via a multi-step reaction scheme. The starting material, benzaldehyde, was reacted with aniline in the presence of an acid catalyst to form the intermediate product, N-phenylbenzamide. The intermediate product was then reacted with thionyl chloride to form the corresponding acid chloride. The acid chloride was then reacted with aminoguanidine in the presence of a base catalyst to form the final product, which was purified by recrystallization.\n\nCharacterization\n\nThe synthesized compound was characterized using various spectroscopic techniques. The melting point of the compound was determined using a melting point apparatus and compared to the literature value. The IR spectrum of the compound was obtained using a Fourier transform infrared spectrometer and compared to the expected spectrum. The NMR spectrum of the compound was obtained using a nuclear magnetic resonance spectrometer and analyzed to confirm the structure of the compound.\n\nAntimicrobial Activity\n\nThe antimicrobial activity of the synthesized compound was evaluated against several bacterial strains using the disk diffusion method. The results showed that the compound exhibited significant antimicrobial activity against both Gram-positive and Gram-negative bacteria, suggesting its potential as a new antimicrobial agent.\n\n</p><p>category:2</p><p>category_title:Project CRYPTO-COOL</p><p>category_color:08b329</p><p>status:4</p><p>status_title:Fail</p><p>status_color:C24F3D</p><p>custom_id:</p><p>elabid:20240610-e58fcae31c0ac38f1c797a9f711e337cc24bc23d</p><p>rating:1</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=260\">https://elab.local:3148/experiments.php?mode=view&amp;id=260</a></p>",
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
      "creativeWorkStatus": "Project CRYPTO-COOL",
      "identifier": "20240610-79dc39c59179729f8908339948bd40ebca649548",
      "keywords": "CJK,\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8,eln-export",
      "text": "<p>id:261</p><p>date:2025-01-02</p><p>body:\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002\n\n\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002\n\n\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002\n\n\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\n\n\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002\n</p><p>category:2</p><p>category_title:Project CRYPTO-COOL</p><p>category_color:08b329</p><p>status:2</p><p>status_title:Success</p><p>status_color:54AA08</p><p>custom_id:</p><p>elabid:20240610-2937c25256dcd67f55f4ea2c654e10ef02ac8f9e</p><p>rating:0</p><p>url:<a href=\"https://elab.local:3148/experiments.php?mode=view&amp;id=261\">https://elab.local:3148/experiments.php?mode=view&amp;id=261</a></p>",
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
