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
      "dateCreated": "2026-11-09T10:35:32+01:00",
      "sdPublisher": {
        "@id": "#publisher"
      }
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
      "memberOf": [],
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
      "endTime": "2026-11-09T10:35:32+01:00",
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
      "version": "dev",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "#compound-2",
      "@type": "MolecularEntity",
      "name": "Aspirin",
      "molecularFormula": "C9H8O4",
      "inChI": "InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)",
      "inChIKey": "BSYNRYMUTXBXSQ-UHFFFAOYSA-N",
      "iupacName": "2-acetyloxybenzoic acid",
      "molecularWeight": "180.16",
      "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
      "identifier": [
        {
          "@type": "PropertyValue",
          "propertyID": "CAS Registry Number",
          "value": "50-78-2"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "PubChem CID",
          "value": 2244,
          "sameAs": "https://pubchem.ncbi.nlm.nih.gov/#query=2244"
        }
      ]
    },
    {
      "@id": "./aab966c4-0d20-4057-aa2d-30959b42f548/dc70935f-63c3-48d1-8653-363548463369",
      "@type": "File",
      "name": "pasted-image-20261109-103223-acf08ecf.png",
      "alternateName": "a7/a7336228-3ffd-4bdd-8044-eb430687964a.png",
      "creativeWorkStatus": "Normal",
      "encodingFormat": "application/octet-stream",
      "contentSize": "1947674",
      "sha256": "e08ec8a9bfe24ace1c98802bdc5a024def7b00a6ca48652988aa1a92fd59fb14",
      "position": 0
    },
    {
      "@id": "./88adebb3-4411-40b6-acbb-65cca84e586a/50ea5fea-a15c-464e-9178-bc5250a0bdf7",
      "@type": "File",
      "name": "example.pdf",
      "alternateName": "cf/cf14d8ab-3ab4-46e3-a72d-fd40ea06253b.pdf",
      "creativeWorkStatus": "Normal",
      "encodingFormat": "application/octet-stream",
      "contentSize": "116369",
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1",
      "position": 0
    },
    {
      "@id": "#category-Antibody",
      "@type": "Thing",
      "name": "Antibody",
      "color": "aaaabd"
    },
    {
      "@id": "./88adebb3-4411-40b6-acbb-65cca84e586a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://b6e08eac1fa1bdc4bdb04615a095ed061036beb0b547cee3bf7308f3a4bcf319?hash_algo=sha256"
      },
      "dateCreated": "2026-11-06T18:07:57+01:00",
      "dateModified": "2026-11-09T10:34:46+01:00",
      "temporal": "2026-08-06T00:00:00+02:00",
      "name": "Anti-GFP antibody",
      "encodingFormat": "text/html",
      "url": "https://elab.localhost:3148/database.php?mode=view&id=22",
      "genre": "resource",
      "conditionsOfAccess": "Unlocked",
      "subjectOf": [
        {
          "@id": "updateaction://c278e958-6a7a-4b1e-8ef9-9e1384f49749",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "uploads",
          "result": "Added upload \"example.pdf\" with id: 93",
          "startTime": "2026-11-09T10:34:46+01:00"
        },
        {
          "@id": "updateaction://32fff39e-2754-47a9-9db9-87a1f9c1d817",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://b6e08eac1fa1bdc4bdb04615a095ed061036beb0b547cee3bf7308f3a4bcf319?hash_algo=sha256"
          },
          "object": "created",
          "result": "Resource was created",
          "startTime": "2026-11-06T18:07:57+01:00"
        },
        {
          "@id": "updateaction://4b122750-e906-4965-b05f-f55872017fa2",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://b6e08eac1fa1bdc4bdb04615a095ed061036beb0b547cee3bf7308f3a4bcf319?hash_algo=sha256"
          },
          "object": "is_bookable",
          "result": "1",
          "startTime": "2026-11-06T18:07:57+01:00"
        }
      ],
      "status": "Normal",
      "hasPart": [
        {
          "@id": "./88adebb3-4411-40b6-acbb-65cca84e586a/50ea5fea-a15c-464e-9178-bc5250a0bdf7"
        }
      ],
      "identifier": "20261106-36475f39bb0a3a0851e9de67d61e9fbbd1e7533a",
      "about": {
        "@id": "#category-Antibody"
      }
    },
    {
      "@id": "#category-Biology",
      "@type": "Thing",
      "name": "Biology",
      "color": "a5ab35"
    },
    {
      "@id": "pv://e3cbd30a-fa8d-4758-81e8-22d320b935b2",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"extra_fields\": {\"Email input\": {\"type\": \"email\", \"value\": \"hello@example.com\", \"description\": \"only accepts emails\"}, \"Text custom field\": {\"type\": \"text\", \"value\": \"The value\", \"required\": true, \"description\": \"Description of the field\", \"blank_value_on_duplicate\": true}, \"Multi value custom field\": {\"type\": \"text\", \"value\": [\"First value\", \"Second value\"], \"value_labels\": [\"Label of first value\", \"Second label\"], \"allow_multi_values\": true}}}"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://11183de6-129d-4625-81e6-c2d0ef114db7",
      "propertyID": "Email input",
      "valueReference": "email",
      "value": "hello@example.com",
      "description": "only accepts emails"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://efa31003-18b4-47b9-a4fe-b12e24ca5509",
      "propertyID": "Text custom field",
      "valueReference": "text",
      "value": "The value",
      "description": "Description of the field"
    },
    {
      "@type": "PropertyValue",
      "@id": "pv://d3aec9a4-e542-4fe4-b69c-9d5d44f147cb",
      "propertyID": "Multi value custom field",
      "valueReference": "text",
      "value": [
        "First value",
        "Second value"
      ]
    },
    {
      "@id": "howtostep://79ec59ef-ef2a-40ac-bf13-2fdb7445837e",
      "@type": "HowToStep",
      "position": 0,
      "creativeWorkStatus": "finished",
      "temporal": "2026-11-09T10:34:19+01:00",
      "itemListElement": {
        "@id": "howtodirection://f2cb15de-4b0c-4ff3-b439-96a119e51689"
      }
    },
    {
      "@id": "howtodirection://f2cb15de-4b0c-4ff3-b439-96a119e51689",
      "@type": "HowToDirection",
      "text": "First step"
    },
    {
      "@id": "howtostep://f2276a4f-9e6a-4b87-b884-bae34dd6fd88",
      "@type": "HowToStep",
      "position": 1,
      "creativeWorkStatus": "finished",
      "temporal": "2026-11-09T10:34:20+01:00",
      "itemListElement": {
        "@id": "howtodirection://53be50b6-994d-412e-899e-99d94976c343"
      }
    },
    {
      "@id": "howtodirection://53be50b6-994d-412e-899e-99d94976c343",
      "@type": "HowToDirection",
      "text": "Second step"
    },
    {
      "@id": "howtostep://4b779624-89de-4455-8d18-e5581677ae63",
      "@type": "HowToStep",
      "position": 2,
      "creativeWorkStatus": "unfinished",
      "itemListElement": {
        "@id": "howtodirection://0077aec4-ab59-4d80-b4cf-6adb7e3914f7"
      }
    },
    {
      "@id": "howtodirection://0077aec4-ab59-4d80-b4cf-6adb7e3914f7",
      "@type": "HowToDirection",
      "text": "Another step"
    },
    {
      "@id": "./aab966c4-0d20-4057-aa2d-30959b42f548/",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "dateCreated": "2026-11-09T10:29:43+01:00",
      "dateModified": "2026-11-09T10:35:19+01:00",
      "temporal": "2026-11-09T00:00:00+01:00",
      "name": "An experiment title",
      "encodingFormat": "text/html",
      "url": "https://elab.localhost:3148/experiments.php?mode=view&id=223",
      "genre": "experiment",
      "alternateName": 123,
      "compounds_links": [
        {
          "@id": "#compound-2"
        }
      ],
      "conditionsOfAccess": "Unlocked",
      "creativeWorkStatus": "Success",
      "subjectOf": [
        {
          "@id": "updateaction://a900af11-0d6a-48e4-9fdb-42983cfb13b9",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "container_created",
          "result": "Added container with 1.00 \u2022 at \"Hospital > 4th floor\" (container #21)",
          "startTime": "2026-11-09T10:35:19+01:00"
        },
        {
          "@id": "updateaction://1fe84752-bcd1-46f7-bda0-97581cc7b81a",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "compounds",
          "result": "Added link to compound: Aspirin (CAS Number: 50-78-2) with id: 2",
          "startTime": "2026-11-09T10:35:11+01:00"
        },
        {
          "@id": "updateaction://f131cfe7-b514-4ae4-a168-df7310b38b16",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "links",
          "result": "Added link to resource: <a href=\"/database.php?mode=view&amp;id=22\">Anti-GFP antibody</a>",
          "startTime": "2026-11-09T10:34:28+01:00"
        },
        {
          "@id": "updateaction://47159565-0993-4474-a1b3-23b27ed0731f",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Finished step with id: 66",
          "startTime": "2026-11-09T10:34:20+01:00"
        },
        {
          "@id": "updateaction://372c37cb-d059-4d4d-afa4-dd54f04ea347",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Finished step with id: 65",
          "startTime": "2026-11-09T10:34:19+01:00"
        },
        {
          "@id": "updateaction://d9800d7a-798c-4464-9b02-d3021c335521",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Created step with id: 67",
          "startTime": "2026-11-09T10:34:17+01:00"
        },
        {
          "@id": "updateaction://df6159d9-53db-47df-a061-7e769900b4be",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Created step with id: 66",
          "startTime": "2026-11-09T10:34:15+01:00"
        },
        {
          "@id": "updateaction://84816a66-80ce-4384-82b4-f4a70c4bdbcb",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Created step with id: 65",
          "startTime": "2026-11-09T10:34:12+01:00"
        },
        {
          "@id": "updateaction://da2a01e5-1aea-4c0b-9eb4-a9bee54adaec",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Email input",
          "result": "hello@example.com",
          "startTime": "2026-11-09T10:33:53+01:00"
        },
        {
          "@id": "updateaction://c1e04fca-e744-4807-b952-9412062c396d",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata",
          "result": "{\"extra_fields\":{\"Text custom field\":{\"type\":\"text\",\"value\":\"The value\",\"required\":true,\"description\":\"Description of the field\",\"blank_value_on_duplicate\":true},\"Multi value custom field\":{\"type\":\"text\",\"value\":[\"First value\",\"Second value\"],\"value_labels\":[\"Label of first value\",\"Second label\"],\"allow_multi_values\":true},\"Email input\":{\"type\":\"email\",\"value\":\"\",\"description\":\"only accepts emails\"}}}",
          "startTime": "2026-11-09T10:33:47+01:00"
        },
        {
          "@id": "updateaction://1f03c803-7fb2-4515-9bf4-f5d361b29943",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "First value, Second value",
          "startTime": "2026-11-09T10:33:34+01:00"
        },
        {
          "@id": "updateaction://f9895d2e-bc29-4212-b848-63fea040eb37",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "First value, ",
          "startTime": "2026-11-09T10:33:29+01:00"
        },
        {
          "@id": "updateaction://7d722e08-4a16-447c-bd89-793cbda51421",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "First value",
          "startTime": "2026-11-09T10:33:26+01:00"
        },
        {
          "@id": "updateaction://f9329289-0cc4-4492-b54a-b267172ad181",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "",
          "startTime": "2026-11-09T10:33:15+01:00"
        },
        {
          "@id": "updateaction://89c84064-b9b1-4d17-b76a-bfe1c76916e6",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata",
          "result": "{\"extra_fields\":{\"Text custom field\":{\"type\":\"text\",\"value\":\"The value\",\"required\":true,\"description\":\"Description of the field\",\"blank_value_on_duplicate\":true},\"Multi value custom field\":{\"type\":\"text\",\"value\":[\"\"],\"allow_multi_values\":true}}}",
          "startTime": "2026-11-09T10:33:06+01:00"
        },
        {
          "@id": "updateaction://cfed65ba-7d3d-43c2-b83d-3b14be054300",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata",
          "result": "{\"extra_fields\":{\"Text custom field\":{\"type\":\"text\",\"value\":\"The value\",\"description\":\"Description of the field\",\"blank_value_on_duplicate\":true,\"required\":true}}}",
          "startTime": "2026-11-09T10:32:54+01:00"
        },
        {
          "@id": "updateaction://e690fc41-5446-4235-86e7-79594aece800",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:32:35+01:00"
        },
        {
          "@id": "updateaction://da682b12-a0b2-4790-8b88-51885433dfca",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:32:23+01:00"
        },
        {
          "@id": "updateaction://eddaffda-f2d8-42b4-9e8b-16ec60b4f0f8",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "uploads",
          "result": "Added upload \"pasted-image-20261109-103223-acf08ecf.png\" with id: 92",
          "startTime": "2026-11-09T10:32:23+01:00"
        },
        {
          "@id": "updateaction://07f6bcd1-318d-4b25-9598-cd85f81e603e",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:32:14+01:00"
        },
        {
          "@id": "updateaction://a5c4c674-7b29-41a8-bdc8-378ad5a0377b",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:31:28+01:00"
        },
        {
          "@id": "updateaction://a3dd2da4-6358-4dc0-a10b-c4fe47fb8c47",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:30:28+01:00"
        },
        {
          "@id": "updateaction://e9d06c6d-8456-4f2b-8956-bcab3b546520",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "custom_id",
          "result": "123",
          "startTime": "2026-11-09T10:30:13+01:00"
        },
        {
          "@id": "updateaction://17acd763-dcde-4381-bd44-e3672fa97cce",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "rating",
          "result": "5",
          "startTime": "2026-11-09T10:30:07+01:00"
        },
        {
          "@id": "updateaction://f04ed9f6-e77c-4476-86fc-bc5d9f4253dc",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "status",
          "result": "2",
          "startTime": "2026-11-09T10:30:04+01:00"
        },
        {
          "@id": "updateaction://a9488ae2-b1c6-4333-8e72-cd182000cc3d",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "category",
          "result": "4",
          "startTime": "2026-11-09T10:30:02+01:00"
        },
        {
          "@id": "updateaction://2aef2547-db07-487c-8b96-f7535cbaceea",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "tags",
          "result": "Added tag \"tag2\" with id: 1426",
          "startTime": "2026-11-09T10:29:53+01:00"
        },
        {
          "@id": "updateaction://c00cd66f-1183-43bd-b428-2dfd17ed34a3",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "tags",
          "result": "Added tag \"tag1\" with id: 1425",
          "startTime": "2026-11-09T10:29:51+01:00"
        },
        {
          "@id": "updateaction://505f2169-e69d-4d1c-a14c-220d0dde372d",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "created",
          "result": "Experiment was created",
          "startTime": "2026-11-09T10:29:44+01:00"
        }
      ],
      "status": "Normal",
      "hasPart": [
        {
          "@id": "./aab966c4-0d20-4057-aa2d-30959b42f548/dc70935f-63c3-48d1-8653-363548463369"
        }
      ],
      "identifier": "20261109-62025cc4886281b363b4faef05742ad24f9ebe5d",
      "keywords": "tag1,tag2",
      "mentions": [
        {
          "@id": "./88adebb3-4411-40b6-acbb-65cca84e586a/"
        }
      ],
      "text": "<p style=\"line-height:1;\">This is the main text. It's <strong>HTML</strong>.</p>\n<ul>\n<li style=\"line-height:1;\">a list</li>\n<li style=\"line-height:1;\">another item on the list</li>\n<li style=\"line-height:1;\">third one</li>\n</ul>\n<p style=\"line-height:1;\">\u00a0</p>\n<p style=\"line-height:1;\">Now a table:</p>\n<table style=\"min-width:25%;\" border=\"1\">\n\n<tr>\n<td>Sample</td>\n<td>Concentration (\u03bcg/\u03bcL)</td>\n<td>Size (nm)</td>\n<td>Comment</td>\n</tr>\n<tr>\n<td>1</td>\n<td>30</td>\n<td>12</td>\n<td>-</td>\n</tr>\n<tr>\n<td>2</td>\n<td><span style=\"color:rgb(224,62,45);\">20</span></td>\n<td><span style=\"background-color:rgb(251,238,184);\">24</span></td>\n<td>-</td>\n</tr>\n\n</table>\n<p>And an image in the text:</p>\n<p><img src=\"app/download.php?f=a7/a7336228-3ffd-4bdd-8044-eb430687964a.png&amp;storage=1\" width=\"413\" height=\"413\" alt=\"a7336228-3ffd-4bdd-8044-eb430687964a.png&amp;storage=1\"></p>\n<p>\u00a0</p>",
      "about": {
        "@id": "#category-Biology"
      },
      "variableMeasured": [
        {
          "@id": "pv://e3cbd30a-fa8d-4758-81e8-22d320b935b2"
        },
        {
          "@id": "pv://11183de6-129d-4625-81e6-c2d0ef114db7"
        },
        {
          "@id": "pv://efa31003-18b4-47b9-a4fe-b12e24ca5509"
        },
        {
          "@id": "pv://d3aec9a4-e542-4fe4-b69c-9d5d44f147cb"
        }
      ],
      "aggregateRating": {
        "@id": "rating://b3fd5dbc-80d6-486e-8b9a-8a2f27f4e721",
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      },
      "step": [
        {
          "@id": "howtostep://79ec59ef-ef2a-40ac-bf13-2fdb7445837e"
        },
        {
          "@id": "howtostep://f2276a4f-9e6a-4b87-b884-bae34dd6fd88"
        },
        {
          "@id": "howtostep://4b779624-89de-4455-8d18-e5581677ae63"
        }
      ]
    },
    {
      "@id": "./",
      "identifier": "47c2fb74-c19c-4d30-a8ba-fc5ab3657c49",
      "conformsTo": {
        "@id": "https://purl.org/elnconsortium/eln-spec/1.2+20260923"
      },
      "@type": "Dataset",
      "datePublished": "2026-11-09T10:35:32+01:00",
      "hasPart": [
        {
          "@id": "./aab966c4-0d20-4057-aa2d-30959b42f548/"
        },
        {
          "@id": "./88adebb3-4411-40b6-acbb-65cca84e586a/"
        }
      ],
      "name": "eLabFTW export",
      "description": "This is a .eln export from eLabFTW",
      "version": "108",
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
      }
    },
    {
      "@id": "person://b6e08eac1fa1bdc4bdb04615a095ed061036beb0b547cee3bf7308f3a4bcf319?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Lucinda",
      "familyName": "White",
      "email": "mollitia-29138117@yopmail.com",
      "affiliation": []
    },
    {
      "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Toto",
      "familyName": "Le sysadmin",
      "email": "toto@yopmail.com",
      "affiliation": []
    }
  ]
}
```
