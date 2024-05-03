#Sensolytics example

## Information
Sensolytics GmbH is developing and producing instruments for electrochemical research, focused on localised electrochemistry. Our Scanning Droplet Cell Systems are used to run user-defined electroanalytical experiments at defined positions of a sample surface, and can produce large numbers of datafiles (binary, undisclosed format of a third-party), depending on the users experimental settings. To provide users an easy way of loading the measured data into their electronic labbook, we added an export function which is saving a .eln file including the raw data and the scan parameters (*i.e. the grid definition*).

### SDC Experiment.eln
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
      "dateCreated": "2024-04-25T17:06:07+02:00",
      "sdPublisher": {
        "@type": "Organization",
        "name": "Sensolytics GmbH",
        "logo": "https://www.sensolytics.de/images/stories/sensolytics_cropped.png",
        "slogan": "Electrochemistry at the tip.",
        "url": "https://www.sensolytics.de"
      }
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
      "name": "MyExperiment",
      "text": "<p>Description of the experiment!</p>",
      "hasPart": [
        {
          "@id": "./Data/0001_16082,5_17494_CV.nox"
        },
        {
          "@id": "./Data/0002_15582,5_17994_CV.nox"
        },
        {
          "@id": "./Data/0003_16082,5_17994_CV.nox"
        },
        {
          "@id": "./Data/0004_16582,5_17994_CV.nox"
        },
        {
          "@id": "./Data/0005_16082,5_18494_CV.nox"
        },
        {
          "@id": "./Data/24-04-25_045906 Experiment Info.txt"
        }
      ]
    },
    {
      "@id": "./Data/0001_16082,5_17494_CV.nox",
      "@type": "File",
      "sha256": "248c1631ff1ad27919cbed1c29baeb39822de2b91087582d7fc17a532cc91c76"
    },
    {
      "@id": "./Data/0002_15582,5_17994_CV.nox",
      "@type": "File",
      "sha256": "1ef5b91dd127dc7120262d5c0433bf7afc95e4f188d75aea1c019972f6e67a6b"
    },
    {
      "@id": "./Data/0003_16082,5_17994_CV.nox",
      "@type": "File",
      "sha256": "e41409cdca9520410f8f47c4f215ffc02b03b55c60f902693e6618cc8f79dc2b"
    },
    {
      "@id": "./Data/0004_16582,5_17994_CV.nox",
      "@type": "File",
      "sha256": "11adbbd769aecf7f78a9130c58607565f3c5fd4a557ba95a3efab3c0207a0eb1"
    },
    {
      "@id": "./Data/0005_16082,5_18494_CV.nox",
      "@type": "File",
      "sha256": "cf028bc5a6f2760234bf60ab69df2d760c1aca963e4cf3e039f6834f07954deb"
    },
    {
      "@id": "./Data/24-04-25_045906 Experiment Info.txt",
      "@type": "File",
      "sha256": "bd27a8bd0689a6ee8839d84beada231407103dfe96186662dbcbf8828b99f781"
    }
  ]
}
```
