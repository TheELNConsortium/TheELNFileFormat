# Specification for the ELN file format

## Generalities

This format is an open format, licensed under the [MIT](./LICENSE) license and specified by the present document.

The file is a ZIP archive, so it MUST follow the standard ZIP specifications and be readable by all zip utilities.

The contents of the archive MAY be encrypted, as with any ZIP archive.

An up to date version of this document can be accessed at: https://github.com/TheELNConsortium/eln-file-format

This archive format is basically a zipped RO-Crate, with a `.eln` file extension.

## Structure of the archive

Inside a .eln file, there MUST be a folder that will contain the rest of the data. The name of the folder SHOULD be the same as the archive name. This folder at root prevents issues when opening the file as a zip file and getting archived files extracted in the current directory, possibly overwriting other files, and probably polluting the current directory. There MUST be only one folder at the root of the archive.

Inside that root folder, there MUST be a file named `ro-crate-metadata.json`. This file follows the [RO-Crate 1.1+ Specification](https://w3id.org/ro/crate/1.1).

The rest of the archive is composed of 0 or more folders that each describe one experiment or coherent set of data. Thus, the ELN archive can accomodate one or several experimental set of data.

Example for file: some-data.eln

~~~yaml
<root>
  some-data.eln/
    - ro-crate-metadata.json
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

## Structure of ro-crate-metadata.json

This is of course described in the [RO-Crate Specification](https://w3id.org/ro/crate/1.1) but let's go over an example to understand how it works.

### Root

At the root of our json-ld object, we have a context and a graph. The graph will contain an array of everything we put in our crate.

~~~json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [<EVERYTHING IS IN THERE>]
}
~~~

### First object: ro-crate-metadata.json

The first thing we do is describe the `ro-crate-metadata.json` object:

~~~json
{
  "@id": "ro-crate-metadata.json",
  "@type": "CreativeWork",
  "about": {
    "@id": "./"
  },
  "conformsTo": {
    "@id": "https://w3id.org/ro/crate/1.1"
  },
  "dateCreated": "2022-05-30T12:25:36+0200",
}
~~~

It is a `CreativeWork` about the current directory where it is, and conforms to the RO-Crate specification. Other fields like `dateCreated` (added here), `sdPublisher` or [any other property](https://schema.org/CreativeWork) of `CreativeWork` can be added.


### Second object: current directory

The second object is basically describing the current directory (`./`).

~~~json
 {
    "@id": "./",
    "@type": [
      "Dataset"
    ],
    "hasPart": [
      "./2022-05-29 - Some-experiment",
      "./2022-05-29 - Some-experiment/2022-05-30-export.elabftw.csv",
      "./2022-05-29 - Some-experiment/2022-05-29 - Some-experiment.pdf",
      "./2022-05-29 - Some-experiment/example.mp4",
      "./2022-05-29 - Some-experiment/example.pdb",
      "./2022-05-29 - Some-experiment/example.jpg",
      "./2022-05-29 - Id-asperiores-explicabo-quod-mollitia",
      "./2022-05-29 - Id-asperiores-explicabo-quod-mollitia/2022-05-30-export.elabftw.csv",
      "./2022-05-29 - Id-asperiores-explicabo-quod-mollitia/2022-05-29 - Id-asperiores-explicabo-quod-mollitia.pdf",
      "./2022-05-29 - Id-asperiores-explicabo-quod-mollitia/example.pps",
    ]
}
~~~

Its type is an array of `Dataset` and `hasPart` which corresponds to the differents `@id` of the other objects. Think of it like a Table of Contents.

### The rest

After that, all the other objects have an `@type` of either `Dataset` for directories or `File` for well..., files. And the `@id` corresponds to something in the `hasPart` of `./`.

All objects (nodes) with an `@type` such as `Comment` or `Person` exist at the root node (once), and can be referenced via their `@id` in other parts.

For instance, a "comment" on an experiment will exist as a `@type: Comment` node at the root node, and be referenced through its `@id` in the `comment` part of the experiment's node. See "Example Dataset with Comment" example below.

#### Example Dataset

~~~json
{
    "@id": "./2022-05-29 - Some-experiment",
    "@type": "Dataset",
    "author": {
      "@id": "./author/23"
    },
    "dateCreated": "2022-05-29 16:17:38",
    "dateModified": "2022-05-29 16:17:57",
    "name": "Some experiment",
    "text": "<h1><span style=\"font-size:14pt;\">Goal :</span></h1>\n<p> </p>\n<h1><span style=\"font-size:14pt;\">Procedure :</span></h1>\n<p> </p>\n<h1><span style=\"font-size:14pt;\">Results :<br></span></h1>\n<p> </p>",
    "url": "https://elab.example.com/experiments.php?mode=view&id=256"
}
~~~

#### Example File

~~~json
{
    "@id": "./2022-05-29 - Some-experiment/2022-05-30-export.elabftw.csv",
    "@type": "File",
    "description": "CSV Export",
    "name": "2022-05-30-export.elabftw.csv",
    "contentType": "text/csv; charset=UTF-8",
    "contentSize": "247",
    "sha256": "f3278e796c687371cc63a600b6f12ea32167067fed3ef98099d0c1aad2426531"
}
~~~

#### Example Dataset with Comment

Here we show three nodes, the Dataset (main experiment), a Comment and a Person. The Person leaving the Comment is the same as the author of the Dataset.

~~~json
{
  "@id": "./some-unique-id/23",
  "@type": "Dataset",
  "author": {
    "@id": "./some-author-id/44"
  },
  "dateCreated": "2023-09-23T01:02:26+02:00",
  "dateModified": "2023-09-27T23:02:44+02:00",
  "comment": [
    {
      "@id": "./some-comment-id/91"
    }
  ],
 },
{
  "@id": "./some-comment-id/91",
  "@type": "Comment",
  "dateCreated": "2023-09-23T01:02:26+02:00",
  "text": "This is the content of the comment.",
  "author": {
    "@id": "./some-author-id/44"
  }
},
{
   "@id": "./some-author-id/44"
   "@type": "Person",
   "familyName": "Tapie",
   "givenName": "Bernard"
}
~~~

### Going further

See the [RO-Crate website](https://www.researchobject.org/ro-crate/1.1/data-entities.html#example-linking-to-a-file-and-folders).

## Concrete examples files

See the [examples folder](./examples).
