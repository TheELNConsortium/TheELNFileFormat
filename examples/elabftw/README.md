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


### single-database-item.eln
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
      "dateCreated": "2023-07-31T14:39:04+02:00",
      "sdPublisher": {
        "@type": "Organization",
        "name": "eLabFTW",
        "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
        "slogan": "A free and open source electronic lab notebook.",
        "url": "https://www.elabftw.net",
        "parentOrganization": {
          "@type": "Organization",
          "name": "Deltablot",
          "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
          "slogan": "Open Source software for research labs.",
          "url": "https://www.deltablot.com"
        }
      },
      "version": "1.0"
    },
    {
      "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 679440a2/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1764",
      "sha256": "262199f35750f3abdff5ce342d19ce1a96e133e61029bf682eb128a5f7e0c138"
    },
    {
      "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 679440a2/example.jcamp",
      "@type": "File",
      "description": "",
      "name": "example.jcamp",
      "alternateName": "85/8546e3a18049cf69cf960994e0c204fc8f39967051f48986f8cb27562b6ee422730587235b6c81112d36d76e7a5479d9182d73df2c93b4a582256e9394d4a3d5.jcamp",
      "contentSize": 110797,
      "sha256": "b412adc50ab3583b5bf8b73b6e2f392d720058b5fc12b5a3b46f40fd6f64ed48"
    },
    {
      "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 679440a2",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:58+02:00",
      "dateModified": "2023-07-31T13:38:58+02:00",
      "identifier": "20230729-679440a211115d1389f9173d51f3457b13369ccd",
      "comment": [],
      "keywords": [
        "nostrumnisi",
        "eumullam",
        "voluptatemconsequatur"
      ],
      "name": "Hydrochloric acid - HCl",
      "text": "<p>main body.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=166",
      "hasPart": [
        {
          "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 679440a2/export-elabftw.json"
        },
        {
          "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 679440a2/example.jcamp"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Chemical-compound - Hydrochloric-acid-HCl - 679440a2"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### experiment-template.eln
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
      "dateCreated": "2023-07-31T14:27:35+02:00",
      "sdPublisher": {
        "@type": "Organization",
        "name": "eLabFTW",
        "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
        "slogan": "A free and open source electronic lab notebook.",
        "url": "https://www.elabftw.net",
        "parentOrganization": {
          "@type": "Organization",
          "name": "Deltablot",
          "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
          "slogan": "Open Source software for research labs.",
          "url": "https://www.deltablot.com"
        }
      },
      "version": "1.0"
    },
    {
      "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1720",
      "sha256": "ed15e7b86e4112eb95665725ea29387722fda9110524795b15b97f42b5b339b4"
    },
    {
      "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-31T13:23:43+02:00",
      "dateModified": "2023-07-31T13:27:26+02:00",
      "identifier": "",
      "comment": [],
      "keywords": [
        "microscopy",
        "example"
      ],
      "name": "This is an experiment template",
      "text": "<p>Experiment templates are used to speed up the creation of experiments. They are very similar to experiments or items but do not contain attached files.</p>",
      "url": "https://elab.local:3148/.php?mode=view&id=13",
      "hasPart": [
        {
          "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f/export-elabftw.json"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=163",
          "@type": "Dataset",
          "name": "Plasmid - pRSF-Duet-1",
          "identifier": "20230729-81ed0cc30bf8d243df5753bee7324308864c68e9"
        }
      ]
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Experiment template - This-is-an-experiment-template - 9db7e29f"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### single-experiment.eln
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
      "dateCreated": "2023-07-31T14:38:33+02:00",
      "sdPublisher": {
        "@type": "Organization",
        "name": "eLabFTW",
        "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
        "slogan": "A free and open source electronic lab notebook.",
        "url": "https://www.elabftw.net",
        "parentOrganization": {
          "@type": "Organization",
          "name": "Deltablot",
          "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
          "slogan": "Open Source software for research labs.",
          "url": "https://www.deltablot.com"
        }
      },
      "version": "1.0"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "16642",
      "sha256": "60e42204f247d611e7c0237a75f3e71b97b8baad0a4b7b5ecb018fa017452cb5"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.avi",
      "@type": "File",
      "description": "",
      "name": "example.avi",
      "alternateName": "26/26baccf540f1aeaa96084223b8292f0b52a32792c96dab59a7c71b80b842eb1a15e3e5d6fa63d640f1803dad48268346283e474531fffe3864d80d9d96d02812.avi",
      "contentSize": 200334,
      "sha256": "ebae6bea18cf01d4bc9a974ad71a9aad2ecfaf03ec483a2364d22b8b37ae00bd"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.bmp",
      "@type": "File",
      "description": "",
      "name": "example.bmp",
      "alternateName": "42/428ef674b3d9fc278786adef727d42bd70a05b44ad5362df5981d74cd75e4a2fe97a9ee123e4989b91a29a6c049357ff20a920ab952886fca44d17a4fd6e3c6b.bmp",
      "contentSize": 3000122,
      "sha256": "2b9835aa11ec6fe69d525eed76247728ef55df16d20a7258bf6e04377e7f33da"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cdx",
      "@type": "File",
      "description": "",
      "name": "example.cdx",
      "alternateName": "6c/6c7e15d8048c64afcb9ad1ccbf6f4476219e6f9540c53ae3d01de760ffa036a208654af1d4b850dc23d53026d558d74c85bc1743fea2c423b2d38a2391ba7a7c.cdx",
      "contentSize": 1514,
      "sha256": "5efbea7d56c052e2e1fc418ff24ef8b445cd543d07a4c892994647e90d5258dc"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cif",
      "@type": "File",
      "description": "",
      "name": "example.cif",
      "alternateName": "7e/7e02efd3a57a3b13b94e146501815cacdfdf77c84b6e2b7c8a806f21d8dfdfc273da0d6a107a011669bd5f4083e227d0310d6470ca6f4671aaef321e28baacba.cif",
      "contentSize": 178876,
      "sha256": "84a65798c5a227119ad96b921e6f3e19ed34b23cfcee350be8d74c63e0e95d40"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.dna",
      "@type": "File",
      "description": "",
      "name": "example.dna",
      "alternateName": "da/da0d53ba80033e36fa2d86d7de38d66b4ad588ca19b453e72a0401cdd47e90e63e7e974f13a98101407c87a72911657221c190f20eb073067aee20342e7885c2.dna",
      "contentSize": 27050,
      "sha256": "96639ecb57ddec5116d3cb3a9d4a3d5b37e89bbd9a7a3df782fe3e827f3fd787"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.docx",
      "@type": "File",
      "description": "",
      "name": "example.docx",
      "alternateName": "71/7181ab9a4af526d4cdedd09397d45e28b3f2beb740c0eaf5f0cd36a51f3e78bf316b9cf32f8d63baee8da7efeca3f0d469746bb8f20fade1338a3a3d12716ac6.docx",
      "contentSize": 4147,
      "sha256": "f1bc2027abdc4df60fbb1b0123fa73f768fe85f4e7cd277ad6a338b2cae089c0"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.epub",
      "@type": "File",
      "description": "",
      "name": "example.epub",
      "alternateName": "a1/a1b1bd7168e298582af6cadeca5fe4a7093074107ec546fdd6fd1e63571b6a0b45b7eccf384e43940924f8e68da794da8b990017f2e31be199dbac991e7bebad.epub",
      "contentSize": 4051596,
      "sha256": "d2e2091e98c37e43e6ea101101f667b50901a1fd35ac1d3fc949eed96d876bf2"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gbk",
      "@type": "File",
      "description": "",
      "name": "example.gbk",
      "alternateName": "50/501463c206f84aa082eea31105c11e0c03f0a3a0bc3b7a5a05f15c0170f443086a08e823ea8e55d4894b4de9e2cd3a93c350dbe8996a9d6cb4cf5eadf033ebe3.gbk",
      "contentSize": 7472,
      "sha256": "a092b86343c74697ac70542d5a75843230b69555e01e5460bac8cddab1dbecea"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gif",
      "@type": "File",
      "description": "",
      "name": "example.gif",
      "alternateName": "ee/eefcf9ec863fcf9edd5eb6eb58461264ffc59bc99caf7743cad5705a8b87981cb8e60b81441db39828ae4bee3bb5f9c652330a533f4ed033e7a49b6c7a08728b.gif",
      "contentSize": 761850,
      "sha256": "b82134e798bdd719324859b08bf21698e4ec11f2eac64a56cae88e4bf654fbb6"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gz",
      "@type": "File",
      "description": "",
      "name": "example.gz",
      "alternateName": "90/9086a42687d9132d3564b4a61d9f32b684afbb20032a66635941a150e64ed72e981e6d91fe07271b800d0e7da9cfc47b420c8d2dc3762c3fe22085e1b7abea56.gz",
      "contentSize": 183635,
      "sha256": "70c6cee1cb22095026ebddaac03afe10550087c3397d1f2b05850b48ef618dde"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jcamp",
      "@type": "File",
      "description": "",
      "name": "example.jcamp",
      "alternateName": "d0/d0e2a12fb7b546cc7da8b77bb8fbc929676472df34321f7e200825a9d00f41c92990ea6d61c3cc9f9b29d85a8f82a495e863a7ae63f5bbbb0f41ad4a18a5d6e0.jcamp",
      "contentSize": 110797,
      "sha256": "b412adc50ab3583b5bf8b73b6e2f392d720058b5fc12b5a3b46f40fd6f64ed48"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jdx",
      "@type": "File",
      "description": "",
      "name": "example.jdx",
      "alternateName": "44/44a75b98c5addb36e980abc00a176c09a08d6f44b660ef5d3abdf9cf7eba10088939e41f18eb019e73b9ab26e5192425d549a9b2a681d959a070204598f343d7.jdx",
      "contentSize": 37207,
      "sha256": "3ff02ba7a73c1340e83a73179115aee794a90a6e1bcc9775afff82a822cdb6e0"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jpg",
      "@type": "File",
      "description": "",
      "name": "example.jpg",
      "alternateName": "29/2993b708756f0e827d3da5b22da6ab66aad991b1131b03ec74f2f7361c81ac49785f9d22933836106d939c2d3ba4317807b2b1c5e9bac89e48874c731b05bf84.jpg",
      "contentSize": 85530,
      "sha256": "b73626c9a9ed8561ed6126df2493bc0d84fb8feedc9fe34aed94f7d2d5f4f60f"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.json",
      "@type": "File",
      "description": "",
      "name": "example.json",
      "alternateName": "73/7386a19849c0daedc002f59aed22679f9b415e0ca6b0b126d92bcdaffc2bea708741d958901590854858186b418f0ac71069718397b87b4f9baa129944d6f512.json",
      "contentSize": 1734,
      "sha256": "58de2671fcd268ffd1706d5e217bac191b02354f0345a0ee948fa1139600b988"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mnova",
      "@type": "File",
      "description": "",
      "name": "example.mnova",
      "alternateName": "a3/a3a81c24f9f1d2fc49dc12cd45c21021e59ed98166864b92bf100c04dcbb524b3980db59a2fd31d94f8fd2307cedb49c56ce3878f0108de252a10fcbf864e382.mnova",
      "contentSize": 139349,
      "sha256": "4e5b9311b1c8a4d6a1c8c4ec94aa7ee5cd2ee676b6ad7720fac67c33d670e383"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mol",
      "@type": "File",
      "description": "",
      "name": "example.mol",
      "alternateName": "ed/edfa30f08d64bb8c71e3ec2692a0d1f5af58c1cbb9152034863e3aa94c3396a54beed294e2de88d8fda41d60920e0ed247333fcebd1527e53fa24e5cf4591486.mol",
      "contentSize": 1664,
      "sha256": "5622cb4d7a5e6166a3527345ffc864a768cd03c3f77511a5988853c402c504a4"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mp4",
      "@type": "File",
      "description": "",
      "name": "example.mp4",
      "alternateName": "ae/aea416d40ea71b1e9c5048b861a4418266a11a0c23e3d5a3b421e8411fe7312b532355b2928ed8bc6c27b44742d2e7e0cdd64a0dfe57a4d0a6f2f7ad7ac2d94b.mp4",
      "contentSize": 184144,
      "sha256": "2a729ba8ddca2e2270effed052ceed5a1167a8d1c4ee856ace3d55635fca243d"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.odp",
      "@type": "File",
      "description": "",
      "name": "example.odp",
      "alternateName": "e9/e92076d7a9181d73a796507134644a2fef4d7472be0f5bfc01ddcdb8a644e123688991b13dd9054f6f840ff65ea71adffffdc319714b74794515026aadb1249f.odp",
      "contentSize": 50014,
      "sha256": "7a6eb056b0c2a67da89f1a3f42f348b06f931d07f5124468dfdee187702e2444"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdb",
      "@type": "File",
      "description": "",
      "name": "example.pdb",
      "alternateName": "c7/c7efe2df0cfee747597532804b3f4e592291ad3df996ded49fe42bf4b8e6c5dbe3b4d7b3d2916b3ee74f55db19d9a0fd528711581171e63588635da553c83f54.pdb",
      "contentSize": 515889,
      "sha256": "aa8a72b1c6fe310d25851742e4c30599bbcd4764c2a26578bad0fae70d8f0627"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdf",
      "@type": "File",
      "description": "",
      "name": "example.pdf",
      "alternateName": "2f/2f9c2d6a298ae1e31f3c72a524e9ffedd70680d5caa4cf4f66e1e86c85d337a8735200b855d32394166083402e0acc04f04d1eb30f74630e34ef878ed96c3aad.pdf",
      "contentSize": 116369,
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.png",
      "@type": "File",
      "description": "",
      "name": "example.png",
      "alternateName": "5d/5d8813cede85d152c8960b0f459b1832811b8ddbd8eb2b4e7a667e2c310209fd02a89da41173ac19abf318dcde0aa9f6d44b88a97692b8eb8481878ef0cb8266.png",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pps",
      "@type": "File",
      "description": "",
      "name": "example.pps",
      "alternateName": "23/23e1ee184021357d0a68a74cb986873d6e4be35a8a85c645c4a941004caefc49d0f52032aa9402accfe0ea23cdc675270730cdf2c6304ade383f93d654b1d7d9.pps",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppsx",
      "@type": "File",
      "description": "",
      "name": "example.ppsx",
      "alternateName": "90/90afa1d4af023351e6d7870192e99aaf74aee53d6cd551d0b433eb3ed9f24714018fdd4fb4d22d0104c225af4de00c7d3b28e80899650bbaf34f713c47b6445e.ppsx",
      "contentSize": 57375,
      "sha256": "7af9d974a47b6d081f1ce7ad0e3d5af21be6aeb664938cef6cfd8bdf1937cb2a"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppt",
      "@type": "File",
      "description": "",
      "name": "example.ppt",
      "alternateName": "9b/9bba763855d2dcf12dae08c87e46b7c1f9e3e39f6f49dff0cfed8e4266f0a13747a9c90fbf145d485e20533cacf87770932808876594c027ce531e2a398409d9.ppt",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pptx",
      "@type": "File",
      "description": "",
      "name": "example.pptx",
      "alternateName": "a1/a1b1e04f9d5c27592a136657f104779f3241333cbad08ccd53a00ff0867085b9d1b857a0e9d3672bff5dac4ff36c6ce6c8b8ebb60668def22604af9d5796b527.pptx",
      "contentSize": 57375,
      "sha256": "4fc01c51e094f4410a56f05f513be829425f12e7b33b5296115126a84aba74e7"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.sdf",
      "@type": "File",
      "description": "",
      "name": "example.sdf",
      "alternateName": "e4/e406de40ed0b0df4b5ef632314c36856e9fb49cc535985d281c924fb3cf030ce69b1f227ebd79a4f5826b1198ec18c50f4880bf1f9c07bb0446863528a8b5682.sdf",
      "contentSize": 3782,
      "sha256": "f44f2e734602a5ac09f4692e111f2c386af5c88691488d4bc2a5ecbd507e4ad4"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.tif",
      "@type": "File",
      "description": "",
      "name": "example.tif",
      "alternateName": "30/3034cf92edab4068e0da359580f6f9e14afdb0320592eb9809ebfcb998de5a51b1096b83d01922f305d8ac76c464d062eab8287be6083a967f77ff154900faf2.tif",
      "contentSize": 678520,
      "sha256": "69ca1ba6fed2b3f44f12fcc8ce8d4f945fe42dc81675acbd894a430676ebdc2e"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.xyz",
      "@type": "File",
      "description": "",
      "name": "example.xyz",
      "alternateName": "a2/a2b74ec8e3dc322e0fb60d5b80fd1ac4ddaf7d33227f8df7bdb22e7e6657044efddc459fb41c761846b36d85eecac75cd73e8c3abc2ef1de33dd8df8d0d6fcf9.xyz",
      "contentSize": 1079,
      "sha256": "99f6c504dad42fe09f6d7c2422f720a671384a0de47c6bbb24f6b895baa87aec"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/README.md",
      "@type": "File",
      "description": "",
      "name": "README.md",
      "alternateName": "e8/e8fc2c6c15f6205d6f9ad4a89bf0b06d45f2dc7a6368855696eaae7493025222b1f818b4cc53780fe92598e4f92c3fc09a56f92d461696a3fb0352989b7fa04a.md",
      "contentSize": 265,
      "sha256": "dca1f13c35d4a719c8e8e0c45d84c6ad0f378c245e90a92127b2af8d1df89b9b"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:51+02:00",
      "dateModified": "2023-07-31T13:37:58+02:00",
      "identifier": "20230729-75bb78f9339de02ec3ffe44129de4d0c9cba1550",
      "comment": [
        {
          "@id": "comment://2023-07-29T20%3A24%3A51%2B02%3A00",
          "dateCreated": "2023-07-29T20:24:51+02:00",
          "text": "Well, it&#39;s always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
          "author": {
            "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
          }
        }
      ],
      "keywords": [
        "demo",
        "test"
      ],
      "name": "Testing the eLabFTW lab notebook",
      "text": "<h1>Goal</h1><p>Test the software.</p><h1>Procedure</h1><p>Click everywhere and explore everything.</p><h1>Results</h1><p>It's really nice, I think I'll adopt it for our lab.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=264",
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/export-elabftw.json"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.avi"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.bmp"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cdx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cif"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.dna"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.docx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.epub"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gbk"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gif"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gz"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jcamp"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jdx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jpg"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.json"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mnova"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mol"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mp4"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.odp"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdb"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdf"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.png"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pps"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppsx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppt"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pptx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.sdf"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.tif"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.xyz"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/README.md"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=50",
          "@type": "Dataset",
          "name": "Generated - Sint eos explicabo eum incidunt omnis.",
          "identifier": "20230729-78af171c99a3681027cb7cccaa921dbd3e7ff631"
        },
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=51",
          "@type": "Dataset",
          "name": "Generated - Fugit dignissimos ad consequatur facilis necessitatibus.",
          "identifier": "20230729-70f542b44469b7ce7741351e4f4db6dc64a4e6a3"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=256",
          "@type": "Dataset",
          "name": "Success - Test the grouped extra fields",
          "identifier": "20230729-76a26adbc7532fadcb74876ab3efd83921ef478a"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=257",
          "@type": "Dataset",
          "name": "Success - An example experiment",
          "identifier": "20230729-46af8abf379be3f35cf33ad5990a886e9e7da65b"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=258",
          "@type": "Dataset",
          "name": "Success - Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
          "identifier": "20230729-ac1839136f9d133973dff2c074a2c6619c9cec3e"
        }
      ]
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```

### multiple-experiments.eln
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
      "dateCreated": "2023-07-31T14:38:16+02:00",
      "sdPublisher": {
        "@type": "Organization",
        "name": "eLabFTW",
        "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
        "slogan": "A free and open source electronic lab notebook.",
        "url": "https://www.elabftw.net",
        "parentOrganization": {
          "@type": "Organization",
          "name": "Deltablot",
          "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
          "slogan": "Open Source software for research labs.",
          "url": "https://www.deltablot.com"
        }
      },
      "version": "1.0"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "16642",
      "sha256": "60e42204f247d611e7c0237a75f3e71b97b8baad0a4b7b5ecb018fa017452cb5"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.avi",
      "@type": "File",
      "description": "",
      "name": "example.avi",
      "alternateName": "26/26baccf540f1aeaa96084223b8292f0b52a32792c96dab59a7c71b80b842eb1a15e3e5d6fa63d640f1803dad48268346283e474531fffe3864d80d9d96d02812.avi",
      "contentSize": 200334,
      "sha256": "ebae6bea18cf01d4bc9a974ad71a9aad2ecfaf03ec483a2364d22b8b37ae00bd"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.bmp",
      "@type": "File",
      "description": "",
      "name": "example.bmp",
      "alternateName": "42/428ef674b3d9fc278786adef727d42bd70a05b44ad5362df5981d74cd75e4a2fe97a9ee123e4989b91a29a6c049357ff20a920ab952886fca44d17a4fd6e3c6b.bmp",
      "contentSize": 3000122,
      "sha256": "2b9835aa11ec6fe69d525eed76247728ef55df16d20a7258bf6e04377e7f33da"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cdx",
      "@type": "File",
      "description": "",
      "name": "example.cdx",
      "alternateName": "6c/6c7e15d8048c64afcb9ad1ccbf6f4476219e6f9540c53ae3d01de760ffa036a208654af1d4b850dc23d53026d558d74c85bc1743fea2c423b2d38a2391ba7a7c.cdx",
      "contentSize": 1514,
      "sha256": "5efbea7d56c052e2e1fc418ff24ef8b445cd543d07a4c892994647e90d5258dc"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cif",
      "@type": "File",
      "description": "",
      "name": "example.cif",
      "alternateName": "7e/7e02efd3a57a3b13b94e146501815cacdfdf77c84b6e2b7c8a806f21d8dfdfc273da0d6a107a011669bd5f4083e227d0310d6470ca6f4671aaef321e28baacba.cif",
      "contentSize": 178876,
      "sha256": "84a65798c5a227119ad96b921e6f3e19ed34b23cfcee350be8d74c63e0e95d40"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.dna",
      "@type": "File",
      "description": "",
      "name": "example.dna",
      "alternateName": "da/da0d53ba80033e36fa2d86d7de38d66b4ad588ca19b453e72a0401cdd47e90e63e7e974f13a98101407c87a72911657221c190f20eb073067aee20342e7885c2.dna",
      "contentSize": 27050,
      "sha256": "96639ecb57ddec5116d3cb3a9d4a3d5b37e89bbd9a7a3df782fe3e827f3fd787"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.docx",
      "@type": "File",
      "description": "",
      "name": "example.docx",
      "alternateName": "71/7181ab9a4af526d4cdedd09397d45e28b3f2beb740c0eaf5f0cd36a51f3e78bf316b9cf32f8d63baee8da7efeca3f0d469746bb8f20fade1338a3a3d12716ac6.docx",
      "contentSize": 4147,
      "sha256": "f1bc2027abdc4df60fbb1b0123fa73f768fe85f4e7cd277ad6a338b2cae089c0"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.epub",
      "@type": "File",
      "description": "",
      "name": "example.epub",
      "alternateName": "a1/a1b1bd7168e298582af6cadeca5fe4a7093074107ec546fdd6fd1e63571b6a0b45b7eccf384e43940924f8e68da794da8b990017f2e31be199dbac991e7bebad.epub",
      "contentSize": 4051596,
      "sha256": "d2e2091e98c37e43e6ea101101f667b50901a1fd35ac1d3fc949eed96d876bf2"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gbk",
      "@type": "File",
      "description": "",
      "name": "example.gbk",
      "alternateName": "50/501463c206f84aa082eea31105c11e0c03f0a3a0bc3b7a5a05f15c0170f443086a08e823ea8e55d4894b4de9e2cd3a93c350dbe8996a9d6cb4cf5eadf033ebe3.gbk",
      "contentSize": 7472,
      "sha256": "a092b86343c74697ac70542d5a75843230b69555e01e5460bac8cddab1dbecea"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gif",
      "@type": "File",
      "description": "",
      "name": "example.gif",
      "alternateName": "ee/eefcf9ec863fcf9edd5eb6eb58461264ffc59bc99caf7743cad5705a8b87981cb8e60b81441db39828ae4bee3bb5f9c652330a533f4ed033e7a49b6c7a08728b.gif",
      "contentSize": 761850,
      "sha256": "b82134e798bdd719324859b08bf21698e4ec11f2eac64a56cae88e4bf654fbb6"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gz",
      "@type": "File",
      "description": "",
      "name": "example.gz",
      "alternateName": "90/9086a42687d9132d3564b4a61d9f32b684afbb20032a66635941a150e64ed72e981e6d91fe07271b800d0e7da9cfc47b420c8d2dc3762c3fe22085e1b7abea56.gz",
      "contentSize": 183635,
      "sha256": "70c6cee1cb22095026ebddaac03afe10550087c3397d1f2b05850b48ef618dde"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jcamp",
      "@type": "File",
      "description": "",
      "name": "example.jcamp",
      "alternateName": "d0/d0e2a12fb7b546cc7da8b77bb8fbc929676472df34321f7e200825a9d00f41c92990ea6d61c3cc9f9b29d85a8f82a495e863a7ae63f5bbbb0f41ad4a18a5d6e0.jcamp",
      "contentSize": 110797,
      "sha256": "b412adc50ab3583b5bf8b73b6e2f392d720058b5fc12b5a3b46f40fd6f64ed48"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jdx",
      "@type": "File",
      "description": "",
      "name": "example.jdx",
      "alternateName": "44/44a75b98c5addb36e980abc00a176c09a08d6f44b660ef5d3abdf9cf7eba10088939e41f18eb019e73b9ab26e5192425d549a9b2a681d959a070204598f343d7.jdx",
      "contentSize": 37207,
      "sha256": "3ff02ba7a73c1340e83a73179115aee794a90a6e1bcc9775afff82a822cdb6e0"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jpg",
      "@type": "File",
      "description": "",
      "name": "example.jpg",
      "alternateName": "29/2993b708756f0e827d3da5b22da6ab66aad991b1131b03ec74f2f7361c81ac49785f9d22933836106d939c2d3ba4317807b2b1c5e9bac89e48874c731b05bf84.jpg",
      "contentSize": 85530,
      "sha256": "b73626c9a9ed8561ed6126df2493bc0d84fb8feedc9fe34aed94f7d2d5f4f60f"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.json",
      "@type": "File",
      "description": "",
      "name": "example.json",
      "alternateName": "73/7386a19849c0daedc002f59aed22679f9b415e0ca6b0b126d92bcdaffc2bea708741d958901590854858186b418f0ac71069718397b87b4f9baa129944d6f512.json",
      "contentSize": 1734,
      "sha256": "58de2671fcd268ffd1706d5e217bac191b02354f0345a0ee948fa1139600b988"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mnova",
      "@type": "File",
      "description": "",
      "name": "example.mnova",
      "alternateName": "a3/a3a81c24f9f1d2fc49dc12cd45c21021e59ed98166864b92bf100c04dcbb524b3980db59a2fd31d94f8fd2307cedb49c56ce3878f0108de252a10fcbf864e382.mnova",
      "contentSize": 139349,
      "sha256": "4e5b9311b1c8a4d6a1c8c4ec94aa7ee5cd2ee676b6ad7720fac67c33d670e383"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mol",
      "@type": "File",
      "description": "",
      "name": "example.mol",
      "alternateName": "ed/edfa30f08d64bb8c71e3ec2692a0d1f5af58c1cbb9152034863e3aa94c3396a54beed294e2de88d8fda41d60920e0ed247333fcebd1527e53fa24e5cf4591486.mol",
      "contentSize": 1664,
      "sha256": "5622cb4d7a5e6166a3527345ffc864a768cd03c3f77511a5988853c402c504a4"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mp4",
      "@type": "File",
      "description": "",
      "name": "example.mp4",
      "alternateName": "ae/aea416d40ea71b1e9c5048b861a4418266a11a0c23e3d5a3b421e8411fe7312b532355b2928ed8bc6c27b44742d2e7e0cdd64a0dfe57a4d0a6f2f7ad7ac2d94b.mp4",
      "contentSize": 184144,
      "sha256": "2a729ba8ddca2e2270effed052ceed5a1167a8d1c4ee856ace3d55635fca243d"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.odp",
      "@type": "File",
      "description": "",
      "name": "example.odp",
      "alternateName": "e9/e92076d7a9181d73a796507134644a2fef4d7472be0f5bfc01ddcdb8a644e123688991b13dd9054f6f840ff65ea71adffffdc319714b74794515026aadb1249f.odp",
      "contentSize": 50014,
      "sha256": "7a6eb056b0c2a67da89f1a3f42f348b06f931d07f5124468dfdee187702e2444"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdb",
      "@type": "File",
      "description": "",
      "name": "example.pdb",
      "alternateName": "c7/c7efe2df0cfee747597532804b3f4e592291ad3df996ded49fe42bf4b8e6c5dbe3b4d7b3d2916b3ee74f55db19d9a0fd528711581171e63588635da553c83f54.pdb",
      "contentSize": 515889,
      "sha256": "aa8a72b1c6fe310d25851742e4c30599bbcd4764c2a26578bad0fae70d8f0627"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdf",
      "@type": "File",
      "description": "",
      "name": "example.pdf",
      "alternateName": "2f/2f9c2d6a298ae1e31f3c72a524e9ffedd70680d5caa4cf4f66e1e86c85d337a8735200b855d32394166083402e0acc04f04d1eb30f74630e34ef878ed96c3aad.pdf",
      "contentSize": 116369,
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.png",
      "@type": "File",
      "description": "",
      "name": "example.png",
      "alternateName": "5d/5d8813cede85d152c8960b0f459b1832811b8ddbd8eb2b4e7a667e2c310209fd02a89da41173ac19abf318dcde0aa9f6d44b88a97692b8eb8481878ef0cb8266.png",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pps",
      "@type": "File",
      "description": "",
      "name": "example.pps",
      "alternateName": "23/23e1ee184021357d0a68a74cb986873d6e4be35a8a85c645c4a941004caefc49d0f52032aa9402accfe0ea23cdc675270730cdf2c6304ade383f93d654b1d7d9.pps",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppsx",
      "@type": "File",
      "description": "",
      "name": "example.ppsx",
      "alternateName": "90/90afa1d4af023351e6d7870192e99aaf74aee53d6cd551d0b433eb3ed9f24714018fdd4fb4d22d0104c225af4de00c7d3b28e80899650bbaf34f713c47b6445e.ppsx",
      "contentSize": 57375,
      "sha256": "7af9d974a47b6d081f1ce7ad0e3d5af21be6aeb664938cef6cfd8bdf1937cb2a"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppt",
      "@type": "File",
      "description": "",
      "name": "example.ppt",
      "alternateName": "9b/9bba763855d2dcf12dae08c87e46b7c1f9e3e39f6f49dff0cfed8e4266f0a13747a9c90fbf145d485e20533cacf87770932808876594c027ce531e2a398409d9.ppt",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pptx",
      "@type": "File",
      "description": "",
      "name": "example.pptx",
      "alternateName": "a1/a1b1e04f9d5c27592a136657f104779f3241333cbad08ccd53a00ff0867085b9d1b857a0e9d3672bff5dac4ff36c6ce6c8b8ebb60668def22604af9d5796b527.pptx",
      "contentSize": 57375,
      "sha256": "4fc01c51e094f4410a56f05f513be829425f12e7b33b5296115126a84aba74e7"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.sdf",
      "@type": "File",
      "description": "",
      "name": "example.sdf",
      "alternateName": "e4/e406de40ed0b0df4b5ef632314c36856e9fb49cc535985d281c924fb3cf030ce69b1f227ebd79a4f5826b1198ec18c50f4880bf1f9c07bb0446863528a8b5682.sdf",
      "contentSize": 3782,
      "sha256": "f44f2e734602a5ac09f4692e111f2c386af5c88691488d4bc2a5ecbd507e4ad4"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.tif",
      "@type": "File",
      "description": "",
      "name": "example.tif",
      "alternateName": "30/3034cf92edab4068e0da359580f6f9e14afdb0320592eb9809ebfcb998de5a51b1096b83d01922f305d8ac76c464d062eab8287be6083a967f77ff154900faf2.tif",
      "contentSize": 678520,
      "sha256": "69ca1ba6fed2b3f44f12fcc8ce8d4f945fe42dc81675acbd894a430676ebdc2e"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.xyz",
      "@type": "File",
      "description": "",
      "name": "example.xyz",
      "alternateName": "a2/a2b74ec8e3dc322e0fb60d5b80fd1ac4ddaf7d33227f8df7bdb22e7e6657044efddc459fb41c761846b36d85eecac75cd73e8c3abc2ef1de33dd8df8d0d6fcf9.xyz",
      "contentSize": 1079,
      "sha256": "99f6c504dad42fe09f6d7c2422f720a671384a0de47c6bbb24f6b895baa87aec"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/README.md",
      "@type": "File",
      "description": "",
      "name": "README.md",
      "alternateName": "e8/e8fc2c6c15f6205d6f9ad4a89bf0b06d45f2dc7a6368855696eaae7493025222b1f818b4cc53780fe92598e4f92c3fc09a56f92d461696a3fb0352989b7fa04a.md",
      "contentSize": 265,
      "sha256": "dca1f13c35d4a719c8e8e0c45d84c6ad0f378c245e90a92127b2af8d1df89b9b"
    },
    {
      "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:51+02:00",
      "dateModified": "2023-07-31T13:37:58+02:00",
      "identifier": "20230729-75bb78f9339de02ec3ffe44129de4d0c9cba1550",
      "comment": [
        {
          "@id": "comment://2023-07-29T20%3A24%3A51%2B02%3A00",
          "dateCreated": "2023-07-29T20:24:51+02:00",
          "text": "Well, it&#39;s always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
          "author": {
            "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
          }
        }
      ],
      "keywords": [
        "demo",
        "test"
      ],
      "name": "Testing the eLabFTW lab notebook",
      "text": "<h1>Goal</h1><p>Test the software.</p><h1>Procedure</h1><p>Click everywhere and explore everything.</p><h1>Results</h1><p>It's really nice, I think I'll adopt it for our lab.</p>",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=264",
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/export-elabftw.json"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.avi"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.bmp"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cdx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.cif"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.dna"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.docx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.epub"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gbk"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gif"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.gz"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jcamp"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jdx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.jpg"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.json"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mnova"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mol"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.mp4"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.odp"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdb"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pdf"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.png"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pps"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppsx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.ppt"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.pptx"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.sdf"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.tif"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/example.xyz"
        },
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9/README.md"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=50",
          "@type": "Dataset",
          "name": "Generated - Sint eos explicabo eum incidunt omnis.",
          "identifier": "20230729-78af171c99a3681027cb7cccaa921dbd3e7ff631"
        },
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=51",
          "@type": "Dataset",
          "name": "Generated - Fugit dignissimos ad consequatur facilis necessitatibus.",
          "identifier": "20230729-70f542b44469b7ce7741351e4f4db6dc64a4e6a3"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=256",
          "@type": "Dataset",
          "name": "Success - Test the grouped extra fields",
          "identifier": "20230729-76a26adbc7532fadcb74876ab3efd83921ef478a"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=257",
          "@type": "Dataset",
          "name": "Success - An example experiment",
          "identifier": "20230729-46af8abf379be3f35cf33ad5990a886e9e7da65b"
        },
        {
          "@id": "https://elab.local:3148/experiments.php?mode=view&id=258",
          "@type": "Dataset",
          "name": "Success - Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
          "identifier": "20230729-ac1839136f9d133973dff2c074a2c6619c9cec3e"
        }
      ]
    },
    {
      "@id": "./2025-01-02 - Synthesis-of-Aspirin - 0fe20329/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "4901",
      "sha256": "1ad499abee58803fe4bf3b11fc4a9fe5c4aa8bbac3054a5ffa5f09ed72c0484d"
    },
    {
      "@id": "./2025-01-02 - Synthesis-of-Aspirin - 0fe20329",
      "@type": "Dataset",
      "author": {
        "@id": "person://3056605372202682ba1f40a0cd27abd010aa21854c735ff127f3eeff05eba6fd?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:51+02:00",
      "dateModified": "2023-07-29T20:24:51+02:00",
      "identifier": "20230729-0fe203297d4cf567e21f8c2e9eb1c633e0a1c1aa",
      "comment": [],
      "keywords": [
        "chemistry",
        "has-mathjax"
      ],
      "name": "Synthesis of Aspirin",
      "text": "<h1>Introduction</h1>\n<p>\nAspirin is a widely used pain-relieving and anti-inflammatory drug. In this experiment, we aimed to synthesize aspirin from salicylic acid and acetic anhydride.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe mixed salicylic acid and acetic anhydride in the presence of a catalyst, sulfuric acid. The reaction produced aspirin and acetic acid, as shown in the following chemical equation:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nAfter the reaction, we purified the aspirin by recrystallization from hot water. The purity of the aspirin was confirmed using thin-layer chromatography (TLC) and melting point analysis.\n</p>\n<h2>Results</h2>\n<p>\nThe yield of aspirin was 80% based on the amount of salicylic acid used. The purity of the aspirin was confirmed using TLC, which showed a single spot corresponding to aspirin. The melting point of the aspirin was 135-136\u00b0C, which is consistent with the literature value of 135-136.5\u00b0C.\n</p>\n<p>\nThe chemical reaction involved in the synthesis of aspirin can be written as:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nThe theoretical yield of aspirin can be calculated using the stoichiometry of the reaction. Assuming that all the salicylic acid reacts and no aspirin is lost during the purification process, the theoretical yield is calculated as follows:\n</p>\n<p>\n$$\\text{Theoretical yield} = \\frac{\\text{moles of salicylic acid used}}{\\text{molar ratio of salicylic acid to aspirin}} \\times \\text{molar mass of aspirin}$$\n</p>\n<p>\nThe actual yield of aspirin can be calculated by dividing the mass of the purified aspirin by the mass of salicylic acid used and multiplying by 100%. The percent yield can be calculated by dividing the actual yield by the theoretical yield and multiplying by 100%.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=263",
      "hasPart": [
        {
          "@id": "./2025-01-02 - Synthesis-of-Aspirin - 0fe20329/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./2025-01-02 - Testing-relationship-between-acceleration-and-gravity - b5d83c6e/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "3814",
      "sha256": "f8d840037c8ded9b356a37ce8f414e3f210a4dfd42760d26142f32b049f9b0e1"
    },
    {
      "@id": "./2025-01-02 - Testing-relationship-between-acceleration-and-gravity - b5d83c6e",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:50+02:00",
      "dateModified": "2023-07-29T20:24:51+02:00",
      "identifier": "20230729-b5d83c6e5288477c736c078fea57e9a0a3343322",
      "comment": [],
      "keywords": [
        "has-mathjax",
        "physics"
      ],
      "name": "Testing relationship between acceleration and gravity",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=262",
      "hasPart": [
        {
          "@id": "./2025-01-02 - Testing-relationship-between-acceleration-and-gravity - b5d83c6e/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./2025-01-02 - Effect-of-temperature-on-enzyme-activity - ddfea685/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "5533",
      "sha256": "cc43ea6c205c98c7654bf1408fd5fbad1866f82447643d1b8a27212e728d8fe9"
    },
    {
      "@id": "./2025-01-02 - Effect-of-temperature-on-enzyme-activity - ddfea685",
      "@type": "Dataset",
      "author": {
        "@id": "person://6c0f5f0764818e1d283b3324d74a6996a2a207acbad292f44fa8ae1f163ad5d1?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:50+02:00",
      "dateModified": "2023-07-29T20:24:50+02:00",
      "identifier": "20230729-ddfea685c94e09d6561826f56095c8d5f8791d0f",
      "comment": [],
      "keywords": [
        "enzymology",
        "test",
        "Project ENZYTEMP"
      ],
      "name": "Effect of temperature on enzyme activity",
      "text": "<h1>Effect of Temperature on Enzyme Activity</h1>\n<p>\nEnzymes are biological molecules that catalyze chemical reactions in living organisms. In this experiment, we investigated the effect of temperature on the activity of the enzyme amylase, which catalyzes the hydrolysis of starch into glucose.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe prepared a solution of starch and added a small amount of amylase to the solution. We then incubated the solution at different temperatures, ranging from 4\u00b0C to 70\u00b0C, for 5 minutes. After the incubation period, we added iodine to the solution to detect the presence of starch. The disappearance of the blue-black color of the iodine indicated the breakdown of starch into glucose.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the activity of amylase increased with increasing temperature up to 37\u00b0C, which is the optimum temperature for amylase activity. At temperatures above 37\u00b0C, the activity of amylase decreased rapidly, and at 70\u00b0C, the enzyme was completely denatured and lost its catalytic activity.\n</p>\n<p>\nThe relationship between temperature and enzyme activity can be described by the Arrhenius equation, which relates the rate constant of a reaction to the activation energy and temperature. The equation can be written as:\n</p>\n<p>\n$$k = Ae^{-E_a/RT}$$\n</p>\n<p>\nwhere k is the rate constant, A is the pre-exponential factor, E_a is the activation energy, R is the gas constant, and T is the absolute temperature. The activation energy is the energy required to break the bonds in the reactants and form the products. The rate constant increases with increasing temperature due to the increase in the number of reactant molecules with sufficient kinetic energy to overcome the activation energy barrier.\n</p>\n<p>\nThe effect of temperature on enzyme activity can also be described by the Q10 value, which is the ratio of the reaction rate at a given temperature to the reaction rate at a temperature 10\u00b0C lower. The Q10 value for most enzyme-catalyzed reactions is around 2-3, indicating that the reaction rate doubles or triples with each 10\u00b0C increase in temperature.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=261",
      "hasPart": [
        {
          "@id": "./2025-01-02 - Effect-of-temperature-on-enzyme-activity - ddfea685/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./2025-01-02 - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - d6e80daf/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "7292",
      "sha256": "b1fd7d857b31e5f6b4eb164f43182fd9a740230f0a4797e40867d6e75cf71fb6"
    },
    {
      "@id": "./2025-01-02 - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - d6e80daf",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:50+02:00",
      "dateModified": "2023-07-29T20:24:50+02:00",
      "identifier": "20230729-d6e80dafca120e746bdbc357a171a11282c10a0f",
      "comment": [],
      "keywords": [
        "CJK",
        "\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8"
      ],
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "text": "<p>\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002</p>\n\n<p>\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002</p>\n\n<p>\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002</p>\n\n<p>\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002</p>\n\n<p>\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=260",
      "hasPart": [
        {
          "@id": "./2025-01-02 - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - d6e80daf/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./2025-01-02 - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial-Properties - 016a57a1/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "4950",
      "sha256": "c66e2c2e9dda842bdde7abaf9354306228ab285f190ed79d5cc03f6faba61286"
    },
    {
      "@id": "./2025-01-02 - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial-Properties - 016a57a1",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:50+02:00",
      "dateModified": "2023-07-29T20:24:50+02:00",
      "identifier": "20230729-016a57a1cec70e6cf5368f81ba86b686487035a5",
      "comment": [],
      "keywords": [
        "synthesis",
        "antimicrobial",
        "chemistry"
      ],
      "name": "Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties",
      "text": "<h1>Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties</h1>\n<p>\nThe emergence of drug-resistant bacterial strains has become a major public health concern, highlighting the need for the development of new antimicrobial agents. In this study, we aimed to synthesize a novel organic compound with potential antimicrobial activity.\n</p>\n<h2>Experimental Design</h2>\n<p>\nThe compound was synthesized via a multi-step reaction scheme. The starting material, benzaldehyde, was reacted with aniline in the presence of an acid catalyst to form the intermediate product, N-phenylbenzamide. The intermediate product was then reacted with thionyl chloride to form the corresponding acid chloride. The acid chloride was then reacted with aminoguanidine in the presence of a base catalyst to form the final product, which was purified by recrystallization.\n</p>\n<h2>Characterization</h2>\n<p>\nThe synthesized compound was characterized using various spectroscopic techniques. The melting point of the compound was determined using a melting point apparatus and compared to the literature value. The IR spectrum of the compound was obtained using a Fourier transform infrared spectrometer and compared to the expected spectrum. The NMR spectrum of the compound was obtained using a nuclear magnetic resonance spectrometer and analyzed to confirm the structure of the compound.\n</p>\n<h2>Antimicrobial Activity</h2>\n<p>\nThe antimicrobial activity of the synthesized compound was evaluated against several bacterial strains using the disk diffusion method. The results showed that the compound exhibited significant antimicrobial activity against both Gram-positive and Gram-negative bacteria, suggesting its potential as a new antimicrobial agent.\n</p>\n",
      "url": "https://elab.local:3148/experiments.php?mode=view&id=259",
      "hasPart": [
        {
          "@id": "./2025-01-02 - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial-Properties - 016a57a1/export-elabftw.json"
        }
      ],
      "mentions": [
        {
          "@id": "https://elab.local:3148/database.php?mode=view&id=50",
          "@type": "Dataset",
          "name": "Generated - Sint eos explicabo eum incidunt omnis.",
          "identifier": "20230729-78af171c99a3681027cb7cccaa921dbd3e7ff631"
        }
      ]
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./2025-03-03 - Testing-the-eLabFTW-lab-notebook - 75bb78f9"
        },
        {
          "@id": "./2025-01-02 - Synthesis-of-Aspirin - 0fe20329"
        },
        {
          "@id": "./2025-01-02 - Testing-relationship-between-acceleration-and-gravity - b5d83c6e"
        },
        {
          "@id": "./2025-01-02 - Effect-of-temperature-on-enzyme-activity - ddfea685"
        },
        {
          "@id": "./2025-01-02 - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - d6e80daf"
        },
        {
          "@id": "./2025-01-02 - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial-Properties - 016a57a1"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    },
    {
      "@id": "person://3056605372202682ba1f40a0cd27abd010aa21854c735ff127f3eeff05eba6fd?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Stracke",
      "givenName": "Cory"
    },
    {
      "@id": "person://6c0f5f0764818e1d283b3324d74a6996a2a207acbad292f44fa8ae1f163ad5d1?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Pfannerstill",
      "givenName": "Lizeth"
    }
  ]
}
```

### multiple-database-items.eln
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
      "dateCreated": "2023-07-31T14:37:22+02:00",
      "sdPublisher": {
        "@type": "Organization",
        "name": "eLabFTW",
        "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
        "slogan": "A free and open source electronic lab notebook.",
        "url": "https://www.elabftw.net",
        "parentOrganization": {
          "@type": "Organization",
          "name": "Deltablot",
          "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
          "slogan": "Open Source software for research labs.",
          "url": "https://www.deltablot.com"
        }
      },
      "version": "1.0"
    },
    {
      "@id": "./Plasmid - pCMV-Tag2B - 20f8c1ff/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1704",
      "sha256": "91b7d1261f3dabd6f9b64e7b08e424020a61b48f3766e24609b108e780308807"
    },
    {
      "@id": "./Plasmid - pCMV-Tag2B - 20f8c1ff",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:25:00+02:00",
      "dateModified": "2023-07-29T20:25:00+02:00",
      "identifier": "20230729-20f8c1ff8f1cf23c390dd4988b980e39dc7ce0e2",
      "comment": [],
      "keywords": [],
      "name": "pCMV-Tag2B",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=177",
      "hasPart": [
        {
          "@id": "./Plasmid - pCMV-Tag2B - 20f8c1ff/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Plasmid - pMAL-c2x - 12102fd2/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1702",
      "sha256": "d579e562167ce5f64b76fc8f8e3c662bbb4b35ae416247e2118cfc24ee530c76"
    },
    {
      "@id": "./Plasmid - pMAL-c2x - 12102fd2",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-12102fd2be6bb796df494b82ab9067e300cb3de8",
      "comment": [],
      "keywords": [],
      "name": "pMAL-c2x",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=176",
      "hasPart": [
        {
          "@id": "./Plasmid - pMAL-c2x - 12102fd2/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Antibody - Anti-Phospho-AKT-Ser473 - 885dd066/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1650",
      "sha256": "8a13f80670ea36455706f0b012b5fbcfd01ff8b19703ce028ebf6c0609df3921"
    },
    {
      "@id": "./Antibody - Anti-Phospho-AKT-Ser473 - 885dd066",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-885dd06684b5106e1e3146d249ffd27cae96448e",
      "comment": [],
      "keywords": [],
      "name": "Anti-Phospho-AKT (Ser473)",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=175",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-Phospho-AKT-Ser473 - 885dd066/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Antibody - Anti-Caspase-3 - 6e987a21/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1639",
      "sha256": "deabf18d70452e5ebdb02b827871bf0210af99722832853592a1785dbfba16e6"
    },
    {
      "@id": "./Antibody - Anti-Caspase-3 - 6e987a21",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-6e987a216522b0210daec1e6abc1de0705d5e6d8",
      "comment": [],
      "keywords": [],
      "name": "Anti-Caspase-3",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=174",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-Caspase-3 - 6e987a21/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Chemical-compound - Formaldehyde-CH2O - 79fd3fd9/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1216",
      "sha256": "4746d555674596235922bffb082f3b4d9d2b8ea87d1925ff18db1c313fb33e2e"
    },
    {
      "@id": "./Chemical-compound - Formaldehyde-CH2O - 79fd3fd9",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-79fd3fd98b1e44a9977a3e73968da3b02622530e",
      "comment": [],
      "keywords": [],
      "name": "Formaldehyde - CH2O",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=173",
      "hasPart": [
        {
          "@id": "./Chemical-compound - Formaldehyde-CH2O - 79fd3fd9/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Antibody - Anti-CD11b - 2d88b2a6/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1506",
      "sha256": "9341400e55b38ecf7b336822724ea52ba86d70ecb3191fb4ed0fc4cc492fd8ee"
    },
    {
      "@id": "./Antibody - Anti-CD11b - 2d88b2a6",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-2d88b2a65ae4897faa6912e88e93cb20a12e7419",
      "comment": [],
      "keywords": [],
      "name": "Anti-CD11b",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=172",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-CD11b - 2d88b2a6/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Antibody - Anti-CD4 - 3bf425e6/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "2215",
      "sha256": "34c30952244e9c2313704a895a3273deb989589b4c5b4bd14fe2cc328fb04eb4"
    },
    {
      "@id": "./Antibody - Anti-CD4 - 3bf425e6",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-3bf425e6eb2f917dd6715258267784612cd65ec7",
      "comment": [],
      "keywords": [],
      "name": "Anti-CD4",
      "text": "<p>Anti-CD4 is a monoclonal mouse antibody that recognizes the CD4 antigen, a cell surface glycoprotein found on T-helper cells, regulatory T-cells, and monocytes. This antibody has been extensively used for flow cytometry, immunohistochemistry, and Western blotting. The antibody was generated by immunizing mice with human CD4-positive T-cell lines.</p>",
      "url": "https://elab.local:3148/database.php?mode=view&id=171",
      "hasPart": [
        {
          "@id": "./Antibody - Anti-CD4 - 3bf425e6/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./Microscope - Video-microscope-Bravo - a7c2409c/export-elabftw.json",
      "@type": "File",
      "description": "JSON export",
      "name": "export-elabftw.json",
      "encodingFormat": "application/json",
      "contentSize": "1821",
      "sha256": "d1a21ec5d6ea07df664b0835aa7dc4938b130ff85edf14e8637489bdf6f64627"
    },
    {
      "@id": "./Microscope - Video-microscope-Bravo - a7c2409c",
      "@type": "Dataset",
      "author": {
        "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256"
      },
      "dateCreated": "2023-07-29T20:24:59+02:00",
      "dateModified": "2023-07-29T20:24:59+02:00",
      "identifier": "20230729-a7c2409c657e3c534bc4e6f794a1b46d49084fd3",
      "comment": [],
      "keywords": [],
      "name": "Video microscope Bravo",
      "text": "",
      "url": "https://elab.local:3148/database.php?mode=view&id=170",
      "hasPart": [
        {
          "@id": "./Microscope - Video-microscope-Bravo - a7c2409c/export-elabftw.json"
        }
      ],
      "mentions": []
    },
    {
      "@id": "./",
      "@type": [
        "Dataset"
      ],
      "hasPart": [
        {
          "@id": "./Plasmid - pCMV-Tag2B - 20f8c1ff"
        },
        {
          "@id": "./Plasmid - pMAL-c2x - 12102fd2"
        },
        {
          "@id": "./Antibody - Anti-Phospho-AKT-Ser473 - 885dd066"
        },
        {
          "@id": "./Antibody - Anti-Caspase-3 - 6e987a21"
        },
        {
          "@id": "./Chemical-compound - Formaldehyde-CH2O - 79fd3fd9"
        },
        {
          "@id": "./Antibody - Anti-CD11b - 2d88b2a6"
        },
        {
          "@id": "./Antibody - Anti-CD4 - 3bf425e6"
        },
        {
          "@id": "./Microscope - Video-microscope-Bravo - a7c2409c"
        }
      ]
    },
    {
      "@id": "person://a0568e4aa35eec2cf3962db57eec039a205d3b7d7c7132388af976dfaf8f2694?hash_algo=sha256",
      "@type": "Person",
      "familyName": "Le sysadmin",
      "givenName": "Toto"
    }
  ]
}
```
