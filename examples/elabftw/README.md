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
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.2"
      },
      "dateCreated": "2025-09-12T00:00:53+02:00",
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
      "endTime": "2025-09-12T00:00:53+02:00",
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
      "version": "5.3.0-alpha5",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "comment://be5c717abd6a045e174424d22006e2dbba021a0576ca9384c7263bb0b3182ffa?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-09-11T23:01:40+02:00",
      "text": "Imported comment from Toto Le sysadmin (2025-09-11T22:44:49+02:00)\n\nImported comment from Toto Le sysadmin (2025-09-11T22:22:19+02:00)\n\nSigned by Toto Le sysadmin (Approval)",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Tests - Eln-version-103 - f2702332/example.fasta",
      "@type": "File",
      "name": "example.fasta",
      "alternateName": "7a/7a2b66209a37f3eabed5fb7bd103a2d5c33ff505717c236af5297804182fb08aaec174af3b19f87b41d78f9693ee63b8c8b320d9b1b73a18ee571c07d72eca61.fasta",
      "encodingFormat": "application/octet-stream",
      "contentSize": 819,
      "sha256": "ca6e575af2d237d895ef3d697eb0bf4102513bd85b949fc2ec6d7f40b0f280b6",
      "description": "my great dna sequence"
    },
    {
      "@id": "./Tests - Eln-version-103 - f2702332/example.mol",
      "@type": "File",
      "name": "example.mol",
      "alternateName": "94/946492f1d550f5851309756a1b2b249baaa7bacfa7ff484a52551e365ea9698c088f007353045a64291a2ab3eb687735434904fd2df21049216f822326fe31ee.mol",
      "encodingFormat": "application/octet-stream",
      "contentSize": 1664,
      "sha256": "5622cb4d7a5e6166a3527345ffc864a768cd03c3f77511a5988853c402c504a4"
    },
    {
      "@id": "./Tests - Eln-version-103 - f2702332/example.docx",
      "@type": "File",
      "name": "example.docx",
      "alternateName": "12/12f1767133fa2f46db46a9a78c19d923cd3c4cb0c664c3e189a6562622eab0f7f663dbe13b7ae0dd79b00a05f83cb7ea479d0f5305568a7a9ea4d399b521883e.docx",
      "encodingFormat": "application/octet-stream",
      "contentSize": 4147,
      "sha256": "f1bc2027abdc4df60fbb1b0123fa73f768fe85f4e7cd277ad6a338b2cae089c0",
      "description": "who doesn't love a docx :/"
    },
    {
      "@id": "#category-Cell biology",
      "@type": "Thing",
      "name": "Cell biology",
      "color": "2B2C3A"
    },
    {
      "@id": "./Cell-biology - Transfection-of-p103D12-22-into-RPE-1-Actin-RFP - 5752d55a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:41+02:00",
      "dateModified": "2025-09-11T23:01:41+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=69",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250911-5752d55ae635b27e4e373190210f0f869af68de4",
      "keywords": "generated from yml,transfection,biocell,RPE-1",
      "text": "<h1>Goal</h1><p>Transfecting the plasmid p103\u039412-22 into the RPE-1 Actin-RFP cells and look at the death rate.</p>",
      "about": {
        "@id": "#category-Cell biology"
      }
    },
    {
      "@id": "#category-Demo",
      "@type": "Thing",
      "name": "Demo",
      "color": "AFBD27"
    },
    {
      "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - a5ded55a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:41+02:00",
      "dateModified": "2025-09-11T23:01:41+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Testing relationship between acceleration and gravity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=70",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250911-a5ded55af3bde49f235340cccffb7374490fa8da",
      "keywords": "generated from yml,has-mathjax,physics",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "about": {
        "@id": "#category-Demo"
      }
    },
    {
      "@id": "comment://00de060316423d5c697b29b3d9cf0ce41ed3de43bfe409115a5b28fd8089348e?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-09-11T23:01:41+02:00",
      "text": "Imported comment from Geovanni O'Kon (2025-09-02T10:17:17+02:00)\n\nImported comment from Geovanni O'Kon (2025-09-01T18:23:58+02:00)\n\nGreat results on the DNA extraction. The yield and purity look good. For the wash steps, consider extending the final centrifugation to 3 minutes to ensure no residual buffer. Nice work!",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "pv://1135020c-597c-4f57-85ee-962d9916bd4e",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group 1\"}, {\"id\": 2, \"name\": \"Group 2\"}, {\"id\": 3, \"name\": \"Last group\"}]}, \"extra_fields\": {\"Number\": {\"type\": \"number\", \"unit\": \"\", \"units\": [], \"value\": \"\", \"group_id\": 2, \"description\": \"no units\"}, \"Type URL\": {\"type\": \"url\", \"value\": \"https://www.elabftw.net\", \"group_id\": 2, \"readonly\": true, \"description\": \"a link (readonly)\"}, \"Just time\": {\"type\": \"time\", \"value\": \"17:00\", \"group_id\": 2, \"description\": \"tea time\"}, \"Some date\": {\"type\": \"date\", \"value\": \"2024-07-14\", \"group_id\": 2, \"description\": \"is a date\"}, \"Type user\": {\"type\": \"users\", \"value\": 1, \"group_id\": 3, \"description\": \"this is a link to a user\"}, \"A checkbox\": {\"type\": \"checkbox\", \"value\": \"on\", \"group_id\": 2, \"description\": \"is checked\"}, \"Email input\": {\"type\": \"email\", \"value\": \"louis@example.com\", \"group_id\": 2, \"description\": \"type email\"}, \"Date and time\": {\"type\": \"datetime-local\", \"value\": \"2024-07-14T13:37\", \"group_id\": 2, \"description\": \"datetime description\"}, \"Radio buttons\": {\"type\": \"radio\", \"value\": \"Oui\", \"options\": [\"Oui\", \"Non\", \"Peut-\u00eatre\"], \"group_id\": 1, \"description\": \"radio description\"}, \"Type resource\": {\"type\": \"items\", \"value\": 208, \"group_id\": 3, \"description\": \"This is a link to a resource\"}, \"A dropdown menu\": {\"type\": \"select\", \"value\": \"Choice 1\", \"options\": [\"Choice 1\", \"Choice 2\", \"Choice 3\"], \"group_id\": 1, \"description\": \"Single select\"}, \"Text input name\": {\"type\": \"text\", \"value\": \"some text\", \"group_id\": 1, \"readonly\": true, \"required\": true, \"description\": \"type text + all attributes\", \"blank_value_on_duplicate\": true}, \"Type experiment\": {\"type\": \"experiments\", \"value\": 373, \"group_id\": 3, \"description\": \"This is a link to an experiment\"}, \"Number with units\": {\"type\": \"number\", \"unit\": \"mM\", \"units\": [\"mM\", \"\u03bcM\", \"nM\"], \"value\": \"\", \"group_id\": 2, \"description\": \"this one has units\"}, \"Unchecked checkbox\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 2, \"description\": \"this one is not checked\"}, \"Multi dropdown menu\": {\"type\": \"select\", \"value\": \"Option 1\", \"options\": [\"Option 1\", \"Option 2\", \"Option 3\"], \"group_id\": 1, \"description\": \"Allows multiple selection\", \"allow_multi_values\": true}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://79eb95db-6986-41ba-a0cc-dd7c22ee9c89",
      "propertyID": "Number",
      "valueReference": "number",
      "value": "",
      "description": "no units"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://33ff9e7a-7468-4bb2-a241-94b83b7c5f0a",
      "propertyID": "Type URL",
      "valueReference": "url",
      "value": "https://www.elabftw.net",
      "description": "a link (readonly)"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://87c84364-d87a-4c17-8faa-c23d6f20b0fe",
      "propertyID": "Just time",
      "valueReference": "time",
      "value": "17:00",
      "description": "tea time"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://69bf9e01-af7a-469f-a9b2-ed73fa1be703",
      "propertyID": "Some date",
      "valueReference": "date",
      "value": "2024-07-14",
      "description": "is a date"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://3c3e2c28-9b4f-43a4-a7f2-b64cad3412b5",
      "propertyID": "Type user",
      "valueReference": "users",
      "value": 1,
      "description": "this is a link to a user"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://eccf01ad-bfde-453e-a877-bd2e7f1ef990",
      "propertyID": "A checkbox",
      "valueReference": "checkbox",
      "value": "on",
      "description": "is checked"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://d3b03380-f716-4772-9bf5-281ef48414a6",
      "propertyID": "Email input",
      "valueReference": "email",
      "value": "louis@example.com",
      "description": "type email"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://c2feab1b-54a6-4466-a018-b8416b326295",
      "propertyID": "Date and time",
      "valueReference": "datetime-local",
      "value": "2024-07-14T13:37",
      "description": "datetime description"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://23fa4eab-13e6-4f90-bc29-a69a000af2b4",
      "propertyID": "Radio buttons",
      "valueReference": "radio",
      "value": "Oui",
      "description": "radio description"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://6e6abbd2-1cfb-4ec1-9223-f0e43a2bedda",
      "propertyID": "Type resource",
      "valueReference": "items",
      "value": 208,
      "description": "This is a link to a resource"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://ec71108b-6214-41f0-9167-b1daf0b7ac84",
      "propertyID": "A dropdown menu",
      "valueReference": "select",
      "value": "Choice 1",
      "description": "Single select"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://4697f166-9d22-4680-9431-cee12183afbf",
      "propertyID": "Text input name",
      "valueReference": "text",
      "value": "some text",
      "description": "type text + all attributes"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://0a4cd787-0d1e-4970-bbb0-151a6b781e3d",
      "propertyID": "Type experiment",
      "valueReference": "experiments",
      "value": 373,
      "description": "This is a link to an experiment"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://4c602f77-be48-4e6e-82f8-7d1c79ac96e6",
      "propertyID": "Number with units",
      "valueReference": "number",
      "value": "",
      "description": "this one has units",
      "unitText": "mM"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://f049b439-ec7d-423d-96d4-e8d0b18d2689",
      "propertyID": "Unchecked checkbox",
      "valueReference": "checkbox",
      "value": "",
      "description": "this one is not checked"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://d0a21280-e546-42ff-aaad-c6c31061a29b",
      "propertyID": "Multi dropdown menu",
      "valueReference": "select",
      "value": "Option 1",
      "description": "Allows multiple selection"
    },
    {
      "@id": "./Demo - Gold-master-experiment - c0236c67/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:41+02:00",
      "dateModified": "2025-09-11T23:01:41+02:00",
      "temporal": "2025-01-03T00:00:00+01:00",
      "name": "Gold master experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=71",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://00de060316423d5c697b29b3d9cf0ce41ed3de43bfe409115a5b28fd8089348e?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "identifier": "20250911-c0236c6713510230597d5b1d4bfac5e736e07c30",
      "keywords": "generated from yml,test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1",
      "text": "<h1>Level 1 title</h1>\n<h2>Level 2 title</h2>\n<p>The <strong>goal</strong> of this <em>experiment</em> is to have <span style=\"text-decoration:underline;\">all</span> <span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\">attributes</span>:</p>\n<ul>\n<li>all extra fields types</li>\n<li>links to experiments and items</li>\n<li>links from experiments and items</li>\n<li>status, category, tags and uploaded files</li>\n</ul>\n<h3>Here is a table</h3>\n<table style=\"width:100%;\" border=\"1\">\n\n<tr>\n<td>Something</td>\n<td>in H<sub>2</sub></td>\n<td>the</td>\n</tr>\n<tr>\n<td>table</td>\n<td style=\"background-color:rgb(185,106,217);border:2px dashed rgb(224,62,45);\">31<sup>321</sup></td>\n<td>there</td>\n</tr>\n\n</table>\n<p>an emoji: \ud83e\udd2a</p>\n<p>\u221e \u2211</p>\n<h4>An image</h4>\n<p><img src=\"app/download.php?name=example.jpg&amp;f=78/7834c99a3af687a043d7e9c5bec5e4877469748dca1e898892962ab769be562e069204c19f3bf4663dd2f036cd2a9673b8db53702405ad5298a6e1fd78d6d7da.jpg&amp;storage=1\" width=\"173\" height=\"260\" alt=\"7834c99a3af687a043d7e9c5bec5e4877469748dca1e898892962ab769be562e069204c19f3bf4663dd2f036cd2a9673b8db53702405ad5298a6e1fd78d6d7da.jpg&amp;storage=1\"></p>\n<p><a href=\"https://www.elabftw.net/\" target=\"_blank\" rel=\"noreferrer noopener\">A link to elabftw.net</a>.</p>\n<p>\u00a0</p>\n",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://1135020c-597c-4f57-85ee-962d9916bd4e"
        },
        {
          "@id": "pv://79eb95db-6986-41ba-a0cc-dd7c22ee9c89"
        },
        {
          "@id": "pv://33ff9e7a-7468-4bb2-a241-94b83b7c5f0a"
        },
        {
          "@id": "pv://87c84364-d87a-4c17-8faa-c23d6f20b0fe"
        },
        {
          "@id": "pv://69bf9e01-af7a-469f-a9b2-ed73fa1be703"
        },
        {
          "@id": "pv://3c3e2c28-9b4f-43a4-a7f2-b64cad3412b5"
        },
        {
          "@id": "pv://eccf01ad-bfde-453e-a877-bd2e7f1ef990"
        },
        {
          "@id": "pv://d3b03380-f716-4772-9bf5-281ef48414a6"
        },
        {
          "@id": "pv://c2feab1b-54a6-4466-a018-b8416b326295"
        },
        {
          "@id": "pv://23fa4eab-13e6-4f90-bc29-a69a000af2b4"
        },
        {
          "@id": "pv://6e6abbd2-1cfb-4ec1-9223-f0e43a2bedda"
        },
        {
          "@id": "pv://ec71108b-6214-41f0-9167-b1daf0b7ac84"
        },
        {
          "@id": "pv://4697f166-9d22-4680-9431-cee12183afbf"
        },
        {
          "@id": "pv://0a4cd787-0d1e-4970-bbb0-151a6b781e3d"
        },
        {
          "@id": "pv://4c602f77-be48-4e6e-82f8-7d1c79ac96e6"
        },
        {
          "@id": "pv://f049b439-ec7d-423d-96d4-e8d0b18d2689"
        },
        {
          "@id": "pv://d0a21280-e546-42ff-aaad-c6c31061a29b"
        }
      ]
    },
    {
      "@id": "#category-Enzymo",
      "@type": "Thing",
      "name": "Enzymo",
      "color": "AB3536"
    },
    {
      "@id": "./Enzymo - Effect-of-temperature-on-enzyme-activity - c8736c19/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:41+02:00",
      "dateModified": "2025-09-11T23:01:42+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Effect of temperature on enzyme activity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=72",
      "genre": "experiment",
      "creativeWorkStatus": "Need to be redone",
      "identifier": "20250911-c8736c192fd5a5a636232ee056691d8a4d22c7a0",
      "keywords": "generated from yml,enzymology,test,Project ENZYTEMP",
      "text": "<h1>Effect of Temperature on Enzyme Activity</h1>\n<p>\nEnzymes are biological molecules that catalyze chemical reactions in living organisms. In this experiment, we investigated the effect of temperature on the activity of the enzyme amylase, which catalyzes the hydrolysis of starch into glucose.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe prepared a solution of starch and added a small amount of amylase to the solution. We then incubated the solution at different temperatures, ranging from 4\u00b0C to 70\u00b0C, for 5 minutes. After the incubation period, we added iodine to the solution to detect the presence of starch. The disappearance of the blue-black color of the iodine indicated the breakdown of starch into glucose.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the activity of amylase increased with increasing temperature up to 37\u00b0C, which is the optimum temperature for amylase activity. At temperatures above 37\u00b0C, the activity of amylase decreased rapidly, and at 70\u00b0C, the enzyme was completely denatured and lost its catalytic activity.\n</p>\n<p>\nThe relationship between temperature and enzyme activity can be described by the Arrhenius equation, which relates the rate constant of a reaction to the activation energy and temperature. The equation can be written as:\n</p>\n<p>\n$$k = Ae^{-E_a/RT}$$\n</p>\n<p>\nwhere k is the rate constant, A is the pre-exponential factor, E_a is the activation energy, R is the gas constant, and T is the absolute temperature. The activation energy is the energy required to break the bonds in the reactants and form the products. The rate constant increases with increasing temperature due to the increase in the number of reactant molecules with sufficient kinetic energy to overcome the activation energy barrier.\n</p>\n<p>\nThe effect of temperature on enzyme activity can also be described by the Q10 value, which is the ratio of the reaction rate at a given temperature to the reaction rate at a temperature 10\u00b0C lower. The Q10 value for most enzyme-catalyzed reactions is around 2-3, indicating that the reaction rate doubles or triples with each 10\u00b0C increase in temperature.\n</p>\n",
      "about": {
        "@id": "#category-Enzymo"
      }
    },
    {
      "@id": "#category-Synthesis",
      "@type": "Thing",
      "name": "Synthesis",
      "color": "2122B0"
    },
    {
      "@id": "./Synthesis - Synthesis-of-Aspirin - 87810ece/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:42+02:00",
      "dateModified": "2025-09-11T23:01:42+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Synthesis of Aspirin",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=73",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250911-87810eceb66e98190f61d282fc45f3b4b3cee555",
      "keywords": "generated from yml,has-mathjax,chemistry",
      "text": "<h1>Introduction</h1>\n<p>\nAspirin is a widely used pain-relieving and anti-inflammatory drug. In this experiment, we aimed to synthesize aspirin from salicylic acid and acetic anhydride.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe mixed salicylic acid and acetic anhydride in the presence of a catalyst, sulfuric acid. The reaction produced aspirin and acetic acid, as shown in the following chemical equation:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nAfter the reaction, we purified the aspirin by recrystallization from hot water. The purity of the aspirin was confirmed using thin-layer chromatography (TLC) and melting point analysis.\n</p>\n<h2>Results</h2>\n<p>\nThe yield of aspirin was 80% based on the amount of salicylic acid used. The purity of the aspirin was confirmed using TLC, which showed a single spot corresponding to aspirin. The melting point of the aspirin was 135-136\u00b0C, which is consistent with the literature value of 135-136.5\u00b0C.\n</p>\n<p>\nThe chemical reaction involved in the synthesis of aspirin can be written as:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nThe theoretical yield of aspirin can be calculated using the stoichiometry of the reaction. Assuming that all the salicylic acid reacts and no aspirin is lost during the purification process, the theoretical yield is calculated as follows:\n</p>\n<p>\n$$\\text{Theoretical yield} = \\frac{\\text{moles of salicylic acid used}}{\\text{molar ratio of salicylic acid to aspirin}} \\times \\text{molar mass of aspirin}$$\n</p>\n<p>\nThe actual yield of aspirin can be calculated by dividing the mass of the purified aspirin by the mass of salicylic acid used and multiplying by 100%. The percent yield can be calculated by dividing the actual yield by the theoretical yield and multiplying by 100%.\n</p>\n",
      "about": {
        "@id": "#category-Synthesis"
      }
    },
    {
      "@id": "#category-\u30cf\u30a8",
      "@type": "Thing",
      "name": "\u30cf\u30a8",
      "color": "B4BFB1"
    },
    {
      "@id": "./ -  - 36c73bdd/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:42+02:00",
      "dateModified": "2025-09-11T23:01:42+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=74",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250911-36c73bdd6f6988c85ed05eaca97c85be9a25d5a1",
      "keywords": "generated from yml,CJK,\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8",
      "text": "<p>\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002</p>\n\n<p>\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002</p>\n\n<p>\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002</p>\n\n<p>\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002</p>\n\n<p>\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002</p>\n",
      "about": {
        "@id": "#category-\u30cf\u30a8"
      }
    },
    {
      "@id": "#category-Solvants",
      "@type": "Thing",
      "name": "Solvants",
      "color": "355d17"
    },
    {
      "@id": "./Solvants - Phenol-machin - 98a8d24a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:42+02:00",
      "dateModified": "2025-09-11T23:01:42+02:00",
      "temporal": "2025-09-02T00:00:00+02:00",
      "name": "Ph\u00e9nol machin",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=275",
      "genre": "resource",
      "identifier": "20250911-98a8d24a7c77899a98a67dfa7d4d004c0a24df83",
      "about": {
        "@id": "#category-Solvants"
      }
    },
    {
      "@id": "#category-Yeast",
      "@type": "Thing",
      "name": "Yeast",
      "color": "B8AC3E"
    },
    {
      "@id": "pv://26a92f54-7b15-46d3-8550-6080c309ce22",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"extra_fields\": {\"Genotype\": {\"type\": \"text\", \"value\": \"\"}, \"Mating type\": {\"type\": \"select\", \"value\": \"haploid a\", \"options\": [\"haploid a\", \"haploid \u03b1\", \"diploid\"]}, \"Strain name\": {\"type\": \"text\", \"value\": \"\"}, \"Person in charge\": {\"type\": \"users\", \"value\": \"\", \"description\": \"Select the person responsible for this strain\"}, \"Selection marker\": {\"type\": \"select\", \"value\": \"URA3\", \"options\": [\"URA3\", \"LEU2\", \"HIS3\", \"TRP1\", \"KanMX\", \"NatMX\"]}, \"Storage condition\": {\"type\": \"select\", \"value\": \"-80 \u00b0C\", \"options\": [\"-80 \u00b0C\", \"4 \u00b0C\", \"on plate\", \"in liquid culture\"]}, \"Growth temperature\": {\"type\": \"number\", \"value\": \"\", \"description\": \"in \u00b0C\"}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://f024cdee-310c-4471-bb2c-7ecf7e43cee0",
      "propertyID": "Genotype",
      "valueReference": "text",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://657ebbe1-d6c2-4313-b14d-14e1bf6e3aa1",
      "propertyID": "Mating type",
      "valueReference": "select",
      "value": "haploid a"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://be822b83-b8d1-4836-b1b0-26b3b7d5aece",
      "propertyID": "Strain name",
      "valueReference": "text",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://6e4dbb81-7657-4e2c-94d8-beea7493d050",
      "propertyID": "Person in charge",
      "valueReference": "users",
      "value": "",
      "description": "Select the person responsible for this strain"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://e5726902-93ed-4ba8-b253-2582032905ae",
      "propertyID": "Selection marker",
      "valueReference": "select",
      "value": "URA3"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://17f9e12b-ef53-476e-a961-ac3677fc503a",
      "propertyID": "Storage condition",
      "valueReference": "select",
      "value": "-80 \u00b0C"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://cd657b29-0eba-420f-bb39-828391923a6d",
      "propertyID": "Growth temperature",
      "valueReference": "number",
      "value": "",
      "description": "in \u00b0C"
    },
    {
      "@id": "./Yeast - 2-6-Dimethyl-3-nitrobenzoic-acid - 0b94dc1f/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:42+02:00",
      "dateModified": "2025-09-11T23:01:42+02:00",
      "temporal": "2025-09-08T00:00:00+02:00",
      "name": "2,6-Dimethyl-3-nitrobenzoic acid",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=276",
      "genre": "resource",
      "identifier": "20250911-0b94dc1f2b733d0b73b6e8dac4d119097c5d36f7",
      "about": {
        "@id": "#category-Yeast"
      },
      "variableMeasured": [
        {
          "@id": "pv://26a92f54-7b15-46d3-8550-6080c309ce22"
        },
        {
          "@id": "pv://f024cdee-310c-4471-bb2c-7ecf7e43cee0"
        },
        {
          "@id": "pv://657ebbe1-d6c2-4313-b14d-14e1bf6e3aa1"
        },
        {
          "@id": "pv://be822b83-b8d1-4836-b1b0-26b3b7d5aece"
        },
        {
          "@id": "pv://6e4dbb81-7657-4e2c-94d8-beea7493d050"
        },
        {
          "@id": "pv://e5726902-93ed-4ba8-b253-2582032905ae"
        },
        {
          "@id": "pv://17f9e12b-ef53-476e-a961-ac3677fc503a"
        },
        {
          "@id": "pv://cd657b29-0eba-420f-bb39-828391923a6d"
        }
      ]
    },
    {
      "@id": "#category-Tests",
      "@type": "Thing",
      "name": "Tests",
      "color": "A528BD"
    },
    {
      "@id": "pv://cfd1dec9-6d54-4fed-8d93-31ba91004273",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"elabftw\": {\"extra_fields_groups\": [{\"id\": 1, \"name\": \"Basic inputs\"}, {\"id\": 2, \"name\": \"Another group of inputs\"}]}, \"extra_fields\": {\"A date input\": {\"type\": \"date\", \"value\": \"2025-09-11\", \"group_id\": 1}, \"A text input\": {\"type\": \"text\", \"value\": \"Textual value\", \"group_id\": 1, \"readonly\": true, \"required\": true, \"description\": \"Some descriptive value\", \"blank_value_on_duplicate\": true}, \"An empty one\": {\"type\": \"email\", \"value\": \"\", \"group_id\": 1, \"description\": \"This one is empty (no value)\"}, \"Concentration\": {\"type\": \"number\", \"unit\": \"mM\", \"units\": [\"mM\", \"M\", \"\u03bcM\"], \"value\": \"\", \"description\": \"this input has units\", \"blank_value_on_duplicate\": true}, \"This is a checkbox\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 2, \"description\": \"Check it if you like to check things\"}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://a3a43d8c-4f2a-4f0f-9147-bce26fc05efc",
      "propertyID": "A date input",
      "valueReference": "date",
      "value": "2025-09-11"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://b5a3d841-d144-400b-8695-e11d452e4a94",
      "propertyID": "A text input",
      "valueReference": "text",
      "value": "Textual value",
      "description": "Some descriptive value"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://feecf8f9-d2dd-4f1d-a621-84ed6fa5b8ee",
      "propertyID": "An empty one",
      "valueReference": "email",
      "value": "",
      "description": "This one is empty (no value)"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://93980b30-4184-4873-9d15-cb959cde90c4",
      "propertyID": "Concentration",
      "valueReference": "number",
      "value": "",
      "description": "this input has units",
      "unitText": "mM"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://7461b633-f9f8-45cd-bdec-7a76b3a94b7d",
      "propertyID": "This is a checkbox",
      "valueReference": "checkbox",
      "value": "",
      "description": "Check it if you like to check things"
    },
    {
      "@id": "./Tests - Eln-version-103 - f2702332/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2025-09-11T23:01:40+02:00",
      "dateModified": "2025-09-11T23:01:43+02:00",
      "temporal": "2025-09-11T00:00:00+02:00",
      "name": "Eln version 103",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=68",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://be5c717abd6a045e174424d22006e2dbba021a0576ca9384c7263bb0b3182ffa?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "hasPart": [
        {
          "@id": "./Tests - Eln-version-103 - f2702332/example.fasta"
        },
        {
          "@id": "./Tests - Eln-version-103 - f2702332/example.mol"
        },
        {
          "@id": "./Tests - Eln-version-103 - f2702332/example.docx"
        }
      ],
      "identifier": "20250911-f2702332e76c08d2798da0c1621b30616796d960",
      "keywords": "tags can have space,another,demo,tests",
      "mentions": [
        {
          "@id": "./Cell-biology - Transfection-of-p103D12-22-into-RPE-1-Actin-RFP - 5752d55a/"
        },
        {
          "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - a5ded55a/"
        },
        {
          "@id": "./Demo - Gold-master-experiment - c0236c67/"
        },
        {
          "@id": "./Enzymo - Effect-of-temperature-on-enzyme-activity - c8736c19/"
        },
        {
          "@id": "./Synthesis - Synthesis-of-Aspirin - 87810ece/"
        },
        {
          "@id": "./ -  - 36c73bdd/"
        },
        {
          "@id": "./Solvants - Phenol-machin - 98a8d24a/"
        },
        {
          "@id": "./Yeast - 2-6-Dimethyl-3-nitrobenzoic-acid - 0b94dc1f/"
        }
      ],
      "text": "<p>This is a <em>.eln</em> created with <code>INTERNAL_ELN_VERSION = 103</code>. The difference with <strong>102</strong> is that the <code>variableMeasured</code> is flattened.</p>\n<p style=\"line-height:1;\">\u00a0</p>",
      "about": {
        "@id": "#category-Tests"
      },
      "variableMeasured": [
        {
          "@id": "pv://cfd1dec9-6d54-4fed-8d93-31ba91004273"
        },
        {
          "@id": "pv://a3a43d8c-4f2a-4f0f-9147-bce26fc05efc"
        },
        {
          "@id": "pv://b5a3d841-d144-400b-8695-e11d452e4a94"
        },
        {
          "@id": "pv://feecf8f9-d2dd-4f1d-a621-84ed6fa5b8ee"
        },
        {
          "@id": "pv://93980b30-4184-4873-9d15-cb959cde90c4"
        },
        {
          "@id": "pv://7461b633-f9f8-45cd-bdec-7a76b3a94b7d"
        }
      ],
      "aggregateRating": {
        "@id": "rating://3a32f1d7-c550-46ee-9a99-3dcab5713a0c",
        "@type": "AggregateRating",
        "ratingValue": 3,
        "reviewCount": 1
      },
      "step": [
        {
          "@id": "howtostep://cf6fb83d-a148-40a1-9d4d-a6f7219a0600",
          "@type": "HowToStep",
          "position": 0,
          "creativeWorkStatus": "finished",
          "temporal": "2025-09-11T22:56:55+02:00",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "Prepare chamber"
            }
          ]
        },
        {
          "@id": "howtostep://8e9cbae8-cc37-4cf1-bcc0-a5c071ebeded",
          "@type": "HowToStep",
          "position": 1,
          "creativeWorkStatus": "unfinished",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "Add radioactive material"
            }
          ]
        },
        {
          "@id": "howtostep://2c101b95-1071-4271-942d-069dcfd4d80f",
          "@type": "HowToStep",
          "position": 2,
          "creativeWorkStatus": "unfinished",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "Add radioactive emission triggered poison delivery device"
            }
          ]
        },
        {
          "@id": "howtostep://ef76a300-74ea-49cf-992b-bf33b92a2ce3",
          "@type": "HowToStep",
          "position": 3,
          "creativeWorkStatus": "unfinished",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "Add cat"
            }
          ]
        }
      ]
    },
    {
      "@id": "./",
      "identifier": "b6f22cbf-44bd-4039-8388-ac3141b7f3b4",
      "@type": "Dataset",
      "datePublished": "2025-09-12T00:00:53+02:00",
      "hasPart": [
        {
          "@id": "./Tests - Eln-version-103 - f2702332/"
        },
        {
          "@id": "./Cell-biology - Transfection-of-p103D12-22-into-RPE-1-Actin-RFP - 5752d55a/"
        },
        {
          "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - a5ded55a/"
        },
        {
          "@id": "./Demo - Gold-master-experiment - c0236c67/"
        },
        {
          "@id": "./Enzymo - Effect-of-temperature-on-enzyme-activity - c8736c19/"
        },
        {
          "@id": "./Synthesis - Synthesis-of-Aspirin - 87810ece/"
        },
        {
          "@id": "./ -  - 36c73bdd/"
        },
        {
          "@id": "./Solvants - Phenol-machin - 98a8d24a/"
        },
        {
          "@id": "./Yeast - 2-6-Dimethyl-3-nitrobenzoic-acid - 0b94dc1f/"
        }
      ],
      "name": "eLabFTW export",
      "description": "This is a .eln export from eLabFTW",
      "version": "103",
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
