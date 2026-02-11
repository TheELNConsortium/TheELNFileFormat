## PASTA ELN
Its home is at: https://github.com/PASTA-ELN

This folder contains two files:
- PASTA.eln an export of the standard example of an installation with samples, measurements, devices, ...
- A gold‑standard sibling triplet consists of an ELN file, a JSON‑LD file, and a Turtle file. The example shows
  that the ELN file fully supersedes the JSON‑LD/Turtle files in terms of content. [more](goldStandard.md)



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
      "datePublished": "2025-10-05T13:46:45.795150",
      "dateCreated": "2025-10-05T13:46:45.795214",
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
      "version": "3.2.1b1"
    },
    {
      "@id": "affiliation_Forschungszentrum J\u00fclich",
      "@type": "Organization",
      "name": "Forschungszentrum J\u00fclich"
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
          "@id": "affiliation_Forschungszentrum J\u00fclich"
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
          "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/example.tif"
        },
        {
          "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/"
        },
        {
          "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/"
        },
        {
          "@id": "./PastasExampleProject/workplan.py"
        },
        {
          "@id": "./CommonFiles/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/procedure.md"
        },
        {
          "@id": "./PastasExampleProject/worklog.log"
        }
      ],
      "name": "Exported from PASTA ELN",
      "description": "Exported content from PASTA ELN",
      "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
      "datePublished": "2025-10-05T13:46:45.795277",
      "creator": [
        {
          "@id": "author_Steffen_Brinckmann"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-302b90b8983d46c5a6b044f1b64ca4b4",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2025-09-30T13:59:35.527369",
      "dateModified": "2025-09-30T13:59:35.527383",
      "description": "This is hard!",
      "keywords": "TODO",
      "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-486467ba5c88479e9daba818747323db",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2025-09-30T13:59:35.535625",
      "dateModified": "2025-09-30T13:59:35.535641",
      "description": "Random comment 1",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-28cdd6245bd94331a845092958cc5d6b",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2025-09-30T13:59:35.539104",
      "dateModified": "2025-09-30T13:59:35.539162",
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
      "identifier": "m-caa8c49495674168b93362dd75da63cc",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2025-09-30T13:59:35.904659",
      "dateModified": "2025-09-30T13:59:36.243134",
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
      "identifier": "x-d955594ae0d5414cb064c072b5e4565c",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2025-09-30T13:59:35.530746",
      "dateModified": "2025-09-30T13:59:35.530759",
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
      "value": "w-8c030d6d07864ce58ab63efc8969234b",
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
      "identifier": "m-31148bcf77fa4dcc83eae7fe4f65eda2",
      "name": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Misc_pollen.jpg/315px-Misc_pollen.jpg",
      "genre": "measurement/image",
      "dateCreated": "2025-09-30T13:59:36.187021",
      "dateModified": "2025-09-30T13:59:36.187033",
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
      "identifier": "m-8bab0f4ebc8545c6a001add863c29837",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2025-09-30T13:59:35.876617",
      "dateModified": "2025-09-30T13:59:36.248293",
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
      "identifier": "m-caa8c49495674168b93362dd75da63cc",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2025-09-30T13:59:35.904659",
      "dateModified": "2025-09-30T13:59:36.243134",
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
      "identifier": "m-f482e5f4ee1e4e67a2d70e1e42f8fef6",
      "name": "example.tif",
      "genre": "measurement/image",
      "dateCreated": "2025-09-30T13:59:35.738269",
      "dateModified": "2025-09-30T13:59:35.738282",
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
      "encodingFormat": "text/markdown",
      "identifier": "x-3d01c1d8d3db4dab83be9a4df48594a1",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2025-09-30T13:59:35.542559",
      "dateModified": "2025-09-30T13:59:35.542571",
      "hasPart": [
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
          "@id": "./PastasExampleProject/002_DataFiles/example.tif"
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
      "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/_.model"
    },
    {
      "value": "Company A",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/_.vendor"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "d-8d5732e15d6d45c8b56c9a84180f9626",
      "name": "Big instrument",
      "genre": "device",
      "dateCreated": "2025-09-30T13:59:35.633891",
      "dateModified": "2025-09-30T13:59:35.633900",
      "description": "Instrument onto which attachments can be added",
      "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/_.model"
        },
        {
          "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/_.vendor"
        }
      ]
    },
    {
      "value": "org.comp.98765",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/_.model"
    },
    {
      "value": "Company B",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/_.vendor"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "d-eda9aadea13b45eda396e565910580db",
      "name": "Sensor",
      "genre": "device/extension",
      "dateCreated": "2025-09-30T13:59:35.637267",
      "dateModified": "2025-09-30T13:59:35.637281",
      "description": "Attachment that increases functionality of big instrument",
      "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/_.model"
        },
        {
          "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/_.vendor"
        }
      ]
    },
    {
      "value": "13214124",
      "propertyID": "qrCodes.0",
      "name": "Qrcodes \u2192 0",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_qrCodes.0"
    },
    {
      "value": "99698708",
      "propertyID": "qrCodes.1",
      "name": "Qrcodes \u2192 1",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_qrCodes.1"
    },
    {
      "value": "A2B2C3",
      "propertyID": ".chemistry",
      "name": " \u2192 Chemistry",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_.chemistry"
    },
    {
      "value": "4",
      "propertyID": "geometry.height",
      "name": "Geometry \u2192 Height",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_geometry.height",
      "unitText": "mm",
      "description": "Sample height",
      "identifier": "https://schema.org/height"
    },
    {
      "value": "2",
      "propertyID": "geometry.width",
      "name": "Geometry \u2192 Width",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_geometry.width",
      "unitText": "mm",
      "description": "Sample width"
    },
    {
      "value": "6",
      "propertyID": "weight.initial",
      "name": "Weight \u2192 Initial",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_weight.initial"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-d6538d1a6de94bc386bba54e268f7299",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2025-09-30T13:59:35.609750",
      "dateModified": "2025-09-30T13:59:35.609760",
      "description": "this sample has multiple groups of metadata",
      "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/",
      "@type": "Dataset",
      "variableMeasured": [
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_qrCodes.0"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_qrCodes.1"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_.chemistry"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_geometry.height"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_geometry.width"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/_weight.initial"
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
      "identifier": "w-7f4c698b0d854a4490e4cc2b63e6763b",
      "name": "workplan.py",
      "genre": "workflow/workplan",
      "dateCreated": "2025-09-30T13:59:35.588600",
      "dateModified": "2025-09-30T13:59:35.588620",
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
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./CommonFiles/Example_SOP.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-8c030d6d07864ce58ab63efc8969234b",
      "name": "Example_SOP.md",
      "genre": "workflow/procedure/markdown",
      "dateCreated": "2025-09-30T13:59:35.556360",
      "dateModified": "2025-09-30T13:59:35.556373",
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
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/procedure.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-8d5f188afaba42f49cc1303b1f6c4362",
      "name": "procedure.md",
      "genre": "workflow/procedure/markdown",
      "dateCreated": "2025-09-30T13:59:35.581810",
      "dateModified": "2025-09-30T13:59:35.581905",
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
      "value": "log",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "./PastasExampleProject/worklog.log_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-d5847c97687e4440aefe61151225ea36",
      "name": "worklog.log",
      "genre": "workflow/worklog",
      "dateCreated": "2025-09-30T13:59:35.594870",
      "dateModified": "2025-09-30T13:59:35.594891",
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
      "identifier": "x-3221d4ff68ea45be85fb6d753f01f328",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2025-09-30T13:59:35.471250",
      "dateModified": "2025-09-30T13:59:35.471267",
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
          "@id": "./PastasExampleProject/d-8d5732e15d6d45c8b56c9a84180f9626/"
        },
        {
          "@id": "./PastasExampleProject/d-eda9aadea13b45eda396e565910580db/"
        },
        {
          "@id": "./PastasExampleProject/s-d6538d1a6de94bc386bba54e268f7299/"
        },
        {
          "@id": "./PastasExampleProject/workplan.py"
        },
        {
          "@id": "./CommonFiles/Example_SOP.md"
        },
        {
          "@id": "./PastasExampleProject/procedure.md"
        },
        {
          "@id": "./PastasExampleProject/worklog.log"
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

### goldStandard.eln
```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@type": "Organization",
      "name": "Chemie, Ludwig-Maximilians-Universit\u00e4t M\u00fcnchen, Germany",
      "identifier": "https://ror.org/05591te55",
      "@id": "Organization_Chemie_LudwigMaximiliansUniversitt_Mnchen_Germany"
    },
    {
      "@type": "Person",
      "name": "Rachel Jan\u00dfen",
      "familyName": "Jan\u00dfen",
      "givenName": "Rachel",
      "@id": "Person_Rachel_Janen",
      "worksFor": {
        "@id": "Organization_Chemie_LudwigMaximiliansUniversitt_Mnchen_Germany"
      }
    },
    {
      "@type": "Person",
      "name": "Violeta Aleksandrova Vetsova",
      "familyName": "Vetsova",
      "givenName": "Violeta Aleksandrova",
      "identifier": "https://orcid.org/0000-0002-4631-377X",
      "@id": "Person_Violeta_Aleksandrova_Vetsova",
      "worksFor": {
        "@id": "Organization_Chemie_LudwigMaximiliansUniversitt_Mnchen_Germany"
      }
    },
    {
      "@type": "Person",
      "name": "Dominik Gerold Putz",
      "familyName": "Putz",
      "givenName": "Dominik Gerold",
      "@id": "Person_Dominik_Gerold_Putz",
      "worksFor": {
        "@id": "Organization_Chemie_LudwigMaximiliansUniversitt_Mnchen_Germany"
      }
    },
    {
      "@type": "Person",
      "name": "Peter  Mayer",
      "familyName": "Mayer",
      "givenName": "Peter ",
      "@id": "Person_Peter__Mayer",
      "worksFor": {
        "@id": "Organization_Chemie_LudwigMaximiliansUniversitt_Mnchen_Germany"
      }
    },
    {
      "@type": "Person",
      "name": "Lena J. Daumann",
      "familyName": "Daumann",
      "givenName": "Lena J.",
      "@id": "Person_Lena_J_Daumann",
      "worksFor": {
        "@id": "Organization_Chemie_LudwigMaximiliansUniversitt_Mnchen_Germany"
      }
    },
    {
      "@type": "Organization",
      "name": "chemotion-repository",
      "logo": "https://www.chemotion-repository.net/images/repo/Chemotion-V1.png",
      "url": "https://www.chemotion-repository.net",
      "@id": "Organization_chemotionrepository"
    },
    {
      "@type": "CreativeWork",
      "name": "Total synthesis of the quinonoid alcohol dehydrogenase coenzyme (1) of methylotrophic bacteria",
      "url": "https://doi.org/10.1021/ja00408a067",
      "@id": "CreativeWork_Total_synthesis_of_the_quinonoid_alcohol_dehydrogenase_coenzyme_1_of_methylotrophic_bacteria",
      "authors": "Corey, E. J. and Tramontano, Alfonso"
    },
    {
      "@type": "CreativeWork",
      "@id": "https://bioschemas.org/types/MolecularEntity/0.3-RELEASE-2019_09_02"
    },
    {
      "@id": "QuantitativeValue_1",
      "@type": "PropertyValue",
      "value": 128.12592,
      "unitCode": "g/mol",
      "propertyID": "molecularWeight"
    },
    {
      "@type": "MolecularEntity",
      "dct:conformsTo": [
        {
          "@id": "https://bioschemas.org/types/MolecularEntity/0.3-RELEASE-2019_09_02"
        }
      ],
      "smiles": "COC(=O)/C=C/C(=O)C",
      "inChIKey": "GLVNZYODMKSEPS-ONEGZZNKSA-N",
      "inChI": "InChI=1S/C6H8O3/c1-5(7)3-4-6(8)9-2/h3-4H,1-2H3/b4-3+",
      "molecularFormula": "C6H8O3",
      "name": "methyl (E)-4-oxopent-2-enoate",
      "molecularWeight": {
        "@id": "QuantitativeValue_1"
      },
      "iupacName": "methyl (E)-4-oxopent-2-enoate",
      "@id": "GLVNZYODMKSEPS-ONEGZZNKSA-N"
    },
    {
      "@type": "CreativeWork",
      "@id": "https://schema.org/Dataset"
    },
    {
      "@type": "DefinedTermSet",
      "name": "chmo",
      "@id": "http://purl.obolibrary.org/obo/chmo.owl"
    },
    {
      "@type": "DefinedTerm",
      "name": "1H nuclear magnetic resonance spectroscopy",
      "termCode": "CHMO:0000593",
      "@id": "http://purl.obolibrary.org/obo/CHMO_0000593",
      "alternateName": [
        "1H-NMR spectrometry",
        "proton nuclear magnetic resonance spectroscopy",
        "1H-NMR spectroscopy",
        "1H-NMR",
        "1H NMR",
        "1H NMR spectroscopy",
        "1H nuclear magnetic resonance spectrometry",
        "proton NMR"
      ],
      "url": "https://terminology.nfdi4chem.de/ts/ontologies/chmo/terms?iri=http://purl.obolibrary.org/obo/CHMO_0000593",
      "inDefinedTermSet": {
        "@id": "http://purl.obolibrary.org/obo/chmo.owl"
      }
    },
    {
      "@type": "DefinedTermSet",
      "name": "Semanticscience Integrated Ontology",
      "@id": "http://semanticscience.org/ontology/sio.owl"
    },
    {
      "@type": "DefinedTerm",
      "name": "sample",
      "inDefinedTermSet": {
        "@id": "http://semanticscience.org/ontology/sio.owl"
      },
      "@id": "http://semanticscience.org/resource/SIO_001050"
    },
    {
      "@type": "DefinedTerm",
      "name": "chemical reaction",
      "inDefinedTermSet": {
        "@id": "http://semanticscience.org/ontology/sio.owl"
      },
      "@id": "http://semanticscience.org/resource/SIO_010345"
    },
    {
      "@type": "DefinedTermSet",
      "name": "NCI Thesaurus OBO Edition",
      "@id": "http://purl.obolibrary.org/obo/ncit.owl"
    },
    {
      "@type": "DefinedTerm",
      "name": "Analytical Chemistry",
      "alternateName": [
        "Chemistry, Analytical"
      ],
      "inDefinedTermSet": {
        "@id": "http://purl.obolibrary.org/obo/ncit.owl"
      },
      "@id": "http://purl.obolibrary.org/obo/NCIT_C16415"
    },
    {
      "@type": "Organization",
      "name": "Karlsruhe Institute of Technology (KIT)",
      "url": "https://www.kit.edu/",
      "identifier": "https://ror.org/04t3en479",
      "@id": "Organization_Karlsruhe_Institute_of_Technology_KIT"
    },
    {
      "@type": "Person",
      "givenName": "An",
      "familyName": "Nguyen",
      "@id": "https://orcid.org/0000-0002-1692-6778",
      "name": "An Nguyen"
    },
    {
      "@type": "Person",
      "givenName": "Chia-Lin",
      "familyName": "Lin",
      "@id": "https://orcid.org/0000-0002-9772-0455",
      "name": "Chia-Lin Lin"
    },
    {
      "@type": "Person",
      "givenName": "Felix",
      "familyName": "Bach",
      "@id": "https://orcid.org/0000-0002-5035-7978",
      "name": "Felix Bach"
    },
    {
      "@type": "Person",
      "givenName": "Nicole",
      "familyName": "Jung",
      "@id": "https://orcid.org/0000-0001-9513-2468",
      "name": "Nicole Jung"
    },
    {
      "@type": "Person",
      "givenName": "Pei-Chi",
      "familyName": "Huang",
      "@id": "https://orcid.org/0000-0002-9976-4507",
      "name": "Pei-Chi Huang"
    },
    {
      "@type": "Person",
      "givenName": "Pierre",
      "familyName": "Tremouilhac",
      "@id": "https://orcid.org/0000-0002-0487-3947",
      "name": "Pierre Tremouilhac"
    },
    {
      "@type": "Person",
      "givenName": "Stefan",
      "familyName": "Braese",
      "@id": "https://orcid.org/0000-0003-4845-3191",
      "name": "Stefan Braese"
    },
    {
      "@type": "Person",
      "givenName": "Yu-Chieh",
      "familyName": "Huang",
      "@id": "https://orcid.org/0000-0002-4261-9886",
      "name": "Yu-Chieh Huang"
    },
    {
      "@type": "DataCatalog",
      "@id": "https://www.chemotion-repository.net",
      "description": "Repository for samples, reactions and related research data.",
      "name": "Chemotion Repository",
      "provider": {
        "@id": "Organization_Karlsruhe_Institute_of_Technology_KIT"
      },
      "url": "https://www.chemotion-repository.net",
      "license": "https://www.gnu.org/licenses/agpl-3.0.en.html",
      "contributor": [
        {
          "@id": "https://orcid.org/0000-0002-1692-6778"
        },
        {
          "@id": "https://orcid.org/0000-0002-9772-0455"
        },
        {
          "@id": "https://orcid.org/0000-0002-5035-7978"
        },
        {
          "@id": "https://orcid.org/0000-0001-9513-2468"
        },
        {
          "@id": "https://orcid.org/0000-0002-9976-4507"
        },
        {
          "@id": "https://orcid.org/0000-0002-0487-3947"
        },
        {
          "@id": "https://orcid.org/0000-0003-4845-3191"
        },
        {
          "@id": "https://orcid.org/0000-0002-4261-9886"
        }
      ],
      "isAccessibleForFree": true,
      "keywordsList": [
        {
          "@id": "http://semanticscience.org/resource/SIO_001050"
        },
        {
          "@id": "http://semanticscience.org/resource/SIO_010345"
        },
        {
          "@id": "http://purl.obolibrary.org/obo/NCIT_C16415"
        }
      ]
    },
    {
      "@type": "CreativeWork",
      "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
    },
    {
      "@type": "ChemicalSubstance",
      "@id": "10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N.1",
      "identifier": "CRS-25899",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N.1",
      "name": "methyl (E)-4-oxopent-2-enoate",
      "alternateName": "InChI=1S/C6H8O3/c1-5(7)3-4-6(8)9-2/h3-4H,1-2H3/b4-3+",
      "image": "https://www.chemotion-repository.net/images/samples/49c85c066fb3825bc3c07f4205214fe6e099afb0bf615e4238bd53e9d3f000a603ed4d9b87ade4df7be2cf437b9bd3927f144738a4ccf603b5aa3ff4df9e98db.svg",
      "description": "",
      "hasBioChemEntityPart": {
        "@id": "GLVNZYODMKSEPS-ONEGZZNKSA-N"
      }
    },
    {
      "@type": "CreativeWork",
      "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000593",
      "dct:conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "Person_Rachel_Janen"
      },
      "citation": [],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "1H_NMR-1H/",
      "identifier": "CRD-25895",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000593",
      "dct:conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "license": "http://creativecommons.org/licenses/by-sa/4.0/",
      "name": "1H nuclear magnetic resonance spectroscopy (1H NMR)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000593"
      },
      "creator": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ],
      "description": "dataset for 1H nuclear magnetic resonance spectroscopy (1H NMR)\n\n",
      "includedInDataCatalog": {
        "@id": "https://www.chemotion-repository.net"
      },
      "isPartOf": {
        "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000593"
      },
      "instrument": "Bruker Avance III (400 MHz)",
      "hasPart": [
        {
          "@id": "1H_NMR-1H/1H.peak.png"
        },
        {
          "@id": "1H_NMR-1H/1H.jpeg"
        },
        {
          "@id": "1H_NMR-1H/1H.jcamp"
        },
        {
          "@id": "1H_NMR-1H/1H.peak.jdx"
        }
      ],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@type": "DefinedTerm",
      "name": "infrared absorption spectroscopy",
      "termCode": "CHMO:0000630",
      "@id": "http://purl.obolibrary.org/obo/CHMO_0000630",
      "alternateName": [
        "IR absorption spectrometry",
        "infrared (IR) spectroscopy",
        "IR",
        "infra-red absorption spectroscopy",
        "infra-red spectrophotometry",
        "IR spectroscopy",
        "infrared absorption spectrometry",
        "infrared spectrophotometry",
        "IR spectrometry",
        "IR absorption spectroscopy",
        "infra-red spectrometry",
        "infrared spectrometry",
        "infra-red absorption spectrometry",
        "IR spectrophotometry",
        "infrared spectroscopy"
      ],
      "url": "https://terminology.nfdi4chem.de/ts/ontologies/chmo/terms?iri=http://purl.obolibrary.org/obo/CHMO_0000630",
      "inDefinedTermSet": {
        "@id": "http://purl.obolibrary.org/obo/chmo.owl"
      }
    },
    {
      "@type": "CreativeWork",
      "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000630",
      "dct:conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "Person_Rachel_Janen"
      },
      "citation": [],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "IR-RQQIV-V/",
      "identifier": "CRD-25897",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000630",
      "dct:conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "license": "http://creativecommons.org/licenses/by-sa/4.0/",
      "name": "infrared absorption spectroscopy (IR)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000630"
      },
      "creator": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ],
      "description": "dataset for infrared absorption spectroscopy (IR)\n\n",
      "includedInDataCatalog": {
        "@id": "https://www.chemotion-repository.net"
      },
      "isPartOf": {
        "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000630"
      },
      "instrument": "Jasco FT/IR-460Plus with ATR Diamond Plate",
      "hasPart": [
        {
          "@id": "IR-RQQIV-V/IRRQQIV-V.png"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.infer.json"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.peak.jdx"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.dx"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.peak.png"
        }
      ],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@type": "DefinedTerm",
      "name": "high-resolution mass spectrometry",
      "termCode": "CHMO:0000498",
      "@id": "http://purl.obolibrary.org/obo/CHMO_0000498",
      "alternateName": [
        "high-resolution mass spectrometry",
        "HRMS",
        "HR-MS",
        "high resolution mass spectroscopy"
      ],
      "url": "https://terminology.nfdi4chem.de/ts/ontologies/chmo/terms?iri=http://purl.obolibrary.org/obo/CHMO_0000498",
      "inDefinedTermSet": {
        "@id": "http://purl.obolibrary.org/obo/chmo.owl"
      }
    },
    {
      "@type": "CreativeWork",
      "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000498",
      "dct:conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "Person_Rachel_Janen"
      },
      "citation": [],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "HRMS__28EI_29-202206031449161000/",
      "identifier": "CRD-25898",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000498",
      "dct:conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "license": "http://creativecommons.org/licenses/by-sa/4.0/",
      "name": "high-resolution mass spectrometry (HRMS)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000498"
      },
      "creator": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ],
      "description": "dataset for high-resolution mass spectrometry (HRMS)\n\n",
      "includedInDataCatalog": {
        "@id": "https://www.chemotion-repository.net"
      },
      "isPartOf": {
        "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000498"
      },
      "instrument": "Thermo Q Exactive GC, a Thermo Finnigan MAT 95 or a Jeol MStation",
      "hasPart": [
        {
          "@id": "HRMS__28EI_29-202206031449161000/202206031449161000.jpg"
        }
      ],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@type": "DefinedTerm",
      "name": "13C nuclear magnetic resonance spectroscopy",
      "termCode": "CHMO:0000595",
      "@id": "http://purl.obolibrary.org/obo/CHMO_0000595",
      "alternateName": [
        "13C-NMR spectrometry",
        "13C nuclear magnetic resonance spectrometry",
        "13C-NMR spectroscopy",
        "carbon NMR",
        "13C NMR spectroscopy",
        "C-NMR",
        "13C NMR"
      ],
      "url": "https://terminology.nfdi4chem.de/ts/ontologies/chmo/terms?iri=http://purl.obolibrary.org/obo/CHMO_0000595",
      "inDefinedTermSet": {
        "@id": "http://purl.obolibrary.org/obo/chmo.owl"
      }
    },
    {
      "@type": "CreativeWork",
      "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000595",
      "dct:conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "Person_Rachel_Janen"
      },
      "citation": [],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "13C_NMR-13C/",
      "identifier": "CRD-25896",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000595",
      "dct:conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "license": "http://creativecommons.org/licenses/by-sa/4.0/",
      "name": "13C nuclear magnetic resonance spectroscopy (13C NMR)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000595"
      },
      "creator": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ],
      "description": "dataset for 13C nuclear magnetic resonance spectroscopy (13C NMR)\n\n",
      "includedInDataCatalog": {
        "@id": "https://www.chemotion-repository.net"
      },
      "isPartOf": {
        "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000595"
      },
      "instrument": "Bruker Avance III (400 MHz)",
      "hasPart": [
        {
          "@id": "13C_NMR-13C/13C.edit.png"
        },
        {
          "@id": "13C_NMR-13C/13C.jpeg"
        },
        {
          "@id": "13C_NMR-13C/13C.infer.json"
        },
        {
          "@id": "13C_NMR-13C/13C.edit.jdx"
        },
        {
          "@id": "13C_NMR-13C/13C.jcamp"
        }
      ],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "./",
      "identifier": "CRR-25894",
      "url": "https://www.chemotion-repository.net/inchikey/reaction/SA-FUHFF-UHFFFADPSC-GLVNZYODMK-UHFFFADPSC-NUHFF-NSOPS-NUHFF-ZZZ",
      "additionalType": "Reaction",
      "name": "Short-RInChIKey=SA-FUHFF-UAGJVSRUFN-GLVNZYODMK-VCORZAIRCD-NUHFF-NSOPS-NUHFF-ZZZ",
      "creator": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ],
      "description": "",
      "license": "http://creativecommons.org/licenses/by-sa/4.0/",
      "datePublished": "2022-11-02",
      "dateCreated": "2022-08-25",
      "publisher": {
        "@id": "Organization_chemotionrepository"
      },
      "provider": {
        "@id": "Organization_chemotionrepository"
      },
      "keywords": "chemical reaction: structures conditions",
      "citation": [
        {
          "@id": "CreativeWork_Total_synthesis_of_the_quinonoid_alcohol_dehydrogenase_coenzyme_1_of_methylotrophic_bacteria"
        }
      ],
      "subjectOf": [
        {
          "@id": "10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N.1"
        }
      ],
      "hasPart": [
        {
          "@id": "1H_NMR-1H/"
        },
        {
          "@id": "IR-RQQIV-V/"
        },
        {
          "@id": "HRMS__28EI_29-202206031449161000/"
        },
        {
          "@id": "13C_NMR-13C/"
        },
        {
          "@id": "1H_NMR-1H/1H.peak.png"
        },
        {
          "@id": "1H_NMR-1H/1H.jpeg"
        },
        {
          "@id": "1H_NMR-1H/1H.jcamp"
        },
        {
          "@id": "1H_NMR-1H/1H.peak.jdx"
        },
        {
          "@id": "IR-RQQIV-V/IRRQQIV-V.png"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.infer.json"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.peak.jdx"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.dx"
        },
        {
          "@id": "IR-RQQIV-V/IR RAJ15.peak.png"
        },
        {
          "@id": "HRMS__28EI_29-202206031449161000/202206031449161000.jpg"
        },
        {
          "@id": "13C_NMR-13C/13C.edit.png"
        },
        {
          "@id": "13C_NMR-13C/13C.jpeg"
        },
        {
          "@id": "13C_NMR-13C/13C.infer.json"
        },
        {
          "@id": "13C_NMR-13C/13C.edit.jdx"
        },
        {
          "@id": "13C_NMR-13C/13C.jcamp"
        }
      ],
      "authors": [
        {
          "@id": "Person_Rachel_Janen"
        },
        {
          "@id": "Person_Violeta_Aleksandrova_Vetsova"
        },
        {
          "@id": "Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "Person_Peter__Mayer"
        },
        {
          "@id": "Person_Lena_J_Daumann"
        }
      ]
    },
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
      "datePublished": "2025-11-21T13:19:43.554504",
      "dateCreated": "2025-11-21T13:19:43.554516",
      "sdPublisher": {
        "@id": "GOLD_STANDARD_PUBLISHER"
      }
    },
    {
      "@id": "GOLD_STANDARD_PUBLISHER",
      "@type": "Person",
      "givenName": "Steffen",
      "familyName": "Brinckmann",
      "honorificPrefix": "Dr.",
      "email": "s.brinckmann@fz-juelich.de",
      "identifier": "https://orcid.org/0000-0003-0930-082X",
      "name": "Steffen Brinckmann"
    },
    {
      "@id": "1H_NMR-1H/1H.peak.png",
      "@type": "File",
      "name": "1H.peak.png",
      "sha256": "3f716f9ace0138393528585f4be10a15",
      "encodingFormat": "image/png",
      "contentSize": "54255"
    },
    {
      "@id": "1H_NMR-1H/1H.jpeg",
      "@type": "File",
      "name": "1H.jpeg",
      "sha256": "fe6477d2f26890e50ac129f238f93c79",
      "encodingFormat": "image/jpeg",
      "contentSize": "638717"
    },
    {
      "@id": "1H_NMR-1H/1H.jcamp",
      "@type": "File",
      "name": "1H.jcamp",
      "sha256": "2dfb64df27339cfe53a981b51a661122",
      "encodingFormat": "text/plain",
      "contentSize": "619889"
    },
    {
      "@id": "1H_NMR-1H/1H.peak.jdx",
      "@type": "File",
      "name": "1H.peak.jdx",
      "sha256": "eeed3522816561f91392547509d05b93",
      "encodingFormat": "text/plain",
      "contentSize": "662028"
    },
    {
      "@id": "IR-RQQIV-V/IRRQQIV-V.png",
      "@type": "File",
      "name": "IRRQQIV-V.png",
      "sha256": "dadfa0ae152d4b4f24e52a93edd898b8",
      "encodingFormat": "image/png",
      "contentSize": "24907"
    },
    {
      "@id": "IR-RQQIV-V/IR RAJ15.infer.json",
      "@type": "File",
      "name": "IR RAJ15.infer.json",
      "sha256": "RAJ15.infer.json",
      "encodingFormat": "application/json",
      "contentSize": "8712"
    },
    {
      "@id": "IR-RQQIV-V/IR RAJ15.peak.jdx",
      "@type": "File",
      "name": "IR RAJ15.peak.jdx",
      "sha256": "RAJ15.peak.jdx",
      "encodingFormat": "text/plain",
      "contentSize": "34894"
    },
    {
      "@id": "IR-RQQIV-V/IR RAJ15.dx",
      "@type": "File",
      "name": "IR RAJ15.dx",
      "sha256": "RAJ15.dx",
      "encodingFormat": "text/plain",
      "contentSize": "43237"
    },
    {
      "@id": "IR-RQQIV-V/IR RAJ15.peak.png",
      "@type": "File",
      "name": "IR RAJ15.peak.png",
      "sha256": "RAJ15.peak.png",
      "encodingFormat": "image/png",
      "contentSize": "103380"
    },
    {
      "@id": "HRMS__28EI_29-202206031449161000/202206031449161000.jpg",
      "@type": "File",
      "name": "202206031449161000.jpg",
      "sha256": "2fbe8838353c27851c6bb82ac97faee8",
      "encodingFormat": "image/jpeg",
      "contentSize": "606186"
    },
    {
      "@id": "13C_NMR-13C/13C.edit.png",
      "@type": "File",
      "name": "13C.edit.png",
      "sha256": "05d6294393ad34b27fe0b7d646e67ba7",
      "encodingFormat": "image/png",
      "contentSize": "51616"
    },
    {
      "@id": "13C_NMR-13C/13C.jpeg",
      "@type": "File",
      "name": "13C.jpeg",
      "sha256": "2551a4d100498f068723201da7b1d5e9",
      "encodingFormat": "image/jpeg",
      "contentSize": "685470"
    },
    {
      "@id": "13C_NMR-13C/13C.infer.json",
      "@type": "File",
      "name": "13C.infer.json",
      "sha256": "42d64939ddc5990a59bb0f23b78be98f",
      "encodingFormat": "application/json",
      "contentSize": "13074"
    },
    {
      "@id": "13C_NMR-13C/13C.edit.jdx",
      "@type": "File",
      "name": "13C.edit.jdx",
      "sha256": "a52b09233f2818f096c11b03021ed3f7",
      "encodingFormat": "text/plain",
      "contentSize": "471185"
    },
    {
      "@id": "13C_NMR-13C/13C.jcamp",
      "@type": "File",
      "name": "13C.jcamp",
      "sha256": "2a4bc1adcf8492d4f4eb94130ab05056",
      "encodingFormat": "text/plain",
      "contentSize": "567966"
    }
  ]
}
```
