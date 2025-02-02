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
      "datePublished": "2024-12-04T12:17:43.310832",
      "dateCreated": "2024-12-04T12:17:43.310852",
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
        {
          "@id": "./PastasExampleProject/"
        },
        {
          "@id": "./PastasExampleProject/pasta512.png"
        },
        {
          "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/"
        },
        {
          "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/"
        },
        {
          "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/"
        },
        {
          "@id": "./StandardOperatingProcedures/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/"
        }
      ],
      "name": "Exported from PASTA ELN",
      "description": "Exported content from PASTA ELN",
      "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
      "datePublished": "2024-12-04T12:17:43.310891",
      "creator": [
        {
          "@id": "author_Steffen_Brinckmann"
        }
      ]
    },
    {
      "value": "512+/- 3",
      "propertyID": "metaUser.imageHeight",
      "name": "Metauser \u2192 Imageheight",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/pasta512.png_metaUser.imageHeight",
      "unitText": "mm",
      "description": "H\u00f6he des Bildes",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
    },
    {
      "value": "512",
      "propertyID": "metaUser.imageWidth",
      "name": "Metauser \u2192 Imagewidth",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/pasta512.png_metaUser.imageWidth",
      "unitText": "mm",
      "description": "Largeur de l`image",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
    },
    {
      "value": "www.inkscape.org",
      "propertyID": "metaVendor.Software",
      "name": "Metavendor \u2192 Software",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/pasta512.png_metaVendor.Software"
    },
    {
      "value": "png",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/pasta512.png_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-d56b91fb17b14b1f9260e2d88ded7041",
      "name": "pasta512.png",
      "genre": "measurement/image",
      "dateCreated": "2024-12-04T12:09:12.677203",
      "dateModified": "2024-12-04T12:09:12.677216",
      "@id": "./PastasExampleProject/pasta512.png",
      "contentSize": "36341",
      "sha256": "880a4c5cb12b90b91c8aafd49829b588d2befa7406840fff418fc64db7663c70",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/pasta512.png_metaUser.imageHeight"
        },
        {
          "@id": "./PastasExampleProject/pasta512.png_metaUser.imageWidth"
        },
        {
          "@id": "./PastasExampleProject/pasta512.png_metaVendor.Software"
        },
        {
          "@id": "./PastasExampleProject/pasta512.png_metaVendor.fileExtension"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-724dd150de3e43e0bccfde4a1e103cc8",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2024-12-04T12:09:11.667253",
      "dateModified": "2024-12-04T12:09:11.667268",
      "description": "This is hard!",
      "keywords": "TODO",
      "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-42cde5bb1f854c6bb5dee86197e10557",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2024-12-04T12:09:11.673512",
      "dateModified": "2024-12-04T12:09:11.673523",
      "description": "Random comment 1",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-5008991586c34441a7139d29a3dc32e6",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2024-12-04T12:09:11.676193",
      "dateModified": "2024-12-04T12:09:11.676203",
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
      "identifier": "m-9566cb365c9e4477b97f0f0198a555bf",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-12-04T12:09:12.226789",
      "dateModified": "2024-12-04T12:09:12.541639",
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
      "identifier": "x-b53b70c1e7df47d8aa87cc3c95a3c4e8",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2024-12-04T12:09:11.670407",
      "dateModified": "2024-12-04T12:09:11.670419",
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
      "identifier": "--c11a73e4a1f64222900e806a94293d06",
      "name": "story.odt",
      "dateCreated": "2024-12-04T12:09:12.233418",
      "dateModified": "2024-12-04T12:09:12.233431",
      "@id": "./PastasExampleProject/002_DataFiles/story.odt",
      "contentSize": "8417",
      "sha256": "c0aeebc4bdb1f4ce13cb881e70d26738bc354da855067e2bfb2dcbfd6140a730",
      "@type": "File"
    },
    {
      "value": "p-384ed98f6b3f405c8ccc3da3afe5c440",
      "propertyID": ".procedure",
      "name": " \u2192 Procedure",
      "@type": "PropertyValue",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_.procedure",
      "description": "Which procedure was used?"
    },
    {
      "value": "[240, 315]",
      "propertyID": "metaUser.dimension",
      "name": "Metauser \u2192 Dimension",
      "@type": "PropertyValue",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.dimension"
    },
    {
      "value": "75600",
      "propertyID": "metaUser.number pixel",
      "name": "Metauser \u2192 Number pixel",
      "@type": "PropertyValue",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.number pixel"
    },
    {
      "value": "jpg",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-82dc9a8bf328495e985868b061621ea8",
      "name": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "genre": "measurement/image",
      "dateCreated": "2024-12-04T12:09:12.482149",
      "dateModified": "2024-12-04T12:09:12.482167",
      "description": "- Remote image from wikipedia. Used for testing and reference\n- This item links to a procedure that was used for its creation.\n- One can link to samples, etc. to create complex metadata\n- This item also has a rating",
      "keywords": "_3",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "contentSize": "33597",
      "sha256": "4a1a85bf3fed48c6355eb4ec4c8e3e1d48bc23cb6f8e3e78bdbdd28539d2280b",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_.procedure"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.dimension"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaUser.number pixel"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_metaVendor.fileExtension"
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
      "identifier": "m-9566cb365c9e4477b97f0f0198a555bf",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2024-12-04T12:09:12.226789",
      "dateModified": "2024-12-04T12:09:12.541639",
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
      "identifier": "m-e783e307d1264a04817e5474e7cdb0d4",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2024-12-04T12:09:12.189541",
      "dateModified": "2024-12-04T12:09:12.546167",
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
      "encodingFormat": "text/markdown",
      "identifier": "x-d61e0e3a35c74003a2c5b046d6b46370",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2024-12-04T12:09:11.678834",
      "dateModified": "2024-12-04T12:09:11.678843",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
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
      "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/_.model"
    },
    {
      "value": "Company B",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/_.vendor",
      "description": "Who is the vendor?"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-3e87fced19d34707bf0fc1ddf0acc5e6",
      "name": "Sensor",
      "genre": "instrument/extension",
      "dateCreated": "2024-12-04T12:09:12.083947",
      "dateModified": "2024-12-04T12:09:12.083957",
      "description": "Attachment that increases functionality of big instrument",
      "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/_.model"
        },
        {
          "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/_.vendor"
        }
      ]
    },
    {
      "value": "ABC-123",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/_.model"
    },
    {
      "value": "Company A",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/_.vendor",
      "description": "Who is the vendor?"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "i-3fb5056bedd343e18a164c29012f2ad6",
      "name": "Big instrument",
      "genre": "instrument",
      "dateCreated": "2024-12-04T12:09:12.081230",
      "dateModified": "2024-12-04T12:09:12.081238",
      "description": "Instrument onto which attachments can be added",
      "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/_.model"
        },
        {
          "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/_.vendor"
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
      "identifier": "p-384ed98f6b3f405c8ccc3da3afe5c440",
      "name": "Example_SOP.md",
      "genre": "procedure/markdown",
      "dateCreated": "2024-12-04T12:09:12.036751",
      "dateModified": "2024-12-04T12:09:12.036761",
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
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_qrCodes.0"
    },
    {
      "value": "99698708",
      "propertyID": "qrCodes.1",
      "name": "Qrcodes \u2192 1",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_qrCodes.1"
    },
    {
      "value": "A2B2C3",
      "propertyID": ".chemistry",
      "name": " \u2192 Chemistry",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_.chemistry",
      "description": "What is its chemical composition?"
    },
    {
      "value": "4",
      "propertyID": "geometry.height",
      "name": "Geometry \u2192 Height",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_geometry.height",
      "unitText": "mm",
      "description": "Sample height",
      "identifier": "https://schema.org/height"
    },
    {
      "value": "2",
      "propertyID": "geometry.width",
      "name": "Geometry \u2192 Width",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_geometry.width",
      "unitText": "mm",
      "description": "Sample width"
    },
    {
      "value": "6",
      "propertyID": "weight.initial",
      "name": "Weight \u2192 Initial",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_weight.initial"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-d30b50a42dab4673a07ec4f3f1d36fba",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2024-12-04T12:09:12.062031",
      "dateModified": "2024-12-04T12:09:12.062041",
      "description": "this sample has multiple groups of metadata",
      "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_qrCodes.0"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_qrCodes.1"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_.chemistry"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_geometry.height"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_geometry.width"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/_weight.initial"
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
      "identifier": "x-e18f8f4c76234caab7d743b6149ec721",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2024-12-04T12:09:11.635508",
      "dateModified": "2024-12-04T12:09:12.647135",
      "description": "# PASTA-ELN | The favorite ELN for experimental scientists\n - This is an example .eln output for sharing between different ELNs.",
      "keywords": "Important",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/pasta512.png"
        },
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
          "@id": "./PastasExampleProject/i-3e87fced19d34707bf0fc1ddf0acc5e6/"
        },
        {
          "@id": "./PastasExampleProject/i-3fb5056bedd343e18a164c29012f2ad6/"
        },
        {
          "@id": "./StandardOperatingProcedures/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/s-d30b50a42dab4673a07ec4f3f1d36fba/"
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
