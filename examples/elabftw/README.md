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


### resources.eln
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
      "dateCreated": "2024-06-10T13:40:59+02:00",
      "sdPublisher": {
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
      "version": "1.0"
    },
    {
      "@id": "#ro-crate_created",
      "@type": "CreateAction",
      "object": {
        "@id": "./"
      },
      "name": "RO-Crate created",
      "endTime": "2024-06-10T13:40:59+02:00",
      "instrument": {
        "@id": "https://www.elabftw.net",
        "@type": "SoftwareApplication",
        "name": "eLabFTW",
        "version": "5.1.0",
        "identifier": "https://www.elabftw.net"
      },
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      }
    },
    {
      "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 07f7922f",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:57+02:00",
      "identifier": "20240610-07f7922fc08af84798dbfe9ed1ec8886c0351f8b",
      "comment": [],
      "keywords": [],
      "name": "Hydrochloric acid - HCl",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=177",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Chemical compound",
      "variableMeasured": null
    },
    {
      "@id": "./Microscope - Video-microscope-Bravo - d8a5b42e",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-d8a5b42eba9c2291135cce0fca777857be01834f",
      "comment": [],
      "keywords": [],
      "name": "Video microscope Bravo",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=176",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Microscope",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Location\": {\"type\": \"select\", \"value\": \"Microscopy room 3rd floor\", \"options\": [\"Microscopy room 3rd floor\", \"Nikon imaging center\", \"-2 microscopy room A\", \"That building that is way too far away\"]}, \"Availability\": {\"type\": \"select\", \"value\": \"Works great\", \"options\": [\"Works great\", \"Works most of the time, make sure to reboot the computer\", \"Half broken, do not use\", \"Completely useless\"], \"description\": \"Is it broken?\"}, \"Person in charge\": {\"type\": \"text\", \"value\": \"Paolo\"}, \"Available wavelengths\": {\"type\": \"select\", \"value\": \"405 nm\", \"options\": [\"405 nm\", \"488 nm\", \"561 nm\", \"640 nm\"], \"allow_multi_values\": true}}}"
        },
        {
          "propertyID": "Location",
          "valueReference": "select",
          "value": "Microscopy room 3rd floor"
        },
        {
          "propertyID": "Availability",
          "valueReference": "select",
          "value": "Works great",
          "description": "Is it broken?"
        },
        {
          "propertyID": "Person in charge",
          "valueReference": "text",
          "value": "Paolo"
        },
        {
          "propertyID": "Available wavelengths",
          "valueReference": "select",
          "value": "405 nm"
        }
      ]
    },
    {
      "@id": "./Chemical-compound - Methanol-CH3OH - 9c11e8db",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-9c11e8dbc9834f7e93af01ecf53dc566fccd0ff0",
      "comment": [],
      "keywords": [],
      "name": "Methanol - CH3OH",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=175",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Chemical compound",
      "variableMeasured": null
    },
    {
      "@id": "./Antibody - Anti-GAPDH - 49d9d070",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-49d9d070a04a2afb390dfc57d25b98668d6082bb",
      "comment": [],
      "keywords": [],
      "name": "Anti-GAPDH",
      "text": "<p>Anti-GAPDH is a polyclonal rabbit antibody used to detect the glyceraldehyde-3-phosphate dehydrogenase protein, a well-known housekeeping gene that is ubiquitously expressed in cells. This antibody is commonly used as a loading control in Western blotting and has been shown to work in a wide range of species including human, mouse, rat, and others. The antibody was generated by immunizing rabbits with purified GAPDH protein.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=174",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Antibody",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"text\", \"value\": \"Rabbit\"}, \"Isotype\": {\"type\": \"text\", \"value\": \"IgG\"}, \"Dilution for IF\": {\"type\": \"text\", \"value\": \"1:1000\"}, \"Dilution for WB\": {\"type\": \"text\", \"value\": \"1:5000\"}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"-20\u00b0C\", \"options\": [\"+4\u00b0C\", \"-20\u00b0C\", \"-80\u00b0C\"]}}}"
        },
        {
          "propertyID": "Host",
          "valueReference": "text",
          "value": "Rabbit"
        },
        {
          "propertyID": "Isotype",
          "valueReference": "text",
          "value": "IgG"
        },
        {
          "propertyID": "Dilution for IF",
          "valueReference": "text",
          "value": "1:1000"
        },
        {
          "propertyID": "Dilution for WB",
          "valueReference": "text",
          "value": "1:5000"
        },
        {
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "-20\u00b0C"
        }
      ]
    },
    {
      "@id": "./Antibody - Anti-CD45 - 1cde8d97",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-1cde8d97fe7b9c8b2e7aa4d3391f57e24e44ba4c",
      "comment": [],
      "keywords": [],
      "name": "Anti-CD45",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=173",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Antibody",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"select\", \"value\": \"Rabbit\", \"options\": [\"Rabbit\", \"Mouse\", \"Goat\", \"Chicken\"]}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"+4 \u00b0C\", \"options\": [\"+4 \u00b0C\", \"-20 \u00b0C\", \"-80 \u00b0C\"]}, \"Dilution to use for IF\": {\"type\": \"text\", \"value\": \"\"}, \"Dilution to use for WB\": {\"type\": \"text\", \"value\": \"\"}, \"Number of aliquots left\": {\"type\": \"number\", \"value\": \"\", \"description\": \"Make sure to decrement this when using one!\"}}}"
        },
        {
          "propertyID": "Host",
          "valueReference": "select",
          "value": "Rabbit"
        },
        {
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "+4 \u00b0C"
        },
        {
          "propertyID": "Dilution to use for IF",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Dilution to use for WB",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Number of aliquots left",
          "valueReference": "number",
          "value": "",
          "description": "Make sure to decrement this when using one!"
        }
      ]
    },
    {
      "@id": "./Antibody - Anti-CD4 - 69c57daf",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-69c57dafd3e8ee357ff9d8c2f14a402e72dd2c39",
      "comment": [],
      "keywords": [],
      "name": "Anti-CD4",
      "text": "<p>Anti-CD4 is a monoclonal mouse antibody that recognizes the CD4 antigen, a cell surface glycoprotein found on T-helper cells, regulatory T-cells, and monocytes. This antibody has been extensively used for flow cytometry, immunohistochemistry, and Western blotting. The antibody was generated by immunizing mice with human CD4-positive T-cell lines.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=172",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Antibody",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"text\", \"value\": \"Mouse\"}, \"Isotype\": {\"type\": \"text\", \"value\": \"IgG1\"}, \"Dilution for IF\": {\"type\": \"text\", \"value\": \"1:100\"}, \"Dilution for WB\": {\"type\": \"text\", \"value\": \"1:500\"}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"-20\u00b0C\", \"options\": [\"+4\u00b0C\", \"-20\u00b0C\", \"-80\u00b0C\"]}}}"
        },
        {
          "propertyID": "Host",
          "valueReference": "text",
          "value": "Mouse"
        },
        {
          "propertyID": "Isotype",
          "valueReference": "text",
          "value": "IgG1"
        },
        {
          "propertyID": "Dilution for IF",
          "valueReference": "text",
          "value": "1:100"
        },
        {
          "propertyID": "Dilution for WB",
          "valueReference": "text",
          "value": "1:500"
        },
        {
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "-20\u00b0C"
        }
      ]
    },
    {
      "@id": "./Yeast - JK9-3d - 42b153ea",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-42b153ea593f10709b9677378b4d4b83fad88703",
      "comment": [],
      "keywords": [],
      "name": "JK9-3d",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=171",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Yeast",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Genotype\": {\"type\": \"text\", \"value\": \"MATa his3\u0394200 leu2\u03941 trp1\u039463 ura3\u039452\"}, \"Plasmids\": {\"type\": \"text\", \"value\": \"pRS416\"}, \"Temperature\": {\"type\": \"text\", \"value\": \"30\u00b0C\"}}}"
        },
        {
          "propertyID": "Genotype",
          "valueReference": "text",
          "value": "MATa his3\u0394200 leu2\u03941 trp1\u039463 ura3\u039452"
        },
        {
          "propertyID": "Plasmids",
          "valueReference": "text",
          "value": "pRS416"
        },
        {
          "propertyID": "Temperature",
          "valueReference": "text",
          "value": "30\u00b0C"
        }
      ]
    },
    {
      "@id": "./Chemical-compound - Sodium-chloride-NaCl - 1834463f",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:56+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-1834463f80574bf2defa8f68a110134e6672afe5",
      "comment": [],
      "keywords": [],
      "name": "Sodium chloride - NaCl",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=170",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Chemical compound",
      "variableMeasured": null
    },
    {
      "@id": "./Antibody - Anti-Actin - 6cc432d2",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:56+02:00",
      "identifier": "20240610-6cc432d28d30a202a62c576d5891d91c0a320b41",
      "comment": [],
      "keywords": [],
      "name": "Anti-Actin",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=169",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Antibody",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"select\", \"value\": \"Rabbit\", \"options\": [\"Rabbit\", \"Mouse\", \"Goat\", \"Chicken\"]}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"+4 \u00b0C\", \"options\": [\"+4 \u00b0C\", \"-20 \u00b0C\", \"-80 \u00b0C\"]}, \"Dilution to use for IF\": {\"type\": \"text\", \"value\": \"\"}, \"Dilution to use for WB\": {\"type\": \"text\", \"value\": \"\"}, \"Number of aliquots left\": {\"type\": \"number\", \"value\": \"\", \"description\": \"Make sure to decrement this when using one!\"}}}"
        },
        {
          "propertyID": "Host",
          "valueReference": "select",
          "value": "Rabbit"
        },
        {
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "+4 \u00b0C"
        },
        {
          "propertyID": "Dilution to use for IF",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Dilution to use for WB",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Number of aliquots left",
          "valueReference": "number",
          "value": "",
          "description": "Make sure to decrement this when using one!"
        }
      ]
    },
    {
      "@id": "./Microscope - Spinning-Disk-2 - e2900447",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "identifier": "20240610-e2900447b78b6ab18ff22e5bfe785904a01f7492",
      "comment": [],
      "keywords": [],
      "name": "Spinning Disk 2",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=168",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Microscope",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Location\": {\"type\": \"select\", \"value\": \"Microscopy room 3rd floor\", \"options\": [\"Microscopy room 3rd floor\", \"Nikon imaging center\", \"-2 microscopy room A\", \"That building that is way too far away\"]}, \"Availability\": {\"type\": \"select\", \"value\": \"Works great\", \"options\": [\"Works great\", \"Works most of the time, make sure to reboot the computer\", \"Half broken, do not use\", \"Completely useless\"], \"description\": \"Is it broken?\"}, \"Person in charge\": {\"type\": \"text\", \"value\": \"Paolo\"}, \"Available wavelengths\": {\"type\": \"select\", \"value\": \"405 nm\", \"options\": [\"405 nm\", \"488 nm\", \"561 nm\", \"640 nm\"], \"allow_multi_values\": true}}}"
        },
        {
          "propertyID": "Location",
          "valueReference": "select",
          "value": "Microscopy room 3rd floor"
        },
        {
          "propertyID": "Availability",
          "valueReference": "select",
          "value": "Works great",
          "description": "Is it broken?"
        },
        {
          "propertyID": "Person in charge",
          "valueReference": "text",
          "value": "Paolo"
        },
        {
          "propertyID": "Available wavelengths",
          "valueReference": "select",
          "value": "405 nm"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      }
    },
    {
      "@id": "./Plasmid - pCR2.1-TOPO - a1b08932",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "identifier": "20240610-a1b08932345c7ece4eff55a33b0e024991745873",
      "comment": [],
      "keywords": [],
      "name": "pCR2.1-TOPO",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=167",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Plasmid",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Concentration\": {\"type\": \"number\", \"value\": \"\", \"description\": \"in \u03bcg/\u03bcL\"}, \"Vector backbone\": {\"type\": \"text\", \"value\": \"\"}, \"Growth temperature\": {\"type\": \"text\", \"value\": \"\", \"description\": \"in \u00b0C\"}, \"Bacterial resistance\": {\"type\": \"select\", \"value\": \"Ampicillin\", \"options\": [\"Ampicillin\", \"Kanamycin\", \"Tetracyclin\", \"Chloramphenicol\", \"Gentamicin\", \"Streptomycin\"]}, \"Mammalian resistance\": {\"type\": \"select\", \"value\": \"Neomycin\", \"options\": [\"Neomycin\", \"Hygromycin\", \"Puromycin\", \"Blasticidin\", \"Zeocin\"]}}}"
        },
        {
          "propertyID": "Concentration",
          "valueReference": "number",
          "value": "",
          "description": "in \u03bcg/\u03bcL"
        },
        {
          "propertyID": "Vector backbone",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Growth temperature",
          "valueReference": "text",
          "value": "",
          "description": "in \u00b0C"
        },
        {
          "propertyID": "Bacterial resistance",
          "valueReference": "select",
          "value": "Ampicillin"
        },
        {
          "propertyID": "Mammalian resistance",
          "valueReference": "select",
          "value": "Neomycin"
        }
      ]
    },
    {
      "@id": "./Antibody - Anti-Phospho-STAT3-Tyr705 - b88ca409",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "identifier": "20240610-b88ca409a5184787e9f7b9781eacc108596fa2d0",
      "comment": [],
      "keywords": [],
      "name": "Anti-Phospho-STAT3 (Tyr705)",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=166",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Antibody",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"select\", \"value\": \"Rabbit\", \"options\": [\"Rabbit\", \"Mouse\", \"Goat\", \"Chicken\"]}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"+4 \u00b0C\", \"options\": [\"+4 \u00b0C\", \"-20 \u00b0C\", \"-80 \u00b0C\"]}, \"Dilution to use for IF\": {\"type\": \"text\", \"value\": \"\"}, \"Dilution to use for WB\": {\"type\": \"text\", \"value\": \"\"}, \"Number of aliquots left\": {\"type\": \"number\", \"value\": \"\", \"description\": \"Make sure to decrement this when using one!\"}}}"
        },
        {
          "propertyID": "Host",
          "valueReference": "select",
          "value": "Rabbit"
        },
        {
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "+4 \u00b0C"
        },
        {
          "propertyID": "Dilution to use for IF",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Dilution to use for WB",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Number of aliquots left",
          "valueReference": "number",
          "value": "",
          "description": "Make sure to decrement this when using one!"
        }
      ]
    },
    {
      "@id": "./Antibody - Anti-HA - 74fb240d",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "identifier": "20240610-74fb240d1328daca7eb901331a6bf57d09d25eb8",
      "comment": [],
      "keywords": [],
      "name": "Anti-HA",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=165",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Antibody",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Host\": {\"type\": \"select\", \"value\": \"Rabbit\", \"options\": [\"Rabbit\", \"Mouse\", \"Goat\", \"Chicken\"]}, \"Storage temperature\": {\"type\": \"select\", \"value\": \"+4 \u00b0C\", \"options\": [\"+4 \u00b0C\", \"-20 \u00b0C\", \"-80 \u00b0C\"]}, \"Dilution to use for IF\": {\"type\": \"text\", \"value\": \"\"}, \"Dilution to use for WB\": {\"type\": \"text\", \"value\": \"\"}, \"Number of aliquots left\": {\"type\": \"number\", \"value\": \"\", \"description\": \"Make sure to decrement this when using one!\"}}}"
        },
        {
          "propertyID": "Host",
          "valueReference": "select",
          "value": "Rabbit"
        },
        {
          "propertyID": "Storage temperature",
          "valueReference": "select",
          "value": "+4 \u00b0C"
        },
        {
          "propertyID": "Dilution to use for IF",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Dilution to use for WB",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Number of aliquots left",
          "valueReference": "number",
          "value": "",
          "description": "Make sure to decrement this when using one!"
        }
      ]
    },
    {
      "@id": "./Chemical-compound - Potassium-chloride-KCl - 9ca2ca08",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "identifier": "20240610-9ca2ca089b4854074337d85e30f3799b55a03395",
      "comment": [],
      "keywords": [],
      "name": "Potassium chloride - KCl",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=164",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Chemical compound",
      "variableMeasured": null
    },
    {
      "@id": "./Yeast - DBY746 - f6d47fdd",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:55+02:00",
      "dateModified": "2024-06-10T13:31:55+02:00",
      "identifier": "20240610-f6d47fdd9b27f8311e22ae6d8adff88518160410",
      "comment": [],
      "keywords": [],
      "name": "DBY746",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=163",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Yeast",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Genotype\": {\"type\": \"text\", \"value\": \"MAT\u03b1 ura3-52 his3-\u0394200 leu2-\u03941 trp1-\u039463\"}, \"Plasmids\": {\"type\": \"text\", \"value\": \"pRS416\"}, \"Temperature\": {\"type\": \"text\", \"value\": \"30\u00b0C\"}}}"
        },
        {
          "propertyID": "Genotype",
          "valueReference": "text",
          "value": "MAT\u03b1 ura3-52 his3-\u0394200 leu2-\u03941 trp1-\u039463"
        },
        {
          "propertyID": "Plasmids",
          "valueReference": "text",
          "value": "pRS416"
        },
        {
          "propertyID": "Temperature",
          "valueReference": "text",
          "value": "30\u00b0C"
        }
      ]
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 07f7922f"
        },
        {
          "@id": "./Microscope - Video-microscope-Bravo - d8a5b42e"
        },
        {
          "@id": "./Chemical-compound - Methanol-CH3OH - 9c11e8db"
        },
        {
          "@id": "./Antibody - Anti-GAPDH - 49d9d070"
        },
        {
          "@id": "./Antibody - Anti-CD45 - 1cde8d97"
        },
        {
          "@id": "./Antibody - Anti-CD4 - 69c57daf"
        },
        {
          "@id": "./Yeast - JK9-3d - 42b153ea"
        },
        {
          "@id": "./Chemical-compound - Sodium-chloride-NaCl - 1834463f"
        },
        {
          "@id": "./Antibody - Anti-Actin - 6cc432d2"
        },
        {
          "@id": "./Microscope - Spinning-Disk-2 - e2900447"
        },
        {
          "@id": "./Plasmid - pCR2.1-TOPO - a1b08932"
        },
        {
          "@id": "./Antibody - Anti-Phospho-STAT3-Tyr705 - b88ca409"
        },
        {
          "@id": "./Antibody - Anti-HA - 74fb240d"
        },
        {
          "@id": "./Chemical-compound - Potassium-chloride-KCl - 9ca2ca08"
        },
        {
          "@id": "./Yeast - DBY746 - f6d47fdd"
        }
      ]
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

### experiments.eln
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
      "dateCreated": "2024-06-10T13:40:44+02:00",
      "sdPublisher": {
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
      "version": "1.0"
    },
    {
      "@id": "#ro-crate_created",
      "@type": "CreateAction",
      "object": {
        "@id": "./"
      },
      "name": "RO-Crate created",
      "endTime": "2024-06-10T13:40:44+02:00",
      "instrument": {
        "@id": "https://www.elabftw.net",
        "@type": "SoftwareApplication",
        "name": "eLabFTW",
        "version": "5.1.0",
        "identifier": "https://www.elabftw.net"
      },
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      }
    },
    {
      "@id": "comment://2024-06-10T13%3A31%3A47%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2024-06-10T13:31:47+02:00",
      "text": "Well, it's always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 854e72d3",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:44+02:00",
      "dateModified": "2024-06-10T13:31:44+02:00",
      "identifier": "20240610-854e72d32638e17a9258c70a58b1902262baa47c",
      "comment": [],
      "keywords": "dev,extra fields",
      "name": "Test the grouped extra fields",
      "text": "",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=256",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"elabftw\": {\"display_main_text\": false, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group with id 1, first position\"}, {\"id\": 2, \"name\": \"Group with id 2, second position\"}, {\"id\": 3, \"name\": \"Group with id 3, third position\"}]}, \"extra_fields\": {\"Has group_id 3 as number\": {\"type\": \"text\", \"value\": \"\", \"group_id\": 3}, \"Has group_id 3 as string\": {\"type\": \"text\", \"value\": \"\", \"group_id\": \"3\"}, \"Has no group_id property\": {\"type\": \"text\", \"value\": \"\"}, \"Group_id 1 and position 1\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 1, \"position\": 1, \"description\": \"This is a checkbox custom input\"}, \"Group_id 2 and position 1\": {\"type\": \"url\", \"value\": \"\", \"group_id\": 2, \"position\": 1}, \"Group_id 2 and position 2\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\", \"group_id\": 2, \"position\": 2}, \"Group_id 2 and position 3\": {\"type\": \"url\", \"value\": \"\", \"group_id\": 2, \"position\": 3}, \"Another one without group_id property\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"this element has no group property defined\"}, \"Has group_id that is not in elabftw.groups\": {\"type\": \"text\", \"value\": \"I am lost!\", \"group_id\": \"19\"}}}"
        },
        {
          "propertyID": "Has group_id 3 as number",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Has group_id 3 as string",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Has no group_id property",
          "valueReference": "text",
          "value": ""
        },
        {
          "propertyID": "Group_id 1 and position 1",
          "valueReference": "checkbox",
          "value": "",
          "description": "This is a checkbox custom input"
        },
        {
          "propertyID": "Group_id 2 and position 1",
          "valueReference": "url",
          "value": ""
        },
        {
          "propertyID": "Group_id 2 and position 2",
          "valueReference": "url",
          "value": "https://datalake.example.com/experiments/3921"
        },
        {
          "propertyID": "Group_id 2 and position 3",
          "valueReference": "url",
          "value": ""
        },
        {
          "propertyID": "Another one without group_id property",
          "valueReference": "select",
          "value": "Some choice",
          "description": "this element has no group property defined"
        },
        {
          "propertyID": "Has group_id that is not in elabftw.groups",
          "valueReference": "text",
          "value": "I am lost!"
        }
      ]
    },
    {
      "@id": "comment://2024-06-10T13%3A31%3A45%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2024-06-10T13:31:45+02:00",
      "text": "Oh, how fascinating. I'm sure the groundbreaking discovery that water is wet will change the course of human history forever.",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "comment://2024-06-10T13%3A31%3A45%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2024-06-10T13:31:45+02:00",
      "text": "Well, it's a relief to see that the scientific community is hard at work discovering what we already suspected: that the sky is indeed blue. I can't wait for their next groundbreaking revelation that grass is green.",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - An-example-experiment - fc07130d",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:44+02:00",
      "dateModified": "2024-06-10T13:31:45+02:00",
      "identifier": "20240610-fc07130d293361d384b2425c5ec8512e454238ee",
      "comment": [
        {
          "@id": "comment://2024-06-10T13%3A31%3A45%2B02%3A00"
        },
        {
          "@id": "comment://2024-06-10T13%3A31%3A45%2B02%3A00"
        }
      ],
      "keywords": "example,demo",
      "name": "An example experiment",
      "text": "This is the content of the experiment",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=257",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - c6bff418",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:45+02:00",
      "dateModified": "2024-06-10T13:31:45+02:00",
      "identifier": "20240610-c6bff418669b56a40f914c36e4bc871be7a210da",
      "comment": [],
      "keywords": "transfection,biocell,RPE-1",
      "name": "Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "text": "<h1>Goal</h1><p>Transfecting the plasmid p103\u039412-22 into the RPE-1 Actin-RFP cells and look at the death rate.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=258",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": null
    },
    {
      "@id": "./Generated - Itaque-accusantium-eos-et - f4d54504",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:30:31+02:00",
      "dateModified": "2024-06-10T13:30:31+02:00",
      "identifier": "20240610-f4d54504a2e484fa326b9164379d8c60fe92e2d9",
      "comment": [],
      "keywords": "microbiology,molecular cloning,Western Blot,protein purification,scientific discovery,statistical analysis",
      "name": "Itaque accusantium eos et.",
      "text": "Alice thought), and it set to work shaking him and punching him in the window, and one foot up the fan she was now, and she at once to eat her up in her head, and she thought it would be the best of educations--in fact, we went to work throwing everything within her reach at the Queen, who was talking. 'How CAN I have to turn into a large cauldron which seemed to be rude, so she began thinking over other children she knew the name of the Nile On every golden scale! 'How cheerfully he seems to be no sort of way to explain the mistake it had lost something; and she tried her best to climb up one of the cattle in the sea. But they HAVE their tails in their mouths. So they couldn't get them out of breath, and till the puppy's bark sounded quite faint in the book,' said the Hatter. 'Nor I,' said the Duchess. An invitation from the Gryphon, before Alice could not help thinking there MUST be more to do next, when suddenly a White Rabbit hurried by--the frightened Mouse splashed his way.",
      "url": "https://elab.local:3148/database.php?mode=view&id=50",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Generated",
      "status": "Waiting"
    },
    {
      "@id": "./Generated - Aut-corrupti-debitis-tenetur-enim-molestiae-architecto - 45ea546e",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:30:31+02:00",
      "dateModified": "2024-06-10T13:30:32+02:00",
      "identifier": "20240610-45ea546ec72626d76509db55f7844447dce04045",
      "comment": [],
      "keywords": "Fly",
      "name": "Aut corrupti debitis tenetur enim molestiae architecto.",
      "text": "Queen's hedgehog just now, only it ran away when it grunted again, so violently, that she did not at all know whether it was growing, and growing, and growing, and growing, and she looked down at her side. She was looking at everything about her, to pass away the moment she appeared; but she stopped hastily, for the baby, it was out of his tail. 'As if I like being that person, I'll come up: if not, I'll stay down here! It'll be no chance of getting her hands on her hand, and a sad tale!' said the King. The White Rabbit put on his spectacles. 'Where shall I begin, please your Majesty,' said Two, in a few minutes that she had but to get dry very soon. 'Ahem!' said the Gryphon: 'I went to school every day--' 'I'VE been to the seaside once in a hurry that she was in the grass, merely remarking as it was empty: she did not like the wind, and the little dears came jumping merrily along hand in hand with Dinah, and saying to her to begin.' He looked anxiously round, to make out at all a.",
      "url": "https://elab.local:3148/database.php?mode=view&id=51",
      "hasPart": [],
      "mentions": [],
      "genre": "resource",
      "category": "Generated",
      "status": "Maintenance mode"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 4f5f9594",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:47+02:00",
      "dateModified": "2024-06-10T13:31:47+02:00",
      "identifier": "20240610-4f5f9594b82830ff19d8751ec13be98cf485c9d4",
      "comment": [
        {
          "@id": "comment://2024-06-10T13%3A31%3A47%2B02%3A00"
        }
      ],
      "keywords": "demo,test",
      "name": "Testing the eLabFTW lab notebook",
      "text": "<h1>Goal</h1><p>Test the software.</p><h1>Procedure</h1><p>Click everywhere and explore everything.</p><h1>Results</h1><p>It's really nice, I think I'll adopt it for our lab.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=265",
      "hasPart": [],
      "mentions": [
        {
          "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 854e72d3"
        },
        {
          "@id": "./Project-CRYPTO-COOL - An-example-experiment - fc07130d"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - c6bff418"
        },
        {
          "@id": "./Generated - Itaque-accusantium-eos-et - f4d54504"
        },
        {
          "@id": "./Generated - Aut-corrupti-debitis-tenetur-enim-molestiae-architecto - 45ea546e"
        }
      ],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Running",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Raw data URL\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\"}, \"Annie, are you okay\": {\"type\": \"checkbox\", \"value\": \"\", \"description\": \"This is a checkbox custom input\"}, \"This is a custom list input\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"The value is selected from a pre-defined list\"}}}"
        },
        {
          "propertyID": "Raw data URL",
          "valueReference": "url",
          "value": "https://datalake.example.com/experiments/3921"
        },
        {
          "propertyID": "Annie, are you okay",
          "valueReference": "checkbox",
          "value": "",
          "description": "This is a checkbox custom input"
        },
        {
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
      "@id": "./Project-CRYPTO-COOL - Synthesis-of-Aspirin - 07102ec6",
      "@type": "Dataset",
      "author": {
        "@id": "person://dc47268b9fef253b139f72dcb2853c584a1e199448f4c9f8a65519373d57b2d2?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:47+02:00",
      "dateModified": "2024-06-10T13:31:47+02:00",
      "identifier": "20240610-07102ec6189d8645491a3f5ddbeb89760eea112e",
      "comment": [],
      "keywords": "chemistry,has-mathjax",
      "name": "Synthesis of Aspirin",
      "text": "<h1>Introduction</h1>\n<p>\nAspirin is a widely used pain-relieving and anti-inflammatory drug. In this experiment, we aimed to synthesize aspirin from salicylic acid and acetic anhydride.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe mixed salicylic acid and acetic anhydride in the presence of a catalyst, sulfuric acid. The reaction produced aspirin and acetic acid, as shown in the following chemical equation:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nAfter the reaction, we purified the aspirin by recrystallization from hot water. The purity of the aspirin was confirmed using thin-layer chromatography (TLC) and melting point analysis.\n</p>\n<h2>Results</h2>\n<p>\nThe yield of aspirin was 80% based on the amount of salicylic acid used. The purity of the aspirin was confirmed using TLC, which showed a single spot corresponding to aspirin. The melting point of the aspirin was 135-136\u00b0C, which is consistent with the literature value of 135-136.5\u00b0C.\n</p>\n<p>\nThe chemical reaction involved in the synthesis of aspirin can be written as:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nThe theoretical yield of aspirin can be calculated using the stoichiometry of the reaction. Assuming that all the salicylic acid reacts and no aspirin is lost during the purification process, the theoretical yield is calculated as follows:\n</p>\n<p>\n$$\\text{Theoretical yield} = \\frac{\\text{moles of salicylic acid used}}{\\text{molar ratio of salicylic acid to aspirin}} \\times \\text{molar mass of aspirin}$$\n</p>\n<p>\nThe actual yield of aspirin can be calculated by dividing the mass of the purified aspirin by the mass of salicylic acid used and multiplying by 100%. The percent yield can be calculated by dividing the actual yield by the theoretical yield and multiplying by 100%.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=264",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-relationship-between-acceleration-and-gravity - d827e2d9",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:47+02:00",
      "dateModified": "2024-06-10T13:31:47+02:00",
      "identifier": "20240610-d827e2d9b90d27c96f669abb72248e7cd5254cb2",
      "comment": [],
      "keywords": "has-mathjax,physics",
      "name": "Testing relationship between acceleration and gravity",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=263",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Effect-of-temperature-on-enzyme-activity - 6b15dada",
      "@type": "Dataset",
      "author": {
        "@id": "person://797dd58d4ee3e5e9c6cc81c28ee2cd60d408a48bded24131581f98fa7de0b141?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:46+02:00",
      "dateModified": "2024-06-10T13:31:46+02:00",
      "identifier": "20240610-6b15dada88df0d9a3b1d6f507dd80dbe26e0987d",
      "comment": [],
      "keywords": "enzymology,test,Project ENZYTEMP",
      "name": "Effect of temperature on enzyme activity",
      "text": "<h1>Effect of Temperature on Enzyme Activity</h1>\n<p>\nEnzymes are biological molecules that catalyze chemical reactions in living organisms. In this experiment, we investigated the effect of temperature on the activity of the enzyme amylase, which catalyzes the hydrolysis of starch into glucose.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe prepared a solution of starch and added a small amount of amylase to the solution. We then incubated the solution at different temperatures, ranging from 4\u00b0C to 70\u00b0C, for 5 minutes. After the incubation period, we added iodine to the solution to detect the presence of starch. The disappearance of the blue-black color of the iodine indicated the breakdown of starch into glucose.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the activity of amylase increased with increasing temperature up to 37\u00b0C, which is the optimum temperature for amylase activity. At temperatures above 37\u00b0C, the activity of amylase decreased rapidly, and at 70\u00b0C, the enzyme was completely denatured and lost its catalytic activity.\n</p>\n<p>\nThe relationship between temperature and enzyme activity can be described by the Arrhenius equation, which relates the rate constant of a reaction to the activation energy and temperature. The equation can be written as:\n</p>\n<p>\n$$k = Ae^{-E_a/RT}$$\n</p>\n<p>\nwhere k is the rate constant, A is the pre-exponential factor, E_a is the activation energy, R is the gas constant, and T is the absolute temperature. The activation energy is the energy required to break the bonds in the reactants and form the products. The rate constant increases with increasing temperature due to the increase in the number of reactant molecules with sufficient kinetic energy to overcome the activation energy barrier.\n</p>\n<p>\nThe effect of temperature on enzyme activity can also be described by the Q10 value, which is the ratio of the reaction rate at a given temperature to the reaction rate at a temperature 10\u00b0C lower. The Q10 value for most enzyme-catalyzed reactions is around 2-3, indicating that the reaction rate doubles or triples with each 10\u00b0C increase in temperature.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=262",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Need to be redone",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - 2937c252",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:46+02:00",
      "dateModified": "2024-06-10T13:31:46+02:00",
      "identifier": "20240610-2937c25256dcd67f55f4ea2c654e10ef02ac8f9e",
      "comment": [],
      "keywords": "CJK,\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8",
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "text": "<p>\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002</p>\n\n<p>\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002</p>\n\n<p>\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002</p>\n\n<p>\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002</p>\n\n<p>\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=261",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - e58fcae3",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:46+02:00",
      "dateModified": "2024-06-10T13:31:46+02:00",
      "identifier": "20240610-e58fcae31c0ac38f1c797a9f711e337cc24bc23d",
      "comment": [],
      "keywords": "synthesis,antimicrobial,chemistry",
      "name": "Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties",
      "text": "<h1>Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties</h1>\n<p>\nThe emergence of drug-resistant bacterial strains has become a major public health concern, highlighting the need for the development of new antimicrobial agents. In this study, we aimed to synthesize a novel organic compound with potential antimicrobial activity.\n</p>\n<h2>Experimental Design</h2>\n<p>\nThe compound was synthesized via a multi-step reaction scheme. The starting material, benzaldehyde, was reacted with aniline in the presence of an acid catalyst to form the intermediate product, N-phenylbenzamide. The intermediate product was then reacted with thionyl chloride to form the corresponding acid chloride. The acid chloride was then reacted with aminoguanidine in the presence of a base catalyst to form the final product, which was purified by recrystallization.\n</p>\n<h2>Characterization</h2>\n<p>\nThe synthesized compound was characterized using various spectroscopic techniques. The melting point of the compound was determined using a melting point apparatus and compared to the literature value. The IR spectrum of the compound was obtained using a Fourier transform infrared spectrometer and compared to the expected spectrum. The NMR spectrum of the compound was obtained using a nuclear magnetic resonance spectrometer and analyzed to confirm the structure of the compound.\n</p>\n<h2>Antimicrobial Activity</h2>\n<p>\nThe antimicrobial activity of the synthesized compound was evaluated against several bacterial strains using the disk diffusion method. The results showed that the compound exhibited significant antimicrobial activity against both Gram-positive and Gram-negative bacteria, suggesting its potential as a new antimicrobial agent.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=260",
      "hasPart": [],
      "mentions": [
        {
          "@id": "./Generated - Itaque-accusantium-eos-et - f4d54504"
        }
      ],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Fail",
      "variableMeasured": null,
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 1,
        "reviewCount": 1
      }
    },
    {
      "@id": "comment://2024-06-10T13%3A31%3A46%2B02%3A00",
      "@type": "Comment",
      "dateCreated": "2024-06-10T13:31:46+02:00",
      "text": "Great results on the DNA extraction. The yield and purity look good. For the wash steps, consider extending the final centrifugation to 3 minutes to ensure no residual buffer. Nice work!",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      }
    },
    {
      "@id": "./RD - Est-eius-ea-ut-facere - d7cf49ba",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:30:13+02:00",
      "dateModified": "2024-06-10T13:30:13+02:00",
      "identifier": "20240610-d7cf49ba1228930ec37d23682f21ff67b49d7312",
      "comment": [],
      "keywords": "FLIM,scientific discovery",
      "name": "Est eius ea ut facere.",
      "text": "Queen of Hearts were seated on their hands and feet, to make it stop. 'Well, I'd hardly finished the first sentence in her hands, and she put them into a pig, and she hastily dried her eyes anxiously fixed on it, for she was going to leave the court; but on the twelfth?' Alice went on, 'that they'd let Dinah stop in the distance, and she jumped up on to the end: then stop.' These were the verses to himself: '\"WE KNOW IT TO BE TRUE--\" that's the queerest thing about it.' 'She's in prison,' the Queen had never heard before, 'Sure then I'm here! Digging for apples, indeed!' said the Queen, and Alice rather unwillingly took the hookah out of sight: 'but it sounds uncommon nonsense.' Alice said to Alice, that she began thinking over other children she knew, who might do very well without--Maybe it's always pepper that had made out that the reason so many lessons to learn! No, I've made up my mind about it; if I'm not particular as to the Cheshire Cat sitting on the English coast you find.",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=32",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "R&D",
      "status": "Fail"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - af6df858",
      "@type": "Dataset",
      "author": {
        "@id": "person://42c713981f75caa8c9d8e3a60c883dc4788c0563de13ba5607a12f385fe534fe?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:45+02:00",
      "dateModified": "2024-06-10T13:31:46+02:00",
      "identifier": "20240610-af6df8588593f3a3189b8564a9105d4246c0011a",
      "comment": [
        {
          "@id": "comment://2024-06-10T13%3A31%3A46%2B02%3A00"
        }
      ],
      "keywords": "test-data,eln,tag with space,special chars {[\u00e9\u00e8\u00c0\u00ae]}:*<>\u00d7\u00f7\u00b1",
      "name": "Gold master experiment",
      "text": "<h1>Level 1 title</h1>\n<h2>Level 2 title</h2>\n<p>The <strong>goal</strong> of this <em>experiment</em> is to have <span style=\"text-decoration:underline;\">all</span> <span style=\"background-color:rgb(241,196,15);color:rgb(224,62,45);\">attributes</span>:</p>\n<ul>\n<li>all extra fields types</li>\n<li>links to experiments and items</li>\n<li>links from experiments and items</li>\n<li>status, category, tags and uploaded files</li>\n</ul>\n<h3>Here is a table</h3>\n<table style=\"border-collapse:collapse;width:100%;\" border=\"1\">\n\n<tr>\n<td>Something</td>\n<td>in H<sub>2</sub></td>\n<td>the</td>\n</tr>\n<tr>\n<td>table</td>\n<td style=\"background-color:rgb(185,106,217);border:2px dashed rgb(224,62,45);\">31<sup>321</sup></td>\n<td>there</td>\n</tr>\n\n</table>\n<p>an emoji: \ud83e\udd2a</p>\n<p>\u221e \u2211</p>\n<h4>An image</h4>\n<p><img src=\"app/download.php?name=example.jpg&amp;f=78/7834c99a3af687a043d7e9c5bec5e4877469748dca1e898892962ab769be562e069204c19f3bf4663dd2f036cd2a9673b8db53702405ad5298a6e1fd78d6d7da.jpg&amp;storage=1\" width=\"173\" height=\"260\" alt=\"7834c99a3af687a043d7e9c5bec5e4877469748dca1e898892962ab769be562e069204c19f3bf4663dd2f036cd2a9673b8db53702405ad5298a6e1fd78d6d7da.jpg&amp;storage=1\"></p>\n<p><a href=\"https://www.elabftw.net/\" target=\"_blank\" rel=\"noreferrer noopener\">A link to elabftw.net</a>.</p>\n<p>\u00a0</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=259",
      "hasPart": [],
      "mentions": [
        {
          "@id": "./RD - Est-eius-ea-ut-facere - d7cf49ba"
        }
      ],
      "genre": "experiment",
      "category": "Project CRYPTO-COOL",
      "status": "Success",
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"elabftw\": {\"display_main_text\": true, \"extra_fields_groups\": [{\"id\": 1, \"name\": \"Group 1\"}, {\"id\": 2, \"name\": \"Group 2\"}, {\"id\": 3, \"name\": \"Last group\"}]}, \"extra_fields\": {\"Number\": {\"type\": \"number\", \"unit\": \"\", \"units\": [], \"value\": \"\", \"group_id\": 2, \"description\": \"no units\"}, \"Type URL\": {\"type\": \"url\", \"value\": \"https://www.elabftw.net\", \"group_id\": 2, \"readonly\": true, \"description\": \"a link (readonly)\"}, \"Just time\": {\"type\": \"time\", \"value\": \"17:00\", \"group_id\": 2, \"description\": \"tea time\"}, \"Some date\": {\"type\": \"date\", \"value\": \"2024-07-14\", \"group_id\": 2, \"description\": \"is a date\"}, \"Type user\": {\"type\": \"users\", \"value\": 1, \"group_id\": 3, \"description\": \"this is a link to a user\"}, \"A checkbox\": {\"type\": \"checkbox\", \"value\": \"on\", \"group_id\": 2, \"description\": \"is checked\"}, \"Email input\": {\"type\": \"email\", \"value\": \"louis@example.com\", \"group_id\": 2, \"description\": \"type email\"}, \"Date and time\": {\"type\": \"datetime-local\", \"value\": \"2024-07-14T13:37\", \"group_id\": 2, \"description\": \"datetime description\"}, \"Radio buttons\": {\"type\": \"radio\", \"value\": \"Oui\", \"options\": [\"Oui\", \"Non\", \"Peut-\u00eatre\"], \"group_id\": 1, \"description\": \"radio description\"}, \"Type resource\": {\"type\": \"items\", \"value\": 208, \"group_id\": 3, \"description\": \"This is a link to a resource\"}, \"A dropdown menu\": {\"type\": \"select\", \"value\": \"Choice 1\", \"options\": [\"Choice 1\", \"Choice 2\", \"Choice 3\"], \"group_id\": 1, \"description\": \"Single select\"}, \"Text input name\": {\"type\": \"text\", \"value\": \"some text\", \"group_id\": 1, \"readonly\": true, \"required\": true, \"description\": \"type text + all attributes\", \"blank_value_on_duplicate\": true}, \"Type experiment\": {\"type\": \"experiments\", \"value\": 373, \"group_id\": 3, \"description\": \"This is a link to an experiment\"}, \"Number with units\": {\"type\": \"number\", \"unit\": \"mM\", \"units\": [\"mM\", \"\u03bcM\", \"nM\"], \"value\": \"\", \"group_id\": 2, \"description\": \"this one has units\"}, \"Unchecked checkbox\": {\"type\": \"checkbox\", \"value\": \"\", \"group_id\": 2, \"description\": \"this one is not checked\"}, \"Multi dropdown menu\": {\"type\": \"select\", \"value\": \"Option 1\", \"options\": [\"Option 1\", \"Option 2\", \"Option 3\"], \"group_id\": 1, \"description\": \"Allows multiple selection\", \"allow_multi_values\": true}}}"
        },
        {
          "propertyID": "Number",
          "valueReference": "number",
          "value": "",
          "description": "no units"
        },
        {
          "propertyID": "Type URL",
          "valueReference": "url",
          "value": "https://www.elabftw.net",
          "description": "a link (readonly)"
        },
        {
          "propertyID": "Just time",
          "valueReference": "time",
          "value": "17:00",
          "description": "tea time"
        },
        {
          "propertyID": "Some date",
          "valueReference": "date",
          "value": "2024-07-14",
          "description": "is a date"
        },
        {
          "propertyID": "Type user",
          "valueReference": "users",
          "value": 1,
          "description": "this is a link to a user"
        },
        {
          "propertyID": "A checkbox",
          "valueReference": "checkbox",
          "value": "on",
          "description": "is checked"
        },
        {
          "propertyID": "Email input",
          "valueReference": "email",
          "value": "louis@example.com",
          "description": "type email"
        },
        {
          "propertyID": "Date and time",
          "valueReference": "datetime-local",
          "value": "2024-07-14T13:37",
          "description": "datetime description"
        },
        {
          "propertyID": "Radio buttons",
          "valueReference": "radio",
          "value": "Oui",
          "description": "radio description"
        },
        {
          "propertyID": "Type resource",
          "valueReference": "items",
          "value": 208,
          "description": "This is a link to a resource"
        },
        {
          "propertyID": "A dropdown menu",
          "valueReference": "select",
          "value": "Choice 1",
          "description": "Single select"
        },
        {
          "propertyID": "Text input name",
          "valueReference": "text",
          "value": "some text",
          "description": "type text + all attributes"
        },
        {
          "propertyID": "Type experiment",
          "valueReference": "experiments",
          "value": 373,
          "description": "This is a link to an experiment"
        },
        {
          "propertyID": "Number with units",
          "valueReference": "number",
          "value": "",
          "description": "this one has units",
          "unitText": "mM"
        },
        {
          "propertyID": "Unchecked checkbox",
          "valueReference": "checkbox",
          "value": "",
          "description": "this one is not checked"
        },
        {
          "propertyID": "Multi dropdown menu",
          "valueReference": "select",
          "value": "Option 1",
          "description": "Allows multiple selection"
        }
      ]
    },
    {
      "@id": "./Support-ticket - Inventore-adipisci-voluptas-recusandae-odit-mollitia - ea44e8de",
      "@type": "Dataset",
      "author": {
        "@id": "person://eeba0a6c30513efca7b8bad8d1ddf8d8d135ec3befade0c517d283cefe76dcd7?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:13+02:00",
      "dateModified": "2024-06-10T13:31:14+02:00",
      "identifier": "20240610-ea44e8dede47e32b8f8ec09d3c697b5e599dca44",
      "comment": [],
      "keywords": "collaboration,Dark Arts,genetics",
      "name": "Inventore adipisci voluptas recusandae odit mollitia.",
      "text": "When she got to the table to measure herself by it, and found in it a very respectful tone, but frowning and making faces at him as he spoke, and then she noticed that one of the house before she got used to say it over) '--yes, that's about the twentieth time that day. 'A likely story indeed!' said the Mock Turtle: 'why, if a dish or kettle had been jumping about like mad things all this time, and was going on, as she added, to herself, as usual. I wonder what they WILL do next! If they had at the top of her head on her hand, and Alice joined the procession, wondering very much what would happen next. The first thing she heard the Queen's ears--' the Rabbit was no one else seemed inclined to say \"HOW DOTH THE LITTLE BUSY BEE,\" but it did not like to go down--Here, Bill! the master says you're to go down--Here, Bill! the master says you're to go on. 'And so these three little sisters,' the Dormouse followed him: the March Hare meekly replied. 'Yes, but some crumbs must have been.",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=204",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Support ticket",
      "status": "Running"
    },
    {
      "@id": "./Project-CASIMIR - Deleniti-dolorem-consequatur-et-cum-harum-vel - f94314ed",
      "@type": "Dataset",
      "author": {
        "@id": "person://eeba0a6c30513efca7b8bad8d1ddf8d8d135ec3befade0c517d283cefe76dcd7?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:13+02:00",
      "dateModified": "2024-06-10T13:31:13+02:00",
      "identifier": "20240610-f94314ed032182477fc1657c64cfa7c7e8d59705",
      "comment": [],
      "keywords": "molecular cloning,scientific literature,COVID-24,cell culture",
      "name": "Deleniti dolorem consequatur et cum harum vel.",
      "text": "White Rabbit with pink eyes ran close by it, and fortunately was just possible it had some kind of rule, 'and vinegar that makes them bitter--and--and barley-sugar and such things that make children sweet-tempered. I only wish people knew that: then they both bowed low, and their slates and pencils had been to the other, saying, in a soothing tone: 'don't be angry about it. And yet I don't remember where.' 'Well, it must be a lesson to you never to lose YOUR temper!' 'Hold your tongue!' said the Duchess, digging her sharp little chin into Alice's head. 'Is that all?' said Alice, who felt ready to talk about wasting IT. It's HIM.' 'I don't even know what to do, and in another minute the whole thing very absurd, but they all stopped and looked at the Gryphon went on, 'What HAVE you been doing here?' 'May it please your Majesty,' said the Dodo, pointing to the executioner: 'fetch her here.' And the moral of that dark hall, and close to them, and was immediately suppressed by the Hatter.",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=203",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "Project CASIMIR",
      "status": "Running"
    },
    {
      "@id": "./Cell-biology - Omnis-explicabo-ipsum-sunt-cumque-ut - 62644cc7/doloremet.json",
      "@type": "File",
      "name": "doloremet.json",
      "alternateName": "86/86d5373337766fefa2f8bb92c818d2ca04f98f1bd4f035be3fb0e030ead1ca1b697f80cfe32ea46711efa0aff7898b22403a537021d0d9c72e5054ae7437dfbc.json",
      "contentSize": 21,
      "sha256": "66bd0965616378a8b4698bf8b01784e7d29f15c7bde4fe86fb4f5dc959cf189c"
    },
    {
      "@id": "./Cell-biology - Omnis-explicabo-ipsum-sunt-cumque-ut - 62644cc7",
      "@type": "Dataset",
      "author": {
        "@id": "person://eeba0a6c30513efca7b8bad8d1ddf8d8d135ec3befade0c517d283cefe76dcd7?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:12+02:00",
      "dateModified": "2024-06-10T13:31:13+02:00",
      "identifier": "20240610-62644cc72ca76182f29237ad4381b2b019d0b354",
      "comment": [],
      "keywords": "Dark Arts,biotechnology,spectroscopy,ethics in research,experimental design",
      "name": "Omnis explicabo ipsum sunt cumque ut.",
      "text": "Majesty!' the soldiers shouted in reply. 'Idiot!' said the last word two or three times over to the confused clamour of the house, quite forgetting her promise. 'Treacle,' said a sleepy voice behind her. 'Collar that Dormouse,' the Queen of Hearts, he stole those tarts, And took them quite away!' 'Consider your verdict,' the King eagerly, and he hurried off. Alice thought over all the jurors had a door leading right into it. 'That's very curious!' she thought. 'But everything's curious today. I think I can remember feeling a little sharp bark just over her head through the neighbouring pool--she could hear the very tones of her sharp little chin. 'I've a right to think,' said Alice indignantly. 'Ah! then yours wasn't a bit of the e--e--evening, Beautiful, beauti--FUL SOUP!' 'Chorus again!' cried the Mouse, in a very hopeful tone though), 'I won't have any rules in particular; at least, if there were TWO little shrieks, and more puzzled, but she could remember them, all these changes.",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=201",
      "hasPart": [
        {
          "@id": "./Cell-biology - Omnis-explicabo-ipsum-sunt-cumque-ut - 62644cc7/doloremet.json"
        }
      ],
      "mentions": [],
      "genre": "experiment",
      "category": "Cell biology",
      "status": "Success"
    },
    {
      "@id": "./RD - Rerum-nisi-eligendi-libero - 8709ac7d",
      "@type": "Dataset",
      "author": {
        "@id": "person://eeba0a6c30513efca7b8bad8d1ddf8d8d135ec3befade0c517d283cefe76dcd7?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:12+02:00",
      "dateModified": "2024-06-10T13:31:12+02:00",
      "identifier": "20240610-8709ac7daee351631ba3b1f01750352b4d2a6858",
      "comment": [],
      "keywords": "molecular cloning,lab techniques,spectroscopy,experimental design",
      "name": "Rerum nisi eligendi libero.",
      "text": "She felt that this could not be denied, so she went on, looking anxiously about her. 'Oh, do let me help to undo it!' 'I shall sit here,' he said, turning to Alice, and she tried hard to whistle to it; but she could not remember ever having heard of uglifying!' it exclaimed. 'You know what they're about!' 'Read them,' said the March Hare moved into the garden, called out 'The race is over!' and they can't prove I did: there's no use in waiting by the time at the Footman's head: it just missed her. Alice caught the flamingo and brought it back, the fight was over, and both creatures hid their faces in their mouths. So they got settled down in an angry voice--the Rabbit's--'Pat! Pat! Where are you?' And then a great thistle, to keep herself from being broken. She hastily put down her flamingo, and began to repeat it, when a sharp hiss made her draw back in their mouths--and they're all over crumbs.' 'You're wrong about the temper of your nose-- What made you so awfully clever?' 'I have.",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=200",
      "hasPart": [],
      "mentions": [],
      "genre": "experiment",
      "category": "R&D",
      "status": "Need to be redone"
    },
    {
      "@id": "./Production - Ducimus-sit-qui-ad-nihil - 0d595a31/velest.json",
      "@type": "File",
      "name": "velest.json",
      "alternateName": "cc/cc9d399b64deca57bd3b3da2dc0a724b96a29b3aac59486a57c48fbe6418a3387de915fb28498c655a300fe91cb62a20998b74c1661d06cd6080ff94642c4628.json",
      "contentSize": 21,
      "sha256": "66bd0965616378a8b4698bf8b01784e7d29f15c7bde4fe86fb4f5dc959cf189c"
    },
    {
      "@id": "./Production - Ducimus-sit-qui-ad-nihil - 0d595a31",
      "@type": "Dataset",
      "author": {
        "@id": "person://eeba0a6c30513efca7b8bad8d1ddf8d8d135ec3befade0c517d283cefe76dcd7?hash_algo=sha256"
      },
      "alternateName": "",
      "dateCreated": "2024-06-10T13:31:12+02:00",
      "dateModified": "2024-06-10T13:31:12+02:00",
      "identifier": "20240610-0d595a3170d5beb94437ca9d770d7acad06c80c7",
      "comment": [],
      "keywords": "hardness testing,molecular biology,cell culture,cell culture techniques",
      "name": "Ducimus sit qui ad nihil.",
      "text": "Mock Turtle. Alice was very uncomfortable, and, as the doubled-up soldiers were always getting up and repeat something now. Tell her to wink with one foot. 'Get up!' said the Mouse, frowning, but very glad that it might appear to others that what you had been anything near the centre of the trees upon her face. 'Wake up, Dormouse!' And they pinched it on both sides at once. The Dormouse slowly opened his eyes were looking up into hers--she could hear the name of nearly everything there. 'That's the most important piece of bread-and-butter in the trial one way up as the rest of my life.' 'You are not attending!' said the cook. The King looked anxiously round, to make ONE respectable person!' Soon her eye fell on a crimson velvet cushion; and, last of all her riper years, the simple and loving heart of her sister, who was passing at the beginning,' the King added in an impatient tone: 'explanations take such a puzzled expression that she was quite out of a well?' The Dormouse had.",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=199",
      "hasPart": [
        {
          "@id": "./Production - Ducimus-sit-qui-ad-nihil - 0d595a31/velest.json"
        }
      ],
      "mentions": [],
      "genre": "experiment",
      "category": "Production",
      "status": "Need to be redone"
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 4f5f9594"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Test-the-grouped-extra-fields - 854e72d3"
        },
        {
          "@id": "./Project-CRYPTO-COOL - An-example-experiment - fc07130d"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - c6bff418"
        },
        {
          "@id": "./Generated - Itaque-accusantium-eos-et - f4d54504"
        },
        {
          "@id": "./Generated - Aut-corrupti-debitis-tenetur-enim-molestiae-architecto - 45ea546e"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Synthesis-of-Aspirin - 07102ec6"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-relationship-between-acceleration-and-gravity - d827e2d9"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Effect-of-temperature-on-enzyme-activity - 6b15dada"
        },
        {
          "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - 2937c252"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - e58fcae3"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Gold-master-experiment - af6df858"
        },
        {
          "@id": "./RD - Est-eius-ea-ut-facere - d7cf49ba"
        },
        {
          "@id": "./Support-ticket - Inventore-adipisci-voluptas-recusandae-odit-mollitia - ea44e8de"
        },
        {
          "@id": "./Project-CASIMIR - Deleniti-dolorem-consequatur-et-cum-harum-vel - f94314ed"
        },
        {
          "@id": "./Cell-biology - Omnis-explicabo-ipsum-sunt-cumque-ut - 62644cc7"
        },
        {
          "@id": "./RD - Rerum-nisi-eligendi-libero - 8709ac7d"
        },
        {
          "@id": "./Production - Ducimus-sit-qui-ad-nihil - 0d595a31"
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
      "@id": "person://dc47268b9fef253b139f72dcb2853c584a1e199448f4c9f8a65519373d57b2d2?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Dudley",
      "familyName": "Brekke",
      "email": "tutu@yopmail.com"
    },
    {
      "@id": "person://797dd58d4ee3e5e9c6cc81c28ee2cd60d408a48bded24131581f98fa7de0b141?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Kian",
      "familyName": "Daugherty",
      "email": "titi@yopmail.com"
    },
    {
      "@id": "person://eeba0a6c30513efca7b8bad8d1ddf8d8d135ec3befade0c517d283cefe76dcd7?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Annalise",
      "familyName": "Zulauf",
      "email": "demo@elabftw.net"
    }
  ]
}
```
