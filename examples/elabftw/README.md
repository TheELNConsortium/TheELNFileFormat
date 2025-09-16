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
      "dateCreated": "2025-09-16T10:37:31+02:00",
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
      "endTime": "2025-09-16T10:37:31+02:00",
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
      "version": "5.3.0-alpha6",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "comment://f10fb61bae7a073a0c94363b8cb5de2fef812491b92067e3ef8dc02fcb0687ff?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "text": "Great results on the DNA extraction. The yield and purity look good. For the wash steps, consider extending the final centrifugation to 3 minutes to ensure no residual buffer. Nice work!",
      "author": {
        "@id": "person://f6084a2b68f4c7e039aebf7d53fe634a7a74e30a5a48e4623d222775c61b9921?hash_algo=sha256"
      }
    },
    {
      "@id": "./Demo - Gold-master-experiment - 4af4da4e/example.jpg",
      "@type": "File",
      "name": "example.jpg",
      "alternateName": "7b/7b82e081f08828fa461979b340d28673a32773169bf19884b61276355c0d873098977ad10b68d6845209108b8470ac4b72a1992b3d81140d0ab0af9e25d886a0.jpg",
      "encodingFormat": "application/octet-stream",
      "contentSize": 85530,
      "sha256": "b73626c9a9ed8561ed6126df2493bc0d84fb8feedc9fe34aed94f7d2d5f4f60f"
    },
    {
      "@id": "./Molecular-biology - Facilis-illum-sed-reprehenderit - a7658b02/autesse.json",
      "@type": "File",
      "name": "autesse.json",
      "alternateName": "fd/fdedffebcfbbdc8eb9a554d54951783ced67e23ac0c38445f67112bfb81543147d8960561fcd7745e3e3ec098ded2d5f86730ad635520319e502c11c5260ba2c.json",
      "encodingFormat": "application/octet-stream",
      "contentSize": 21,
      "sha256": "66bd0965616378a8b4698bf8b01784e7d29f15c7bde4fe86fb4f5dc959cf189c"
    },
    {
      "@id": "#category-Molecular biology",
      "@type": "Thing",
      "name": "Molecular biology",
      "color": "3026BC"
    },
    {
      "@id": "./Molecular-biology - Facilis-illum-sed-reprehenderit - a7658b02/",
      "@type": "Dataset",
      "author": {
        "@id": "person://f6084a2b68f4c7e039aebf7d53fe634a7a74e30a5a48e4623d222775c61b9921?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:50+02:00",
      "dateModified": "2025-09-16T10:32:50+02:00",
      "temporal": "2021-04-14T00:00:00+02:00",
      "name": "Facilis illum sed reprehenderit.",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=32",
      "genre": "experiment",
      "creativeWorkStatus": "Running",
      "hasPart": [
        {
          "@id": "./Molecular-biology - Facilis-illum-sed-reprehenderit - a7658b02/autesse.json"
        }
      ],
      "identifier": "20250916-a7658b02dcd43bdaabb9430614184264702ae754",
      "keywords": "Fly,Copper,lab supplies",
      "text": "TRUE--\" that's the jury-box,' thought Alice, 'or perhaps they won't walk the way down one side and up the fan and gloves--that is, if I like being that person, I'll come up: if not, I'll stay down here! It'll be no use in waiting by the hand, it hurried off, without waiting for the moment how large she had not gone (We know it to make the arches. The chief difficulty Alice found at first was in the distance. 'Come on!' cried the Mock Turtle: 'nine the next, and so on.' 'What a curious dream, dear, certainly: but now run in to your places!' shouted the Queen. 'I haven't opened it yet,' said the Cat: 'we're all mad here. I'm mad. You're mad.' 'How do you know about it, you know.' It was, no doubt: only Alice did not answer, so Alice soon began talking again. 'Dinah'll miss me very much at this, she was quite impossible to say 'creatures,' you see, because some of the sort!' said Alice. 'Then it doesn't matter much,' thought Alice, 'it'll never do to hold it. As soon as the game began.",
      "about": {
        "@id": "#category-Molecular biology"
      }
    },
    {
      "@id": "#category-Synthesis",
      "@type": "Thing",
      "name": "Synthesis",
      "color": "2825B0"
    },
    {
      "@id": "pv://283374c3-0aaa-430f-b390-a71157cd64a9",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./Synthesis - Synthesis-of-Aspirin - 076f68c6/",
      "@type": "Dataset",
      "author": {
        "@id": "person://8f5ab7f6890c9999cf1ba3890ad36f6c1c6908743bddd38a58c76426d61a648c?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Synthesis of Aspirin",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=57",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250916-076f68c6b56f8ab6cb023ff295e869e3c0d6e0f0",
      "keywords": "generated from yml,chemistry,has-mathjax",
      "text": "<h1>Introduction</h1>\n<p>\nAspirin is a widely used pain-relieving and anti-inflammatory drug. In this experiment, we aimed to synthesize aspirin from salicylic acid and acetic anhydride.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe mixed salicylic acid and acetic anhydride in the presence of a catalyst, sulfuric acid. The reaction produced aspirin and acetic acid, as shown in the following chemical equation:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nAfter the reaction, we purified the aspirin by recrystallization from hot water. The purity of the aspirin was confirmed using thin-layer chromatography (TLC) and melting point analysis.\n</p>\n<h2>Results</h2>\n<p>\nThe yield of aspirin was 80% based on the amount of salicylic acid used. The purity of the aspirin was confirmed using TLC, which showed a single spot corresponding to aspirin. The melting point of the aspirin was 135-136\u00b0C, which is consistent with the literature value of 135-136.5\u00b0C.\n</p>\n<p>\nThe chemical reaction involved in the synthesis of aspirin can be written as:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nThe theoretical yield of aspirin can be calculated using the stoichiometry of the reaction. Assuming that all the salicylic acid reacts and no aspirin is lost during the purification process, the theoretical yield is calculated as follows:\n</p>\n<p>\n$$\\text{Theoretical yield} = \\frac{\\text{moles of salicylic acid used}}{\\text{molar ratio of salicylic acid to aspirin}} \\times \\text{molar mass of aspirin}$$\n</p>\n<p>\nThe actual yield of aspirin can be calculated by dividing the mass of the purified aspirin by the mass of salicylic acid used and multiplying by 100%. The percent yield can be calculated by dividing the actual yield by the theoretical yield and multiplying by 100%.\n</p>\n",
      "about": {
        "@id": "#category-Synthesis"
      },
      "variableMeasured": [
        {
          "@id": "pv://283374c3-0aaa-430f-b390-a71157cd64a9"
        }
      ]
    },
    {
      "@id": "#category-\ud83d\udd2c Microscope",
      "@type": "Thing",
      "name": "\ud83d\udd2c Microscope",
      "color": "29A6A3"
    },
    {
      "@id": "./Microscope - Video-microscope-Bravo - 6bf0e813/",
      "@type": "Dataset",
      "author": {
        "@id": "person://9d870f42291406588b2f8876eefe7dd5f9ab41593809a7fc1b2e737149dfaa91?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:57+02:00",
      "dateModified": "2025-09-16T10:32:57+02:00",
      "temporal": "2022-02-09T00:00:00+01:00",
      "name": "Video microscope Bravo",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=110",
      "genre": "resource",
      "identifier": "20250916-6bf0e8137d59707cd849d19f47698e806357cecb",
      "about": {
        "@id": "#category-\ud83d\udd2c Microscope"
      }
    },
    {
      "@id": "#category-Demo",
      "@type": "Thing",
      "name": "Demo",
      "color": "A9B2B7"
    },
    {
      "@id": "pv://d4c36197-bf2a-42e6-be7d-95d1941d793c",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group 1\"}, {\"id\": 2, \"name\": \"Group 2\"}, {\"id\": 3, \"name\": \"Last group\"}]}, \"extra_fields\": {\"Number\": {\"type\": \"number\", \"unit\": \"\", \"units\": [], \"value\": \"12\", \"group_id\": 2, \"description\": \"no units\"}, \"Type URL\": {\"type\": \"url\", \"value\": \"https://www.elabftw.net\", \"group_id\": 2, \"readonly\": true, \"description\": \"a link (readonly)\"}, \"Just time\": {\"type\": \"time\", \"value\": \"17:00\", \"group_id\": 2, \"description\": \"tea time\"}, \"Some date\": {\"type\": \"date\", \"value\": \"2024-07-14\", \"group_id\": 2, \"description\": \"is a date\"}, \"Type user\": {\"type\": \"users\", \"value\": 1, \"group_id\": 3, \"description\": \"this is a link to a user\"}, \"A checkbox\": {\"type\": \"checkbox\", \"value\": \"on\", \"group_id\": 2, \"description\": \"is checked\"}, \"Email input\": {\"type\": \"email\", \"value\": \"louis@example.com\", \"group_id\": 2, \"description\": \"type email\"}, \"Date and time\": {\"type\": \"datetime-local\", \"value\": \"2024-07-14T13:37\", \"group_id\": 2, \"description\": \"datetime description\"}, \"Radio buttons\": {\"type\": \"radio\", \"value\": \"Oui\", \"options\": [\"Oui\", \"Non\", \"Peut-\u00eatre\"], \"group_id\": 1, \"description\": \"radio description\"}, \"Type resource\": {\"type\": \"items\", \"value\": 208, \"group_id\": 3, \"description\": \"This is a link to a resource\"}, \"A dropdown menu\": {\"type\": \"select\", \"value\": \"Choice 1\", \"options\": [\"Choice 1\", \"Choice 2\", \"Choice 3\"], \"group_id\": 1, \"description\": \"Single select\"}, \"Text input name\": {\"type\": \"text\", \"value\": \"some text\", \"group_id\": 1, \"readonly\": true, \"required\": true, \"description\": \"type text + all attributes\", \"blank_value_on_duplicate\": true}, \"Type experiment\": {\"type\": \"experiments\", \"value\": 57, \"group_id\": 3, \"description\": \"This is a link to an experiment\"}, \"Number with units\": {\"type\": \"number\", \"unit\": \"mM\", \"units\": [\"mM\", \"\u03bcM\", \"nM\"], \"value\": \"12\", \"group_id\": 2, \"description\": \"this one has units\"}, \"Unchecked checkbox\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 2, \"description\": \"this one is not checked\"}, \"Multi dropdown menu\": {\"type\": \"select\", \"value\": \"Option 1\", \"options\": [\"Option 1\", \"Option 2\", \"Option 3\"], \"group_id\": 1, \"description\": \"Allows multiple selection\", \"allow_multi_values\": true}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://78b5f21c-5836-4b74-8a72-12be5ab2e22a",
      "propertyID": "Number",
      "valueReference": "number",
      "value": "12",
      "description": "no units"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://6dc4e3ce-72e7-4312-a832-e846d51b129b",
      "propertyID": "Type URL",
      "valueReference": "url",
      "value": "https://www.elabftw.net",
      "description": "a link (readonly)"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://2ae99eae-c274-4391-ae5a-087442932bbb",
      "propertyID": "Just time",
      "valueReference": "time",
      "value": "17:00",
      "description": "tea time"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://d31cf5eb-4ccd-40e2-aa66-57c49fcf55e1",
      "propertyID": "Some date",
      "valueReference": "date",
      "value": "2024-07-14",
      "description": "is a date"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://dddd1d2a-037c-4c44-b05a-c9262c24124d",
      "propertyID": "Type user",
      "valueReference": "users",
      "value": 1,
      "description": "this is a link to a user"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://171ec8df-9d33-4333-8c07-721ebc8a6b79",
      "propertyID": "A checkbox",
      "valueReference": "checkbox",
      "value": "on",
      "description": "is checked"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://ce3ce33a-9d80-42f2-be01-5fe14514bed7",
      "propertyID": "Email input",
      "valueReference": "email",
      "value": "louis@example.com",
      "description": "type email"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://f0df19c8-c0fb-4db0-a4a1-1de217dffc81",
      "propertyID": "Date and time",
      "valueReference": "datetime-local",
      "value": "2024-07-14T13:37",
      "description": "datetime description"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://dde49431-0854-457b-a57b-1d4e0dd99fda",
      "propertyID": "Radio buttons",
      "valueReference": "radio",
      "value": "Oui",
      "description": "radio description"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://fa0b7569-2b88-4b7c-b539-b0eaf1ba8e18",
      "propertyID": "Type resource",
      "valueReference": "items",
      "value": 208,
      "description": "This is a link to a resource"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://873c2683-238d-4c95-ba64-91a2a77f6fee",
      "propertyID": "A dropdown menu",
      "valueReference": "select",
      "value": "Choice 1",
      "description": "Single select"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://bb0fc618-e7b4-497e-ba0f-fdfae64851ce",
      "propertyID": "Text input name",
      "valueReference": "text",
      "value": "some text",
      "description": "type text + all attributes"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://f61ac5f5-3786-465b-bc1c-af0d4474584d",
      "propertyID": "Type experiment",
      "valueReference": "experiments",
      "value": 57,
      "description": "This is a link to an experiment"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://91955c74-12cb-489a-bb99-a0ab097bef05",
      "propertyID": "Number with units",
      "valueReference": "number",
      "value": "12",
      "description": "this one has units",
      "unitText": "mM"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://39bff384-ad71-4c85-9ecf-c18ad2d62301",
      "propertyID": "Unchecked checkbox",
      "valueReference": "checkbox",
      "value": "",
      "description": "this one is not checked"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://5fd11741-4b17-441e-9bf3-678217bcc389",
      "propertyID": "Multi dropdown menu",
      "valueReference": "select",
      "value": "Option 1",
      "description": "Allows multiple selection"
    },
    {
      "@id": "howtostep://817043b4-689d-4496-96bb-7adfd4f15177",
      "@type": "HowToStep",
      "position": 1,
      "creativeWorkStatus": "finished",
      "temporal": "2025-09-16T10:36:24+02:00",
      "itemListElement": {
        "@id": "howtodirection://7e020a09-293c-47f4-a00e-203de6c41248"
      }
    },
    {
      "@id": "howtodirection://7e020a09-293c-47f4-a00e-203de6c41248",
      "@type": "HowToDirection",
      "text": "a step"
    },
    {
      "@id": "howtostep://9e8429e1-d380-4fd5-b75a-6e1151be1a9f",
      "@type": "HowToStep",
      "position": 2,
      "creativeWorkStatus": "unfinished",
      "itemListElement": {
        "@id": "howtodirection://75973fb2-f043-49e3-81fa-b21f896af4e0"
      }
    },
    {
      "@id": "howtodirection://75973fb2-f043-49e3-81fa-b21f896af4e0",
      "@type": "HowToDirection",
      "text": "another step"
    },
    {
      "@id": "./Demo - Gold-master-experiment - 4af4da4e/",
      "@type": "Dataset",
      "author": {
        "@id": "person://f6084a2b68f4c7e039aebf7d53fe634a7a74e30a5a48e4623d222775c61b9921?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:37:05+02:00",
      "temporal": "2025-01-03T00:00:00+01:00",
      "name": "Gold master experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=52",
      "genre": "experiment",
      "alternateName": 1,
      "comment": [
        {
          "@id": "comment://f10fb61bae7a073a0c94363b8cb5de2fef812491b92067e3ef8dc02fcb0687ff?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "hasPart": [
        {
          "@id": "./Demo - Gold-master-experiment - 4af4da4e/example.jpg"
        }
      ],
      "identifier": "20250916-4af4da4ef50c6512782c3b0b484aad236ccd7591",
      "keywords": "generated from yml,test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1",
      "mentions": [
        {
          "@id": "./Molecular-biology - Facilis-illum-sed-reprehenderit - a7658b02/"
        },
        {
          "@id": "./Synthesis - Synthesis-of-Aspirin - 076f68c6/"
        },
        {
          "@id": "./Microscope - Video-microscope-Bravo - 6bf0e813/"
        }
      ],
      "text": "<h1 style=\"line-height:1;\">Level 1 title</h1>\n<h2>Level 2 title</h2>\n<p>The <strong>goal</strong> of this <em>experiment</em> is to have <span style=\"text-decoration:underline;\">all</span> <span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\">attributes</span>:</p>\n<ul>\n<li>all extra fields types</li>\n<li>links to experiments and items</li>\n<li>links from experiments and items</li>\n<li>status, category, tags and uploaded files</li>\n</ul>\n<h3>Here is a table</h3>\n<table style=\"width:100%;\" border=\"1\">\n\n<tr>\n<td>Something</td>\n<td>in H<sub>2</sub></td>\n<td>the</td>\n</tr>\n<tr>\n<td>table</td>\n<td style=\"background-color:rgb(185,106,217);border:2px dashed rgb(224,62,45);\">31<sup>321</sup></td>\n<td>there</td>\n</tr>\n\n</table>\n<p>an emoji: \ud83e\udd2a</p>\n<p>\u221e \u2211</p>\n<h4>An image</h4>\n<p><img src=\"app/download.php?name=example.jpg&amp;f=7b/7b82e081f08828fa461979b340d28673a32773169bf19884b61276355c0d873098977ad10b68d6845209108b8470ac4b72a1992b3d81140d0ab0af9e25d886a0.jpg&amp;storage=1\" width=\"261\" height=\"392\" alt=\"7b82e081f08828fa461979b340d28673a32773169bf19884b61276355c0d873098977ad10b68d6845209108b8470ac4b72a1992b3d81140d0ab0af9e25d886a0.jpg&amp;storage=1\"></p>\n<p><a href=\"https://www.elabftw.net/\" target=\"_blank\" rel=\"noreferrer noopener\">A link to elabftw.net</a>.</p>\n<p>\u00a0</p>",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://d4c36197-bf2a-42e6-be7d-95d1941d793c"
        },
        {
          "@id": "pv://78b5f21c-5836-4b74-8a72-12be5ab2e22a"
        },
        {
          "@id": "pv://6dc4e3ce-72e7-4312-a832-e846d51b129b"
        },
        {
          "@id": "pv://2ae99eae-c274-4391-ae5a-087442932bbb"
        },
        {
          "@id": "pv://d31cf5eb-4ccd-40e2-aa66-57c49fcf55e1"
        },
        {
          "@id": "pv://dddd1d2a-037c-4c44-b05a-c9262c24124d"
        },
        {
          "@id": "pv://171ec8df-9d33-4333-8c07-721ebc8a6b79"
        },
        {
          "@id": "pv://ce3ce33a-9d80-42f2-be01-5fe14514bed7"
        },
        {
          "@id": "pv://f0df19c8-c0fb-4db0-a4a1-1de217dffc81"
        },
        {
          "@id": "pv://dde49431-0854-457b-a57b-1d4e0dd99fda"
        },
        {
          "@id": "pv://fa0b7569-2b88-4b7c-b539-b0eaf1ba8e18"
        },
        {
          "@id": "pv://873c2683-238d-4c95-ba64-91a2a77f6fee"
        },
        {
          "@id": "pv://bb0fc618-e7b4-497e-ba0f-fdfae64851ce"
        },
        {
          "@id": "pv://f61ac5f5-3786-465b-bc1c-af0d4474584d"
        },
        {
          "@id": "pv://91955c74-12cb-489a-bb99-a0ab097bef05"
        },
        {
          "@id": "pv://39bff384-ad71-4c85-9ecf-c18ad2d62301"
        },
        {
          "@id": "pv://5fd11741-4b17-441e-9bf3-678217bcc389"
        }
      ],
      "aggregateRating": {
        "@id": "rating://b312930e-fb5b-44cb-88bf-bdc2302301c0",
        "@type": "AggregateRating",
        "ratingValue": 4,
        "reviewCount": 1
      },
      "step": [
        {
          "@id": "howtostep://817043b4-689d-4496-96bb-7adfd4f15177"
        },
        {
          "@id": "howtostep://9e8429e1-d380-4fd5-b75a-6e1151be1a9f"
        }
      ]
    },
    {
      "@id": "comment://891dc96e9ae4bd17ea96077e8c8e8fa117d1e465ac95937d5024c8480dfd5ccb?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "text": "Well, it's always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://fab8c19cc817cbd5361ff4dd62ce16cad61192bfb42bf06919cee96e0f238818?hash_algo=sha256"
      }
    },
    {
      "@id": "pv://8d0cca89-4be2-450e-a607-16191e4f2db7",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"extra_fields\": {\"Raw data URL\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\"}, \"Annie, are you okay\": {\"type\": \"checkbox\", \"value\": \"\", \"description\": \"This is a checkbox custom input\"}, \"This is a custom list input\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"The value is selected from a pre-defined list\"}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://b840ebc1-9d8c-4913-8914-4647af9aa636",
      "propertyID": "Raw data URL",
      "valueReference": "url",
      "value": "https://datalake.example.com/experiments/3921"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://ea0f90e0-3f9d-4916-bd92-de96cc965607",
      "propertyID": "Annie, are you okay",
      "valueReference": "checkbox",
      "value": "",
      "description": "This is a checkbox custom input"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://d131e37c-fcfe-418d-9c4e-361a72372688",
      "propertyID": "This is a custom list input",
      "valueReference": "select",
      "value": "Some choice",
      "description": "The value is selected from a pre-defined list"
    },
    {
      "@id": "./Demo - Testing-the-eLabFTW-lab-notebook - 4192afd2/",
      "@type": "Dataset",
      "author": {
        "@id": "person://fab8c19cc817cbd5361ff4dd62ce16cad61192bfb42bf06919cee96e0f238818?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-03-03T00:00:00+01:00",
      "name": "Testing the eLabFTW lab notebook",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=58",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://891dc96e9ae4bd17ea96077e8c8e8fa117d1e465ac95937d5024c8480dfd5ccb?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Running",
      "identifier": "20250916-4192afd20591278aff2da65172b334ee059d5b56",
      "keywords": "generated from yml,demo,test",
      "text": "<h1>Goal</h1><p>Test the software.</p><h1>Procedure</h1><p>Click everywhere and explore everything.</p><h1>Results</h1><p>It's really nice, I think I'll adopt it for our lab.</p>",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://8d0cca89-4be2-450e-a607-16191e4f2db7"
        },
        {
          "@id": "pv://b840ebc1-9d8c-4913-8914-4647af9aa636"
        },
        {
          "@id": "pv://ea0f90e0-3f9d-4916-bd92-de96cc965607"
        },
        {
          "@id": "pv://d131e37c-fcfe-418d-9c4e-361a72372688"
        }
      ],
      "aggregateRating": {
        "@id": "rating://3bad36d3-887a-4732-83ce-85c07e7c7a85",
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      }
    },
    {
      "@id": "pv://3e5bcf0e-0ae5-4441-9e7d-8abb6fbf1553",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - 321efb16/",
      "@type": "Dataset",
      "author": {
        "@id": "person://8f5ab7f6890c9999cf1ba3890ad36f6c1c6908743bddd38a58c76426d61a648c?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Testing relationship between acceleration and gravity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=56",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250916-321efb1682f88a435d9f25e66f2ba1ad1279f851",
      "keywords": "generated from yml,has-mathjax,physics",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://3e5bcf0e-0ae5-4441-9e7d-8abb6fbf1553"
        }
      ]
    },
    {
      "@id": "#category-Enzymo",
      "@type": "Thing",
      "name": "Enzymo",
      "color": "A8A321"
    },
    {
      "@id": "pv://43819275-a431-4a95-8c5a-1b993c1f4c38",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./Enzymo - Effect-of-temperature-on-enzyme-activity - 96ce1b12/",
      "@type": "Dataset",
      "author": {
        "@id": "person://d5d9a96c536d1958169f370af86038105f487d26ebc8b280ec2132652c3ee89a?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Effect of temperature on enzyme activity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=55",
      "genre": "experiment",
      "creativeWorkStatus": "Need to be redone",
      "identifier": "20250916-96ce1b1268b62a7e083ce8b1afa3fda5dd6e26a5",
      "keywords": "generated from yml,enzymology,test,Project ENZYTEMP",
      "text": "<h1>Effect of Temperature on Enzyme Activity</h1>\n<p>\nEnzymes are biological molecules that catalyze chemical reactions in living organisms. In this experiment, we investigated the effect of temperature on the activity of the enzyme amylase, which catalyzes the hydrolysis of starch into glucose.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe prepared a solution of starch and added a small amount of amylase to the solution. We then incubated the solution at different temperatures, ranging from 4\u00b0C to 70\u00b0C, for 5 minutes. After the incubation period, we added iodine to the solution to detect the presence of starch. The disappearance of the blue-black color of the iodine indicated the breakdown of starch into glucose.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the activity of amylase increased with increasing temperature up to 37\u00b0C, which is the optimum temperature for amylase activity. At temperatures above 37\u00b0C, the activity of amylase decreased rapidly, and at 70\u00b0C, the enzyme was completely denatured and lost its catalytic activity.\n</p>\n<p>\nThe relationship between temperature and enzyme activity can be described by the Arrhenius equation, which relates the rate constant of a reaction to the activation energy and temperature. The equation can be written as:\n</p>\n<p>\n$$k = Ae^{-E_a/RT}$$\n</p>\n<p>\nwhere k is the rate constant, A is the pre-exponential factor, E_a is the activation energy, R is the gas constant, and T is the absolute temperature. The activation energy is the energy required to break the bonds in the reactants and form the products. The rate constant increases with increasing temperature due to the increase in the number of reactant molecules with sufficient kinetic energy to overcome the activation energy barrier.\n</p>\n<p>\nThe effect of temperature on enzyme activity can also be described by the Q10 value, which is the ratio of the reaction rate at a given temperature to the reaction rate at a temperature 10\u00b0C lower. The Q10 value for most enzyme-catalyzed reactions is around 2-3, indicating that the reaction rate doubles or triples with each 10\u00b0C increase in temperature.\n</p>\n",
      "about": {
        "@id": "#category-Enzymo"
      },
      "variableMeasured": [
        {
          "@id": "pv://43819275-a431-4a95-8c5a-1b993c1f4c38"
        }
      ]
    },
    {
      "@id": "#category-\u30cf\u30a8",
      "@type": "Thing",
      "name": "\u30cf\u30a8",
      "color": "B12FB6"
    },
    {
      "@id": "pv://b028004c-ffdc-4449-8330-ce1e21ad685c",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./ -  - bb8b469d/",
      "@type": "Dataset",
      "author": {
        "@id": "person://7299c4c87f75c05c1e9e61c91fd26328eb9b249f8fdceb1425a6a7dc5833ca09?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=54",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250916-bb8b469d651822d0006046449a33b5c8822b5691",
      "keywords": "generated from yml,CJK,\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8",
      "text": "<p>\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002</p>\n\n<p>\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002</p>\n\n<p>\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002</p>\n\n<p>\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002</p>\n\n<p>\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002</p>\n",
      "about": {
        "@id": "#category-\u30cf\u30a8"
      },
      "variableMeasured": [
        {
          "@id": "pv://b028004c-ffdc-4449-8330-ce1e21ad685c"
        }
      ]
    },
    {
      "@id": "pv://ad266378-7851-4667-a150-8cceeb67c623",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./Demo - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial-Properties - 92786b81/",
      "@type": "Dataset",
      "author": {
        "@id": "person://d5d9a96c536d1958169f370af86038105f487d26ebc8b280ec2132652c3ee89a?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=53",
      "genre": "experiment",
      "creativeWorkStatus": "Fail",
      "identifier": "20250916-92786b81ef6a1a5718f7f26c99bc4a7629eafd6f",
      "keywords": "generated from yml,synthesis,antimicrobial,chemistry",
      "text": "<h1>Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties</h1>\n<p>\nThe emergence of drug-resistant bacterial strains has become a major public health concern, highlighting the need for the development of new antimicrobial agents. In this study, we aimed to synthesize a novel organic compound with potential antimicrobial activity.\n</p>\n<h2>Experimental Design</h2>\n<p>\nThe compound was synthesized via a multi-step reaction scheme. The starting material, benzaldehyde, was reacted with aniline in the presence of an acid catalyst to form the intermediate product, N-phenylbenzamide. The intermediate product was then reacted with thionyl chloride to form the corresponding acid chloride. The acid chloride was then reacted with aminoguanidine in the presence of a base catalyst to form the final product, which was purified by recrystallization.\n</p>\n<h2>Characterization</h2>\n<p>\nThe synthesized compound was characterized using various spectroscopic techniques. The melting point of the compound was determined using a melting point apparatus and compared to the literature value. The IR spectrum of the compound was obtained using a Fourier transform infrared spectrometer and compared to the expected spectrum. The NMR spectrum of the compound was obtained using a nuclear magnetic resonance spectrometer and analyzed to confirm the structure of the compound.\n</p>\n<h2>Antimicrobial Activity</h2>\n<p>\nThe antimicrobial activity of the synthesized compound was evaluated against several bacterial strains using the disk diffusion method. The results showed that the compound exhibited significant antimicrobial activity against both Gram-positive and Gram-negative bacteria, suggesting its potential as a new antimicrobial agent.\n</p>\n",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://ad266378-7851-4667-a150-8cceeb67c623"
        }
      ],
      "aggregateRating": {
        "@id": "rating://5f578456-5a44-4e7c-be17-9a37a5efb02e",
        "@type": "AggregateRating",
        "ratingValue": 1,
        "reviewCount": 1
      }
    },
    {
      "@id": "#category-Cell biology",
      "@type": "Thing",
      "name": "Cell biology",
      "color": "A02D33"
    },
    {
      "@id": "pv://2b68c45b-2d41-4546-9292-30aecae78fea",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./Cell-biology - Transfection-of-p103D12-22-into-RPE-1-Actin-RFP - 7855b2e1/",
      "@type": "Dataset",
      "author": {
        "@id": "person://d5d9a96c536d1958169f370af86038105f487d26ebc8b280ec2132652c3ee89a?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "dateModified": "2025-09-16T10:32:54+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=51",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250916-7855b2e1be224262b958ef9acb13e3b95a3147ac",
      "keywords": "generated from yml,transfection,biocell,RPE-1",
      "text": "<h1>Goal</h1><p>Transfecting the plasmid p103\u039412-22 into the RPE-1 Actin-RFP cells and look at the death rate.</p>",
      "about": {
        "@id": "#category-Cell biology"
      },
      "variableMeasured": [
        {
          "@id": "pv://2b68c45b-2d41-4546-9292-30aecae78fea"
        }
      ]
    },
    {
      "@id": "comment://59ca77985ac5eb364f5cc41c48d8c7dc278ffccae5b82d213120f13171bc5bf7?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "text": "Oh, how fascinating. I'm sure the groundbreaking discovery that water is wet will change the course of human history forever.",
      "author": {
        "@id": "person://7299c4c87f75c05c1e9e61c91fd26328eb9b249f8fdceb1425a6a7dc5833ca09?hash_algo=sha256"
      }
    },
    {
      "@id": "comment://252b2078f3205342cc1bc59dfea7a828e66008da85e517672f3b9c9bc2cc3fb8?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-09-16T10:32:54+02:00",
      "text": "Well, it's a relief to see that the scientific community is hard at work discovering what we already suspected: that the sky is indeed blue. I can't wait for their next groundbreaking revelation that grass is green.",
      "author": {
        "@id": "person://7299c4c87f75c05c1e9e61c91fd26328eb9b249f8fdceb1425a6a7dc5833ca09?hash_algo=sha256"
      }
    },
    {
      "@id": "pv://847947e7-cdbe-476f-b500-01d44a829dd8",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{}"
    },
    {
      "@id": "./Demo - An-example-experiment - bf9a1a34/",
      "@type": "Dataset",
      "author": {
        "@id": "person://7299c4c87f75c05c1e9e61c91fd26328eb9b249f8fdceb1425a6a7dc5833ca09?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:53+02:00",
      "dateModified": "2025-09-16T10:32:53+02:00",
      "temporal": "2025-01-01T00:00:00+01:00",
      "name": "An example experiment",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=50",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://59ca77985ac5eb364f5cc41c48d8c7dc278ffccae5b82d213120f13171bc5bf7?hash_algo=sha256"
        },
        {
          "@id": "comment://252b2078f3205342cc1bc59dfea7a828e66008da85e517672f3b9c9bc2cc3fb8?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "identifier": "20250916-bf9a1a34eed57f3ace21f6fe32cd6c149eafcd8c",
      "keywords": "generated from yml,example,demo",
      "text": "This is the content of the experiment",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://847947e7-cdbe-476f-b500-01d44a829dd8"
        }
      ]
    },
    {
      "@id": "pv://03ccef4f-bbdd-4de7-a6d0-4f8b18807280",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"elabftw\": {\"display_main_text\": false, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group with id 1, first position\"}, {\"id\": 2, \"name\": \"Group with id 2, second position\"}, {\"id\": 3, \"name\": \"Group with id 3, third position\"}]}, \"extra_fields\": {\"Has group_id 3 as number\": {\"type\": \"text\", \"value\": \"\", \"group_id\": 3}, \"Has group_id 3 as string\": {\"type\": \"text\", \"value\": \"\", \"group_id\": \"3\"}, \"Has no group_id property\": {\"type\": \"text\", \"value\": \"\"}, \"Group_id 1 and position 1\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 1, \"position\": 1, \"description\": \"This is a checkbox custom input\"}, \"Group_id 2 and position 1\": {\"type\": \"url\", \"value\": \"\", \"group_id\": 2, \"position\": 1}, \"Group_id 2 and position 2\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\", \"group_id\": 2, \"position\": 2}, \"Group_id 2 and position 3\": {\"type\": \"url\", \"value\": \"\", \"group_id\": 2, \"position\": 3}, \"Another one without group_id property\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"this element has no group property defined\"}, \"Has group_id that is not in elabftw.groups\": {\"type\": \"text\", \"value\": \"I am lost!\", \"group_id\": \"19\"}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://8b0e9509-c33d-40d4-aac6-3f0e8a6378f4",
      "propertyID": "Has group_id 3 as number",
      "valueReference": "text",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://4703bf4b-f4dd-4dd5-92ef-6b61fb38619e",
      "propertyID": "Has group_id 3 as string",
      "valueReference": "text",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://0a7753ca-07a4-4da4-966e-8b437bf2c984",
      "propertyID": "Has no group_id property",
      "valueReference": "text",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://6f9b8f05-175e-44a7-81d0-bd179f468b25",
      "propertyID": "Group_id 1 and position 1",
      "valueReference": "checkbox",
      "value": "",
      "description": "This is a checkbox custom input"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://70c4f417-ef37-4fe1-9ec0-f930864c6458",
      "propertyID": "Group_id 2 and position 1",
      "valueReference": "url",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://564d05a3-1284-4b18-9d23-8d2237bc17f6",
      "propertyID": "Group_id 2 and position 2",
      "valueReference": "url",
      "value": "https://datalake.example.com/experiments/3921"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://e31610a5-f990-44f2-84c7-d3d7c4aa9dab",
      "propertyID": "Group_id 2 and position 3",
      "valueReference": "url",
      "value": ""
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://920249f6-fdfe-41f9-849e-ceaf27e7556c",
      "propertyID": "Another one without group_id property",
      "valueReference": "select",
      "value": "Some choice",
      "description": "this element has no group property defined"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://0303af80-053a-41ff-895c-f93e1be6bdcb",
      "propertyID": "Has group_id that is not in elabftw.groups",
      "valueReference": "text",
      "value": "I am lost!"
    },
    {
      "@id": "./Demo - Test-the-grouped-extra-fields - a9ca1362/",
      "@type": "Dataset",
      "author": {
        "@id": "person://8f5ab7f6890c9999cf1ba3890ad36f6c1c6908743bddd38a58c76426d61a648c?hash_algo=sha256"
      },
      "dateCreated": "2025-09-16T10:32:53+02:00",
      "dateModified": "2025-09-16T10:32:53+02:00",
      "temporal": "2024-12-31T00:00:00+01:00",
      "name": "Test the grouped extra fields",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=49",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250916-a9ca1362117bbef62dbd4144fc38f280075ee32e",
      "keywords": "generated from yml,dev,extra fields",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://03ccef4f-bbdd-4de7-a6d0-4f8b18807280"
        },
        {
          "@id": "pv://8b0e9509-c33d-40d4-aac6-3f0e8a6378f4"
        },
        {
          "@id": "pv://4703bf4b-f4dd-4dd5-92ef-6b61fb38619e"
        },
        {
          "@id": "pv://0a7753ca-07a4-4da4-966e-8b437bf2c984"
        },
        {
          "@id": "pv://6f9b8f05-175e-44a7-81d0-bd179f468b25"
        },
        {
          "@id": "pv://70c4f417-ef37-4fe1-9ec0-f930864c6458"
        },
        {
          "@id": "pv://564d05a3-1284-4b18-9d23-8d2237bc17f6"
        },
        {
          "@id": "pv://e31610a5-f990-44f2-84c7-d3d7c4aa9dab"
        },
        {
          "@id": "pv://920249f6-fdfe-41f9-849e-ceaf27e7556c"
        },
        {
          "@id": "pv://0303af80-053a-41ff-895c-f93e1be6bdcb"
        }
      ]
    },
    {
      "@id": "./",
      "identifier": "a283b96f-06ef-4305-a2fb-b9e175e0f8dd",
      "@type": "Dataset",
      "datePublished": "2025-09-16T10:37:31+02:00",
      "hasPart": [
        {
          "@id": "./Demo - Gold-master-experiment - 4af4da4e/"
        },
        {
          "@id": "./Molecular-biology - Facilis-illum-sed-reprehenderit - a7658b02/"
        },
        {
          "@id": "./Synthesis - Synthesis-of-Aspirin - 076f68c6/"
        },
        {
          "@id": "./Microscope - Video-microscope-Bravo - 6bf0e813/"
        },
        {
          "@id": "./Demo - Testing-the-eLabFTW-lab-notebook - 4192afd2/"
        },
        {
          "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - 321efb16/"
        },
        {
          "@id": "./Enzymo - Effect-of-temperature-on-enzyme-activity - 96ce1b12/"
        },
        {
          "@id": "./ -  - bb8b469d/"
        },
        {
          "@id": "./Demo - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial-Properties - 92786b81/"
        },
        {
          "@id": "./Cell-biology - Transfection-of-p103D12-22-into-RPE-1-Actin-RFP - 7855b2e1/"
        },
        {
          "@id": "./Demo - An-example-experiment - bf9a1a34/"
        },
        {
          "@id": "./Demo - Test-the-grouped-extra-fields - a9ca1362/"
        }
      ],
      "name": "eLabFTW export",
      "description": "This is a .eln export from eLabFTW",
      "version": "104",
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
      }
    },
    {
      "@id": "person://f6084a2b68f4c7e039aebf7d53fe634a7a74e30a5a48e4623d222775c61b9921?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Nicola",
      "familyName": "Mohr",
      "email": "somesamluser@example.com"
    },
    {
      "@id": "person://8f5ab7f6890c9999cf1ba3890ad36f6c1c6908743bddd38a58c76426d61a648c?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Avis",
      "familyName": "Gutkowski",
      "email": "user1@demo.elabftw.net"
    },
    {
      "@id": "person://9d870f42291406588b2f8876eefe7dd5f9ab41593809a7fc1b2e737149dfaa91?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Jevon",
      "familyName": "Conroy",
      "email": "dolores-17378653@yopmail.com"
    },
    {
      "@id": "person://fab8c19cc817cbd5361ff4dd62ce16cad61192bfb42bf06919cee96e0f238818?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Lee",
      "familyName": "Schoen",
      "email": "voluptas-45963321@yopmail.com"
    },
    {
      "@id": "person://d5d9a96c536d1958169f370af86038105f487d26ebc8b280ec2132652c3ee89a?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Jaquelin",
      "familyName": "Leffler",
      "email": "nobis-60442517@yopmail.com"
    },
    {
      "@id": "person://7299c4c87f75c05c1e9e61c91fd26328eb9b249f8fdceb1425a6a7dc5833ca09?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Neva",
      "familyName": "Heaney",
      "email": "maiores-78008163@yopmail.com"
    }
  ]
}
```
