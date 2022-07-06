# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

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
      "@type": "File"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/sequence.gbk",
      "@type": "File"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/Addgene-pIRES-Centrin1-mCherry.pdf",
      "@type": "File"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd",
      "@type": "Dataset",
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
      ]
    },
    {
      "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/export-elabftw.json",
      "@type": "File"
    },
    {
      "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/cnil_guide_securite_personnelle.pdf",
      "@type": "File"
    },
    {
      "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/export-elabftw.json"
        },
        {
          "@id": "./Project - Role-of-Centrin1-in-cell-division - c7d744ea/cnil_guide_securite_personnelle.pdf"
        }
      ]
    },
    {
      "@id": "./Protocol - Plasmid-amplification - 5d0c41b8/export-elabftw.json",
      "@type": "File"
    },
    {
      "@id": "./Protocol - Plasmid-amplification - 5d0c41b8",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./Protocol - Plasmid-amplification - 5d0c41b8/export-elabftw.json"
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
      "@type": "File"
    },
    {
      "@id": "./2022-07-07 - Example-experiment-title-I - d35e26a2",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./2022-07-07 - Example-experiment-title-I - d35e26a2/export-elabftw.json"
        }
      ]
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json",
      "@type": "File"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt",
      "@type": "File"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json"
        },
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt"
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
      "@type": "File"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/sequence.gbk",
      "@type": "File"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd/Addgene-pIRES-Centrin1-mCherry.pdf",
      "@type": "File"
    },
    {
      "@id": "./Plasmid - pIRES-Centrin1-mCherry - 7c2529fd",
      "@type": "Dataset",
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
      "dateCreated": "2022-07-07T01:19:48+0200",
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
      "@type": "File"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt",
      "@type": "File"
    },
    {
      "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/export-elabftw.json"
        },
        {
          "@id": "./2022-06-30 - Example-experiment-title - fc1b8fc4/test.txt"
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
