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
      "dateCreated": "2026-11-09T12:57:42+01:00",
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
      "endTime": "2026-11-09T12:57:42+01:00",
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
      "@id": "./3fbcedee-3618-49fc-bd29-916e494778fb/2477189f-a423-4d6e-bd3e-50738e18ff46",
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
      "@id": "./92eec27d-99b3-47a6-b493-54a3f53a1508/2fcff7b8-64e1-411a-bb3a-79c1b608b554",
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
      "@id": "./92eec27d-99b3-47a6-b493-54a3f53a1508/",
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
          "@id": "updateaction://240f49a5-96c3-49f6-af75-301d65eda7f5",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "uploads",
          "result": "Added upload \"example.pdf\" with id: 93",
          "startTime": "2026-11-09T10:34:46+01:00"
        },
        {
          "@id": "updateaction://596aecad-3856-43ee-b68c-7cdb2c41b155",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://b6e08eac1fa1bdc4bdb04615a095ed061036beb0b547cee3bf7308f3a4bcf319?hash_algo=sha256"
          },
          "object": "created",
          "result": "Resource was created",
          "startTime": "2026-11-06T18:07:57+01:00"
        },
        {
          "@id": "updateaction://33a9c0da-4c03-4394-912e-316f7b0d8299",
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
          "@id": "./92eec27d-99b3-47a6-b493-54a3f53a1508/2fcff7b8-64e1-411a-bb3a-79c1b608b554"
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
      "@id": "pv://28555b81-0cad-430e-b761-1c8a72e2e4fa",
      "@type": "PropertyValue",
      "propertyID": "elabftw_metadata",
      "description": "eLabFTW metadata JSON as string",
      "value": "{\"extra_fields\": {\"Email input\": {\"type\": \"email\", \"value\": \"hello@example.com\", \"description\": \"only accepts emails\"}, \"Text custom field\": {\"type\": \"text\", \"value\": \"The value\", \"required\": true, \"description\": \"Description of the field\", \"blank_value_on_duplicate\": true}, \"Multi value custom field\": {\"type\": \"text\", \"value\": [\"First value\", \"Second value\"], \"value_labels\": [\"Label of first value\", \"Second label\"], \"allow_multi_values\": true}}}"
    },
    {
      "@id": "pv://a67505f2-f150-4b8f-a477-ab14e14321d7",
      "@type": "PropertyValue",
      "propertyID": "Email input",
      "name": "Email input",
      "value": "hello@example.com",
      "additionalType": "email",
      "description": "only accepts emails"
    },
    {
      "@id": "pv://3f8350ec-0b8c-47be-8485-2e3e5953860f",
      "@type": "PropertyValue",
      "propertyID": "Text custom field",
      "name": "Text custom field",
      "value": "The value",
      "additionalType": "text",
      "description": "Description of the field"
    },
    {
      "@id": "pv://21989d0f-fe08-4339-93d4-b525a9fec359",
      "@type": "PropertyValue",
      "propertyID": "Multi value custom field.0",
      "name": "Multi value custom field",
      "value": "First value",
      "additionalType": "text",
      "alternateName": "Label of first value"
    },
    {
      "@id": "pv://43baedeb-92e7-455c-91d4-9d03411a1f6c",
      "@type": "PropertyValue",
      "propertyID": "Multi value custom field.1",
      "name": "Multi value custom field",
      "value": "Second value",
      "additionalType": "text",
      "alternateName": "Second label"
    },
    {
      "@id": "howtostep://77800afe-b41f-4202-b1ef-ef5fc8624b7f",
      "@type": "HowToStep",
      "position": 0,
      "creativeWorkStatus": "finished",
      "temporal": "2026-11-09T10:34:19+01:00",
      "itemListElement": {
        "@id": "howtodirection://c78a4136-d33d-4148-8bad-d872258f57cf"
      }
    },
    {
      "@id": "howtodirection://c78a4136-d33d-4148-8bad-d872258f57cf",
      "@type": "HowToDirection",
      "text": "First step"
    },
    {
      "@id": "howtostep://5ebf4c00-a9c8-4c58-a34f-a6e4acb16a77",
      "@type": "HowToStep",
      "position": 1,
      "creativeWorkStatus": "finished",
      "temporal": "2026-11-09T10:34:20+01:00",
      "itemListElement": {
        "@id": "howtodirection://4d37f065-ca18-4219-81f3-b30b934b7afa"
      }
    },
    {
      "@id": "howtodirection://4d37f065-ca18-4219-81f3-b30b934b7afa",
      "@type": "HowToDirection",
      "text": "Second step"
    },
    {
      "@id": "howtostep://be37d040-31c5-4cfa-919a-5ed1eb2df604",
      "@type": "HowToStep",
      "position": 2,
      "creativeWorkStatus": "unfinished",
      "itemListElement": {
        "@id": "howtodirection://5c2e87ad-2c66-4c03-8102-3c32a8451812"
      }
    },
    {
      "@id": "howtodirection://5c2e87ad-2c66-4c03-8102-3c32a8451812",
      "@type": "HowToDirection",
      "text": "Another step"
    },
    {
      "@id": "./3fbcedee-3618-49fc-bd29-916e494778fb/",
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
          "@id": "updateaction://06067f80-d77a-41da-a7cc-30adc5fafd9b",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "container_created",
          "result": "Added container with 1.00 \u2022 at \"Hospital > 4th floor\" (container #21)",
          "startTime": "2026-11-09T10:35:19+01:00"
        },
        {
          "@id": "updateaction://94000cae-7e54-49d8-a5a4-c24720fbe52c",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "compounds",
          "result": "Added link to compound: Aspirin (CAS Number: 50-78-2) with id: 2",
          "startTime": "2026-11-09T10:35:11+01:00"
        },
        {
          "@id": "updateaction://9876b0e9-5673-413c-850c-9b7d0b01ca75",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "links",
          "result": "Added link to resource: <a href=\"/database.php?mode=view&amp;id=22\">Anti-GFP antibody</a>",
          "startTime": "2026-11-09T10:34:28+01:00"
        },
        {
          "@id": "updateaction://a7d9999f-da4b-4b2c-b550-767a2a3fa734",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Finished step with id: 66",
          "startTime": "2026-11-09T10:34:20+01:00"
        },
        {
          "@id": "updateaction://19613bbd-a8e9-4eb9-ba12-a7e1cde50557",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Finished step with id: 65",
          "startTime": "2026-11-09T10:34:19+01:00"
        },
        {
          "@id": "updateaction://4559c295-ce76-41fc-998a-55c2b1b481e6",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Created step with id: 67",
          "startTime": "2026-11-09T10:34:17+01:00"
        },
        {
          "@id": "updateaction://b8517cd9-85bb-4d03-a74d-ae885c645473",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Created step with id: 66",
          "startTime": "2026-11-09T10:34:15+01:00"
        },
        {
          "@id": "updateaction://3b4081b5-ba68-491d-8d29-198b7aa137f1",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "steps",
          "result": "Created step with id: 65",
          "startTime": "2026-11-09T10:34:12+01:00"
        },
        {
          "@id": "updateaction://9e4a4449-a57a-44f1-b488-4d8f40533634",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Email input",
          "result": "hello@example.com",
          "startTime": "2026-11-09T10:33:53+01:00"
        },
        {
          "@id": "updateaction://d41b22d6-d60c-4153-b4fb-14cf5a6182b6",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata",
          "result": "{\"extra_fields\":{\"Text custom field\":{\"type\":\"text\",\"value\":\"The value\",\"required\":true,\"description\":\"Description of the field\",\"blank_value_on_duplicate\":true},\"Multi value custom field\":{\"type\":\"text\",\"value\":[\"First value\",\"Second value\"],\"value_labels\":[\"Label of first value\",\"Second label\"],\"allow_multi_values\":true},\"Email input\":{\"type\":\"email\",\"value\":\"\",\"description\":\"only accepts emails\"}}}",
          "startTime": "2026-11-09T10:33:47+01:00"
        },
        {
          "@id": "updateaction://7c2fdeb7-34d0-4d94-b958-7530ac2cde94",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "First value, Second value",
          "startTime": "2026-11-09T10:33:34+01:00"
        },
        {
          "@id": "updateaction://49ea4278-11e8-431f-9280-b98c4fc7fa2d",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "First value, ",
          "startTime": "2026-11-09T10:33:29+01:00"
        },
        {
          "@id": "updateaction://ea8a9d43-1495-4149-b3f2-e4af248fd154",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "First value",
          "startTime": "2026-11-09T10:33:26+01:00"
        },
        {
          "@id": "updateaction://1a79f2b0-9261-40c9-a107-63d51747f55f",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata_Multi value custom field",
          "result": "",
          "startTime": "2026-11-09T10:33:15+01:00"
        },
        {
          "@id": "updateaction://b1f72fc8-b8bd-4deb-91d9-f8bff28eb190",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata",
          "result": "{\"extra_fields\":{\"Text custom field\":{\"type\":\"text\",\"value\":\"The value\",\"required\":true,\"description\":\"Description of the field\",\"blank_value_on_duplicate\":true},\"Multi value custom field\":{\"type\":\"text\",\"value\":[\"\"],\"allow_multi_values\":true}}}",
          "startTime": "2026-11-09T10:33:06+01:00"
        },
        {
          "@id": "updateaction://2db83ca3-13b8-4488-97de-b13dce934c8b",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "metadata",
          "result": "{\"extra_fields\":{\"Text custom field\":{\"type\":\"text\",\"value\":\"The value\",\"description\":\"Description of the field\",\"blank_value_on_duplicate\":true,\"required\":true}}}",
          "startTime": "2026-11-09T10:32:54+01:00"
        },
        {
          "@id": "updateaction://c30e3ae7-dfff-4108-89ea-cb8d324997b9",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:32:35+01:00"
        },
        {
          "@id": "updateaction://5ab35506-b4aa-4af4-899b-a8e08501daf6",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:32:23+01:00"
        },
        {
          "@id": "updateaction://9448d2f3-c38d-4a7c-a105-26335a945042",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "uploads",
          "result": "Added upload \"pasted-image-20261109-103223-acf08ecf.png\" with id: 92",
          "startTime": "2026-11-09T10:32:23+01:00"
        },
        {
          "@id": "updateaction://83c5cf3a-beff-4663-ba4d-853bfeaf1c3a",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:32:14+01:00"
        },
        {
          "@id": "updateaction://10afc32c-c1a2-4852-adb8-cdc73f3108e8",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:31:28+01:00"
        },
        {
          "@id": "updateaction://4cd5687b-d16c-4535-9a86-0f0781704e32",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "body",
          "result": "The change in the body is recorded in the revisions. <a href=\"revisions.php?type=experiments&amp;item_id=223\">See revisions page.</a>",
          "startTime": "2026-11-09T10:30:28+01:00"
        },
        {
          "@id": "updateaction://daa81e73-14cb-4bf9-89f0-e203d84ab562",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "custom_id",
          "result": "123",
          "startTime": "2026-11-09T10:30:13+01:00"
        },
        {
          "@id": "updateaction://65ca94b2-fc65-4a0b-8fe6-297a9fb94bc4",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "rating",
          "result": "5",
          "startTime": "2026-11-09T10:30:07+01:00"
        },
        {
          "@id": "updateaction://2aaed770-289c-410a-8b23-c6bde7befc8f",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "status",
          "result": "2",
          "startTime": "2026-11-09T10:30:04+01:00"
        },
        {
          "@id": "updateaction://86a01c59-1cb9-46a8-8632-0451268863ca",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "category",
          "result": "4",
          "startTime": "2026-11-09T10:30:02+01:00"
        },
        {
          "@id": "updateaction://548bed08-818d-47ba-bf19-d965311eadf9",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "tags",
          "result": "Added tag \"tag2\" with id: 1426",
          "startTime": "2026-11-09T10:29:53+01:00"
        },
        {
          "@id": "updateaction://ca48b923-e238-42c2-a55d-7d7a207e21a6",
          "@type": "UpdateAction",
          "agent": {
            "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
          },
          "object": "tags",
          "result": "Added tag \"tag1\" with id: 1425",
          "startTime": "2026-11-09T10:29:51+01:00"
        },
        {
          "@id": "updateaction://1c49a179-f044-4e56-bf44-c2e5ed447d24",
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
          "@id": "./3fbcedee-3618-49fc-bd29-916e494778fb/2477189f-a423-4d6e-bd3e-50738e18ff46"
        }
      ],
      "identifier": "20261109-62025cc4886281b363b4faef05742ad24f9ebe5d",
      "keywords": "tag1,tag2",
      "mentions": [
        {
          "@id": "./92eec27d-99b3-47a6-b493-54a3f53a1508/"
        }
      ],
      "text": "<p style=\"line-height:1;\">This is the main text. It's <strong>HTML</strong>.</p>\n<ul>\n<li style=\"line-height:1;\">a list</li>\n<li style=\"line-height:1;\">another item on the list</li>\n<li style=\"line-height:1;\">third one</li>\n</ul>\n<p style=\"line-height:1;\">\u00a0</p>\n<p style=\"line-height:1;\">Now a table:</p>\n<table style=\"min-width:25%;\" border=\"1\">\n\n<tr>\n<td>Sample</td>\n<td>Concentration (\u03bcg/\u03bcL)</td>\n<td>Size (nm)</td>\n<td>Comment</td>\n</tr>\n<tr>\n<td>1</td>\n<td>30</td>\n<td>12</td>\n<td>-</td>\n</tr>\n<tr>\n<td>2</td>\n<td><span style=\"color:rgb(224,62,45);\">20</span></td>\n<td><span style=\"background-color:rgb(251,238,184);\">24</span></td>\n<td>-</td>\n</tr>\n\n</table>\n<p>And an image in the text:</p>\n<p><img src=\"app/download.php?f=a7/a7336228-3ffd-4bdd-8044-eb430687964a.png&amp;storage=1\" width=\"413\" height=\"413\" alt=\"a7336228-3ffd-4bdd-8044-eb430687964a.png&amp;storage=1\"></p>\n<p>\u00a0</p>",
      "about": {
        "@id": "#category-Biology"
      },
      "variableMeasured": [
        {
          "@id": "pv://28555b81-0cad-430e-b761-1c8a72e2e4fa"
        },
        {
          "@id": "pv://a67505f2-f150-4b8f-a477-ab14e14321d7"
        },
        {
          "@id": "pv://3f8350ec-0b8c-47be-8485-2e3e5953860f"
        },
        {
          "@id": "pv://21989d0f-fe08-4339-93d4-b525a9fec359"
        },
        {
          "@id": "pv://43baedeb-92e7-455c-91d4-9d03411a1f6c"
        }
      ],
      "aggregateRating": {
        "@id": "rating://48f55135-c9da-4d21-9f48-9af1614a60c6",
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      },
      "step": [
        {
          "@id": "howtostep://77800afe-b41f-4202-b1ef-ef5fc8624b7f"
        },
        {
          "@id": "howtostep://5ebf4c00-a9c8-4c58-a34f-a6e4acb16a77"
        },
        {
          "@id": "howtostep://be37d040-31c5-4cfa-919a-5ed1eb2df604"
        }
      ]
    },
    {
      "@id": "./",
      "identifier": "8a678efe-88ff-4bff-8ab2-c340cf405030",
      "conformsTo": {
        "@id": "https://purl.org/elnconsortium/eln-spec/1.2+20260923"
      },
      "@type": "Dataset",
      "datePublished": "2026-11-09T12:57:43+01:00",
      "hasPart": [
        {
          "@id": "./3fbcedee-3618-49fc-bd29-916e494778fb/"
        },
        {
          "@id": "./92eec27d-99b3-47a6-b493-54a3f53a1508/"
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
