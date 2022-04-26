# Specification for the ELN file format

## Generalities

This format is an open format, licensed under the [MIT](./LICENSE) license and specified by the present document.

The file is a ZIP archive, so it MUST follow the standard ZIP specifications and be readable by all zip utilities.

The contents of the archive MAY be encrypted, as with any ZIP archive.

An up to date version of this document can be accessed at: https://github.com/TheELNConsortium/eln-file-format

## Structure of the archive

Inside a .eln file, there MUST be a folder that will contain the rest of the data. The name of the folder SHOULD be the same as the archive name. This folder at root prevents issues when opening the file as a zip file and getting archived files extracted in the current directory, possibly overwriting other files, and probably polluting the current directory. There MUST be only one folder at the root of the archive.

Inside that root folder, there MUST be a file named `manifest.json`. This file content is described below.

The rest of the archive is composed of folders that each describe one experiment or coherent set of data. Thus, the ELN archive can accomodate one or several experimental set of data.

Example for file: some-data.eln

~~~yaml
some-data.eln:
  - some-data/:
    - manifest.json
    - experimentA/:
      - index.json
      - image.tif
      - measurements.csv
      - paper.pdf
    - experimentB/:
      - content.txt
      - image-overexposed.tif
      - results.xlsx
      - subfolder-with-data/:
        - some-data.bin
        - some-data2.bin
~~~

## Strutcture of the manifest.json

The file `manifest.json` contains [JSON-LD](https://json-ld.org/) data in [format 1.1](https://www.w3.org/TR/json-ld11/) or higher.

The tree structure MUST be a [DataCatalog](https://schema.org/DataCatalog) containing one or several [Dataset](https://schema.org/Dataset).

Example:

~~~json
{
  "@context": "https://schema.org/",
  "@type": "DataCatalog",
  "version": "1",
  "sdPublisher": {
    "@type": "Organization",
    "url": "https://eln.example.org"
  },
  "dateCreated": "2022-04-26T10:49:45+0000",
  "dataset": [
    {
      "@type": "Dataset",
      "url": "./experimentA",
      "name": "Some microscopy data",
      "comment": "Survival of HeLa cells after ionizing radiations exposure",
      "author": {
        "@type": "Person",
        "name": "Nikola Tesla"
      },
      "dateCreated": "2022-04-26T10:49:45+0000",
      "associatedMedia": [
        {
          "@type": "MediaObject",
          "contentSize": "402",
          "contentUrl": "./image.tif",
          "encodingFormat": "image/tiff",
          "dateCreated": "2022-04-26T10:49:45+0000",
          "sha256": "311fe3feed16b9cd8df0f8b1517be5cb86048707df4889ba8dc37d4d68866d02"
        },
        {
          "@type": "MediaObject",
          "contentSize": "32",
          "contentUrl": "./measurements.csv",
          "encodingFormat": "text/csv",
          "dateCreated": "2022-04-26T13:37:00+0000",
          "sha256": "75546313da12bbcbbf2079a70002d73cc1800e7ef86339f99a86705caaaa1c85"
        }
      ]
    },
    {
      "@type": "Dataset",
      "url": "./experimentB",
      "name": "Some western blot data",
      "comment": "Effect of siRNA anti Actin on HeLa cells",
      "author": {
        "@type": "Person",
        "name": "Harry Towbin"
      },
      "dateCreated": "2022-07-14T13:37:00+0000",
      "associatedMedia": [
        {
          "@type": "MediaObject",
          "contentSize": "53492",
          "contentUrl": "./blot.jpg",
          "encodingFormat": "image/jpeg",
          "dateCreated": "2022-07-01T15:15:07+0000",
          "sha256": "47806097bc560c15588dc85ccaff6b48ad29b693c6b8610f6bfd62d230be103c"
        }
      ],
      "about": [
        {
          "@type": "Protein",
          "hasBioPolymerSequence": ">sp|P60709|ACTB_HUMAN Actin, cytoplasmic 1 OS=Homo sapiens OX=9606 GN=ACTB PE=1 SV=1
            MDDDIAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQS
            KRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMT
            QIMFETFNTPAMYVAIQAVLSLYASGRTTGIVMDSGDGVTHTVPIYEGYALPHAILRLDL
            AGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKSY
            ELPDGQVITIGNERFRCPEALFQPSFLGMESCGIHETTFNSIMKCDVDIRKDLYANTVLS
            GGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQ
            EYDESGPSIVHRKCF",
          "isEncodedByBioChemEntity": {
            "@type": "Gene",
            "url": "https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:132"
          }
        },
        {
          "@type": "BioChemEntity",
          "name": "Actin siRNA",
          "url": "https://www.ncbi.nlm.nih.gov/nuccore/NM_001100"
        }
      ]
    }
  ]
}

~~~

## About the content of folders (DataCatalog)

At the same level than the `manifest.json`, on or several folders containing experimental data will exist. Their contents are described in the `manifest.json` file and thus they can contain 0 or more files.
