## Preface
Sensolytics GmbH is developing an producing instruments for electrochemical research, focussed on localised electrochemistry. Our Scanning Droplet Cell Systems are used to run user-defined electroanalytical experiments at defined positions of a sample surface, and can produce large numbers of datafiles (binary, undisclosed format of a third-party), depending on the users experimental settings. To provide users an easy way of loading the measured data into their electronic labbook, we added an export function which is saving a *eln file including the raw data and the scan parameters (i.e. the grid definition)

## Example file 23-09-20_113808 Experiment.eln
This example is a very light-weighted one, containing the experimental parameters and five raw data files
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
      "dateCreated": "2023-09-20T11:38:09+02:00"
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Data"
        }
      ]
    },
    {
      "@id": "./Data",
      "@type": "Dataset",
      "name": "23-09-20_113808 Experiment",
      "text": "<p>Sensolytics SDC Experiment</p><p>Experiment started: 20.09.2023 11:36:58</p><p></p><p>XLength [µm]: 200</p><p>XIncrement [µm]: 50</p><p>YLength [µm]: -200</p><p>YIncrement [µm]: 50</p><p>TravelSpeed [µm/s]: 5000</p><p>Scan Direction X lines: False</p><p></p><p>Dispensing Speed [µL/s]: 25</p><p>Dispensing Volume [µL]: 150</p><p>Aspiration Speed [µL/s]: 25</p><p>Aspiration Volume [µL]: 100</p><p></p><p>Force [mN]: 0</p><p>ControlLoopKp [µm/mN]: 0.05</p><p>ApproachSpeed [µm/s]: 1000</p><p></p><p>Waste position: 2000 µm, 25000 µm, 25000 µm</p><p>Dip position: 20419.2 µm, 22456 µm, 11545.5 µm</p><p>Start position: 0 µm, 0 µm</p><p>Travel height waste: 15000 µm</p><p>Travel height sample:  11000 µm</p><p></p><p>Procedure: NOVA-LSV.nox</p><p></p><p>Point coordinates relative to the start position in µm:</p><p>50, -100</p><p>50, -150</p><p>50, -200</p><p>100, -100</p><p>100, -150</p><p></p>",
      "hasPart": [
        {
          "@id": "./Data/0001_50_-100_NOVA-LSV.nox"
        },
        {
          "@id": "./Data/0002_50_-150_NOVA-LSV.nox"
        },
        {
          "@id": "./Data/0003_50_-200_NOVA-LSV.nox"
        },
        {
          "@id": "./Data/0004_100_-100_NOVA-LSV.nox"
        },
        {
          "@id": "./Data/0005_100_-150_NOVA-LSV.nox"
        }
      ]
    },
    {
      "@id": "./Data/0001_50_-100_NOVA-LSV.nox",
      "@type": "File",
      "sha256": "4c5712a6839be7d19534cc270ad84c97efdfb3361a0e3a5c79779a1e6ae8188d"
    },
    {
      "@id": "./Data/0002_50_-150_NOVA-LSV.nox",
      "@type": "File",
      "sha256": "7c9d6390e4e14e102b59422b7648b560dc1edf06a1abe2bf987cbbb1ab78acde"
    },
    {
      "@id": "./Data/0003_50_-200_NOVA-LSV.nox",
      "@type": "File",
      "sha256": "89371714289737dd008088f96c87a7963a180a0cf9169f4c4ab0d3d9f24de0b3"
    },
    {
      "@id": "./Data/0004_100_-100_NOVA-LSV.nox",
      "@type": "File",
      "sha256": "c5d6c3fd6c5c565cfdcf74a890f818d8e4a28af52028e31ea5d6e3b5862b000b"
    },
    {
      "@id": "./Data/0005_100_-150_NOVA-LSV.nox",
      "@type": "File",
      "sha256": "71f59cba60e6313bb093fee8427397c3636dd1f53ce692295ee5f19b38cbf82b"
    }
  ]
}
```