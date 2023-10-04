# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

## Concepts used

A file `elabftw-export.json` is created during export and added to the archive, it corresponds to the JSON export on the entry by eLabFTW and might contain fields that are not present in the metadata file because too specific to eLabFTW.

Here is a correspondance between concepts in eLabFTW and how they are translated in the metadata json file in the archive:

| eLabFTW concepts    | JSON property          |
|---------------------|------------------------|
| tags                | keywords               |
| links               | mentions               |
| comments            | comment                |
| steps               | in elabftw-export.json |
| elabid              | identifier             |
| title               | name                   |
| body (main content) | text                   |


### multiple-resource.eln
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
      "dateCreated": "2023-10-02T15:53:13+02:00",
      "sdPublisher": {
        "@type": "Organization",
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
      "version": "1.0"
    },
    {
      "@id": "./Antibody - Anti-CD11b - 5cd9891c/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1617",
      "sha256": "1fedbc1a4c363a381dae3156dff18f475311831fc866d718ff32520deae88683"
    },
    {
      "@id": "./Antibody - Anti-CD11b - 5cd9891c",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:45:03+02:00",
      "dateModified": "2023-09-28T03:45:03+02:00",
      "identifier": "20230928-5cd9891c47f4cb255996247332f69cf66150c7a0",
      "comment": [],
      "keywords": [],
      "name": "Anti-CD11b",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=175",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-CD11b - 5cd9891c/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Antibody - Anti-BrdU - f9f2a14d/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1926",
      "sha256": "7de0c67e1b915328ee750a11dafee14c08162b249f1ff82daa9fdbc0348f2237"
    },
    {
      "@id": "./Antibody - Anti-BrdU - f9f2a14d",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:45:02+02:00",
      "dateModified": "2023-09-28T03:45:02+02:00",
      "identifier": "20230928-f9f2a14d29c2126aa1f960a89d56621f50aaaaa6",
      "comment": [],
      "keywords": [],
      "name": "Anti-BrdU",
      "text": "<p>This antibody targets the BrdU molecule and is commonly used to detect DNA replication in cells. It was raised in mouse and has an isotype of IgG1.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=170",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-BrdU - f9f2a14d/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Antibody - Anti-CD3\u03b5 - 955880c1/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "2324",
      "sha256": "1796e1c651be2deb2d3c699d4f47a7f78aacd29cf370ad9a83f260286fd08e40"
    },
    {
      "@id": "./Antibody - Anti-CD3\u03b5 - 955880c1",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:45:02+02:00",
      "dateModified": "2023-09-28T03:45:02+02:00",
      "identifier": "20230928-955880c1bc0d876fd140602f91bb47874e93b845",
      "comment": [],
      "keywords": [],
      "name": "Anti-CD3\u03b5",
      "text": "<p>Anti-CD3\u03b5 is a polyclonal rabbit antibody used to detect the CD3\u03b5 subunit of the T-cell receptor complex. The antibody can be used in various immunological applications such as Western blotting, immunoprecipitation, and immunofluorescence. This antibody was generated by immunizing rabbits with purified recombinant CD3\u03b5 protein.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=167",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-CD3\u03b5 - 955880c1/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Antibody - Anti-CD11b - 5cd9891c"
        },
        {
          "@id": "./Antibody - Anti-BrdU - f9f2a14d"
        },
        {
          "@id": "./Antibody - Anti-CD3\u03b5 - 955880c1"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### experiment-template.eln
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
      "dateCreated": "2023-07-31T14:27:35+02:00",
      "sdPublisher": {
        "@type": "Organization",
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
      "version": "1.0"
    },
    {
      "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1720",
      "sha256": "ed15e7b86e4112eb95665725ea29387722fda9110524795b15b97f42b5b339b4"
    },
    {
      "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-31T13:23:43+02:00",
      "dateModified": "2023-07-31T13:27:26+02:00",
      "identifier": "",
      "comment": [],
      "keywords": [
        "microscopy",
        "example"
      ],
      "name": "This is an experiment template",
      "text": "<p>Experiment templates are used to speed up the creation of experiments. They are very similar to experiments or items but do not contain attached files.</p>",
      "url": "https://elab.local:3148/.php?mode=view&id=13",
      "hasPart": [
        {
          "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f/export-elabftw.json"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=163",
          "@type": "Dataset",
          "name": "Plasmid - pRSF-Duet-1",
          "identifier": "20230729-81ed0cc30bf8d243df5753bee7324308864c68e9"
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
          "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### single-experiment.eln
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
      "dateCreated": "2023-10-02T15:52:01+02:00",
      "sdPublisher": {
        "@type": "Organization",
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
      "version": "1.0"
    },
    {
      "@id": "https://elab.local:3148/database.php?mode=view&id=51",
      "@type": "Dataset",
      "name": " - Vel debitis aspernatur adipisci consectetur praesentium omnis distinctio.",
      "identifier": "20230928-ec8566c655af7310cd6c1ff77882d6a916191ead"
    },
    {
      "@id": "https://elab.local:3148/database.php?mode=view&id=50",
      "@type": "Dataset",
      "name": " - Cumque et odit soluta dolore autem consequuntur fugit.",
      "identifier": "20230928-7c266f9b2a2503dc39cafebab0a24f987d1aa35e"
    },
    {
      "@id": "https://elab.local:3148/experiments.php?mode=view&id=256",
      "@type": "Dataset",
      "name": " - Test the grouped extra fields",
      "identifier": "20230928-eeab26c6b0d5f22a38e63761d288de4e330e97ae"
    },
    {
      "@id": "https://elab.local:3148/experiments.php?mode=view&id=257",
      "@type": "Dataset",
      "name": " - An example experiment",
      "identifier": "20230928-67aec89ca84a8140537de53e37d9ef9e4288ec41"
    },
    {
      "@id": "https://elab.local:3148/experiments.php?mode=view&id=258",
      "@type": "Dataset",
      "name": " - Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "identifier": "20230928-29d03424a48e4f7d970840f7f7b65d354190b096"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "4613",
      "sha256": "416b80afd9eb25ae38e47097e4954b8f75e25c8b4310fc91dfd91615de02d517"
    },
    {
      "@id": "comment://2023-09-28T03%3A44%3A54%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2023-09-28T03:44:54+02:00",
      "text": "Well, it&#39;s always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      }
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.png",
      "@type": "File",
      "description": "",
      "name": "example.png",
      "alternateName": "6b/6befead611faa1c99829ee811f5973e308f28cc8faea98594efc9ecf637bb62db3da3172e5c53e23f03bec7750b7ead5a32542b099544f8ee2902e4d66a99583.png",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.pdf",
      "@type": "File",
      "description": "",
      "name": "example.pdf",
      "alternateName": "f5/f5571362e29643a494946317891e2f97f66fbd33e3a473027901daf14bdfec0e4150c684b06a7c5def9a85535969ad7e3edaba82a010696762053c55c5c60ef6.pdf",
      "contentSize": 116369,
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:44:54+02:00",
      "dateModified": "2023-10-02T14:51:49+02:00",
      "identifier": "20230928-b6db898e231dbc2234227d19656d7e19a77654b7",
      "comment": [
        {
          "@id": "comment://2023-09-28T03%3A44%3A54%2B02%3A00"
        }
      ],
      "keywords": [
        "demo",
        "test"
      ],
      "name": "Testing the eLabFTW lab notebook",
      "text": "<h1>Goal</h1>\n<p>Test the software.</p>\n<h1>Procedure</h1>\n<p>Click everywhere and explore everything.</p>\n<h1>Results</h1>\n<p>It's really nice, I think I'll adopt it for our lab.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=264",
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/export-elabftw.json"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.png"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.pdf"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=51"
        },
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=50"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=256"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=257"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=258"
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
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### multiple-experiments.eln
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
      "dateCreated": "2023-10-02T15:52:26+02:00",
      "sdPublisher": {
        "@type": "Organization",
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
      "version": "1.0"
    },
    {
      "@id": "https://elab.local:3148/database.php?mode=view&id=51",
      "@type": "Dataset",
      "name": " - Vel debitis aspernatur adipisci consectetur praesentium omnis distinctio.",
      "identifier": "20230928-ec8566c655af7310cd6c1ff77882d6a916191ead"
    },
    {
      "@id": "https://elab.local:3148/database.php?mode=view&id=50",
      "@type": "Dataset",
      "name": " - Cumque et odit soluta dolore autem consequuntur fugit.",
      "identifier": "20230928-7c266f9b2a2503dc39cafebab0a24f987d1aa35e"
    },
    {
      "@id": "https://elab.local:3148/experiments.php?mode=view&id=256",
      "@type": "Dataset",
      "name": " - Test the grouped extra fields",
      "identifier": "20230928-eeab26c6b0d5f22a38e63761d288de4e330e97ae"
    },
    {
      "@id": "https://elab.local:3148/experiments.php?mode=view&id=257",
      "@type": "Dataset",
      "name": " - An example experiment",
      "identifier": "20230928-67aec89ca84a8140537de53e37d9ef9e4288ec41"
    },
    {
      "@id": "https://elab.local:3148/experiments.php?mode=view&id=258",
      "@type": "Dataset",
      "name": " - Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "identifier": "20230928-29d03424a48e4f7d970840f7f7b65d354190b096"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "4613",
      "sha256": "416b80afd9eb25ae38e47097e4954b8f75e25c8b4310fc91dfd91615de02d517"
    },
    {
      "@id": "comment://2023-09-28T03%3A44%3A54%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2023-09-28T03:44:54+02:00",
      "text": "Well, it&#39;s always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      }
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.png",
      "@type": "File",
      "description": "",
      "name": "example.png",
      "alternateName": "6b/6befead611faa1c99829ee811f5973e308f28cc8faea98594efc9ecf637bb62db3da3172e5c53e23f03bec7750b7ead5a32542b099544f8ee2902e4d66a99583.png",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.pdf",
      "@type": "File",
      "description": "",
      "name": "example.pdf",
      "alternateName": "f5/f5571362e29643a494946317891e2f97f66fbd33e3a473027901daf14bdfec0e4150c684b06a7c5def9a85535969ad7e3edaba82a010696762053c55c5c60ef6.pdf",
      "contentSize": 116369,
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:44:54+02:00",
      "dateModified": "2023-10-02T14:51:49+02:00",
      "identifier": "20230928-b6db898e231dbc2234227d19656d7e19a77654b7",
      "comment": [
        {
          "@id": "comment://2023-09-28T03%3A44%3A54%2B02%3A00"
        }
      ],
      "keywords": [
        "demo",
        "test"
      ],
      "name": "Testing the eLabFTW lab notebook",
      "text": "<h1>Goal</h1>\n<p>Test the software.</p>\n<h1>Procedure</h1>\n<p>Click everywhere and explore everything.</p>\n<h1>Results</h1>\n<p>It's really nice, I think I'll adopt it for our lab.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=264",
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/export-elabftw.json"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.png"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e/example.pdf"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=51"
        },
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=50"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=256"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=257"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=258"
        }
      ]
    },
    {
      "@id": "./2025-01-01 - An-example-experiment - 67aec89c/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "2035",
      "sha256": "5e4af208df28886354de4689eb060c8e7ca886ad432beb28fdee69a0f12cca04"
    },
    {
      "@id": "comment://2023-09-28T03%3A44%3A52%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2023-09-28T03:44:52+02:00",
      "text": "Oh, how fascinating. I&#39;m sure the groundbreaking discovery that water is wet will change the course of human history forever.",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      }
    },
    {
      "@id": "comment://2023-09-28T03%3A44%3A52%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2023-09-28T03:44:52+02:00",
      "text": "Well, it&#39;s a relief to see that the scientific community is hard at work discovering what we already suspected: that the sky is indeed blue. I can&#39;t wait for their next groundbreaking revelation that grass is green.",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      }
    },
    {
      "@id": "./2025-01-01 - An-example-experiment - 67aec89c",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:44:52+02:00",
      "dateModified": "2023-09-28T03:44:52+02:00",
      "identifier": "20230928-67aec89ca84a8140537de53e37d9ef9e4288ec41",
      "comment": [
        {
          "@id": "comment://2023-09-28T03%3A44%3A52%2B02%3A00"
        },
        {
          "@id": "comment://2023-09-28T03%3A44%3A52%2B02%3A00"
        }
      ],
      "keywords": [
        "example",
        "demo"
      ],
      "name": "An example experiment",
      "text": "This is the content of the experiment",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=257",
      "hasPart": [
        {
          "@id": "./2025-01-01 - An-example-experiment - 67aec89c/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - b6db898e"
        },
        {
          "@id": "./2025-01-01 - An-example-experiment - 67aec89c"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### single-resource.eln
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
      "dateCreated": "2023-10-02T15:52:54+02:00",
      "sdPublisher": {
        "@type": "Organization",
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
      "version": "1.0"
    },
    {
      "@id": "./Chemical-compound - Sodium-chloride-NaCl - 2c13a298/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1848",
      "sha256": "da4c3c699c58d674101725a9d10665229e81217a482d08dbc4c93838c1689f62"
    },
    {
      "@id": "./Chemical-compound - Sodium-chloride-NaCl - 2c13a298/example.pdb",
      "@type": "File",
      "description": "",
      "name": "example.pdb",
      "alternateName": "98/9869e96f76a6d0f2081dbe8142d05912f1f60ef77357b6a23bf7da5fd99588c0f38e85c45e47edc8ab92cfc1546dda50bb068930e42ea2028729393d466169e5.pdb",
      "contentSize": 515889,
      "sha256": "aa8a72b1c6fe310d25851742e4c30599bbcd4764c2a26578bad0fae70d8f0627"
    },
    {
      "@id": "./Chemical-compound - Sodium-chloride-NaCl - 2c13a298",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-09-28T03:45:03+02:00",
      "dateModified": "2023-10-02T14:52:50+02:00",
      "identifier": "20230928-2c13a298fee83f11b285021c49e351a0f95bb9c2",
      "comment": [],
      "keywords": [],
      "name": "Sodium chloride - NaCl",
      "text": "<p>Main text content.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=176",
      "hasPart": [
        {
          "@id": "./Chemical-compound - Sodium-chloride-NaCl - 2c13a298/export-elabftw.json"
        },
        {
          "@id": "./Chemical-compound - Sodium-chloride-NaCl - 2c13a298/example.pdb"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Chemical-compound - Sodium-chloride-NaCl - 2c13a298"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```
