## PASTA ELN
Its home is at: https://github.com/PASTA-ELN



### PASTA.eln
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
      "schemaVersion": "v1.0",
      "version": "1.0",
      "datePublished": "2024-10-06T10:29:10.866306",
      "dateCreated": "2024-10-06T10:29:10.866327",
      "sdPublisher": {
        "@id": "PASTA-ELN"
      }
    },
    {
      "@id": "PASTA-ELN",
      "@type": "Organization",
      "name": "PASTA ELN",
      "logo": "https://raw.githubusercontent.com/PASTA-ELN/desktop/main/pasta.png",
      "slogan": "The favorite ELN for experimental scientists",
      "url": "https://github.com/PASTA-ELN/",
      "description": "Version 2.6.0"
    },
    {
      "@id": "affiliation_Forschungszentrum Juelich",
      "@type": "organization",
      "name": "Forschungszentrum Juelich",
      "RODID": ""
    },
    {
      "@id": "author_Steffen_Brinckmann",
      "@type": "author",
      "firstName": "Steffen",
      "surname": "Brinckmann",
      "title": "Dr.",
      "emailAddress": "s.brinckmann@fz-juelich.de",
      "identifier": "https://orcid.org/0000-0003-0930-082X",
      "affiliation": [
        {
          "@id": "affiliation_Forschungszentrum Juelich"
        }
      ]
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "hasPart": [
        {
          "@id": "./PASTA/PastasExampleProject/"
        }
      ],
      "name": "Exported from PASTA ELN",
      "description": "Exported content from PASTA ELN",
      "license": "CC BY 4.0",
      "datePublished": "2024-10-06T10:29:10.866351",
      "author": [
        {
          "@id": "author_Steffen_Brinckmann"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-f89b1738d4d54b41ba817d32e878ff7d",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2024-10-04T22:28:25.191400",
      "dateModified": "2024-10-04T22:28:25.191412",
      "description": "This is hard!",
      "keywords": "TODO",
      "variableMeasured": [],
      "@id": "./PASTA/PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-8c6826d779e742b08e13c59dba5d8398",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2024-10-04T22:28:25.196977",
      "dateModified": "2024-10-04T22:28:25.196986",
      "description": "Random comment 1",
      "variableMeasured": [],
      "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-2e928cfdb49847b7835bd78959990820",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2024-10-04T22:28:25.199512",
      "dateModified": "2024-10-04T22:28:25.199521",
      "description": "Random comment 2",
      "variableMeasured": [],
      "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-a6ca5dc9077a4bab903bd5b245f14abb",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-10-04T22:28:26.105581",
      "dateModified": "2024-10-04T22:28:26.456138",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / IRI to an ontology node.\n - Units are also supported, obviously.",
      "variableMeasured": [
        {
          "value": "600+/- 3",
          "propertyID": "metaUser.imageHeight",
          "name": "Metauser \u2192 Imageheight",
          "@type": "PropertyValue",
          "unitText": "mm",
          "description": "H\u00f6he des Bildes",
          "mentions": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
        },
        {
          "value": "800",
          "propertyID": "metaUser.imageWidth",
          "name": "Metauser \u2192 Imagewidth",
          "@type": "PropertyValue",
          "unitText": "mm",
          "description": "Largeur de l`image",
          "mentions": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
        },
        {
          "value": "Created with GIMP",
          "propertyID": "metaVendor.Comment",
          "name": "Metavendor \u2192 Comment",
          "@type": "PropertyValue"
        },
        {
          "value": "png",
          "propertyID": "metaVendor.fileExtension",
          "name": "Metavendor \u2192 Fileextension",
          "@type": "PropertyValue"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png",
      "contentSize": "9450",
      "sha256": "e8b9e203eff32379a69bb3785e51a5edce8aa7fc4809c696eae8ddee7bab8210",
      "@type": "File"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-f20c37c6dcfd48de8d0c9ddd4728990a",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2024-10-04T22:28:25.194161",
      "dateModified": "2024-10-04T22:28:25.194170",
      "description": "This will take a long time.",
      "keywords": "WAIT",
      "variableMeasured": [],
      "hasPart": [
        {
          "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/"
        },
        {
          "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/"
        },
        {
          "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "--e7c1326b90be46c090f2c84b7d99dd20",
      "name": "story.odt",
      "dateCreated": "2024-10-04T22:28:26.110297",
      "dateModified": "2024-10-04T22:28:26.110310",
      "variableMeasured": [],
      "@id": "./PASTA/PastasExampleProject/002_DataFiles/story.odt",
      "contentSize": "8417",
      "sha256": "c0aeebc4bdb1f4ce13cb881e70d26738bc354da855067e2bfb2dcbfd6140a730",
      "@type": "File"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-95d4ec8bd9b34d5a8385f0b389294574",
      "name": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "genre": "measurement/image",
      "dateCreated": "2024-10-04T22:28:26.404401",
      "dateModified": "2024-10-04T22:28:26.404414",
      "description": "- Remote image from wikipedia. Used for testing and reference\n- This item links to a procedure that was used for its creation.\n- One can link to samples, etc. to create complex metadata\n- This item also has a rating",
      "keywords": "_3",
      "variableMeasured": [
        {
          "value": "p-736c0b6b15a84313b4b0b52259f0db4f",
          "propertyID": ".procedure",
          "name": " \u2192 Procedure",
          "@type": "PropertyValue",
          "description": "Which procedure was used?"
        },
        {
          "value": "[240, 315]",
          "propertyID": "metaUser.dimension",
          "name": "Metauser \u2192 Dimension",
          "@type": "PropertyValue"
        },
        {
          "value": "75600",
          "propertyID": "metaUser.number pixel",
          "name": "Metauser \u2192 Number pixel",
          "@type": "PropertyValue"
        },
        {
          "value": "jpg",
          "propertyID": "metaVendor.fileExtension",
          "name": "Metavendor \u2192 Fileextension",
          "@type": "PropertyValue"
        }
      ],
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "contentSize": "33597",
      "sha256": "4a1a85bf3fed48c6355eb4ec4c8e3e1d48bc23cb6f8e3e78bdbdd28539d2280b",
      "@type": "File"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-a6ca5dc9077a4bab903bd5b245f14abb",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-10-04T22:28:26.105581",
      "dateModified": "2024-10-04T22:28:26.456138",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / IRI to an ontology node.\n - Units are also supported, obviously.",
      "variableMeasured": [
        {
          "value": "600+/- 3",
          "propertyID": "metaUser.imageHeight",
          "name": "Metauser \u2192 Imageheight",
          "@type": "PropertyValue",
          "unitText": "mm",
          "description": "H\u00f6he des Bildes",
          "mentions": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
        },
        {
          "value": "800",
          "propertyID": "metaUser.imageWidth",
          "name": "Metauser \u2192 Imagewidth",
          "@type": "PropertyValue",
          "unitText": "mm",
          "description": "Largeur de l`image",
          "mentions": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
        },
        {
          "value": "Created with GIMP",
          "propertyID": "metaVendor.Comment",
          "name": "Metavendor \u2192 Comment",
          "@type": "PropertyValue"
        },
        {
          "value": "png",
          "propertyID": "metaVendor.fileExtension",
          "name": "Metavendor \u2192 Fileextension",
          "@type": "PropertyValue"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/002_DataFiles/simple.png",
      "contentSize": "9450",
      "sha256": "e8b9e203eff32379a69bb3785e51a5edce8aa7fc4809c696eae8ddee7bab8210",
      "@type": "File"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-aa748a24078d4ba28d6f9f8176a1ad55",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2024-10-04T22:28:26.071345",
      "dateModified": "2024-10-04T22:28:26.460348",
      "description": "# These .csv files use the simple concept of units for metadata entries",
      "variableMeasured": [
        {
          "value": "0.9996",
          "propertyID": "metaUser.maximumYData",
          "name": "Metauser \u2192 Maximumydata",
          "@type": "PropertyValue",
          "unitText": "m",
          "description": "Maximum y-data"
        },
        {
          "value": "2.5",
          "propertyID": "metaUser.sampleFrequency",
          "name": "Metauser \u2192 Samplefrequency",
          "@type": "PropertyValue",
          "unitText": "Hz",
          "description": "Sample frequency"
        },
        {
          "value": "csv",
          "propertyID": "metaVendor.fileExtension",
          "name": "Metavendor \u2192 Fileextension",
          "@type": "PropertyValue"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/002_DataFiles/simple.csv",
      "contentSize": "187",
      "sha256": "8e31450cd99a013801de9f84e2d3648ec8d70dd0b6d5be23c7cc82782a90ba73",
      "@type": "File"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-f362262170b5456793596fe1b1eb02e9",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2024-10-04T22:28:25.201968",
      "dateModified": "2024-10-04T22:28:25.201976",
      "variableMeasured": [],
      "hasPart": [
        {
          "@id": "./PASTA/PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PASTA/PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PASTA/PastasExampleProject/002_DataFiles/simple.csv"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/002_DataFiles/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-78121f69d3d84a25836b4d406e41826d",
      "name": "Sensor",
      "genre": "instrument/extension",
      "dateCreated": "2024-10-04T22:28:25.972990",
      "dateModified": "2024-10-04T22:28:25.972997",
      "description": "Attachment that increases functionality of big instrument",
      "variableMeasured": [
        {
          "value": "org.comp.98765",
          "propertyID": ".model",
          "name": " \u2192 Model",
          "@type": "PropertyValue"
        },
        {
          "value": "Company B",
          "propertyID": ".vendor",
          "name": " \u2192 Vendor",
          "@type": "PropertyValue",
          "description": "Who is the vendor?"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/i-78121f69d3d84a25836b4d406e41826d/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-e04561a6d27b44bebe51d1d56f341fc6",
      "name": "Big instrument",
      "genre": "instrument",
      "dateCreated": "2024-10-04T22:28:25.970513",
      "dateModified": "2024-10-04T22:28:25.970522",
      "description": "Instrument onto which attachments can be added",
      "variableMeasured": [
        {
          "value": "ABC-123",
          "propertyID": ".model",
          "name": " \u2192 Model",
          "@type": "PropertyValue"
        },
        {
          "value": "Company A",
          "propertyID": ".vendor",
          "name": " \u2192 Vendor",
          "@type": "PropertyValue",
          "description": "Who is the vendor?"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/i-e04561a6d27b44bebe51d1d56f341fc6/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "p-736c0b6b15a84313b4b0b52259f0db4f",
      "name": "Example_SOP.md",
      "genre": "procedure/markdown",
      "dateCreated": "2024-10-04T22:28:25.936614",
      "dateModified": "2024-10-04T22:28:25.936625",
      "text": "# Put sample in instrument\n# Do something\nDo not forget to\n- not do anything wrong\n- **USE BOLD LETTERS**",
      "keywords": "v1",
      "variableMeasured": [
        {
          "value": "md",
          "propertyID": "metaVendor.fileExtension",
          "name": "Metavendor \u2192 Fileextension",
          "@type": "PropertyValue"
        }
      ],
      "@id": "./PASTA/StandardOperatingProcedures/Example_SOP.md",
      "contentSize": "106",
      "sha256": "8b2965159885bc2ac7cb3b0be098a140d8c38e86feee425351735ac26b09a941",
      "@type": "File"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-f48b8f49f1f246a39dda615015b0439b",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2024-10-04T22:28:25.952491",
      "dateModified": "2024-10-04T22:28:25.952503",
      "description": "this sample has multiple groups of metadata",
      "variableMeasured": [
        {
          "value": "13214124",
          "propertyID": "qrCodes.0",
          "name": "Qrcodes \u2192 0",
          "@type": "PropertyValue"
        },
        {
          "value": "99698708",
          "propertyID": "qrCodes.1",
          "name": "Qrcodes \u2192 1",
          "@type": "PropertyValue"
        },
        {
          "value": "A2B2C3",
          "propertyID": ".chemistry",
          "name": " \u2192 Chemistry",
          "@type": "PropertyValue",
          "description": "What is its chemical composition?"
        },
        {
          "value": "4",
          "propertyID": "geometry.height",
          "name": "Geometry \u2192 Height",
          "@type": "PropertyValue",
          "unitText": "mm",
          "description": "Sample height",
          "mentions": "https://schema.org/height"
        },
        {
          "value": "2",
          "propertyID": "geometry.width",
          "name": "Geometry \u2192 Width",
          "@type": "PropertyValue",
          "unitText": "mm",
          "description": "Sample width"
        },
        {
          "value": "6",
          "propertyID": "weight.initial",
          "name": "Weight \u2192 Initial",
          "@type": "PropertyValue"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/s-f48b8f49f1f246a39dda615015b0439b/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-ca321d38a9e04a12ba3cafae028318ae",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2024-10-04T22:28:25.164323",
      "dateModified": "2024-10-04T22:28:25.164337",
      "description": "Can be used as reference or deleted",
      "keywords": "Important",
      "variableMeasured": [
        {
          "value": "Test if everything is working as intended.",
          "propertyID": ".objective",
          "name": " \u2192 Objective",
          "@type": "PropertyValue",
          "description": "What is the objective?"
        },
        {
          "value": "active",
          "propertyID": ".status",
          "name": " \u2192 Status",
          "@type": "PropertyValue",
          "description": "What is the project status"
        }
      ],
      "hasPart": [
        {
          "@id": "./PASTA/PastasExampleProject/000_ThisIsAnExampleTask/"
        },
        {
          "@id": "./PASTA/PastasExampleProject/001_ThisIsAnotherExampleTask/"
        },
        {
          "@id": "./PASTA/PastasExampleProject/002_DataFiles/"
        },
        {
          "@id": "./PASTA/PastasExampleProject/i-78121f69d3d84a25836b4d406e41826d/"
        },
        {
          "@id": "./PASTA/PastasExampleProject/i-e04561a6d27b44bebe51d1d56f341fc6/"
        },
        {
          "@id": "./PASTA/StandardOperatingProcedures/Example_SOP.md"
        },
        {
          "@id": "./PASTA/PastasExampleProject/s-f48b8f49f1f246a39dda615015b0439b/"
        }
      ],
      "@id": "./PASTA/PastasExampleProject/",
      "@type": "Dataset"
    }
  ]
}
```
