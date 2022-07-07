# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

## Concepts used

The "Links" in eLabFTW are stored in the `mentions` property, they point to to the URL of the resource.

The comments are in the `comment` property.

A file `elabftw-export.json` is created during export and added to the archive, it corresponds to the JSON export on the entry by eLabFTW and might contain fields that are not present in the metadata file because too specific to eLabFTW.

### multiple-database-items.eln
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
      "dateCreated": "2022-07-07T01:18:01+0200",
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
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "3768",
      "sha256": "3bcd16b13e88b15cb976aba2dd596f7def2b6f0fc5db460f42f5c4067a189f57"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/sequence.gbk",
      "@type": "File",
      "description": "plasmid sequence",
      "name": "sequence.gbk",
      "contentSize": "16678",
      "sha256": "d84d8f0336c96345f72a5b4cb48f7874ac9e79dc1cc84c56f42aac3d542f6cdf"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/Addgene-pIRES-Centrin1-mCherry.pdf",
      "@type": "File",
      "description": "addgene page",
      "name": "Addgene-pIRES-Centrin1-mCherry.pdf",
      "contentSize": "186817",
      "sha256": "986e5f502783889bf019ea7bc36358044f1b695a4183bb05ef5f20d852143cec"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-07-06T00:31:47+0200",
      "dateModified": "2022-07-07T01:08:09+0200",
      "identifier": "20220630-7c2529fd5e4dbe1f65a0d37ad63b04aab9b405a4",
      "keywords": [
        "mCherry",
        "centrin"
      ],
      "name": "pIRES Centrin1 mCherry",
      "text": "<h1>Purpose</h1>\n<p>Bicistronic expression of mCherry-Centrin1 fusion and Hygro resistance gene</p>\n<p>Gene name: Centrin1 (Human)</p>\n<p>Backbone: pIREShyg3</p>\n<p>Purified on Wed, Jul 6, 2022, 12:46 AM.</p>\n<h1>Poem</h1>\n<p>C'est un trou de verdure o\u00f9 chante une rivi\u00e8re,<br>Accrochant follement aux herbes des haillons<br>D'argent ; o\u00f9 le soleil, de la montagne fi\u00e8re,<br>Luit : c'est un petit val qui mousse de rayons.</p>\n<p>Un soldat jeune, bouche ouverte, t\u00eate nue,<br>Et la nuque baignant dans le frais cresson bleu,<br>Dort ; il est \u00e9tendu dans l'herbe, sous la nue,<br>P\u00e2le dans son lit vert o\u00f9 la lumi\u00e8re pleut.</p>\n<p>Les pieds dans les gla\u00efeuls, il dort. Souriant comme<br>Sourirait un enfant malade, il fait un somme :<br>Nature, berce-le chaudement : il a froid.</p>\n<p>Les parfums ne font pas frissonner sa narine ;<br>Il dort dans le soleil, la main sur sa poitrine,<br>Tranquille. Il a deux trous rouges au c\u00f4t\u00e9 droit.</p>\n<p>Arthur Rimbaud, Le dormeur du val</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=16099",
      "hasPart": [
        {
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/export-elabftw.json"
        },
        {
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/sequence.gbk"
        },
        {
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/Addgene-pIRES-Centrin1-mCherry.pdf"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=16176",
          "@type": "Dataset",
          "name": "Project - Role of Centrin1 in cell division",
          "identifier": "20220707-c7d744ea92ce76ad7640c5540624614833434159"
        },
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=16177",
          "@type": "Dataset",
          "name": "Protocol - Plasmid amplification",
          "identifier": "20220707-5d0c41b8cfd3318e5fcbc9eb7df563ab72455865"
        }
      ]
    },
    {
      "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "1325",
      "sha256": "82424d9ea909930d95ec3f39ad2f257ce7a775d45107c1848f7d226900a5667b"
    },
    {
      "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/cnil_guide_securite_personnelle.pdf",
      "@type": "File",
      "description": "a file comment",
      "name": "cnil_guide_securite_personnelle.pdf",
      "contentSize": "422657",
      "sha256": "3781ab69b539230df24aafb5c2253998323bbcac02e740e9779fc20c88554648"
    },
    {
      "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-07-07T01:05:46+0200",
      "dateModified": "2022-07-07T01:15:19+0200",
      "identifier": "20220707-c7d744ea92ce76ad7640c5540624614833434159",
      "keywords": [
        "centrin"
      ],
      "name": "Role of Centrin1 in cell division",
      "text": "<p>Main content.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=16176",
      "hasPart": [
        {
          "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/export-elabftw.json"
        },
        {
          "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/cnil_guide_securite_personnelle.pdf"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Protocol - Plasmid-amplification - 5d0c41b8/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "859",
      "sha256": "696ed5aba6c86a20194b4adbb3ea5b634954490ff4a0ab16728888a44aaf4962"
    },
    {
      "@id": "./Protocol - Plasmid-amplification - 5d0c41b8",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-07-07T01:06:44+0200",
      "dateModified": "2022-07-07T01:16:57+0200",
      "identifier": "20220707-5d0c41b8cfd3318e5fcbc9eb7df563ab72455865",
      "keywords": [],
      "name": "Plasmid amplification",
      "text": "<p>Here be the content of the protocol.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=16177",
      "hasPart": [
        {
          "@id": "./Protocol - Plasmid-amplification - 5d0c41b8/export-elabftw.json"
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
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd"
        },
        {
          "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea"
        },
        {
          "@id": "./Protocol - Plasmid-amplification - 5d0c41b8"
        }
      ]
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
      "dateCreated": "2022-07-07T01:22:01+0200",
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
      "@id": "./2022-07-07 - Example-experiment-title-I - d35e26a2/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "1083",
      "sha256": "925a681cc9f66c4e2cb74c333b344be0f38bb8f7e5381d9e6340579bf49d136a"
    },
    {
      "@id": "./2022-07-07 - Example-experiment-title-I - d35e26a2",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-07-07T01:21:22+0200",
      "dateModified": "2022-07-07T01:21:45+0200",
      "identifier": "20220707-d35e26a2238b6920432871d981875c3ae15553e3",
      "keywords": [
        "another tag",
        "some tag"
      ],
      "name": "Example experiment title I",
      "text": "<p>Body content but this time different.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=16045",
      "hasPart": [
        {
          "@id": "./2022-07-07 - Example-experiment-title-I - d35e26a2/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "1656",
      "sha256": "69e9e689997d48adfdd4c3de36532dc45059d762d2d237e4f92f1efeee89ae08"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt",
      "@type": "File",
      "description": "Click to add a comment",
      "name": "test.txt",
      "contentSize": "6",
      "sha256": "d79ed4f50424789cb45aadeec31761e29d8031a3b6cbdaaa42f9e2758372703a"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-06-30T10:48:10+0200",
      "dateModified": "2022-07-07T01:19:23+0200",
      "identifier": "20220630-fc1b8fc4f6759074ff610677e70ede000291381d",
      "keywords": [
        "another tag",
        "some tag"
      ],
      "name": "Example experiment title",
      "text": "<p>Body content</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=16035",
      "hasPart": [
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json"
        },
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=16099",
          "@type": "Dataset",
          "name": "Plasmid - pIRES Centrin1 mCherry",
          "identifier": "20220630-7c2529fd5e4dbe1f65a0d37ad63b04aab9b405a4"
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
          "@id": "./2022-07-07 - Example-experiment-title-I - d35e26a2"
        },
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4"
        }
      ]
    }
  ]
}
```

### single-database-item.eln
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
      "dateCreated": "2022-07-07T01:12:10+0200",
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
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "3768",
      "sha256": "3bcd16b13e88b15cb976aba2dd596f7def2b6f0fc5db460f42f5c4067a189f57"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/sequence.gbk",
      "@type": "File",
      "description": "plasmid sequence",
      "name": "sequence.gbk",
      "contentSize": "16678",
      "sha256": "d84d8f0336c96345f72a5b4cb48f7874ac9e79dc1cc84c56f42aac3d542f6cdf"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/Addgene-pIRES-Centrin1-mCherry.pdf",
      "@type": "File",
      "description": "addgene page",
      "name": "Addgene-pIRES-Centrin1-mCherry.pdf",
      "contentSize": "186817",
      "sha256": "986e5f502783889bf019ea7bc36358044f1b695a4183bb05ef5f20d852143cec"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-07-06T00:31:47+0200",
      "dateModified": "2022-07-07T01:08:09+0200",
      "identifier": "20220630-7c2529fd5e4dbe1f65a0d37ad63b04aab9b405a4",
      "keywords": [
        "mCherry",
        "centrin"
      ],
      "name": "pIRES Centrin1 mCherry",
      "text": "<h1>Purpose</h1>\n<p>Bicistronic expression of mCherry-Centrin1 fusion and Hygro resistance gene</p>\n<p>Gene name: Centrin1 (Human)</p>\n<p>Backbone: pIREShyg3</p>\n<p>Purified on Wed, Jul 6, 2022, 12:46 AM.</p>\n<h1>Poem</h1>\n<p>C'est un trou de verdure o\u00f9 chante une rivi\u00e8re,<br>Accrochant follement aux herbes des haillons<br>D'argent ; o\u00f9 le soleil, de la montagne fi\u00e8re,<br>Luit : c'est un petit val qui mousse de rayons.</p>\n<p>Un soldat jeune, bouche ouverte, t\u00eate nue,<br>Et la nuque baignant dans le frais cresson bleu,<br>Dort ; il est \u00e9tendu dans l'herbe, sous la nue,<br>P\u00e2le dans son lit vert o\u00f9 la lumi\u00e8re pleut.</p>\n<p>Les pieds dans les gla\u00efeuls, il dort. Souriant comme<br>Sourirait un enfant malade, il fait un somme :<br>Nature, berce-le chaudement : il a froid.</p>\n<p>Les parfums ne font pas frissonner sa narine ;<br>Il dort dans le soleil, la main sur sa poitrine,<br>Tranquille. Il a deux trous rouges au c\u00f4t\u00e9 droit.</p>\n<p>Arthur Rimbaud, Le dormeur du val</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=16099",
      "hasPart": [
        {
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/export-elabftw.json"
        },
        {
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/sequence.gbk"
        },
        {
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/Addgene-pIRES-Centrin1-mCherry.pdf"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=16176",
          "@type": "Dataset",
          "name": "Project - Role of Centrin1 in cell division",
          "identifier": "20220707-c7d744ea92ce76ad7640c5540624614833434159"
        },
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=16177",
          "@type": "Dataset",
          "name": "Protocol - Plasmid amplification",
          "identifier": "20220707-5d0c41b8cfd3318e5fcbc9eb7df563ab72455865"
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
          "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd"
        }
      ]
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
      "dateCreated": "2022-07-07T02:38:23+0200",
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
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "contentType": "application/json",
      "contentSize": "2124",
      "sha256": "02b619ad4b69df24cb0d220b5d2380fa1cd97bef77f085bff2666aff425eeeb9"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt",
      "@type": "File",
      "description": "Click to add a comment",
      "name": "test.txt",
      "contentSize": "6",
      "sha256": "d79ed4f50424789cb45aadeec31761e29d8031a3b6cbdaaa42f9e2758372703a"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4",
      "@type": "Dataset",
      "author": {
        "@type": "Person",
        "familyName": "Le sysadmin",
        "givenName": "Toto",
        "identifier": "https://orcid.org/0000-0012-3456-7890"
      },
      "dateCreated": "2022-06-30T10:48:10+0200",
      "dateModified": "2022-07-07T01:19:23+0200",
      "identifier": "20220630-fc1b8fc4f6759074ff610677e70ede000291381d",
      "comment": [
        {
          "dateCreated": "2022-06-30T10:48:10+0200",
          "text": "This is the content of the comment.",
          "author": {
            "@type": "Person",
            "familyName": "Cummings",
            "givenName": "Titi",
            "identifier": "https://orcid.org/0000-0012-3456-7890"
          }
        },
        {
          "dateCreated": "2022-06-30T10:48:10+0200",
          "text": "Yes, this is another great comment.",
          "author": {
            "@type": "Person",
            "familyName": "Le sysadmin",
            "givenName": "Toto",
            "identifier": "https://orcid.org/0000-0012-3456-7890"
          }
        }
      ],
      "keywords": [
        "another tag",
        "some tag"
      ],
      "name": "Example experiment title",
      "text": "<p>Body content</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=16035",
      "hasPart": [
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json"
        },
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=16099",
          "@type": "Dataset",
          "name": "Plasmid - pIRES Centrin1 mCherry",
          "identifier": "20220630-7c2529fd5e4dbe1f65a0d37ad63b04aab9b405a4"
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
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4"
        }
      ]
    }
  ]
}
```
