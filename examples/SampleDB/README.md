# SampleDB

- Code: https://github.com/sciapp/sampledb
- Documentation: https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/

# Export Structure

Each export contains one or more SampleDB objects, identified by their ID, with each object containing one or more versions and an arbitrary number of files. For each object version, the internal data and schema JSON represenation is written out to `data.json` and `schema.json` files. For each object, the JSON representation of internal file data and comment data is written to `files.json` and `comments.json`.

- `ro-crate-metadata.json`
- `objects/`
  - `<object_id>/`
    - `version/`
      - `<version_id>`
        - `data.json`
        - `schema.json`
    - `files/`
      - `<file_id>/`
        - `<file_name>`
    - `files.json`
    - `comments.json`

## Concepts used

| SampleDB concepts            | JSON property | JSON object    |
|------------------------------|---------------|----------------|
| object                       | hasPart       | ./             |
| object name                  | name          | object         |
| object creation time         | dateCreated   | object         |
| object modification time     | dateModified  | object         |
| object url                   | url           | object         |
| object creator               | author        | object         |
| action type                  | genre         | object         |
| comments                     | comment       | object         |
| files                        | hasPart       | object         |
| object version               | hasPart       | object         |
| object version data          | hasPart       | object version |
| object version schema        | hasPart       | object version |
| object version creation time | dateCreated   | object version |
| object version creator       | author        | object version |
| object version url           | url           | object version |
| comment author               | author        | comment        |
| comment creation time        | dateCreated   | comment        |
| comment content              | text          | comment        |
| file name                    | name          | file           |
| file uploader                | author        | file           |
| file upload time             | dateCreated   | file           |

## SampleDB examples

### sampledb_export.eln
```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@type": "CreativeWork",
      "@id": "ro-crate-metadata.json",
      "description": "RO-Crate Metadata File Descriptor",
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "sdPublisher": {
        "@id": "SampleDB"
      },
      "dateCreated": "2023-09-27T06:58:00.292441"
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "version": "1.0",
      "hasPart": [
        {
          "@id": "./objects/1"
        }
      ]
    },
    {
      "@type": "Organization",
      "@id": "SampleDB",
      "name": "SampleDB",
      "logo": "https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/_static/img/logo.svg",
      "slogan": "SampleDB is a web-based electronic lab notebook with a focus on sample and measurement metadata.",
      "url": "https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/"
    },
    {
      "@id": "./objects/1",
      "@type": "Dataset",
      "name": "OMBE-1",
      "description": "Object #1",
      "dateCreated": "2023-09-27T06:57:10.128641",
      "dateModified": "2023-09-27T06:57:10.128641",
      "author": {
        "@id": "./users/2"
      },
      "url": "http://localhost:5000/objects/1",
      "genre": "sample",
      "comment": [
        {
          "@id": "./objects/1/comments/1"
        },
        {
          "@id": "./objects/1/comments/2"
        }
      ],
      "hasPart": [
        {
          "@id": "./objects/1/version/0"
        },
        {
          "@id": "./objects/1/files.json"
        },
        {
          "@id": "./objects/1/files/0/example.txt"
        },
        {
          "@id": "./objects/1/files/1/demo.png"
        }
      ]
    },
    {
      "@id": "./objects/1/version/0",
      "@type": "Dataset",
      "name": "OMBE-1",
      "description": "Object #1 version #0",
      "dateCreated": "2023-09-27T06:57:10.128641",
      "author": {
        "@id": "./users/2"
      },
      "url": "http://localhost:5000/objects/1/versions/0",
      "hasPart": [
        {
          "@id": "./objects/1/version/0/schema.json"
        },
        {
          "@id": "./objects/1/version/0/data.json"
        }
      ]
    },
    {
      "@id": "./objects/1/version/0/schema.json",
      "@type": "File",
      "description": "Schema for Object #1 version #0",
      "name": "schema.json",
      "contentType": "application/json",
      "contentSize": 4073,
      "sha256": "d97ffc5d8d8a04059512b6559bb5f2199646642ef10436d9b910a3f47313015b"
    },
    {
      "@id": "./objects/1/version/0/data.json",
      "@type": "File",
      "description": "Data for Object #1 version #0",
      "name": "data.json",
      "contentType": "application/json",
      "contentSize": 7695,
      "sha256": "79a4238305f0be9d92b059e7f6001b931f5c9eeda531dd39cf376ae501e7e171"
    },
    {
      "@id": "./objects/1/comments/1",
      "@type": "Comment",
      "parentItem": {
        "@id": "./objects/1"
      },
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2023-09-27T06:57:10.175975",
      "text": "This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. This comment is very long. \nThis comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. \n\nThis comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. This comment has three paragraphs. "
    },
    {
      "@id": "./objects/1/comments/2",
      "@type": "Comment",
      "parentItem": {
        "@id": "./objects/1"
      },
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2023-09-27T06:57:10.179670",
      "text": "This is another, shorter comment"
    },
    {
      "@id": "./objects/1/files.json",
      "@type": "File",
      "description": "Data about files for Object #1",
      "name": "files.json",
      "contentType": "application/json",
      "contentSize": 763,
      "sha256": "21ac3b1609e0f0f99fded31e075050d9fbbad53ee4c22bcd3c7ee7940224f04a"
    },
    {
      "@id": "./objects/1/files/0/example.txt",
      "@type": "File",
      "name": "example.txt",
      "description": "File #0 for Object #1",
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2023-09-27T06:57:10.183937",
      "contentType": "text/plain",
      "contentSize": 17,
      "sha256": "9f722959a023c02a3ba0fafdba81aded642d6610eff5dca32dce35132e16b6c5"
    },
    {
      "@id": "./objects/1/files/1/demo.png",
      "@type": "File",
      "name": "demo.png",
      "description": "File #1 for Object #1",
      "author": {
        "@id": "./users/2"
      },
      "dateCreated": "2023-09-27T06:57:10.189271",
      "contentType": "image/png",
      "contentSize": 9952,
      "sha256": "9cef78156ceee44ca84b813b79d7f26afba9307aaa00da40d28a6aa2e623496b"
    },
    {
      "@id": "./users/2",
      "@type": "Person",
      "name": "Instrument Scientist",
      "url": "http://localhost:5000/users/2"
    }
  ]
}
```
