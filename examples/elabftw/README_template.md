# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

## Concepts used

A file `elabftw-export.json` is created during export and added to the archive, it corresponds to the JSON export on the entry by eLabFTW and might contain fields that are not present in the metadata file because too specific to eLabFTW.

Here is a correspondance between concepts in eLabFTW and how they are translated in the metadata json file in the archive:

| eLabFTW concepts    | JSON property          |
|---------------------|------------------------|
| tags                | keywords               |
| links               | mentions               |
| comments            | comment                |
| steps               | in elabftw-export.json |
| elabid              | identifier             |
| title               | name                   |
| body (main content) | text                   |

