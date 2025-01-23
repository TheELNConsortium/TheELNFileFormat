# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

You can generate .eln files from the demo: https://demo.elabftw.net. Select a few entries and export as .eln from the top menu. Or go to the Import section and do a full export.

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
      "dateCreated": "2025-01-23T11:35:52+01:00",
      "sdPublisher": {
        "@id": "#publisher"
      },
      "version": "1.0"
    },
    {
      "@id": "https://www.deltablot.com",
      "@type": "Organization",
      "areaServed": "Laniakea Supercluster",
      "name": "Deltablot",
      "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
      "slogan": "Open Source software for research labs.",
      "url": "https://www.deltablot.com"
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
        "@id": "https://www.deltablot.com"
      }
    },
    {
      "@id": "#ro-crate_created",
      "@type": "CreateAction",
      "object": {
        "@id": "./"
      },
      "name": "RO-Crate created",
      "endTime": "2025-01-23T11:35:52+01:00",
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
      "version": "5.1.14",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "comment://e4d175c5775273ca8d27ec582e6dbb703574ea49b67a91e7ee7ff0e3106078ee?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-01-08T11:02:22+01:00",
      "text": "Great results on the DNA extraction. The yield and purity look good. For the wash steps, consider extending the final centrifugation to 3 minutes to ensure no residual buffer. Nice work!",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.mp4",
      "@type": "File",
      "name": "example.mp4",
      "alternateName": "f0/f0420ee2ce026ff2462882e242f953d9fc4a97c0ab3d27f1e9fbbda75d14fafffb95620e3a7f22be93e386077841f9f66e5edc008da793db04c968b979644962.mp4",
      "contentSize": 184144,
      "sha256": "2a729ba8ddca2e2270effed052ceed5a1167a8d1c4ee856ace3d55635fca243d"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.cdx",
      "@type": "File",
      "name": "example.cdx",
      "alternateName": "2b/2b8ac9970db9b548f05da4c527366a97210e44874f1b718fd1e0e1dde4c90d829a2fe0fc7cf056b62177afd5d1b7e6bdb0e2eedaf64ab96647ca692e9c12c0f9.cdx",
      "contentSize": 1514,
      "sha256": "5efbea7d56c052e2e1fc418ff24ef8b445cd543d07a4c892994647e90d5258dc"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.gbk",
      "@type": "File",
      "name": "example.gbk",
      "alternateName": "6d/6dee66215ddb246e92c8db8d05fbc032b371da0b8d8ee349404e5585abb1af25c75ef9a0e85f8cd237cb490b943b1a46f61d190eddd68ecd876358ce5249abe5.gbk",
      "contentSize": 7472,
      "sha256": "a092b86343c74697ac70542d5a75843230b69555e01e5460bac8cddab1dbecea"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.jpg",
      "@type": "File",
      "name": "example.jpg",
      "alternateName": "92/92fa4ee261d1e8ac9d3675f35bde0f05370151bc8dbedb1d6d26eda8f3fa4710327c700d433660ce2bf0bea1a06885ec3b8ed6c963e09f0ba87b7cfe972de4da.jpg",
      "contentSize": 85530,
      "sha256": "b73626c9a9ed8561ed6126df2493bc0d84fb8feedc9fe34aed94f7d2d5f4f60f"
    },
    {
      "@id": "#category-Cell biology",
      "@type": "Thing",
      "name": "Cell biology",
      "color": "610511"
    },
    {
      "@id": "./Cell-biology - Laborum-est-accusantium-ullam-quis-et-sed - 7b6f582f/",
      "@type": "Dataset",
      "author": {
        "@id": "person://16fe8e900225c4a6e17c165b3de0f032c8d55d87ec81e2d36aed201794650e76?hash_algo=sha256"
      },
      "dateCreated": "2025-01-08T11:01:28+01:00",
      "dateModified": "2025-01-08T11:01:28+01:00",
      "temporal": "2023-02-19T00:00:00+01:00",
      "name": "Laborum est accusantium ullam quis et sed.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php.php?mode=view&id=202",
      "genre": "experiment",
      "creativeWorkStatus": "Running",
      "identifier": "20250108-7b6f582fda9dd9ed0e5d993eae795ea1398bf0c3",
      "keywords": "gene expression",
      "text": "Alice to herself. 'Shy, they seem to encourage the witness at all: he kept shifting from one end of the Lobster Quadrille, that she looked up, but it was not going to shrink any further: she felt unhappy. 'It was a long hookah, and taking not the right words,' said poor Alice, who was sitting between them, fast asleep, and the Panther were sharing a pie--' [later editions continued as follows The Panther took pie-crust, and gravy, and meat, While the Panther received knife and fork with a table in the sea, though you mayn't believe it--' 'I never heard before, 'Sure then I'm here! Digging for apples, indeed!' said the Mock Turtle, capering wildly about. 'Change lobsters again!' yelled the Gryphon added 'Come, let's hear some of them hit her in a shrill, passionate voice. 'Would YOU like cats if you please! \"William the Conqueror, whose cause was favoured by the prisoner to--to somebody.' 'It must have imitated somebody else's hand,' said the March Hare. 'He denies it,' said Alice.",
      "about": {
        "@id": "#category-Cell biology"
      }
    },
    {
      "@id": "#category-R&D",
      "@type": "Thing",
      "name": "R&D",
      "color": "1d11c0"
    },
    {
      "@id": "./RD - Ut-aut-sint-aliquam-nobis-ipsa-adipisci - c6a5262b/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-01-08T11:00:35+01:00",
      "dateModified": "2025-01-08T11:00:36+01:00",
      "temporal": "2024-11-08T00:00:00+01:00",
      "name": "Ut aut sint aliquam nobis ipsa adipisci.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php.php?mode=view&id=32",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250108-c6a5262b41773b2f0eea10ca2bad971f6cd500d9",
      "keywords": "protein analysis,Dark Arts,biochemistry,cell culture techniques,Western Blot",
      "text": "I do hope it'll make me smaller, I can guess that,' she added in a moment: she looked up and ran the faster, while more and more faintly came, carried on the shingle--will you come to the baby, it was very deep, or she fell past it. 'Well!' thought Alice 'without pictures or conversations?' So she was dozing off, and had come back in their mouths--and they're all over with William the Conqueror.' (For, with all their simple sorrows, and find a number of changes she had sat down a large plate came skimming out, straight at the Cat's head with great curiosity, and this was of very little way forwards each time and a long argument with the end of the shepherd boy--and the sneeze of the house, and wondering whether she could not possibly reach it: she could do to come yet, please your Majesty?' he asked. 'Begin at the jury-box, and saw that, in her lessons in here? Why, there's hardly room to open it; but, as the whole party at once took up the little thing was to twist it up into a.",
      "about": {
        "@id": "#category-R&D"
      }
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL",
      "color": "cc006a"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-01-08T11:02:22+01:00",
      "dateModified": "2025-01-23T11:06:39+01:00",
      "temporal": "2025-01-03T00:00:00+01:00",
      "name": "Gold master experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php.php?mode=view&id=310",
      "genre": "experiment",
      "alternateName": 4,
      "comment": [
        {
          "@id": "comment://e4d175c5775273ca8d27ec582e6dbb703574ea49b67a91e7ee7ff0e3106078ee?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.mp4"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.cdx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.gbk"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/example.jpg"
        }
      ],
      "identifier": "20250108-2cb6677ab9007b39c4b8c16b0ff337750d2c8ec2",
      "keywords": "generated from yml,test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1",
      "mentions": [
        {
          "@id": "./Cell-biology - Laborum-est-accusantium-ullam-quis-et-sed - 7b6f582f/"
        },
        {
          "@id": "./RD - Ut-aut-sint-aliquam-nobis-ipsa-adipisci - c6a5262b/"
        }
      ],
      "text": "<h1>Level 1 title</h1>\n<h2>Level 2 title</h2>\n<p>The <strong>goal</strong> of this <em>experiment</em> is to have <span style=\"text-decoration:underline;\">all</span> <span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\">attributes</span>:</p>\n<ul>\n<li>all extra fields types</li>\n<li>links to experiments and items</li>\n<li>links from experiments and items</li>\n<li>status, category, tags and uploaded files</li>\n</ul>\n<h3>Here is a table</h3>\n<table style=\"border-collapse:collapse;width:100%;\" border=\"1\">\n\n<tr>\n<td>Something</td>\n<td>in H<sub>2</sub></td>\n<td>the</td>\n</tr>\n<tr>\n<td>table</td>\n<td style=\"background-color:rgb(185,106,217);border:2px dashed rgb(224,62,45);\">31<sup>321</sup></td>\n<td>there</td>\n</tr>\n\n</table>\n<p>an emoji: \ud83e\udd2a</p>\n<p>\u221e \u2211</p>\n<h4>An image</h4>\n<p>\u00a0</p>\n<p><a href=\"https://www.elabftw.net/\" target=\"_blank\" rel=\"noreferrer noopener\">A link to elabftw.net</a>.</p>\n<p>\u00a0</p>",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group 1\"}, {\"id\": 2, \"name\": \"Group 2\"}, {\"id\": 3, \"name\": \"Last group\"}]}, \"extra_fields\": {\"Number\": {\"type\": \"number\", \"unit\": \"\", \"units\": [], \"value\": \"\", \"group_id\": 2, \"description\": \"no units\"}, \"Type URL\": {\"type\": \"url\", \"value\": \"https://www.elabftw.net\", \"group_id\": 2, \"readonly\": true, \"description\": \"a link (readonly)\"}, \"Just time\": {\"type\": \"time\", \"value\": \"17:00\", \"group_id\": 2, \"description\": \"tea time\"}, \"Some date\": {\"type\": \"date\", \"value\": \"2024-07-14\", \"group_id\": 2, \"description\": \"is a date\"}, \"Type user\": {\"type\": \"users\", \"value\": 1, \"group_id\": 3, \"description\": \"this is a link to a user\"}, \"A checkbox\": {\"type\": \"checkbox\", \"value\": \"on\", \"group_id\": 2, \"description\": \"is checked\"}, \"Email input\": {\"type\": \"email\", \"value\": \"louis@example.com\", \"group_id\": 2, \"description\": \"type email\"}, \"Date and time\": {\"type\": \"datetime-local\", \"value\": \"2024-07-14T13:37\", \"group_id\": 2, \"description\": \"datetime description\"}, \"Radio buttons\": {\"type\": \"radio\", \"value\": \"Oui\", \"options\": [\"Oui\", \"Non\", \"Peut-\u00eatre\"], \"group_id\": 1, \"description\": \"radio description\"}, \"Type resource\": {\"type\": \"items\", \"value\": 208, \"group_id\": 3, \"description\": \"This is a link to a resource\"}, \"A dropdown menu\": {\"type\": \"select\", \"value\": \"Choice 1\", \"options\": [\"Choice 1\", \"Choice 2\", \"Choice 3\"], \"group_id\": 1, \"description\": \"Single select\"}, \"Text input name\": {\"type\": \"text\", \"value\": \"some text\", \"group_id\": 1, \"readonly\": true, \"required\": true, \"description\": \"type text + all attributes\", \"blank_value_on_duplicate\": true}, \"Type experiment\": {\"type\": \"experiments\", \"value\": 202, \"group_id\": 3, \"description\": \"This is a link to an experiment\"}, \"Number with units\": {\"type\": \"number\", \"unit\": \"mM\", \"units\": [\"mM\", \"\u03bcM\", \"nM\"], \"value\": \"\", \"group_id\": 2, \"description\": \"this one has units\"}, \"Unchecked checkbox\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 2, \"description\": \"this one is not checked\"}, \"Multi dropdown menu\": {\"type\": \"select\", \"value\": \"Option 1\", \"options\": [\"Option 1\", \"Option 2\", \"Option 3\"], \"group_id\": 1, \"description\": \"Allows multiple selection\", \"allow_multi_values\": true}}}"
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
          "value": 202,
          "description": "This is a link to an experiment"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Multi dropdown menu",
          "valueReference": "select",
          "value": "Option 1",
          "description": "Allows multiple selection"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 4,
        "reviewCount": 1
      }
    },
    {
      "@id": "./",
      "identifier": "89b86e75-93d6-4a9e-9466-d3d04facf7c1",
      "@type": "Dataset",
      "datePublished": "2025-01-23T11:35:52+01:00",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 2cb6677a/"
        },
        {
          "@id": "./Cell-biology - Laborum-est-accusantium-ullam-quis-et-sed - 7b6f582f/"
        },
        {
          "@id": "./RD - Ut-aut-sint-aliquam-nobis-ipsa-adipisci - c6a5262b/"
        }
      ],
      "name": "eLabFTW export",
      "description": "This is a .eln export from eLabFTW",
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
      }
    },
    {
      "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Toto",
      "familyName": "Le sysadmin",
      "email": "toto@yopmail.com"
    },
    {
      "@id": "person://16fe8e900225c4a6e17c165b3de0f032c8d55d87ec81e2d36aed201794650e76?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Wayne",
      "familyName": "Padberg",
      "email": "demo@elabftw.net"
    }
  ]
}
```
