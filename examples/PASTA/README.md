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
      "version": "1.0",
      "additionalType": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.1",
      "datePublished": "2024-11-18T12:01:17.749967",
      "dateCreated": "2024-11-18T12:01:17.749988",
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
      "@type": "Person",
      "givenName": "Steffen",
      "familyName": "Brinckmann",
      "honorificPrefix": "Dr.",
      "email": "s.brinckmann@fz-juelich.de",
      "identifier": "https://orcid.org/0000-0003-0930-082X",
      "worksFor": [
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
          "@id": "./PastasExampleProject/"
        }
      ],
      "name": "Exported from PASTA ELN",
      "description": "Exported content from PASTA ELN",
      "license": "CC BY 4.0",
      "datePublished": "2024-11-18T12:01:17.750025",
      "creator": [
        {
          "@id": "author_Steffen_Brinckmann"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-90366d2af32743e2b561c497a5ec6d55",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2024-11-18T11:34:36.139180",
      "dateModified": "2024-11-18T11:34:36.139196",
      "description": "This is hard!",
      "keywords": "TODO",
      "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-c9d34f8f873c4432af18f5ad92d3d14c",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2024-11-18T11:34:36.145184",
      "dateModified": "2024-11-18T11:34:36.145196",
      "description": "Random comment 1",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-ad78bb0f284f430db4feac72c591607a",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2024-11-18T11:34:36.147833",
      "dateModified": "2024-11-18T11:34:36.147845",
      "description": "Random comment 2",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "value": "600+/- 3",
      "propertyID": "metaUser.imageHeight",
      "name": "Metauser \u2192 Imageheight",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageHeight",
      "unitText": "mm",
      "description": "H\u00f6he des Bildes",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
    },
    {
      "value": "800",
      "propertyID": "metaUser.imageWidth",
      "name": "Metauser \u2192 Imagewidth",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageWidth",
      "unitText": "mm",
      "description": "Largeur de l`image",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
    },
    {
      "value": "Created with GIMP",
      "propertyID": "metaVendor.Comment",
      "name": "Metavendor \u2192 Comment",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.Comment"
    },
    {
      "value": "png",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-1bc765f30cdb4c4e8ca51b1833900d52",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-11-18T11:34:38.365111",
      "dateModified": "2024-11-18T11:34:38.776051",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / IRI to an ontology node.\n - Units are also supported, obviously.",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png",
      "contentSize": "9450",
      "sha256": "e8b9e203eff32379a69bb3785e51a5edce8aa7fc4809c696eae8ddee7bab8210",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageHeight"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageWidth"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.Comment"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.fileExtension"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-5b713981122044bba9fc56a410be1a95",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2024-11-18T11:34:36.142174",
      "dateModified": "2024-11-18T11:34:36.142186",
      "description": "This will take a long time.",
      "keywords": "WAIT",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png"
        }
      ],
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "--ccbacd0456bc482aa5aa4bc6fc4cb943",
      "name": "story.odt",
      "dateCreated": "2024-11-18T11:34:38.371784",
      "dateModified": "2024-11-18T11:34:38.371799",
      "@id": "./PastasExampleProject/002_DataFiles/story.odt",
      "contentSize": "8417",
      "sha256": "c0aeebc4bdb1f4ce13cb881e70d26738bc354da855067e2bfb2dcbfd6140a730",
      "@type": "File"
    },
    {
      "value": "600+/- 3",
      "propertyID": "metaUser.imageHeight",
      "name": "Metauser \u2192 Imageheight",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaUser.imageHeight",
      "unitText": "mm",
      "description": "H\u00f6he des Bildes",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
    },
    {
      "value": "800",
      "propertyID": "metaUser.imageWidth",
      "name": "Metauser \u2192 Imagewidth",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaUser.imageWidth",
      "unitText": "mm",
      "description": "Largeur de l`image",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
    },
    {
      "value": "Created with GIMP",
      "propertyID": "metaVendor.Comment",
      "name": "Metavendor \u2192 Comment",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaVendor.Comment"
    },
    {
      "value": "png",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-1bc765f30cdb4c4e8ca51b1833900d52",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-11-18T11:34:38.365111",
      "dateModified": "2024-11-18T11:34:38.776051",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / IRI to an ontology node.\n - Units are also supported, obviously.",
      "@id": "./PastasExampleProject/002_DataFiles/simple.png",
      "contentSize": "9450",
      "sha256": "e8b9e203eff32379a69bb3785e51a5edce8aa7fc4809c696eae8ddee7bab8210",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaUser.imageHeight"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaUser.imageWidth"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaVendor.Comment"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "0.9996",
      "propertyID": "metaUser.maximumYData",
      "name": "Metauser \u2192 Maximumydata",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.csv_metaUser.maximumYData",
      "unitText": "m",
      "description": "Maximum y-data"
    },
    {
      "value": "2.5",
      "propertyID": "metaUser.sampleFrequency",
      "name": "Metauser \u2192 Samplefrequency",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.csv_metaUser.sampleFrequency",
      "unitText": "Hz",
      "description": "Sample frequency"
    },
    {
      "value": "csv",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/simple.csv_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-42caf7586cc2478a81b3c2bf82c7c267",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2024-11-18T11:34:38.320465",
      "dateModified": "2024-11-18T11:34:38.780470",
      "description": "# These .csv files use the simple concept of units for metadata entries",
      "@id": "./PastasExampleProject/002_DataFiles/simple.csv",
      "contentSize": "187",
      "sha256": "8e31450cd99a013801de9f84e2d3648ec8d70dd0b6d5be23c7cc82782a90ba73",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv_metaUser.maximumYData"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv_metaUser.sampleFrequency"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "p-83b0b4b481b74714b0c596ec6bb76e95",
      "propertyID": ".procedure",
      "name": " \u2192 Procedure",
      "@type": "PropertyValue",
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_.procedure",
      "description": "Which procedure was used?"
    },
    {
      "value": "[240, 315]",
      "propertyID": "metaUser.dimension",
      "name": "Metauser \u2192 Dimension",
      "@type": "PropertyValue",
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.dimension"
    },
    {
      "value": "75600",
      "propertyID": "metaUser.number pixel",
      "name": "Metauser \u2192 Number pixel",
      "@type": "PropertyValue",
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.number pixel"
    },
    {
      "value": "jpg",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-5dada88c728049edbd169e0b49101a76",
      "name": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "genre": "measurement/image",
      "dateCreated": "2024-11-18T11:34:38.716354",
      "dateModified": "2024-11-18T11:34:38.716364",
      "description": "- Remote image from wikipedia. Used for testing and reference\n- This item links to a procedure that was used for its creation.\n- One can link to samples, etc. to create complex metadata\n- This item also has a rating",
      "keywords": "_3",
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "contentSize": "33597",
      "sha256": "4a1a85bf3fed48c6355eb4ec4c8e3e1d48bc23cb6f8e3e78bdbdd28539d2280b",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_.procedure"
        },
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.dimension"
        },
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.number pixel"
        },
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaVendor.fileExtension"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-f6fd1e9f09414a12be1d445596ae7061",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2024-11-18T11:34:36.150451",
      "dateModified": "2024-11-18T11:34:36.150461",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        }
      ],
      "@id": "./PastasExampleProject/002_DataFiles/",
      "@type": "Dataset"
    },
    {
      "value": "ABC-123",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-80083e096a7d403fa7c1f5a0ea5df681/_.model"
    },
    {
      "value": "Company A",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-80083e096a7d403fa7c1f5a0ea5df681/_.vendor",
      "description": "Who is the vendor?"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-80083e096a7d403fa7c1f5a0ea5df681",
      "name": "Big instrument",
      "genre": "instrument",
      "dateCreated": "2024-11-18T11:34:37.894156",
      "dateModified": "2024-11-18T11:34:37.894174",
      "description": "Instrument onto which attachments can be added",
      "@id": "./PastasExampleProject/i-80083e096a7d403fa7c1f5a0ea5df681/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/i-80083e096a7d403fa7c1f5a0ea5df681/_.model"
        },
        {
          "@id": "./PastasExampleProject/i-80083e096a7d403fa7c1f5a0ea5df681/_.vendor"
        }
      ]
    },
    {
      "value": "org.comp.98765",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-eca6947f108e46a8a95b89ec04cc4eb5/_.model"
    },
    {
      "value": "Company B",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-eca6947f108e46a8a95b89ec04cc4eb5/_.vendor",
      "description": "Who is the vendor?"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-eca6947f108e46a8a95b89ec04cc4eb5",
      "name": "Sensor",
      "genre": "instrument/extension",
      "dateCreated": "2024-11-18T11:34:37.964046",
      "dateModified": "2024-11-18T11:34:37.964061",
      "description": "Attachment that increases functionality of big instrument",
      "@id": "./PastasExampleProject/i-eca6947f108e46a8a95b89ec04cc4eb5/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/i-eca6947f108e46a8a95b89ec04cc4eb5/_.model"
        },
        {
          "@id": "./PastasExampleProject/i-eca6947f108e46a8a95b89ec04cc4eb5/_.vendor"
        }
      ]
    },
    {
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./StandardOperatingProcedures/Example_SOP.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "p-83b0b4b481b74714b0c596ec6bb76e95",
      "name": "Example_SOP.md",
      "genre": "procedure/markdown",
      "dateCreated": "2024-11-18T11:34:37.535801",
      "dateModified": "2024-11-18T11:34:37.535823",
      "text": "# Put sample in instrument\n# Do something\nDo not forget to\n- not do anything wrong\n- **USE BOLD LETTERS**",
      "keywords": "v1",
      "@id": "./StandardOperatingProcedures/Example_SOP.md",
      "contentSize": "106",
      "sha256": "8b2965159885bc2ac7cb3b0be098a140d8c38e86feee425351735ac26b09a941",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./StandardOperatingProcedures/Example_SOP.md_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "13214124",
      "propertyID": "qrCodes.0",
      "name": "Qrcodes \u2192 0",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_qrCodes.0"
    },
    {
      "value": "99698708",
      "propertyID": "qrCodes.1",
      "name": "Qrcodes \u2192 1",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_qrCodes.1"
    },
    {
      "value": "A2B2C3",
      "propertyID": ".chemistry",
      "name": " \u2192 Chemistry",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_.chemistry",
      "description": "What is its chemical composition?"
    },
    {
      "value": "4",
      "propertyID": "geometry.height",
      "name": "Geometry \u2192 Height",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_geometry.height",
      "unitText": "mm",
      "description": "Sample height",
      "identifier": "https://schema.org/height"
    },
    {
      "value": "2",
      "propertyID": "geometry.width",
      "name": "Geometry \u2192 Width",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_geometry.width",
      "unitText": "mm",
      "description": "Sample width"
    },
    {
      "value": "6",
      "propertyID": "weight.initial",
      "name": "Weight \u2192 Initial",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_weight.initial"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-4e4a1609da71425b895381c5c3192ddb",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2024-11-18T11:34:37.733085",
      "dateModified": "2024-11-18T11:34:37.733104",
      "description": "this sample has multiple groups of metadata",
      "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_qrCodes.0"
        },
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_qrCodes.1"
        },
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_.chemistry"
        },
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_geometry.height"
        },
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_geometry.width"
        },
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/_weight.initial"
        }
      ]
    },
    {
      "value": "Test if everything is working as intended.",
      "propertyID": ".objective",
      "name": " \u2192 Objective",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/_.objective",
      "description": "What is the objective?"
    },
    {
      "value": "active",
      "propertyID": ".status",
      "name": " \u2192 Status",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/_.status",
      "description": "What is the project status"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-03bd11fb8462406a9bb1de11b2e35b19",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2024-11-18T11:34:36.092740",
      "dateModified": "2024-11-18T11:34:36.092756",
      "description": "Can be used as reference or deleted",
      "keywords": "Important",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/"
        },
        {
          "@id": "./PastasExampleProject/i-80083e096a7d403fa7c1f5a0ea5df681/"
        },
        {
          "@id": "./PastasExampleProject/i-eca6947f108e46a8a95b89ec04cc4eb5/"
        },
        {
          "@id": "./StandardOperatingProcedures/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/s-4e4a1609da71425b895381c5c3192ddb/"
        }
      ],
      "@id": "./PastasExampleProject/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/_.objective"
        },
        {
          "@id": "./PastasExampleProject/_.status"
        }
      ]
    }
  ]
}
```
