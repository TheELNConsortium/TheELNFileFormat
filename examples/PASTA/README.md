## PASTA ELN
Its home is at: https://github.com/PASTA-ELN

This folder contains two files:
- PASTA.eln an export of the standard example of an installation with samples, measurements, devices, ...
- A gold‑standard sibling triplet consists of an ELN file, a JSON‑LD file, and a Turtle file. The example shows
  that the ELN file fully supersedes the JSON‑LD/Turtle files in terms of content. [more](goldStandard.md)



### PASTA.eln
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
      "name": "RO-Crate metadata descriptor",
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.2"
      },
      "version": "1.0",
      "datePublished": "2026-09-26T21:57:47.134203",
      "dateCreated": "2026-09-26T21:57:47.134221",
      "sdPublisher": {
        "@id": "#PASTA-ELN"
      }
    },
    {
      "@id": "#PASTA-ELN",
      "@type": "Organization",
      "name": "PASTA-ELN",
      "logo": "https://raw.githubusercontent.com/PASTA-ELN/desktop/main/pasta.png",
      "slogan": "The favorite ELN for experimental scientists",
      "url": "https://github.com/PASTA-ELN/",
      "version": "3.3.0"
    },
    {
      "@id": "#affiliation_Forschungszentrum_J\u00fclich",
      "@type": "Organization",
      "name": "Forschungszentrum J\u00fclich"
    },
    {
      "@id": "#author_Steffen_Brinckmann",
      "@type": "Person",
      "name": "Steffen Brinckmann",
      "givenName": "Steffen",
      "familyName": "Brinckmann",
      "honorificPrefix": "Dr.",
      "email": "s.brinckmann@fz-juelich.de",
      "identifier": "https://orcid.org/0000-0003-0930-082X",
      "worksFor": [
        {
          "@id": "#affiliation_Forschungszentrum_J\u00fclich"
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
          "@id": "https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/example.tif"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        },
        {
          "@id": "./PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/"
        },
        {
          "@id": "./PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/"
        },
        {
          "@id": "./PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/"
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
      "name": "Exported from PASTA-ELN",
      "description": "Exported content from PASTA-ELN",
      "conformsTo": [
        {
          "@id": "https://w3id.org/ro/crate/1.2"
        },
        {
          "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609"
        }
      ],
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
      },
      "datePublished": "2026-09-26T21:57:47.134272",
      "creator": [
        {
          "@id": "#author_Steffen_Brinckmann"
        }
      ],
      "publisher": {
        "@id": "#author_Steffen_Brinckmann"
      }
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-1f1772578dc34e0ba19fc5d2635e4dbb",
      "name": "This is an example task",
      "genre": "folder",
      "dateCreated": "2026-09-26T21:57:37.449867",
      "dateModified": "2026-09-26T21:57:37.449878",
      "description": "This is hard!",
      "keywords": "TODO",
      "@id": "./PastasExampleProject/000_ThisIsAnExampleTask/",
      "@type": "Dataset",
      "hasPart": []
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-83c9450b27044b50a6dc79d33bf1eff2",
      "name": "This is an example subtask",
      "genre": "folder",
      "dateCreated": "2026-09-26T21:57:37.457935",
      "dateModified": "2026-09-26T21:57:37.457957",
      "description": "Random comment 1",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/000_ThisIsAnExampleSubtask/",
      "@type": "Dataset",
      "hasPart": []
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-6441f6fb80544698aec4f36eba31c400",
      "name": "This is another example subtask",
      "genre": "folder",
      "dateCreated": "2026-09-26T21:57:37.462986",
      "dateModified": "2026-09-26T21:57:37.463002",
      "description": "Random comment 2",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/001_ThisIsAnotherExampleSubtask/",
      "@type": "Dataset",
      "hasPart": []
    },
    {
      "value": "600+/- 3",
      "propertyID": "metaUser.imageHeight",
      "name": "Metauser \u2192 Imageheight",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageHeight",
      "unitText": "mm",
      "description": "H\u00f6he des Bildes",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
    },
    {
      "value": "800",
      "propertyID": "metaUser.imageWidth",
      "name": "Metauser \u2192 Imagewidth",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageWidth",
      "unitText": "mm",
      "description": "Largeur de l`image",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
    },
    {
      "value": "Created with GIMP",
      "propertyID": "metaVendor.Comment",
      "name": "Metavendor \u2192 Comment",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.Comment"
    },
    {
      "value": "png",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-ecca0754d56f427c9215f1f383982051",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2026-09-26T21:57:41.245455",
      "dateModified": "2026-09-26T21:57:42.562266",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / PURL to an ontology node.\n - Units are also supported, obviously.",
      "@id": "./PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png",
      "contentSize": "9450",
      "sha256": "e8b9e203eff32379a69bb3785e51a5edce8aa7fc4809c696eae8ddee7bab8210",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageHeight"
        },
        {
          "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaUser.imageWidth"
        },
        {
          "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.Comment"
        },
        {
          "@id": "#PastasExampleProject/001_ThisIsAnotherExampleTask/simple.png_metaVendor.fileExtension"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-2af9a19b16c74668beaae3e416a26f80",
      "name": "This is another example task",
      "genre": "folder",
      "dateCreated": "2026-09-26T21:57:37.453482",
      "dateModified": "2026-09-26T21:57:37.453493",
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
      "identifier": "--f2d5e44e38654a80aaf036d68500bc87",
      "name": "story.odt",
      "dateCreated": "2026-09-26T21:57:39.924646",
      "dateModified": "2026-09-26T21:57:39.924662",
      "@id": "./PastasExampleProject/002_DataFiles/story.odt",
      "contentSize": "8417",
      "sha256": "c0aeebc4bdb1f4ce13cb881e70d26738bc354da855067e2bfb2dcbfd6140a730",
      "@type": "File",
      "description": "story.odt"
    },
    {
      "value": "w-1dd586fc6a48408ab50d15915386191d",
      "propertyID": ".workflow/procedure",
      "name": " \u2192 Workflow/procedure",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_.workflow/procedure"
    },
    {
      "value": "[76, 261, 3]",
      "propertyID": "metaUser.dimension",
      "name": "Metauser \u2192 Dimension",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaUser.dimension"
    },
    {
      "value": "59508",
      "propertyID": "metaUser.number pixel",
      "name": "Metauser \u2192 Number pixel",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaUser.number_pixel"
    },
    {
      "value": "100",
      "propertyID": "metaVendor.adobe",
      "name": "Metavendor \u2192 Adobe",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.adobe"
    },
    {
      "value": "1",
      "propertyID": "metaVendor.adobe_transform",
      "name": "Metavendor \u2192 Adobetransform",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.adobe_transform"
    },
    {
      "value": "[72, 72]",
      "propertyID": "metaVendor.dpi",
      "name": "Metavendor \u2192 Dpi",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.dpi"
    },
    {
      "value": "ExifII*",
      "propertyID": "metaVendor.exif",
      "name": "Metavendor \u2192 Exif",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.exif"
    },
    {
      "value": "jpeg",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.fileExtension"
    },
    {
      "value": "{1028: b'\\x1c\\x01Z\\x00\\x03\\x1b%G\\x1c\\x02\\x00\\x00\\x02\\x00\\x02', 1061: b'\\xfc\\xe1\\x1f\\x89\\xc8\\xb7\\xc9x/4b4\\x07Xw\\xeb'}",
      "propertyID": "metaVendor.photoshop",
      "name": "Metavendor \u2192 Photoshop",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.photoshop"
    },
    {
      "value": "b'<?xpacket begin=\"\\xef\\xbb\\xbf\" id=\"W5M0MpCehiHzreSzNTczkc9d\"?> <x:xmpmeta xmlns:x=\"adobe:ns:meta/\" x:xmptk=\"Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27        \"> <rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"> <rdf:Description rdf:about=\"\" xmlns:xmpMM=\"http://ns.adobe.com/xap/1.0/mm/\" xmlns:stRef=\"http://ns.adobe.com/xap/1.0/sType/ResourceRef#\" xmlns:xmp=\"http://ns.adobe.com/xap/1.0/\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmpMM:OriginalDocumentID=\"uuid:5D20892493BFDB11914A8590D31508C8\" xmpMM:DocumentID=\"xmp.did:B1F24488E66411E89F22B5755E96CFD2\" xmpMM:InstanceID=\"xmp.iid:B1F24487E66411E89F22B5755E96CFD2\" xmp:CreatorTool=\"Adobe Photoshop CC (Windows)\"> <xmpMM:DerivedFrom stRef:instanceID=\"xmp.iid:636b3b83-6d32-8d4c-80af-f7a5fe8457ce\" stRef:documentID=\"adobe:docid:photoshop:5ac9abca-c948-11e7-a90f-a1e19e3527f1\"/> <dc:title> <rdf:Alt> <rdf:li xml:lang=\"x-default\">Druck</rdf:li> </rdf:Alt> </dc:title> </rdf:Description> </rdf:RDF> </x:xmpmeta> <?xpacket end=\"r\"?>'",
      "propertyID": "metaVendor.xmp",
      "name": "Metavendor \u2192 Xmp",
      "@type": "PropertyValue",
      "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.xmp"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-79cf5f3d23774ac3a78d810feacdf18e",
      "name": "https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg",
      "genre": "measurement/image",
      "dateCreated": "2026-09-26T21:57:42.484693",
      "dateModified": "2026-09-26T21:57:42.484713",
      "description": "- Remote image from samplelib. Used for testing and reference\n- This item links to a procedure that was used for its creation.\n- One can link to samples, etc. to create complex metadata\n- This item also has a rating",
      "keywords": "_3",
      "@id": "https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg",
      "url": "https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg",
      "sdDatePublished": "2026-09-26T21:57:47.121976",
      "contentSize": "21232",
      "sha256": "a110ce6536f90eea6f4437566f9d5ff706bc7a1c35cf56702efb05b9c48c3f49",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_.workflow/procedure"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaUser.dimension"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaUser.number_pixel"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.adobe"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.adobe_transform"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.dpi"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.exif"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.fileExtension"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.photoshop"
        },
        {
          "@id": "#https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg_metaVendor.xmp"
        }
      ]
    },
    {
      "value": "0.9996",
      "propertyID": "metaUser.maximumYData",
      "name": "Metauser \u2192 Maximumydata",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.csv_metaUser.maximumYData",
      "unitText": "m",
      "description": "Maximum y-data"
    },
    {
      "value": "2.5",
      "propertyID": "metaUser.sampleFrequency",
      "name": "Metauser \u2192 Samplefrequency",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.csv_metaUser.sampleFrequency",
      "unitText": "Hz",
      "description": "Sample frequency"
    },
    {
      "value": "csv",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.csv_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-80bb5fc7583248468a89eb1ba450a4ad",
      "name": "simple.csv",
      "genre": "measurement/csv/linesAndDots",
      "dateCreated": "2026-09-26T21:57:41.250218",
      "dateModified": "2026-09-26T21:57:42.567606",
      "description": "# These .csv files use the simple concept of units for metadata entries",
      "@id": "./PastasExampleProject/002_DataFiles/simple.csv",
      "contentSize": "187",
      "sha256": "8e31450cd99a013801de9f84e2d3648ec8d70dd0b6d5be23c7cc82782a90ba73",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.csv_metaUser.maximumYData"
        },
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.csv_metaUser.sampleFrequency"
        },
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.csv_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "raw",
      "propertyID": "metaVendor.compression",
      "name": "Metavendor \u2192 Compression",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/example.tif_metaVendor.compression"
    },
    {
      "value": "tif",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/example.tif_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-b52c932e107541ffa9308be6c2534ceb",
      "name": "example.tif",
      "genre": "measurement/image",
      "dateCreated": "2026-09-26T21:57:41.232056",
      "dateModified": "2026-09-26T21:57:41.232070",
      "@id": "./PastasExampleProject/002_DataFiles/example.tif",
      "contentSize": "4031",
      "sha256": "375169346c317fc3908616e5fad84efd5c1eba92db1458be55a42e8273ac8a4a",
      "@type": "File",
      "description": "example.tif",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/002_DataFiles/example.tif_metaVendor.compression"
        },
        {
          "@id": "#PastasExampleProject/002_DataFiles/example.tif_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "600+/- 3",
      "propertyID": "metaUser.imageHeight",
      "name": "Metauser \u2192 Imageheight",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaUser.imageHeight",
      "unitText": "mm",
      "description": "H\u00f6he des Bildes",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002467"
    },
    {
      "value": "800",
      "propertyID": "metaUser.imageWidth",
      "name": "Metauser \u2192 Imagewidth",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaUser.imageWidth",
      "unitText": "mm",
      "description": "Largeur de l`image",
      "identifier": "http://purl.allotrope.org/ontologies/result#AFR_0002468"
    },
    {
      "value": "Created with GIMP",
      "propertyID": "metaVendor.Comment",
      "name": "Metavendor \u2192 Comment",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaVendor.Comment"
    },
    {
      "value": "png",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "m-ecca0754d56f427c9215f1f383982051",
      "name": "simple.png",
      "genre": "measurement/image",
      "dateCreated": "2026-09-26T21:57:41.245455",
      "dateModified": "2026-09-26T21:57:42.562266",
      "description": "# File with two locations\n - The same file can be located in different locations across different projects within one project group.\n - Since it is the same file, they share the same metadata: same comment, same tags, ...\n# These .png files use the data-science concept of schemata and ontology\n - The files have a agreed upon name and a custom convenience name (i.e. in german or french)\n - The also have a PID / PURL to an ontology node.\n - Units are also supported, obviously.",
      "@id": "./PastasExampleProject/002_DataFiles/simple.png",
      "contentSize": "9450",
      "sha256": "e8b9e203eff32379a69bb3785e51a5edce8aa7fc4809c696eae8ddee7bab8210",
      "@type": "File",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaUser.imageHeight"
        },
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaUser.imageWidth"
        },
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaVendor.Comment"
        },
        {
          "@id": "#PastasExampleProject/002_DataFiles/simple.png_metaVendor.fileExtension"
        }
      ]
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-28eac78b77bd4c06846addb3e09af39f",
      "name": "Data files",
      "genre": "folder",
      "dateCreated": "2026-09-26T21:57:37.468075",
      "dateModified": "2026-09-26T21:57:37.468093",
      "hasPart": [
        {
          "@id": "./PastasExampleProject/002_DataFiles/story.odt"
        },
        {
          "@id": "https://www.fz-juelich.de/en/ibg/ibg-1/images/research_groups/general/fz-juelich-logo/@@images/image-261-9d3b36703de5ad2157c50aa585e7d2bf.jpeg"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.csv"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/example.tif"
        },
        {
          "@id": "./PastasExampleProject/002_DataFiles/simple.png"
        }
      ],
      "@id": "./PastasExampleProject/002_DataFiles/",
      "@type": "Dataset",
      "description": "Data files"
    },
    {
      "value": "ABC-123",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/_.model"
    },
    {
      "value": "Company A",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/_.vendor"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "d-03c50a0ddb4d42fe96ed53671e4af71a",
      "name": "Big instrument",
      "genre": "device",
      "dateCreated": "2026-09-26T21:57:39.861638",
      "dateModified": "2026-09-26T21:57:39.861653",
      "description": "Instrument onto which attachments can be added",
      "@id": "./PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/",
      "@type": "Dataset",
      "hasPart": [],
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/_.model"
        },
        {
          "@id": "#PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/_.vendor"
        }
      ]
    },
    {
      "value": "org.comp.98765",
      "propertyID": ".model",
      "name": " \u2192 Model",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/_.model"
    },
    {
      "value": "Company B",
      "propertyID": ".vendor",
      "name": " \u2192 Vendor",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/_.vendor"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "d-4af76e86545d4682902d12e526c1dc8e",
      "name": "Sensor",
      "genre": "device/extension",
      "dateCreated": "2026-09-26T21:57:39.865302",
      "dateModified": "2026-09-26T21:57:39.865316",
      "description": "Attachment that increases functionality of big instrument",
      "@id": "./PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/",
      "@type": "Dataset",
      "hasPart": [],
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/_.model"
        },
        {
          "@id": "#PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/_.vendor"
        }
      ]
    },
    {
      "value": "13214124",
      "propertyID": "qrCodes.0",
      "name": "Qrcodes \u2192 0",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_qrCodes.0"
    },
    {
      "value": "99698708",
      "propertyID": "qrCodes.1",
      "name": "Qrcodes \u2192 1",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_qrCodes.1"
    },
    {
      "value": "A2B2C3",
      "propertyID": ".chemistry",
      "name": " \u2192 Chemistry",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_.chemistry"
    },
    {
      "value": "4",
      "propertyID": "geometry.height",
      "name": "Geometry \u2192 Height",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_geometry.height",
      "unitText": "mm"
    },
    {
      "value": "2",
      "propertyID": "geometry.width",
      "name": "Geometry \u2192 Width",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_geometry.width",
      "unitText": "mm"
    },
    {
      "value": "6",
      "propertyID": "weight.initial",
      "name": "Weight \u2192 Initial",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_weight.initial"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "s-4748c55f9aa04e98bca51dac3d4b2d34",
      "name": "Example sample",
      "genre": "sample",
      "dateCreated": "2026-09-26T21:57:39.835372",
      "dateModified": "2026-09-26T21:57:39.835386",
      "description": "this sample has multiple groups of metadata",
      "@id": "./PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/",
      "@type": "Dataset",
      "hasPart": [],
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_qrCodes.0"
        },
        {
          "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_qrCodes.1"
        },
        {
          "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_.chemistry"
        },
        {
          "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_geometry.height"
        },
        {
          "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_geometry.width"
        },
        {
          "@id": "#PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/_weight.initial"
        }
      ]
    },
    {
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#CommonFiles/Example_SOP.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-1dd586fc6a48408ab50d15915386191d",
      "name": "Example_SOP.md",
      "genre": "workflow/procedure/markdown",
      "dateCreated": "2026-09-26T21:57:38.511597",
      "dateModified": "2026-09-26T21:57:38.511617",
      "text": "# Put sample in instrument\n# Do something\nDo not forget to\n- not do anything wrong\n- **USE BOLD LETTERS**",
      "keywords": "v1",
      "@id": "./CommonFiles/Example_SOP.md",
      "contentSize": "106",
      "sha256": "8b2965159885bc2ac7cb3b0be098a140d8c38e86feee425351735ac26b09a941",
      "@type": "File",
      "description": "Example_SOP.md",
      "variableMeasured": [
        {
          "@id": "#CommonFiles/Example_SOP.md_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "py",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/workplan.py_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-24b8e26b19f74458ab65670c0222e685",
      "name": "workplan.py",
      "genre": "workflow/workplan",
      "dateCreated": "2026-09-26T21:57:39.797797",
      "dateModified": "2026-09-26T21:57:39.797822",
      "text": "``` python\n\"\"\" Example workflow for the Sandia Fracture Challenge 3 \"\"\"\n# pylint: skip-file\n# head of workflow: always the same\nfrom urllib.parse import urlparse\nfrom common_workflow_description.commo",
      "@id": "./PastasExampleProject/workplan.py",
      "contentSize": "1926",
      "sha256": "c12f18f0ef845974540a4b00cbf1119c58ce52cc31bbaef4c7cddd79457f1f1c",
      "@type": "File",
      "description": "workplan.py",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/workplan.py_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "log",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/worklog.log_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-5c82cf2b3b61434d9088a58a2d932194",
      "name": "worklog.log",
      "genre": "workflow/worklog",
      "dateCreated": "2026-09-26T21:57:39.803699",
      "dateModified": "2026-09-26T21:57:39.803718",
      "text": "02-21 11:44:54|INFO:Start workflow\n02-21 11:44:54|INFO:Start step sample:{AM_NA_05}  procedure-name:{metallography}  sha256:{aa3df28fb706568036a85375e62ad76149801b141eb07d629422d511fe901735}  paramete",
      "@id": "./PastasExampleProject/worklog.log",
      "contentSize": "14582",
      "sha256": "1b7d679067a8db3aa15eb1eb77bbb19598ec5a7e4c75c08eb160440f47634290",
      "@type": "File",
      "description": "worklog.log",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/worklog.log_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "md",
      "propertyID": "metaVendor.fileExtension",
      "name": "Metavendor \u2192 Fileextension",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/procedure.md_metaVendor.fileExtension"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "w-a1bf465edd094d75a7bd28fe784ebe30",
      "name": "procedure.md",
      "genre": "workflow/procedure/markdown",
      "dateCreated": "2026-09-26T21:57:39.782664",
      "dateModified": "2026-09-26T21:57:39.782682",
      "text": "# Tensile testing with Doli\n\n- Setup control box at instrument\n  - General information\n  - buttons F1..F3 correspond to three symbols above\n  - PC-mode: use for control by PC\n  - turn knob to get ther",
      "@id": "./PastasExampleProject/procedure.md",
      "contentSize": "1322",
      "sha256": "289a5834171343630e233937eebd907599843e3a6792623ff86363e472def0e1",
      "@type": "File",
      "description": "procedure.md",
      "variableMeasured": [
        {
          "@id": "#PastasExampleProject/procedure.md_metaVendor.fileExtension"
        }
      ]
    },
    {
      "value": "Test if everything is working as intended.",
      "propertyID": ".objective",
      "name": " \u2192 Objective",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/_.objective"
    },
    {
      "value": "active",
      "propertyID": ".status",
      "name": " \u2192 Status",
      "@type": "PropertyValue",
      "@id": "#PastasExampleProject/_.status"
    },
    {
      "encodingFormat": "text/markdown",
      "identifier": "x-42057297962a4a889168535d7ce5bad9",
      "name": "PASTAs Example Project",
      "genre": "folder",
      "dateCreated": "2026-09-26T21:57:37.397079",
      "dateModified": "2026-09-26T21:57:37.397101",
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
          "@id": "./PastasExampleProject/d-03c50a0ddb4d42fe96ed53671e4af71a/"
        },
        {
          "@id": "./PastasExampleProject/d-4af76e86545d4682902d12e526c1dc8e/"
        },
        {
          "@id": "./PastasExampleProject/s-4748c55f9aa04e98bca51dac3d4b2d34/"
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
          "@id": "#PastasExampleProject/_.objective"
        },
        {
          "@id": "#PastasExampleProject/_.status"
        }
      ]
    },
    {
      "@id": "https://w3id.org/ro/crate/1.2",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "RO-Crate 1.2 Specification"
    },
    {
      "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "ELN-File Format 1.2+202609 Specification"
    },
    {
      "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
      "@type": "CreativeWork",
      "name": "CC BY-NC-SA 4.0",
      "description": "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International"
    }
  ]
}
```

### goldStandard.eln
```json
{
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "@graph": [
    {
      "@type": "Organization",
      "name": "Chemie, Ludwig-Maximilians-Universit\u00e4t M\u00fcnchen, Germany",
      "identifier": "https://ror.org/05591te55",
      "@id": "https://ror.org/05591te55"
    },
    {
      "@type": "Person",
      "name": "Rachel Jan\u00dfen",
      "familyName": "Jan\u00dfen",
      "givenName": "Rachel",
      "@id": "#Person_Rachel_Janen",
      "worksFor": {
        "@id": "https://ror.org/05591te55"
      },
      "affiliation": {
        "@id": "https://ror.org/05591te55"
      }
    },
    {
      "@type": "Person",
      "name": "Violeta Aleksandrova Vetsova",
      "familyName": "Vetsova",
      "givenName": "Violeta Aleksandrova",
      "identifier": "https://orcid.org/0000-0002-4631-377X",
      "@id": "https://orcid.org/0000-0002-4631-377X",
      "worksFor": {
        "@id": "https://ror.org/05591te55"
      },
      "affiliation": {
        "@id": "https://ror.org/05591te55"
      }
    },
    {
      "@type": "Person",
      "name": "Dominik Gerold Putz",
      "familyName": "Putz",
      "givenName": "Dominik Gerold",
      "@id": "#Person_Dominik_Gerold_Putz",
      "worksFor": {
        "@id": "https://ror.org/05591te55"
      },
      "affiliation": {
        "@id": "https://ror.org/05591te55"
      }
    },
    {
      "@type": "Person",
      "name": "Peter  Mayer",
      "familyName": "Mayer",
      "givenName": "Peter ",
      "@id": "#Person_Peter__Mayer",
      "worksFor": {
        "@id": "https://ror.org/05591te55"
      },
      "affiliation": {
        "@id": "https://ror.org/05591te55"
      }
    },
    {
      "@type": "Person",
      "name": "Lena J. Daumann",
      "familyName": "Daumann",
      "givenName": "Lena J.",
      "@id": "#Person_Lena_J_Daumann",
      "worksFor": {
        "@id": "https://ror.org/05591te55"
      },
      "affiliation": {
        "@id": "https://ror.org/05591te55"
      }
    },
    {
      "@type": "Organization",
      "name": "chemotion-repository",
      "logo": "https://www.chemotion-repository.net/images/repo/Chemotion-V1.png",
      "url": "https://www.chemotion-repository.net",
      "@id": "#Organization_chemotionrepository"
    },
    {
      "@type": "CreativeWork",
      "name": "Total synthesis of the quinonoid alcohol dehydrogenase coenzyme (1) of methylotrophic bacteria",
      "@id": "https://doi.org/10.1021/ja00408a067"
    },
    {
      "@type": "CreativeWork",
      "@id": "https://bioschemas.org/types/MolecularEntity/0.3-RELEASE-2019_09_02"
    },
    {
      "@id": "#QuantitativeValue_1",
      "@type": "PropertyValue",
      "value": 128.12592,
      "unitCode": "g/mol",
      "propertyID": "molecularWeight",
      "name": "molecular weight"
    },
    {
      "@type": "MolecularEntity",
      "conformsTo": {
        "@id": "https://bioschemas.org/types/MolecularEntity/0.3-RELEASE-2019_09_02"
      },
      "smiles": "COC(=O)/C=C/C(=O)C",
      "inChIKey": "GLVNZYODMKSEPS-ONEGZZNKSA-N",
      "inChI": "InChI=1S/C6H8O3/c1-5(7)3-4-6(8)9-2/h3-4H,1-2H3/b4-3+",
      "molecularFormula": "C6H8O3",
      "name": "methyl (E)-4-oxopent-2-enoate",
      "molecularWeight": {
        "@id": "#QuantitativeValue_1"
      },
      "iupacName": "methyl (E)-4-oxopent-2-enoate",
      "@id": "#GLVNZYODMKSEPS-ONEGZZNKSA-N_"
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
      "alternateName": "Chemistry, Analytical",
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
      "@id": "https://ror.org/04t3en479"
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
        "@id": "https://ror.org/04t3en479"
      },
      "url": "https://www.chemotion-repository.net",
      "license": {
        "@id": "https://www.gnu.org/licenses/agpl-3.0.en.html"
      },
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
      "mentions": [
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
      "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N.1",
      "identifier": "CRS-25899",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N.1",
      "name": "methyl (E)-4-oxopent-2-enoate",
      "alternateName": "InChI=1S/C6H8O3/c1-5(7)3-4-6(8)9-2/h3-4H,1-2H3/b4-3+",
      "image": "https://www.chemotion-repository.net/images/samples/49c85c066fb3825bc3c07f4205214fe6e099afb0bf615e4238bd53e9d3f000a603ed4d9b87ade4df7be2cf437b9bd3927f144738a4ccf603b5aa3ff4df9e98db.svg",
      "description": "",
      "hasBioChemEntityPart": {
        "@id": "#GLVNZYODMKSEPS-ONEGZZNKSA-N_"
      }
    },
    {
      "@type": "CreativeWork",
      "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000593",
      "conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "#Person_Rachel_Janen"
      },
      "citation": [],
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
        }
      ],
      "name": "1H nuclear magnetic resonance spectroscopy (1H NMR)"
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "1H_NMR-1H/",
      "identifier": "CRD-25895",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000593",
      "conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "name": "1H nuclear magnetic resonance spectroscopy (1H NMR)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000593"
      },
      "creator": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
      "conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "#Person_Rachel_Janen"
      },
      "citation": [],
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
        }
      ],
      "name": "infrared absorption spectroscopy (IR)"
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "IR-RQQIV-V/",
      "identifier": "CRD-25897",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000630",
      "conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "name": "infrared absorption spectroscopy (IR)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000630"
      },
      "creator": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
          "@id": "IR-RQQIV-V/IR%20RAJ15.infer.json"
        },
        {
          "@id": "IR-RQQIV-V/IR%20RAJ15.peak.jdx"
        },
        {
          "@id": "IR-RQQIV-V/IR%20RAJ15.dx"
        },
        {
          "@id": "IR-RQQIV-V/IR%20RAJ15.peak.png"
        }
      ],
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
      "conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "#Person_Rachel_Janen"
      },
      "citation": [],
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
        }
      ],
      "name": "high-resolution mass spectrometry (HRMS)"
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "HRMS__28EI_29-202206031449161000/",
      "identifier": "CRD-25898",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000498",
      "conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "name": "high-resolution mass spectrometry (HRMS)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000498"
      },
      "creator": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
      "conformsTo": {
        "@id": "https://bioschemas.org/types/Study/0.3-DRAFT"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "dateCreated": "2022-11-02",
      "datePublished": "2022-11-02",
      "contributor": {
        "@id": "#Person_Rachel_Janen"
      },
      "citation": [],
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
        }
      ],
      "name": "13C nuclear magnetic resonance spectroscopy (13C NMR)"
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "13C_NMR-13C/",
      "identifier": "CRD-25896",
      "url": "https://www.chemotion-repository.net/inchikey/GLVNZYODMKSEPS-ONEGZZNKSA-N/CHMO0000595",
      "conformsTo": {
        "@id": "https://schema.org/Dataset"
      },
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "name": "13C nuclear magnetic resonance spectroscopy (13C NMR)",
      "measurementTechnique": {
        "@id": "http://purl.obolibrary.org/obo/CHMO_0000595"
      },
      "creator": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "Dataset",
      "@id": "./",
      "conformsTo": [
        {
          "@id": "https://w3id.org/ro/crate/1.2"
        },
        {
          "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609"
        }
      ],
      "identifier": "CRR-25894",
      "url": "https://www.chemotion-repository.net/inchikey/reaction/SA-FUHFF-UHFFFADPSC-GLVNZYODMK-UHFFFADPSC-NUHFF-NSOPS-NUHFF-ZZZ",
      "genre": "Reaction",
      "name": "Short-RInChIKey=SA-FUHFF-UAGJVSRUFN-GLVNZYODMK-VCORZAIRCD-NUHFF-NSOPS-NUHFF-ZZZ",
      "creator": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
        }
      ],
      "description": "",
      "license": {
        "@id": "http://creativecommons.org/licenses/by-sa/4.0/"
      },
      "datePublished": "2022-11-02",
      "dateCreated": "2022-08-25",
      "publisher": {
        "@id": "#Organization_chemotionrepository"
      },
      "provider": {
        "@id": "#Organization_chemotionrepository"
      },
      "keywords": "chemical reaction: structures conditions",
      "citation": {
        "@id": "https://doi.org/10.1021/ja00408a067"
      },
      "subjectOf": {
        "@id": "https://doi.org/10.14272/GLVNZYODMKSEPS-ONEGZZNKSA-N.1"
      },
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
          "@id": "IR-RQQIV-V/IR%20RAJ15.infer.json"
        },
        {
          "@id": "IR-RQQIV-V/IR%20RAJ15.peak.jdx"
        },
        {
          "@id": "IR-RQQIV-V/IR%20RAJ15.dx"
        },
        {
          "@id": "IR-RQQIV-V/IR%20RAJ15.peak.png"
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
      "author": [
        {
          "@id": "#Person_Rachel_Janen"
        },
        {
          "@id": "https://orcid.org/0000-0002-4631-377X"
        },
        {
          "@id": "#Person_Dominik_Gerold_Putz"
        },
        {
          "@id": "#Person_Peter__Mayer"
        },
        {
          "@id": "#Person_Lena_J_Daumann"
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
        "@id": "https://w3id.org/ro/crate/1.2"
      },
      "version": "1.0",
      "datePublished": "2025-11-21T13:19:43.554504",
      "dateCreated": "2025-11-21T13:19:43.554516",
      "sdPublisher": {
        "@id": "https://orcid.org/0000-0003-0930-082X"
      }
    },
    {
      "@id": "https://orcid.org/0000-0003-0930-082X",
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
      "sha256": "0133d911b1d8782ea6f6ae5e2f0b5c71b3a161228a7f60f3f9fe00b80dc65c3b",
      "encodingFormat": "image/png",
      "contentSize": "54255"
    },
    {
      "@id": "1H_NMR-1H/1H.jpeg",
      "@type": "File",
      "name": "1H.jpeg",
      "sha256": "8064499073f4eeb2ac90689b0a6e5674b53479ff7b885dec247b5f578660c4ec",
      "encodingFormat": "image/jpeg",
      "contentSize": "638717"
    },
    {
      "@id": "1H_NMR-1H/1H.jcamp",
      "@type": "File",
      "name": "1H.jcamp",
      "sha256": "b323ccd783d7f2cc0708c465fdeee477cf46ae0acc56830fe413cab5872a439d",
      "encodingFormat": "text/plain",
      "contentSize": "619889"
    },
    {
      "@id": "1H_NMR-1H/1H.peak.jdx",
      "@type": "File",
      "name": "1H.peak.jdx",
      "sha256": "1d424f7035dd72aa55772bcfca3a5ce811e76ac2956bc2bccc961d9ebf665488",
      "encodingFormat": "text/plain",
      "contentSize": "662028"
    },
    {
      "@id": "IR-RQQIV-V/IRRQQIV-V.png",
      "@type": "File",
      "name": "IRRQQIV-V.png",
      "sha256": "cd9cdeaceaa9d536e1f5dd8f777a9a51f997795ad8520768db4a7f0898bab77d",
      "encodingFormat": "image/png",
      "contentSize": "24907"
    },
    {
      "@id": "IR-RQQIV-V/IR%20RAJ15.infer.json",
      "@type": "File",
      "name": "IR RAJ15.infer.json",
      "sha256": "cfeef651bf454a2b2b768f087e3816798c75a02519e8def30aef741866e5c813",
      "encodingFormat": "application/json",
      "contentSize": "8712"
    },
    {
      "@id": "IR-RQQIV-V/IR%20RAJ15.peak.jdx",
      "@type": "File",
      "name": "IR RAJ15.peak.jdx",
      "sha256": "571166e048e21051c56f3f5aea988c70f4ee4df0c6dfb9862a5d982b6a8803cd",
      "encodingFormat": "text/plain",
      "contentSize": "34894"
    },
    {
      "@id": "IR-RQQIV-V/IR%20RAJ15.dx",
      "@type": "File",
      "name": "IR RAJ15.dx",
      "sha256": "6846d77eb7ada1ccece9ff2c1bf3f80be09de883bbfaf8f5a126240cf146bc8c",
      "encodingFormat": "text/plain",
      "contentSize": "43237"
    },
    {
      "@id": "IR-RQQIV-V/IR%20RAJ15.peak.png",
      "@type": "File",
      "name": "IR RAJ15.peak.png",
      "sha256": "a6a85ea22881c78f1901f47c1357395795b521ab1ddfc529d0c8f8ea3f225140",
      "encodingFormat": "image/png",
      "contentSize": "103380"
    },
    {
      "@id": "HRMS__28EI_29-202206031449161000/202206031449161000.jpg",
      "@type": "File",
      "name": "202206031449161000.jpg",
      "sha256": "a548da43182babee3dde99857238cc1f75fb206ddd84795b6f6cd04feebb660c",
      "encodingFormat": "image/jpeg",
      "contentSize": "606186"
    },
    {
      "@id": "13C_NMR-13C/13C.edit.png",
      "@type": "File",
      "name": "13C.edit.png",
      "sha256": "1f13df5875f528e530fd4ad103af355002d4cfc3263747f587aada1b5629b0e9",
      "encodingFormat": "image/png",
      "contentSize": "51616"
    },
    {
      "@id": "13C_NMR-13C/13C.jpeg",
      "@type": "File",
      "name": "13C.jpeg",
      "sha256": "20f9bb8052fed15b104d3cd80ab2671d85afdc3b30979272579471035d62284a",
      "encodingFormat": "image/jpeg",
      "contentSize": "685470"
    },
    {
      "@id": "13C_NMR-13C/13C.infer.json",
      "@type": "File",
      "name": "13C.infer.json",
      "sha256": "eda051b07ef1771b57ff7a23cbe75d4ac9986ec1e0b5bbd5c76c4a6c9f6aad5b",
      "encodingFormat": "application/json",
      "contentSize": "13074"
    },
    {
      "@id": "13C_NMR-13C/13C.edit.jdx",
      "@type": "File",
      "name": "13C.edit.jdx",
      "sha256": "d7dfd0a08eeaff82fa6e045b5ca250732d428b29433ac7fd348208d302f08f88",
      "encodingFormat": "text/plain",
      "contentSize": "471185"
    },
    {
      "@id": "13C_NMR-13C/13C.jcamp",
      "@type": "File",
      "name": "13C.jcamp",
      "sha256": "8fd7b9dc83cea7c892b37821fa79d284cabe509fae10f8c0dfbc81eccfdcd9ef",
      "encodingFormat": "text/plain",
      "contentSize": "567966"
    },
    {
      "@id": "https://w3id.org/ro/crate/1.2",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "RO-Crate 1.2 Specification"
    },
    {
      "@id": "https://purl.archive.org/purl/elnconsortium/eln-spec/1.2+202609",
      "@type": [
        "CreativeWork",
        "Profile"
      ],
      "name": "ELN-File Format 1.2+202609 Specification"
    },
    {
      "@id": "http://creativecommons.org/licenses/by-sa/4.0/",
      "@type": "CreativeWork",
      "name": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
      "description": "Allows sharing and adapting the material for any purpose, provided appropriate credit is given and derivatives are distributed under the same license."
    },
    {
      "@id": "https://www.gnu.org/licenses/agpl-3.0.en.html",
      "@type": "CreativeWork",
      "name": "GNU Affero General Public License v3.0 (AGPL-3.0)",
      "description": "Copyleft free-software license; modified versions offered over a network must make their source code available under the same license."
    }
  ]
}
```
