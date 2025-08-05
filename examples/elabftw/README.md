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
      "dateCreated": "2025-08-05T10:12:28+02:00",
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
      "endTime": "2025-08-05T10:12:28+02:00",
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
      "version": "5.3.0-alpha",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "comment://45ba73668ad9839f855dcc1e8124ae8c4d75b132abeb1aef2b06c4e848cbdad7?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-08-05T09:56:17+02:00",
      "text": "Well, it's always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://bac116baf8b0bb746558070e20fcbcc3d78d8f828c41466d2329450c601004ee?hash_algo=sha256"
      }
    },
    {
      "@id": "comment://c5eff5450d390eede1b690d1e1a5b446abf6cd9c6602d6438d715132be759497?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2025-08-05T10:03:44+02:00",
      "text": "Signed by Edgardo Murphy (Approval)",
      "author": {
        "@id": "person://edfd00f14230a3a7c32fd5e3fe540ceb2cdb888fb60b65514efb7b6b61dfdf3e?hash_algo=sha256"
      }
    },
    {
      "@id": "./Demo - Testing-the-eLabFTW-lab-notebook - b16abd04/example.png",
      "@type": "File",
      "name": "example.png",
      "alternateName": "66/66afa15ac9332b76443cf380e6c2f55e86ddcefd60df167a1660e878e2db5e5ef1a4c44a27abe51f698f31440848f69105106d1e5b9e8c9149218f476e60b3cb.png",
      "encodingFormat": "application/octet-stream",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "#category-Demo",
      "@type": "Thing",
      "name": "Demo",
      "color": "363EA3"
    },
    {
      "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - 5248e328/",
      "@type": "Dataset",
      "author": {
        "@id": "person://c911cf880616a083521d258af4c0d5c70abe3d436cbc7d31992f068adc2b9f29?hash_algo=sha256"
      },
      "dateCreated": "2025-08-05T09:56:17+02:00",
      "dateModified": "2025-08-05T09:56:17+02:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Testing relationship between acceleration and gravity",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=56",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20250805-5248e3280ec9845973ebf64819062a37f3039b1d",
      "keywords": "generated from yml,has-mathjax,physics",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-\ud83d\udd2c Microscope",
      "@type": "Thing",
      "name": "\ud83d\udd2c Microscope",
      "color": "3A32BE"
    },
    {
      "@id": "./Microscope - TIRF-microscope - 3a11cbcf/",
      "@type": "Dataset",
      "author": {
        "@id": "person://35dc831f42ed485ba05368b2dbec0d3b3f81191120cd0c7cc385681f0cf6cdb0?hash_algo=sha256"
      },
      "dateCreated": "2025-08-05T09:56:19+02:00",
      "dateModified": "2025-08-05T09:56:19+02:00",
      "temporal": "2024-11-17T00:00:00+01:00",
      "name": "TIRF microscope",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/database.php?mode=view&id=78",
      "genre": "resource",
      "identifier": "20250805-3a11cbcf6998459f8f37a8deba7f9a2011c22ae2",
      "about": {
        "@id": "#category-\ud83d\udd2c Microscope"
      }
    },
    {
      "@id": "./Demo - Testing-the-eLabFTW-lab-notebook - b16abd04/",
      "@type": "Dataset",
      "author": {
        "@id": "person://bac116baf8b0bb746558070e20fcbcc3d78d8f828c41466d2329450c601004ee?hash_algo=sha256"
      },
      "dateCreated": "2025-08-05T09:56:17+02:00",
      "dateModified": "2025-08-05T10:03:47+02:00",
      "temporal": "2025-03-03T00:00:00+01:00",
      "name": "Testing the eLabFTW lab notebook",
      "encodingFormat": "text/html",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=58",
      "genre": "experiment",
      "alternateName": 1,
      "comment": [
        {
          "@id": "comment://45ba73668ad9839f855dcc1e8124ae8c4d75b132abeb1aef2b06c4e848cbdad7?hash_algo=sha256"
        },
        {
          "@id": "comment://c5eff5450d390eede1b690d1e1a5b446abf6cd9c6602d6438d715132be759497?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "hasPart": [
        {
          "@id": "./Demo - Testing-the-eLabFTW-lab-notebook - b16abd04/example.png"
        }
      ],
      "identifier": "20250805-b16abd046cd8d3366a3fbad022781a96b2f6286c",
      "keywords": "generated from yml,demo,test",
      "mentions": [
        {
          "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - 5248e328/"
        },
        {
          "@id": "./Microscope - TIRF-microscope - 3a11cbcf/"
        }
      ],
      "text": "<h1>Goal</h1><p>Test the software.</p><h1>Procedure</h1><p>Click everywhere and explore everything.</p><h1>Results</h1><p>It's really nice, I think I'll adopt it for our lab.</p>",
      "about": {
        "@id": "#category-Demo"
      },
      "variableMeasured": [
        {
          "@id": "pv://a7a9218f-6212-4008-a93c-6f28e86b1956",
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Raw data URL\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\"}, \"Annie, are you okay\": {\"type\": \"checkbox\", \"value\": \"\", \"description\": \"This is a checkbox custom input\"}, \"This is a custom list input\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"The value is selected from a pre-defined list\"}}}"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://5b4f703b-c282-4426-b824-33f2cb0dcd1f",
          "propertyID": "Raw data URL",
          "valueReference": "url",
          "value": "https://datalake.example.com/experiments/3921"
        },
        {
          "@type": "PropertyValue",
          "@id": "pv://8e9432fb-0a62-4a93-8ca0-2f82aceb7d50",
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
      },
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "creativeWorkStatus": "finished",
          "temporal": "2025-08-05T10:03:20+02:00",
          "itemListElement": [
            {
              "@type": "HowToDirection",
              "text": "some step"
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
              "text": "another step"
            }
          ]
        }
      ]
    },
    {
      "@id": "./",
      "identifier": "57a7873e-9e40-4d46-aae6-5a5aabed1752",
      "@type": "Dataset",
      "datePublished": "2025-08-05T10:12:28+02:00",
      "hasPart": [
        {
          "@id": "./Demo - Testing-the-eLabFTW-lab-notebook - b16abd04/"
        },
        {
          "@id": "./Demo - Testing-relationship-between-acceleration-and-gravity - 5248e328/"
        },
        {
          "@id": "./Microscope - TIRF-microscope - 3a11cbcf/"
        }
      ],
      "name": "eLabFTW export",
      "description": "This is a .eln export from eLabFTW",
      "version": 102,
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
      }
    },
    {
      "@id": "person://bac116baf8b0bb746558070e20fcbcc3d78d8f828c41466d2329450c601004ee?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Hilda",
      "familyName": "Cummerata",
      "email": "impedit-33542095@yopmail.com"
    },
    {
      "@id": "person://edfd00f14230a3a7c32fd5e3fe540ceb2cdb888fb60b65514efb7b6b61dfdf3e?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Edgardo",
      "familyName": "Murphy",
      "email": "admin1@demo.elabftw.net"
    },
    {
      "@id": "person://c911cf880616a083521d258af4c0d5c70abe3d436cbc7d31992f068adc2b9f29?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Cordia",
      "familyName": "Jacobi",
      "email": "sint-85781528@yopmail.com"
    },
    {
      "@id": "person://35dc831f42ed485ba05368b2dbec0d3b3f81191120cd0c7cc385681f0cf6cdb0?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Zachariah",
      "familyName": "Nienow",
      "email": "notyetvalidateduser@yopmail.com"
    }
  ]
}
```
