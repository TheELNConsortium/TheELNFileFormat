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
      "dateCreated": "2024-06-18T23:49:12+02:00",
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
      "endTime": "2024-06-18T23:49:12+02:00",
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
      "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.pptx",
      "@type": "File",
      "name": "example.pptx",
      "alternateName": "67/6702398d3c3af6755a9bdd3c0f97a10d0e17691302528b81b9ec212e4078b3a39976b46feaab2f8bc525ba0c17610ad11d88b136a7ef32f94888e0e6f38e6d68.pptx",
      "contentSize": 57375,
      "sha256": "4fc01c51e094f4410a56f05f513be829425f12e7b33b5296115126a84aba74e7",
      "description": "a file comment"
    },
    {
      "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.ppt",
      "@type": "File",
      "name": "example.ppt",
      "alternateName": "ef/ef5175e9c8520ca1d44fafb54822df5b0fd5a9a2a18adaade24261f1012b58ff887ef379d4dc06b2954178ae8bb535dc3246f05237d98b55ff121e8a15d5d4dc.ppt",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.ppsx",
      "@type": "File",
      "name": "example.ppsx",
      "alternateName": "77/77d83264f74db6c0ac4a903e05cc269abd20a81f7d3f55da57bd9feefe948ead2de4b29e89321a5579eedfb33cd2304d4c4034160fb5e2d267285da384c789f9.ppsx",
      "contentSize": 57375,
      "sha256": "7af9d974a47b6d081f1ce7ad0e3d5af21be6aeb664938cef6cfd8bdf1937cb2a"
    },
    {
      "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.pps",
      "@type": "File",
      "name": "example.pps",
      "alternateName": "65/65f5f5f3b3e8f4001257efa7c40b6f14453d2bd7fef8234b183f25c6d037eb9c52559b12c19e6a2236b9393a213ad026abb164dcec6daeb3fd001e1831022da1.pps",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "#category-R&D",
      "@type": "Thing",
      "name": "R&D"
    },
    {
      "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:48+02:00",
      "dateModified": "2024-06-17T20:56:58+02:00",
      "name": "Testing relationship between acceleration and gravity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=314",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "hasPart": [
        {
          "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.pptx"
        },
        {
          "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.ppt"
        },
        {
          "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.ppsx"
        },
        {
          "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/example.pps"
        }
      ],
      "identifier": "20240617-5adb0eb3ced9e2fb514ddbdf8b102869355b72fc",
      "keywords": "generated from yml,has-mathjax,physics",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "about": {
        "@id": "#category-R&D"
      },
      "variableMeasured": null,
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 4,
        "reviewCount": 1
      }
    },
    {
      "@id": "#category-Demo",
      "@type": "Thing",
      "name": "Demo"
    },
    {
      "@id": "./Demo - Synthesis-of-Aspirin - 6bc46aec/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ec7c1f6cde2fe4f2edab2ef88546f997f5f9c2328c4bbd4de99309f49b0161f7?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:49+02:00",
      "dateModified": "2024-06-17T20:56:43+02:00",
      "name": "Synthesis of Aspirin",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=315",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20240617-6bc46aec1f90e105d3c91b641accfe804a843b51",
      "keywords": "generated from yml,chemistry,has-mathjax",
      "text": "<h1>Introduction</h1>\n<p>\nAspirin is a widely used pain-relieving and anti-inflammatory drug. In this experiment, we aimed to synthesize aspirin from salicylic acid and acetic anhydride.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe mixed salicylic acid and acetic anhydride in the presence of a catalyst, sulfuric acid. The reaction produced aspirin and acetic acid, as shown in the following chemical equation:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nAfter the reaction, we purified the aspirin by recrystallization from hot water. The purity of the aspirin was confirmed using thin-layer chromatography (TLC) and melting point analysis.\n</p>\n<h2>Results</h2>\n<p>\nThe yield of aspirin was 80% based on the amount of salicylic acid used. The purity of the aspirin was confirmed using TLC, which showed a single spot corresponding to aspirin. The melting point of the aspirin was 135-136\u00b0C, which is consistent with the literature value of 135-136.5\u00b0C.\n</p>\n<p>\nThe chemical reaction involved in the synthesis of aspirin can be written as:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nThe theoretical yield of aspirin can be calculated using the stoichiometry of the reaction. Assuming that all the salicylic acid reacts and no aspirin is lost during the purification process, the theoretical yield is calculated as follows:\n</p>\n<p>\n$$\\text{Theoretical yield} = \\frac{\\text{moles of salicylic acid used}}{\\text{molar ratio of salicylic acid to aspirin}} \\times \\text{molar mass of aspirin}$$\n</p>\n<p>\nThe actual yield of aspirin can be calculated by dividing the mass of the purified aspirin by the mass of salicylic acid used and multiplying by 100%. The percent yield can be calculated by dividing the actual yield by the theoretical yield and multiplying by 100%.\n</p>\n",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": null
    },
    {
      "@id": "comment://ae83188ed6c0efa5f37c81956547f5769eeb0724215d6a456f1a59d3bbaa33aa?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-06-17T20:05:49+02:00",
      "text": "Well, it's always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/example.docx",
      "@type": "File",
      "name": "example.docx",
      "alternateName": "fa/fac02d995b0e107f31fc718b0b1b5bf305485ad87d913863cbd859c38da6e7e26da9e04cc074bca216b5e7f0151587ff98f32d9045b32ad7963e4a0d798dff6f.docx",
      "contentSize": 4147,
      "sha256": "f1bc2027abdc4df60fbb1b0123fa73f768fe85f4e7cd277ad6a338b2cae089c0"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/example.dna",
      "@type": "File",
      "name": "example.dna",
      "alternateName": "cd/cd7ab0ee4a20fb265407f6a2be2bf4c324102836e05b21d946fdb410f8a6572e810c3c7ca873651f8504411aeacdce1bc542ea98e4d6cef677b46211e0493f23.dna",
      "contentSize": 27050,
      "sha256": "96639ecb57ddec5116d3cb3a9d4a3d5b37e89bbd9a7a3df782fe3e827f3fd787"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/example.cif",
      "@type": "File",
      "name": "example.cif",
      "alternateName": "bc/bc955ad376445ad4ead83b3d4a0f7cbfcaf771bf5047daa0f0313b6224838e616f0c3a5e3ef5653892cd90b7f73178c6c332a0b2d6a32ccb2a9b936108f57fff.cif",
      "contentSize": 178876,
      "sha256": "84a65798c5a227119ad96b921e6f3e19ed34b23cfcee350be8d74c63e0e95d40"
    },
    {
      "@id": "comment://eb912fa48283cfc716e5ac8bf0fa1288f05d910945224f520bab1f50d9af353d?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-06-17T20:05:47+02:00",
      "text": "Great results on the DNA extraction. The yield and purity look good. For the wash steps, consider extending the final centrifugation to 3 minutes to ensure no residual buffer. Nice work!",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - df81f900/example.jpg",
      "@type": "File",
      "name": "example.jpg",
      "alternateName": "c0/c03da8102ecfb2922b844da8cbf762dd13ccafaa6089ad38223e10edeaf1b64b2b5d22be4232056a2cbf983d9c4de14dc9df859c750089568253094f8bfde798.jpg",
      "contentSize": 85530,
      "sha256": "b73626c9a9ed8561ed6126df2493bc0d84fb8feedc9fe34aed94f7d2d5f4f60f"
    },
    {
      "@id": "#category-Tests",
      "@type": "Thing",
      "name": "Tests"
    },
    {
      "@id": "./Tests - Numquam-delectus-sint-quis-sint-cupiditate-non-voluptatem - 10df895d/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:03:46+02:00",
      "dateModified": "2024-06-17T20:03:46+02:00",
      "name": "Numquam delectus sint quis sint cupiditate non voluptatem.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=32",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20240617-10df895d5f87320d8ee573007feab824683092c0",
      "keywords": "biological samples",
      "text": "Go on!' 'I'm a poor man, your Majesty,' said Alice in a low, weak voice. 'Now, I give you fair warning,' shouted the Queen. 'You make me larger, it must be on the whole pack rose up into the sea, though you mayn't believe it--' 'I never thought about it,' said Alice, (she had grown up,' she said to herself, and nibbled a little bit, and said to the waving of the sort. Next came the royal children, and everybody else. 'Leave off that!' screamed the Pigeon. 'I can see you're trying to invent something!' 'I--I'm a little while, however, she waited patiently. 'Once,' said the Dodo solemnly presented the thimble, saying 'We beg your pardon,' said Alice aloud, addressing nobody in particular. 'She'd soon fetch it back!' 'And who is Dinah, if I know all the jurors had a large dish of tarts upon it: they looked so good, that it signifies much,' she said this she looked back once or twice she had hurt the poor child, 'for I never was so large a house, that she began shrinking directly. As.",
      "about": {
        "@id": "#category-Tests"
      }
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - df81f900/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:47+02:00",
      "dateModified": "2024-06-17T20:31:53+02:00",
      "name": "Gold master experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=310",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://eb912fa48283cfc716e5ac8bf0fa1288f05d910945224f520bab1f50d9af353d?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - df81f900/example.jpg"
        }
      ],
      "identifier": "20240617-df81f90072b7768da5c80baa3bc962bbc7b3604a",
      "keywords": "generated from yml,test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1",
      "mentions": [
        {
          "@id": "./Tests - Numquam-delectus-sint-quis-sint-cupiditate-non-voluptatem - 10df895d/"
        }
      ],
      "text": "<h1>Level 1 title</h1>\n<h2>Level 2 title</h2>\n<p>The <strong>goal</strong> of this <em>experiment</em> is to have <span style=\"text-decoration:underline;\">all</span> <span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\">attributes</span>:</p>\n<ul>\n<li>all extra fields types</li>\n<li>links to experiments and items</li>\n<li>links from experiments and items</li>\n<li>status, category, tags and uploaded files</li>\n</ul>\n<h3>Here is a table</h3>\n<table style=\"border-collapse:collapse;width:100%;\" border=\"1\">\n\n<tr>\n<td>Something</td>\n<td>in H<sub>2</sub></td>\n<td>the</td>\n</tr>\n<tr>\n<td>table</td>\n<td style=\"background-color:rgb(185,106,217);border:2px dashed rgb(224,62,45);\">31<sup>321</sup></td>\n<td>there</td>\n</tr>\n\n</table>\n<p>an emoji: \ud83e\udd2a</p>\n<p>\u221e \u2211</p>\n<h4>An image</h4>\n<p><img src=\"app/download.php?name=example.jpg&amp;f=c0/c03da8102ecfb2922b844da8cbf762dd13ccafaa6089ad38223e10edeaf1b64b2b5d22be4232056a2cbf983d9c4de14dc9df859c750089568253094f8bfde798.jpg&amp;storage=1\" width=\"200\" height=\"300\" alt=\"c03da8102ecfb2922b844da8cbf762dd13ccafaa6089ad38223e10edeaf1b64b2b5d22be4232056a2cbf983d9c4de14dc9df859c750089568253094f8bfde798.jpg&amp;storage=1\"></p>\n<p><a href=\"https://www.elabftw.net/\" target=\"_blank\" rel=\"noreferrer noopener\">A link to elabftw.net</a>.</p>\n<p>\u00a0</p>",
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
      "@id": "#category-Generated",
      "@type": "Thing",
      "name": "Generated"
    },
    {
      "@id": "./Generated - Architecto-est-recusandae-tempora-facilis-nemo - 67d460ac/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:04:04+02:00",
      "dateModified": "2024-06-17T20:04:05+02:00",
      "name": "Architecto est recusandae tempora facilis nemo.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=50",
      "genre": "resource",
      "creativeWorkStatus": "Destroyed",
      "identifier": "20240617-67d460ac1b3d558fe0c8019e934d3d2a17c62501",
      "keywords": "ecology",
      "text": "I eat\" is the driest thing I ask! It's always six o'clock now.' A bright idea came into Alice's head. 'Is that the poor little thing howled so, that Alice said; 'there's a large cat which was sitting between them, fast asleep, and the moment how large she had somehow fallen into the garden. Then she went on, without attending to her; 'but those serpents! There's no pleasing them!' Alice was not a moment to be executed for having missed their turns, and she put one arm out of that is--\"Birds of a muchness\"--did you ever eat a little way out of the hall: in fact she was coming to, but it makes rather a hard word, I will prosecute YOU.--Come, I'll take no denial; We must have been a RED rose-tree, and we put a stop to this,' she said this, she came rather late, and the baby violently up and rubbed its eyes: then it chuckled. 'What fun!' said the Mouse. 'Of course,' the Gryphon replied rather crossly: 'of course you know that Cheshire cats always grinned; in fact, I didn't know that.",
      "about": {
        "@id": "#category-Generated"
      },
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "creativeWorkStatus": "unfinished",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "voluptatemaperiam"
            }
          ]
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "creativeWorkStatus": "unfinished",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "laborumsoluta"
            }
          ]
        }
      ]
    },
    {
      "@id": "./Generated - Minus-qui-dolorem-praesentium-quos-aliquam-quia-ea - 18fd5717/quout.json",
      "@type": "File",
      "name": "quout.json",
      "alternateName": "9c/9c1e8941b5f8c8c426d14d2aee478e5ae4e77cf75ae9944fa5b2d8f8938e47ec01b980ffa44330224c19775e9e7be50fd9128829052734ee72f90b907c2f7c71.json",
      "contentSize": 21,
      "sha256": "66bd0965616378a8b4698bf8b01784e7d29f15c7bde4fe86fb4f5dc959cf189c"
    },
    {
      "@id": "./Generated - Minus-qui-dolorem-praesentium-quos-aliquam-quia-ea - 18fd5717/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:04:05+02:00",
      "dateModified": "2024-06-17T20:04:05+02:00",
      "name": "Minus qui dolorem praesentium quos aliquam quia ea.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=51",
      "genre": "resource",
      "creativeWorkStatus": "Waiting",
      "hasPart": [
        {
          "@id": "./Generated - Minus-qui-dolorem-praesentium-quos-aliquam-quia-ea - 18fd5717/quout.json"
        }
      ],
      "identifier": "20240617-18fd5717439c845d64c430b390521236efa0ed3d",
      "keywords": "microbiology,HeLa,cell culture techniques,lab supplies,research methodology,scientific discovery",
      "text": "Alice considered a little girl,' said Alice, always ready to make out exactly what they WILL do next! As for pulling me out of a good deal: this fireplace is narrow, to be patted on the Duchess's cook. She carried the pepper-box in her lessons in here? Why, there's hardly room for YOU, and no one could possibly hear you.' And certainly there was a table, with a cart-horse, and expecting every moment to think about it, you know--' 'But, it goes on \"THEY ALL RETURNED FROM HIM TO YOU,\"' said Alice. 'I don't see how he can EVEN finish, if he thought it would be only rustling in the last words out loud, and the Queen till she shook the house, and have next to no toys to play croquet.' The Frog-Footman repeated, in the window, and one foot to the company generally, 'You are not attending!' said the Cat. 'I said pig,' replied Alice; 'and I wish I had to leave the court; but on the floor, as it didn't sound at all for any lesson-books!' And so she sat on, with closed eyes, and half believed."
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:49+02:00",
      "dateModified": "2024-06-17T20:54:35+02:00",
      "name": "Testing the eLabFTW lab notebook",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=316",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://ae83188ed6c0efa5f37c81956547f5769eeb0724215d6a456f1a59d3bbaa33aa?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Running",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/example.docx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/example.dna"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/example.cif"
        }
      ],
      "identifier": "20240617-8ebcfca10c816e3ff3a9d0fe00e367b9b8ab1811",
      "keywords": "generated from yml,demo,test",
      "mentions": [
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - df81f900/"
        },
        {
          "@id": "./Generated - Architecto-est-recusandae-tempora-facilis-nemo - 67d460ac/"
        },
        {
          "@id": "./Generated - Minus-qui-dolorem-praesentium-quos-aliquam-quia-ea - 18fd5717/"
        }
      ],
      "text": "<h1>Goal</h1>\n<p>Test the software.</p>\n<h1>Procedure</h1>\n<p>Click everywhere and explore everything.</p>\n<h1>Results</h1>\n<p>It's really nice, I think I'll adopt it for our lab.</p>",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"OMERO dataset url\": {\"type\": \"url\", \"value\": \"https://omero.uni.example.edu/viewer?team=39&project=194\", \"description\": \"Link to the OMERO server\"}, \"Annie, are you okay\": {\"type\": \"checkbox\", \"value\": \"\", \"description\": \"This is a checkbox custom input\"}, \"This is a custom list input\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"The value is selected from a pre-defined list\"}}}"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "OMERO dataset url",
          "valueReference": "url",
          "value": "https://omero.uni.example.edu/viewer?team=39&project=194",
          "description": "Link to the OMERO server"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Annie, are you okay",
          "valueReference": "checkbox",
          "value": "",
          "description": "This is a checkbox custom input"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "This is a custom list input",
          "valueReference": "select",
          "value": "Some choice",
          "description": "The value is selected from a pre-defined list"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Effect-of-temperature-on-enzyme-activity - d938ab84/",
      "@type": "Dataset",
      "author": {
        "@id": "person://b344adffee437ab4a11d1c722fd096492f586b0d47854a3761efb68647b7b84c?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:48+02:00",
      "dateModified": "2024-06-17T20:05:48+02:00",
      "name": "Effect of temperature on enzyme activity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=313",
      "genre": "experiment",
      "creativeWorkStatus": "Need to be redone",
      "identifier": "20240617-d938ab84ea960b6c6ec3f9c717ba7c3cd29d7506",
      "keywords": "generated from yml,enzymology,test,Project ENZYTEMP",
      "text": "<h1>Effect of Temperature on Enzyme Activity</h1>\n<p>\nEnzymes are biological molecules that catalyze chemical reactions in living organisms. In this experiment, we investigated the effect of temperature on the activity of the enzyme amylase, which catalyzes the hydrolysis of starch into glucose.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe prepared a solution of starch and added a small amount of amylase to the solution. We then incubated the solution at different temperatures, ranging from 4\u00b0C to 70\u00b0C, for 5 minutes. After the incubation period, we added iodine to the solution to detect the presence of starch. The disappearance of the blue-black color of the iodine indicated the breakdown of starch into glucose.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the activity of amylase increased with increasing temperature up to 37\u00b0C, which is the optimum temperature for amylase activity. At temperatures above 37\u00b0C, the activity of amylase decreased rapidly, and at 70\u00b0C, the enzyme was completely denatured and lost its catalytic activity.\n</p>\n<p>\nThe relationship between temperature and enzyme activity can be described by the Arrhenius equation, which relates the rate constant of a reaction to the activation energy and temperature. The equation can be written as:\n</p>\n<p>\n$$k = Ae^{-E_a/RT}$$\n</p>\n<p>\nwhere k is the rate constant, A is the pre-exponential factor, E_a is the activation energy, R is the gas constant, and T is the absolute temperature. The activation energy is the energy required to break the bonds in the reactants and form the products. The rate constant increases with increasing temperature due to the increase in the number of reactant molecules with sufficient kinetic energy to overcome the activation energy barrier.\n</p>\n<p>\nThe effect of temperature on enzyme activity can also be described by the Q10 value, which is the ratio of the reaction rate at a given temperature to the reaction rate at a temperature 10\u00b0C lower. The Q10 value for most enzyme-catalyzed reactions is around 2-3, indicating that the reaction rate doubles or triples with each 10\u00b0C increase in temperature.\n</p>\n",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - f44d2c0b/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:48+02:00",
      "dateModified": "2024-06-17T20:05:48+02:00",
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=312",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20240617-f44d2c0ba07593d783c6ddc35c3d10bc29f12aa5",
      "keywords": "generated from yml,CJK,\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8",
      "text": "<p>\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002</p>\n\n<p>\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002</p>\n\n<p>\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002</p>\n\n<p>\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002</p>\n\n<p>\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002</p>\n",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - 412e346f/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:47+02:00",
      "dateModified": "2024-06-17T20:05:48+02:00",
      "name": "Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=311",
      "genre": "experiment",
      "creativeWorkStatus": "Fail",
      "identifier": "20240617-412e346fec91249c16c95a24d8a3253cd6a5f277",
      "keywords": "generated from yml,synthesis,antimicrobial,chemistry",
      "mentions": [
        {
          "@id": "./Generated - Architecto-est-recusandae-tempora-facilis-nemo - 67d460ac/"
        }
      ],
      "text": "<h1>Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties</h1>\n<p>\nThe emergence of drug-resistant bacterial strains has become a major public health concern, highlighting the need for the development of new antimicrobial agents. In this study, we aimed to synthesize a novel organic compound with potential antimicrobial activity.\n</p>\n<h2>Experimental Design</h2>\n<p>\nThe compound was synthesized via a multi-step reaction scheme. The starting material, benzaldehyde, was reacted with aniline in the presence of an acid catalyst to form the intermediate product, N-phenylbenzamide. The intermediate product was then reacted with thionyl chloride to form the corresponding acid chloride. The acid chloride was then reacted with aminoguanidine in the presence of a base catalyst to form the final product, which was purified by recrystallization.\n</p>\n<h2>Characterization</h2>\n<p>\nThe synthesized compound was characterized using various spectroscopic techniques. The melting point of the compound was determined using a melting point apparatus and compared to the literature value. The IR spectrum of the compound was obtained using a Fourier transform infrared spectrometer and compared to the expected spectrum. The NMR spectrum of the compound was obtained using a nuclear magnetic resonance spectrometer and analyzed to confirm the structure of the compound.\n</p>\n<h2>Antimicrobial Activity</h2>\n<p>\nThe antimicrobial activity of the synthesized compound was evaluated against several bacterial strains using the disk diffusion method. The results showed that the compound exhibited significant antimicrobial activity against both Gram-positive and Gram-negative bacteria, suggesting its potential as a new antimicrobial agent.\n</p>\n",
      "variableMeasured": null,
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 1,
        "reviewCount": 1
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - 4b08c8b1/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:47+02:00",
      "dateModified": "2024-06-17T20:05:47+02:00",
      "name": "Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=309",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20240617-4b08c8b1865d717c0e054062b7676da37f1a0d7a",
      "keywords": "generated from yml,transfection,biocell,RPE-1",
      "text": "<h1>Goal</h1><p>Transfecting the plasmid p103\u039412-22 into the RPE-1 Actin-RFP cells and look at the death rate.</p>",
      "variableMeasured": null
    },
    {
      "@id": "comment://bd4be523f6baba4df3d7482cd2df4b03481d54ad63444f720c99f476c49c8431?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-06-17T20:05:46+02:00",
      "text": "Oh, how fascinating. I'm sure the groundbreaking discovery that water is wet will change the course of human history forever.",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "comment://94292c4f5603efe95bfd6cbd29b36bcd5976c5f365ed19f2cfd69dc01f9bf1fa?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-06-17T20:05:46+02:00",
      "text": "Well, it's a relief to see that the scientific community is hard at work discovering what we already suspected: that the sky is indeed blue. I can't wait for their next groundbreaking revelation that grass is green.",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - An-example-experiment - 4ae900b8/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:46+02:00",
      "dateModified": "2024-06-17T20:05:46+02:00",
      "name": "An example experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=308",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://bd4be523f6baba4df3d7482cd2df4b03481d54ad63444f720c99f476c49c8431?hash_algo=sha256"
        },
        {
          "@id": "comment://94292c4f5603efe95bfd6cbd29b36bcd5976c5f365ed19f2cfd69dc01f9bf1fa?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "identifier": "20240617-4ae900b8e1a93afb825975f2a6ffe993007c6441",
      "keywords": "generated from yml,example,demo",
      "text": "This is the content of the experiment",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 4220974c/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2024-06-17T20:05:46+02:00",
      "dateModified": "2024-06-17T20:05:46+02:00",
      "name": "Test the grouped extra fields",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=307",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20240617-4220974cfb1e4b36b215384b5c4f1f2cc472c833",
      "keywords": "generated from yml,dev,extra fields",
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
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./RD - Testing-relationship-between-acceleration-and-gravity - 5adb0eb3/"
        },
        {
          "@id": "./Demo - Synthesis-of-Aspirin - 6bc46aec/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 8ebcfca1/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - df81f900/"
        },
        {
          "@id": "./Tests - Numquam-delectus-sint-quis-sint-cupiditate-non-voluptatem - 10df895d/"
        },
        {
          "@id": "./Generated - Architecto-est-recusandae-tempora-facilis-nemo - 67d460ac/"
        },
        {
          "@id": "./Generated - Minus-qui-dolorem-praesentium-quos-aliquam-quia-ea - 18fd5717/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Effect-of-temperature-on-enzyme-activity - d938ab84/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - f44d2c0b/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - 412e346f/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - 4b08c8b1/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - An-example-experiment - 4ae900b8/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 4220974c/"
        }
      ]
    },
    {
      "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Toto",
      "familyName": "Le sysadmin",
      "email": "toto@yopmail.com"
    },
    {
      "@id": "person://ec7c1f6cde2fe4f2edab2ef88546f997f5f9c2328c4bbd4de99309f49b0161f7?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Viola",
      "familyName": "Gleichner",
      "email": "tutu@yopmail.com"
    },
    {
      "@id": "person://b344adffee437ab4a11d1c722fd096492f586b0d47854a3761efb68647b7b84c?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Presley",
      "familyName": "Little",
      "email": "titi@yopmail.com"
    }
  ]
}
```
