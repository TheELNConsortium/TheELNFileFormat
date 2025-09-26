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
      "datePublished": "2025-09-26T12:42:43.502266",
      "dateCreated": "2025-09-26T12:42:43.502278",
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
      "description": "Version 3.2.1b1"
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
          "@id": "./PastasExampleProject/002_DataFiles/example.tif"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/"
        },
        {
          "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/"
        },
        {
          "@id": "./CommonFiles/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/workplan.py"
        },
        {
          "@id": "./PastasExampleProject/worklog.log"
        },
        {
          "@id": "./PastasExampleProject/procedure.md"
        }
      ],
      "name": "Exported from PASTA ELN",
      "description": "Exported content from PASTA ELN",
      "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
      "datePublished": "2025-09-26T12:42:43.502295",
      "creator": [
        {
          "@id": "author_Steffen_Brinckmann"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-35f09632895c4b248bcb015ba0e63c00",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2025-09-26T12:42:39.639533",
      "dateModified": "2025-09-26T12:42:39.639547",
      "description": "This is hard!",
      "keywords": "TODO",
      "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-e9e1539277dc468caef6eae5540d0df7",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2025-09-26T12:42:39.646022",
      "dateModified": "2025-09-26T12:42:39.646033",
      "description": "Random comment 1",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-3e4acbd37f8948758dc766fb8da8f1c1",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2025-09-26T12:42:39.648930",
      "dateModified": "2025-09-26T12:42:39.648940",
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
      "identifier": "m-fd5cb84658ae4c3586bbc5e926e25201",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2025-09-26T12:42:39.931150",
      "dateModified": "2025-09-26T12:42:40.194488",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / PURL to an ontology node.\n - Units are also supported, obviously.",
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
      "identifier": "x-09d2a7aa8c6940afa4c656cfe02575ae",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2025-09-26T12:42:39.642697",
      "dateModified": "2025-09-26T12:42:39.642708",
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
      "identifier": "--991c0c1f1af043d787cad64c32c36729",
      "name": "story.odt",
      "dateCreated": "2025-09-26T12:42:39.937157",
      "dateModified": "2025-09-26T12:42:39.937167",
      "@id": "./PastasExampleProject/002_DataFiles/story.odt",
      "contentSize": "8417",
      "sha256": "c0aeebc4bdb1f4ce13cb881e70d26738bc354da855067e2bfb2dcbfd6140a730",
      "@type": "File"
    },
    {
      "value": "raw",
      "propertyID": "metaVendor.compression",
      "name": "Metavendor \u2192 Compression",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/example.tif_metaVendor.compression"
    },
    {
      "value": "tif",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/002_DataFiles/example.tif_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-49490a17f96b4deb8cb3802578456c03",
      "name": "example.tif",
      "genre": "measurement/image",
      "dateCreated": "2025-09-26T12:42:39.804648",
      "dateModified": "2025-09-26T12:42:39.804660",
      "@id": "./PastasExampleProject/002_DataFiles/example.tif",
      "contentSize": "4031",
      "sha256": "375169346c317fc3908616e5fad84efd5c1eba92db1458be55a42e8273ac8a4a",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/example.tif_metaVendor.compression"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/example.tif_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "w-3c021803d8434ba182b88e5ef30265a6",
      "propertyID": ".workflow/procedure",
      "name": " \u2192 Workflow/procedure",
      "@type": "PropertyValue",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_.workflow/procedure"
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
      "identifier": "m-859d6fef5a544b67aac7f2c173dfe01d",
      "name": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "genre": "measurement/image",
      "dateCreated": "2025-09-26T12:42:40.127713",
      "dateModified": "2025-09-26T12:42:40.127731",
      "description": "- Remote image from wikipedia. Used for testing and reference\n- This item links to a procedure that was used for its creation.\n- One can link to samples, etc. to create complex metadata\n- This item also has a rating",
      "keywords": "_3",
      "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg_.workflow/procedure"
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
      "identifier": "m-b56deff707234a588ec80e1d71a52b08",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2025-09-26T12:42:39.907249",
      "dateModified": "2025-09-26T12:42:40.199150",
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
      "identifier": "m-fd5cb84658ae4c3586bbc5e926e25201",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2025-09-26T12:42:39.931150",
      "dateModified": "2025-09-26T12:42:40.194488",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / PURL to an ontology node.\n - Units are also supported, obviously.",
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
      "identifier": "x-8159c636446348a8a32109a32f4fa27d",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2025-09-26T12:42:39.651886",
      "dateModified": "2025-09-26T12:42:39.651896",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/example.tif"
        },
        {
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
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
      "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/_.model"
    },
    {
      "value": "Company B",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/_.vendor"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "d-982e6b9a28204ef5bf7aa8ceb2bf2606",
      "name": "Sensor",
      "genre": "device/extension",
      "dateCreated": "2025-09-26T12:42:39.731854",
      "dateModified": "2025-09-26T12:42:39.731864",
      "description": "Attachment that increases functionality of big instrument",
      "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/_.model"
        },
        {
          "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/_.vendor"
        }
      ]
    },
    {
      "value": "ABC-123",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/_.model"
    },
    {
      "value": "Company A",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/_.vendor"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "d-b11dba4016c64b188484f65dd2aa3ce9",
      "name": "Big instrument",
      "genre": "device",
      "dateCreated": "2025-09-26T12:42:39.728567",
      "dateModified": "2025-09-26T12:42:39.728575",
      "description": "Instrument onto which attachments can be added",
      "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/_.model"
        },
        {
          "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/_.vendor"
        }
      ]
    },
    {
      "value": "13214124",
      "propertyID": "qrCodes.0",
      "name": "Qrcodes \u2192 0",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_qrCodes.0"
    },
    {
      "value": "99698708",
      "propertyID": "qrCodes.1",
      "name": "Qrcodes \u2192 1",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_qrCodes.1"
    },
    {
      "value": "A2B2C3",
      "propertyID": ".chemistry",
      "name": " \u2192 Chemistry",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_.chemistry"
    },
    {
      "value": "4",
      "propertyID": "geometry.height",
      "name": "Geometry \u2192 Height",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_geometry.height",
      "unitText": "mm",
      "description": "Sample height",
      "identifier": "https://schema.org/height"
    },
    {
      "value": "2",
      "propertyID": "geometry.width",
      "name": "Geometry \u2192 Width",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_geometry.width",
      "unitText": "mm",
      "description": "Sample width"
    },
    {
      "value": "6",
      "propertyID": "weight.initial",
      "name": "Weight \u2192 Initial",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_weight.initial"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-4fa8c19b48a54386931840baf36c807a",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2025-09-26T12:42:39.706959",
      "dateModified": "2025-09-26T12:42:39.706969",
      "description": "this sample has multiple groups of metadata",
      "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_qrCodes.0"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_qrCodes.1"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_.chemistry"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_geometry.height"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_geometry.width"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/_weight.initial"
        }
      ]
    },
    {
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./CommonFiles/Example_SOP.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-3c021803d8434ba182b88e5ef30265a6",
      "name": "Example_SOP.md",
      "genre": "workflow/procedure/markdown",
      "dateCreated": "2025-09-26T12:42:39.660928",
      "dateModified": "2025-09-26T12:42:39.660941",
      "text": "# Put sample in instrument\n# Do something\nDo not forget to\n- not do anything wrong\n- **USE BOLD LETTERS**",
      "keywords": "v1",
      "@id": "./CommonFiles/Example_SOP.md",
      "contentSize": "106",
      "sha256": "8b2965159885bc2ac7cb3b0be098a140d8c38e86feee425351735ac26b09a941",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./CommonFiles/Example_SOP.md_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "py",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/workplan.py_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-ac123ef74e0447d5972af24ca1d5b7b6",
      "name": "workplan.py",
      "genre": "workflow/workplan",
      "dateCreated": "2025-09-26T12:42:39.687496",
      "dateModified": "2025-09-26T12:42:39.687509",
      "text": "``` python\n\"\"\" Example workflow for the Sandia Fracture Challenge 3 \"\"\"\n# pylint: skip-file\n# head of workflow: always the same\nfrom urllib.parse import urlparse\nfrom common_workflow_description.commo",
      "@id": "./PastasExampleProject/workplan.py",
      "contentSize": "1926",
      "sha256": "c12f18f0ef845974540a4b00cbf1119c58ce52cc31bbaef4c7cddd79457f1f1c",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/workplan.py_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "log",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/worklog.log_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-ce39b9d778714c58b8aa1fb5862a9dc8",
      "name": "worklog.log",
      "genre": "workflow/worklog",
      "dateCreated": "2025-09-26T12:42:39.691990",
      "dateModified": "2025-09-26T12:42:39.692001",
      "text": "02-21 11:44:54|INFO:Start workflow\n02-21 11:44:54|INFO:Start step sample:{AM_NA_05}  procedure-name:{metallography}  sha256:{aa3df28fb706568036a85375e62ad76149801b141eb07d629422d511fe901735}  paramete",
      "@id": "./PastasExampleProject/worklog.log",
      "contentSize": "14582",
      "sha256": "1b7d679067a8db3aa15eb1eb77bbb19598ec5a7e4c75c08eb160440f47634290",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/worklog.log_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/procedure.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-f446b0bbcf38473c9912b6ba00c59fa0",
      "name": "procedure.md",
      "genre": "workflow/procedure/markdown",
      "dateCreated": "2025-09-26T12:42:39.682297",
      "dateModified": "2025-09-26T12:42:39.682315",
      "text": "# Tensile testing with Doli\n\n- Setup control box at instrument\n  - General information\n  - buttons F1..F3 correspond to three symbols above\n  - PC-mode: use for control by PC\n  - turn knob to get ther",
      "@id": "./PastasExampleProject/procedure.md",
      "contentSize": "1322",
      "sha256": "289a5834171343630e233937eebd907599843e3a6792623ff86363e472def0e1",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/procedure.md_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "Test if everything is working as intended.",
      "propertyID": ".objective",
      "name": " \u2192 Objective",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/_.objective"
    },
    {
      "value": "active",
      "propertyID": ".status",
      "name": " \u2192 Status",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/_.status"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-fab3dddb1ee24c0e91517c5f4658b1f5",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2025-09-26T12:42:39.596656",
      "dateModified": "2025-09-26T12:42:39.596672",
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
          "@id": "./PastasExampleProject/d-982e6b9a28204ef5bf7aa8ceb2bf2606/"
        },
        {
          "@id": "./PastasExampleProject/d-b11dba4016c64b188484f65dd2aa3ce9/"
        },
        {
          "@id": "./PastasExampleProject/s-4fa8c19b48a54386931840baf36c807a/"
        },
        {
          "@id": "./CommonFiles/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/workplan.py"
        },
        {
          "@id": "./PastasExampleProject/worklog.log"
        },
        {
          "@id": "./PastasExampleProject/procedure.md"
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
