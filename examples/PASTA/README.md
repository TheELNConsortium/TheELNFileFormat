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
      "datePublished": "2024-12-03T22:23:31.141317",
      "dateCreated": "2024-12-03T22:23:31.141338",
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
      "description": "Version 3.0.0b2"
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
        "./PastasExampleProject/",
        "./PastasExampleProject/000_ThisIsAnExampleTask/",
        "./PastasExampleProject/001_ThisIsAnotherExampleTask/",
        "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
        "./PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/",
        "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png",
        "./PastasExampleProject/002_DataFiles/",
        "./PastasExampleProject/002_DataFiles/story.odt",
        "./PastasExampleProject/002_DataFiles/simple.csv",
        "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
        "./PastasExampleProject/002_DataFiles/simple.png",
        "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/",
        "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/",
        "./StandardOperatingProcedures/Example_SOP.md",
        "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/"
      ],
      "name": "Exported from PASTA ELN",
      "description": "Exported content from PASTA ELN",
      "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
      "datePublished": "2024-12-03T22:23:31.141360",
      "creator": [
        {
          "@id": "author_Steffen_Brinckmann"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-1be2b8c4657d4df2a251503eaf5f6ea1",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2024-12-02T21:27:33.339750",
      "dateModified": "2024-12-02T21:27:33.339772",
      "description": "This is hard!",
      "keywords": "TODO",
      "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-759a84f865ad4be2bbe51cd21fde0547",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2024-12-02T21:27:33.348665",
      "dateModified": "2024-12-02T21:27:33.348687",
      "description": "Random comment 1",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-15fa62442fa94851b221aaf8816901bf",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2024-12-02T21:27:33.352553",
      "dateModified": "2024-12-02T21:27:33.352568",
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
      "identifier": "m-f62c5dca495648db930c3d2a69c25a61",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-12-02T21:27:34.309051",
      "dateModified": "2024-12-02T21:27:35.261887",
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
      "identifier": "x-a12767dc17994c50b634e565c92c361e",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2024-12-02T21:27:33.344042",
      "dateModified": "2024-12-02T21:27:33.344061",
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
      "identifier": "--71d32be49b674914a7223e566c0c76af",
      "name": "story.odt",
      "dateCreated": "2024-12-02T21:27:34.317495",
      "dateModified": "2024-12-02T21:27:34.317532",
      "@id": "./PastasExampleProject/002_DataFiles/story.odt",
      "contentSize": "8417",
      "sha256": "c0aeebc4bdb1f4ce13cb881e70d26738bc354da855067e2bfb2dcbfd6140a730",
      "@type": "File"
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
      "identifier": "m-339be784fef944c79e41a08f4257e17b",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2024-12-02T21:27:34.251561",
      "dateModified": "2024-12-02T21:27:35.268514",
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
      "value": "p-a3f1c3193b1a45eaaf3dd4e7066b9a29",
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
      "identifier": "m-8f76d0fbec3249caa81b40c499eee628",
      "name": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "genre": "measurement/image",
      "dateCreated": "2024-12-02T21:27:35.177809",
      "dateModified": "2024-12-02T21:27:35.177829",
      "description": "- Remote image from wikipedia. Used for testing and reference\n- This item links to a procedure that was used for its creation.\n- One can link to samples, etc. to create complex metadata\n- This item also has a rating",
      "keywords": "_3",
      "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
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
      "identifier": "m-f62c5dca495648db930c3d2a69c25a61",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-12-02T21:27:34.309051",
      "dateModified": "2024-12-02T21:27:35.261887",
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
      "encodingFormat": "text/markdown",
      "identifier": "x-b320050b04204f39974d5bdea8fb914f",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2024-12-02T21:27:33.356222",
      "dateModified": "2024-12-02T21:27:33.356237",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "https:/upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        }
      ],
      "@id": "./PastasExampleProject/002_DataFiles/",
      "@type": "Dataset"
    },
    {
      "value": "org.comp.98765",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/_.model"
    },
    {
      "value": "Company B",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/_.vendor",
      "description": "Who is the vendor?"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-53814655ee2f4d2a8a25374162d9e35f",
      "name": "Sensor",
      "genre": "instrument/extension",
      "dateCreated": "2024-12-02T21:27:34.087538",
      "dateModified": "2024-12-02T21:27:34.087566",
      "description": "Attachment that increases functionality of big instrument",
      "@id": "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/_.model"
        },
        {
          "@id": "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/_.vendor"
        }
      ]
    },
    {
      "value": "ABC-123",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/_.model"
    },
    {
      "value": "Company A",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/_.vendor",
      "description": "Who is the vendor?"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-a8c8d498d3014371911793c1c2150a36",
      "name": "Big instrument",
      "genre": "instrument",
      "dateCreated": "2024-12-02T21:27:34.082731",
      "dateModified": "2024-12-02T21:27:34.082745",
      "description": "Instrument onto which attachments can be added",
      "@id": "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/_.model"
        },
        {
          "@id": "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/_.vendor"
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
      "identifier": "p-a3f1c3193b1a45eaaf3dd4e7066b9a29",
      "name": "Example_SOP.md",
      "genre": "procedure/markdown",
      "dateCreated": "2024-12-02T21:27:34.021166",
      "dateModified": "2024-12-02T21:27:34.021203",
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
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_qrCodes.0"
    },
    {
      "value": "99698708",
      "propertyID": "qrCodes.1",
      "name": "Qrcodes \u2192 1",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_qrCodes.1"
    },
    {
      "value": "A2B2C3",
      "propertyID": ".chemistry",
      "name": " \u2192 Chemistry",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_.chemistry",
      "description": "What is its chemical composition?"
    },
    {
      "value": "4",
      "propertyID": "geometry.height",
      "name": "Geometry \u2192 Height",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_geometry.height",
      "unitText": "mm",
      "description": "Sample height",
      "identifier": "https://schema.org/height"
    },
    {
      "value": "2",
      "propertyID": "geometry.width",
      "name": "Geometry \u2192 Width",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_geometry.width",
      "unitText": "mm",
      "description": "Sample width"
    },
    {
      "value": "6",
      "propertyID": "weight.initial",
      "name": "Weight \u2192 Initial",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_weight.initial"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-aac7139ff1ce42beb1f9f178b386f825",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2024-12-02T21:27:34.051674",
      "dateModified": "2024-12-02T21:27:34.051691",
      "description": "this sample has multiple groups of metadata",
      "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_qrCodes.0"
        },
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_qrCodes.1"
        },
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_.chemistry"
        },
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_geometry.height"
        },
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_geometry.width"
        },
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/_weight.initial"
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
      "identifier": "x-aa6d010019b84a3881bb7e9fc2532271",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2024-12-02T21:27:33.278036",
      "dateModified": "2024-12-02T21:27:33.278061",
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
          "@id": "./PastasExampleProject/i-53814655ee2f4d2a8a25374162d9e35f/"
        },
        {
          "@id": "./PastasExampleProject/i-a8c8d498d3014371911793c1c2150a36/"
        },
        {
          "@id": "./StandardOperatingProcedures/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/s-aac7139ff1ce42beb1f9f178b386f825/"
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
