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
      "dateCreated": "2025-01-25T20:59:40+01:00",
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
      "endTime": "2025-01-25T20:59:40+01:00",
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
      "@id": "comment://f89d589a1b9c51738c7ec76635b18c2505751d6102aa2ac49f9c847263bf0f57?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-01-11T16:00:09+01:00",
      "text": "Great results on the DNA extraction. The yield and purity look good. For the wash steps, consider extending the final centrifugation to 3 minutes to ensure no residual buffer. Nice work!",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "#category-Demo",
      "@type": "Thing",
      "name": "Demo",
      "color": "eab414"
    },
    {
      "@id": "./Demo - Quidem-laboriosam-deserunt-voluptatum-molestiae-qui - 9ec59773/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-01-11T15:57:59+01:00",
      "dateModified": "2025-01-11T15:57:59+01:00",
      "temporal": "2022-07-05T00:00:00+02:00",
      "name": "Quidem laboriosam deserunt voluptatum molestiae qui.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php.php?mode=view&id=32",
      "genre": "experiment",
      "creativeWorkStatus": "Running",
      "identifier": "20250111-9ec597733e27dfc74e27004a563522c9b2c75016",
      "keywords": "statistical analysis,lab supplies,gene expression,COVID-24,lab safety",
      "text": "And she's such a subject! Our family always HATED cats: nasty, low, vulgar things! Don't let me help to undo it!' 'I shall do nothing of the court, she said these words her foot as far down the little crocodile Improve his shining tail, And pour the waters of the moment he was speaking, and this he handed over to the Classics master, though. He was looking down with one elbow against the roof off.' After a time she had put on his knee, and looking anxiously about as much as she went on talking: 'Dear, dear! How queer everything is queer to-day.' Just then her head made her next remark. 'Then the eleventh day must have been changed in the distance, and she looked down into a pig, my dear,' said Alice, in a very truthful child; 'but little girls in my time, but never ONE with such a wretched height to rest herself, and shouted out, 'You'd better not talk!' said Five. 'I heard every word you fellows were saying.' 'Tell us a story!' said the sage, as he came, 'Oh! the Duchess, 'chop off.",
      "about": {
        "@id": "#category-Demo"
      }
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL",
      "color": "54a4c5"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 739ba7c9/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-01-11T16:00:09+01:00",
      "dateModified": "2025-01-11T16:00:09+01:00",
      "temporal": "2025-01-03T00:00:00+01:00",
      "name": "Gold master experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php.php?mode=view&id=310",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://f89d589a1b9c51738c7ec76635b18c2505751d6102aa2ac49f9c847263bf0f57?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "identifier": "20250111-739ba7c99c77e76b6b8d48b86c60e4eaffda4bb6",
      "keywords": "generated from yml,test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1",
      "mentions": [
        {
          "@id": "./Demo - Quidem-laboriosam-deserunt-voluptatum-molestiae-qui - 9ec59773/"
        }
      ],
      "text": "<h1>Level 1 title</h1>\n<h2>Level 2 title</h2>\n<p>The <strong>goal</strong> of this <em>experiment</em> is to have <span style=\"text-decoration:underline;\">all</span> <span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\">attributes</span>:</p>\n<ul>\n<li>all extra fields types</li>\n<li>links to experiments and items</li>\n<li>links from experiments and items</li>\n<li>status, category, tags and uploaded files</li>\n</ul>\n<h3>Here is a table</h3>\n<table style=\"border-collapse:collapse;width:100%;\" border=\"1\">\n\n<tr>\n<td>Something</td>\n<td>in H<sub>2</sub></td>\n<td>the</td>\n</tr>\n<tr>\n<td>table</td>\n<td style=\"background-color:rgb(185,106,217);border:2px dashed rgb(224,62,45);\">31<sup>321</sup></td>\n<td>there</td>\n</tr>\n\n</table>\n<p>an emoji: \ud83e\udd2a</p>\n<p>\u221e \u2211</p>\n<h4>An image</h4>\n<p><img src=\"app/download.php?name=example.jpg&amp;f=78/7834c99a3af687a043d7e9c5bec5e4877469748dca1e898892962ab769be562e069204c19f3bf4663dd2f036cd2a9673b8db53702405ad5298a6e1fd78d6d7da.jpg&amp;storage=1\" width=\"173\" height=\"260\" alt=\"7834c99a3af687a043d7e9c5bec5e4877469748dca1e898892962ab769be562e069204c19f3bf4663dd2f036cd2a9673b8db53702405ad5298a6e1fd78d6d7da.jpg&amp;storage=1\"></p>\n<p><a href=\"https://www.elabftw.net/\" target=\"_blank\" rel=\"noreferrer noopener\">A link to elabftw.net</a>.</p>\n<p>\u00a0</p>\n",
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
          "@id": "pv://1d050336-5f3e-4a6d-9d2e-93f438b174b0",
          "propertyID": "Number",
          "valueReference": "number",
          "value": "",
          "description": "no units"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://3caa995f-86c3-4a0a-ac00-8d76fb1aef63",
          "propertyID": "Type URL",
          "valueReference": "url",
          "value": "https://www.elabftw.net",
          "description": "a link (readonly)"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://837914e5-9053-4c7d-b964-94e4fe7e39a9",
          "propertyID": "Just time",
          "valueReference": "time",
          "value": "17:00",
          "description": "tea time"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://9db67b42-7a10-42e8-abac-276f0f06a49e",
          "propertyID": "Some date",
          "valueReference": "date",
          "value": "2024-07-14",
          "description": "is a date"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://4cd8f56b-dce8-4a9c-b08f-f10574d65966",
          "propertyID": "Type user",
          "valueReference": "users",
          "value": 1,
          "description": "this is a link to a user"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://0ec8ad17-3ea7-4315-9609-2d6f4f34c234",
          "propertyID": "A checkbox",
          "valueReference": "checkbox",
          "value": "on",
          "description": "is checked"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://1000a24f-5e1a-4417-a80d-006aefdb184b",
          "propertyID": "Email input",
          "valueReference": "email",
          "value": "louis@example.com",
          "description": "type email"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://6122898f-f361-48e5-9ec1-9a160c60237d",
          "propertyID": "Date and time",
          "valueReference": "datetime-local",
          "value": "2024-07-14T13:37",
          "description": "datetime description"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://a34a086f-1b4e-4d40-9f98-550b18eb82e4",
          "propertyID": "Radio buttons",
          "valueReference": "radio",
          "value": "Oui",
          "description": "radio description"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://1c245f73-7e95-4ee9-bc4c-799548eb3f64",
          "propertyID": "Type resource",
          "valueReference": "items",
          "value": 208,
          "description": "This is a link to a resource"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://dcda3edb-8ad1-4004-9df9-e918f5621463",
          "propertyID": "A dropdown menu",
          "valueReference": "select",
          "value": "Choice 1",
          "description": "Single select"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://44f7d8c3-0ea9-4821-8c4f-4599b9871845",
          "propertyID": "Text input name",
          "valueReference": "text",
          "value": "some text",
          "description": "type text + all attributes"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://cb66bd05-cf5f-4275-b51c-cb521e15f787",
          "propertyID": "Type experiment",
          "valueReference": "experiments",
          "value": 373,
          "description": "This is a link to an experiment"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://bf6b3312-2fb1-4586-b3c6-3cc63c7cf4ee",
          "propertyID": "Number with units",
          "valueReference": "number",
          "value": "",
          "description": "this one has units",
          "unitText": "mM"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://13d55443-70d1-4e64-8f3c-947c81234827",
          "propertyID": "Unchecked checkbox",
          "valueReference": "checkbox",
          "value": "",
          "description": "this one is not checked"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://24a46ae0-6d03-44d2-a1c4-cf49f0ff152a",
          "propertyID": "Multi dropdown menu",
          "valueReference": "select",
          "value": "Option 1",
          "description": "Allows multiple selection"
        }
      ]
    },
    {
      "@id": "./",
      "identifier": "afae56c6-71dd-4b1a-9853-dd705ec4b262",
      "@type": "Dataset",
      "datePublished": "2025-01-25T20:59:40+01:00",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - 739ba7c9/"
        },
        {
          "@id": "./Demo - Quidem-laboriosam-deserunt-voluptatum-molestiae-qui - 9ec59773/"
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
    }
  ]
}
```
