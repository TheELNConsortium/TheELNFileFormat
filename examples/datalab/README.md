# *datalab* examples

[Repository](https://github.com/datalab-org/datalab)

## Overview

*datalab* is an open source data management platform targeted at sampled-focused experimental
data and metadata produced in materials chemistry labs. 

*datalab* allows users to export *items*, and *collections* of *items* with all associated
metadata, files and relationships into `.eln` files that can be imported into
any other contributing ELN.

For a given item, the user will have the option in the UI to export all related items to arbitrary depth:

<img width="1335" height="1056" alt="image" src="https://github.com/user-attachments/assets/ecc665c0-eb8e-4582-950e-62b529264a62" />


## Examples

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
      "dateCreated": "2025-10-17T12:05:20.277529+00:00",
      "sdPublisher": {
        "@id": "test"
      }
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Copper ferric oxide samples",
      "description": null,
      "hasPart": [
        {
          "@id": "./KD4-1/"
        },
        {
          "@id": "./FeSn_19_e2_c2_Cu_HV/"
        }
      ]
    },
    {
      "@id": "./KD4-1/",
      "@type": "Dataset",
      "name": "Copper iron oxide with impurities",
      "identifier": "KD4-1",
      "dateCreated": "2024-10-19T16:31:00"
    },
    {
      "@id": "./FeSn_19_e2_c2_Cu_HV/",
      "@type": "Dataset",
      "name": "",
      "identifier": "FeSn_19_e2_c2_Cu_HV",
      "dateCreated": "2025-04-03T17:56:00",
      "hasPart": [
        {
          "@id": "./FeSn_19_e2_c2_Cu_HV/250021-5-6-2818580548.ndax"
        }
      ]
    }
  ]
}

```

