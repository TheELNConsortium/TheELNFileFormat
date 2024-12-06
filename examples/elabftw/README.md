# eLabFTW examples

## Information

* Repo: https://github.com/elabftw/elabftw
* Chat: https://gitter.im/elabftw/elabftw

You can generate .eln files from the demo: https://demo.elabftw.net. Select a few entries and export as .eln from the top menu. Or go to the Import section and do a full export.

## Concepts used

Here is a correspondance between concepts in eLabFTW and how they are translated in the metadata json file in the archive:

| eLabFTW concepts    | JSON property          |
|---------------------|------------------------|
| body (main content) | text                   |
| category            | about                  |
| comments            | comment                |
| content_type        | encodingFormat         |
| created_at          | dateCreated            |
| custom_id           | alternateName          |
| elabid              | identifier             |
| entity type         | genre                  |
| links               | mentions               |
| metadata            | variableMeasured       |
| modified_at         | dateModified           |
| owner               | author                 |
| rating              | aggregateRating        |
| status              | creativeWorkStatus     |
| steps               | step                   |
| tags                | keywords               |
| title               | name                   |


### export.eln
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
      "dateCreated": "2024-11-17T15:10:44+01:00",
      "sdPublisher": {
        "@id": "#publisher"
      },
      "version": "1.0"
    },
    {
      "@id": "https://www.deltablot.com",
      "@type": "Organization",
      "areaServed": "Laniakea Supercluster",
      "name": "Deltablot",
      "logo": "https://www.deltablot.com/img/logos/deltablot.svg",
      "slogan": "Open Source software for research labs.",
      "url": "https://www.deltablot.com"
    },
    {
      "@id": "#publisher",
      "@type": "Organization",
      "areaServed": "Laniakea Supercluster",
      "name": "eLabFTW",
      "logo": "https://www.elabftw.net/img/elabftw-logo-only.svg",
      "slogan": "A free and open source electronic lab notebook.",
      "url": "https://www.elabftw.net",
      "parentOrganization": {
        "@id": "https://www.deltablot.com"
      }
    },
    {
      "@id": "#ro-crate_created",
      "@type": "CreateAction",
      "object": {
        "@id": "./"
      },
      "name": "RO-Crate created",
      "endTime": "2024-11-17T15:10:44+01:00",
      "instrument": {
        "@id": "https://www.elabftw.net"
      },
      "actionStatus": {
        "@id": "http://schema.org/CompletedActionStatus"
      }
    },
    {
      "@id": "https://www.elabftw.net",
      "@type": "SoftwareApplication",
      "name": "eLabFTW",
      "version": "5.1.11",
      "identifier": "https://www.elabftw.net"
    },
    {
      "@id": "comment://4fb80877aeb18492a13ff6ae43049f5730b7846e97a9b99d70397f5ddaf5945d?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-11-17T03:02:01+01:00",
      "text": "Well, it's always reassuring to know that scientists are spending their time and our tax dollars discovering what the rest of us already learned in third-grade science class.",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/README.md",
      "@type": "File",
      "name": "README.md",
      "alternateName": "eb/eb8e9c8c2f4270e35c43cce4f38714f15098c0d2cb22d8e84a9ddbed92f742bdcc9dc8035d119f3e3911639cb46b9204781148bbceca15f9c59eb9e9e437b1a1.md",
      "contentSize": 265,
      "sha256": "dca1f13c35d4a719c8e8e0c45d84c6ad0f378c245e90a92127b2af8d1df89b9b"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.avi",
      "@type": "File",
      "name": "example.avi",
      "alternateName": "be/be5d5862c67bb090a29edab5616031832028945a8acc45e1dbb360dc514f88e0f312612c0b74b439324bce431d5167366a8dc57f455e40fe3fc6e3bb37083292.avi",
      "contentSize": 200334,
      "sha256": "ebae6bea18cf01d4bc9a974ad71a9aad2ecfaf03ec483a2364d22b8b37ae00bd"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.bmp",
      "@type": "File",
      "name": "example.bmp",
      "alternateName": "98/98b9582861cb49275ba9818c1773ee358751165546f63533a5c5fd71ce1f1f5a540bfb3a2449d6ad1092875c9f21fdbb3544c929b3fdf01e4b48448cdd449a6e.bmp",
      "contentSize": 3000122,
      "sha256": "2b9835aa11ec6fe69d525eed76247728ef55df16d20a7258bf6e04377e7f33da"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.epub",
      "@type": "File",
      "name": "example.epub",
      "alternateName": "f7/f7544a0f0554e5d4994da7f93cb9ebc94e8280b18cd5e4162962de10bbcf4962ae3c53390bc584a6fbca1eaf5acd7e44d00c84026bb7addfd3e3891c9ccb1827.epub",
      "contentSize": 4051596,
      "sha256": "d2e2091e98c37e43e6ea101101f667b50901a1fd35ac1d3fc949eed96d876bf2"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.gif",
      "@type": "File",
      "name": "example.gif",
      "alternateName": "23/23426cf403c8f6f88435d0e600c3094ea780472e48497fd682b933b6296ca0756a0b754c32b6acc8c93bc62e35a3b961f9e82c738a5517d7c56079217ca2e732.gif",
      "contentSize": 761850,
      "sha256": "b82134e798bdd719324859b08bf21698e4ec11f2eac64a56cae88e4bf654fbb6"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.mol",
      "@type": "File",
      "name": "example.mol",
      "alternateName": "5f/5f714e9ae73ce08838ada36b17d1d9ba1e4983665093b079a93f3264d1dec844481010204e77799078528c82e721d61f860cfc93685104620a5d2af5a4361675.mol",
      "contentSize": 1664,
      "sha256": "5622cb4d7a5e6166a3527345ffc864a768cd03c3f77511a5988853c402c504a4"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.json",
      "@type": "File",
      "name": "example.json",
      "alternateName": "1f/1f26c34624fb61c29f4f69bc6d62bc1079bb096e29e387faf62c932d14fdf19d063d81b9a1db514c2355cc773288410843f4119d05ca9a3b9e32aaa7a0a2bb61.json",
      "contentSize": 1734,
      "sha256": "58de2671fcd268ffd1706d5e217bac191b02354f0345a0ee948fa1139600b988"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.jpg",
      "@type": "File",
      "name": "example.jpg",
      "alternateName": "34/347012735b20c53f4fbcd2fa2af1b6c1af1b344f843978888de7b8e82c0d3b086f71385a432084c8524414630d55e72bd45b664343bf980cdf1db0cbdd3d685a.jpg",
      "contentSize": 85530,
      "sha256": "b73626c9a9ed8561ed6126df2493bc0d84fb8feedc9fe34aed94f7d2d5f4f60f"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.jdx",
      "@type": "File",
      "name": "example.jdx",
      "alternateName": "6b/6b150c2b0fc1603b0e7324043d6e781e00b002430aae849d4ad1c8434ac00a382baf9769efa2108409144581f2c0b12a7e2263044b5eef7954373523fb469b76.jdx",
      "contentSize": 37207,
      "sha256": "3ff02ba7a73c1340e83a73179115aee794a90a6e1bcc9775afff82a822cdb6e0"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.jcamp",
      "@type": "File",
      "name": "example.jcamp",
      "alternateName": "02/02dc3057c493d6da3cfbe7fba880f2a95769d5154628b2f5f5f64a91fa3087d444c094ce821b1d0610981103a18e815965cda15f3c14497f1dc28bc992a346d4.jcamp",
      "contentSize": 110797,
      "sha256": "b412adc50ab3583b5bf8b73b6e2f392d720058b5fc12b5a3b46f40fd6f64ed48"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.gbk",
      "@type": "File",
      "name": "example.gbk",
      "alternateName": "0e/0edeef46d703befa8480bb8fb7a9d19ffb145ba17920806f0bd58685ee7d762841875728abf7fd44ab136834d9b481ea30b7644cadf7bfe9e8b981235a9c75ea.gbk",
      "contentSize": 7472,
      "sha256": "a092b86343c74697ac70542d5a75843230b69555e01e5460bac8cddab1dbecea"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.docx",
      "@type": "File",
      "name": "example.docx",
      "alternateName": "69/69457d06a034a92d3f569efbc8d0c4ce3f975b74d8a249002aec6a13f43bbc8cf1a1d058094119ffcc5f7d4486c175a373a791650717d6bbfe87790f31afcdb1.docx",
      "contentSize": 4147,
      "sha256": "f1bc2027abdc4df60fbb1b0123fa73f768fe85f4e7cd277ad6a338b2cae089c0"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.dna",
      "@type": "File",
      "name": "example.dna",
      "alternateName": "aa/aa6284b9810144d76c6b15a10abec358be391de24635da901244dfb1eaa7d67def98978995555b01a1da133b4fc1f566ed76574d456048fc5533e5ee43f19cb3.dna",
      "contentSize": 27050,
      "sha256": "96639ecb57ddec5116d3cb3a9d4a3d5b37e89bbd9a7a3df782fe3e827f3fd787"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.cdx",
      "@type": "File",
      "name": "example.cdx",
      "alternateName": "b6/b6578866af6aae6dffc2132ff18daf80d98e7421331000d11ced4a0d5522c0af81cf0ad68c93ea807620bb2af91a3e8e0c99d822e0a3611afbb1310f1b8b5ccd.cdx",
      "contentSize": 1514,
      "sha256": "5efbea7d56c052e2e1fc418ff24ef8b445cd543d07a4c892994647e90d5258dc"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pdf",
      "@type": "File",
      "name": "example.pdf",
      "alternateName": "a4/a4e22d81ccda9daa4c10d3c877aa2d3039c14b20424c77a42a411fd92a08c616ecd190569ccb0b70d724ccf006dff0a25a7e2502f5938e57e8f8219c4b03c38e.pdf",
      "contentSize": 116369,
      "sha256": "39c64aa99f64fbd83b4594f7b1553709a232689bb6cc86067ac79d90019dabb1"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.odp",
      "@type": "File",
      "name": "example.odp",
      "alternateName": "4f/4f507295227e992d82b7b54d5d1d88098c54eaf73b7ef0e42c935691083c7f9e6c075662449d969abd94d35d1866566fa4d27176456f62a94682d939724e2107.odp",
      "contentSize": 50014,
      "sha256": "7a6eb056b0c2a67da89f1a3f42f348b06f931d07f5124468dfdee187702e2444"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pdb",
      "@type": "File",
      "name": "example.pdb",
      "alternateName": "e5/e58fadcf56f2d31b86f0fef337a3664d1c04e909aaea2a976b371d8decd18c813de1e7bc2fc57ef2ee5341a594d3c5ef5d9cabb673038b0c1af0d1727f18ecb1.pdb",
      "contentSize": 515889,
      "sha256": "aa8a72b1c6fe310d25851742e4c30599bbcd4764c2a26578bad0fae70d8f0627"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.png",
      "@type": "File",
      "name": "example.png",
      "alternateName": "cd/cd88e05c123003533178fbb89feb7482cf6e2afb15197394822a320968d45f660515f9da6d62d092605f7c2d271eb15a9dc6deff06a69ac7872601ed18082914.png",
      "contentSize": 40959,
      "sha256": "f2780bb5a8883f8c89a6da1c5bf4604f7cb44bdcb093e16484eb81c1bcb1f580"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pps",
      "@type": "File",
      "name": "example.pps",
      "alternateName": "72/725e682c129bcb393096b3fad494c350c6187f52045c38e8a5937c6efd0be5db28631f9da5b337bc899a849fa4ead0db48274d012c78c8def70ed2fc162046c6.pps",
      "contentSize": 162304,
      "sha256": "a3201e2d74f5cf61863555641642dc189770902e7dcab9e28a0c0777bfad98f9"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.ppsx",
      "@type": "File",
      "name": "example.ppsx",
      "alternateName": "7d/7dee996a9a7c181c1e27163a46ee391ed293f72d06418780dc7f28e8080096848ea4c876333ea2370bab57cf03b561e78024f9a2d807e72fce3dcb5e6b5eed29.ppsx",
      "contentSize": 57375,
      "sha256": "7af9d974a47b6d081f1ce7ad0e3d5af21be6aeb664938cef6cfd8bdf1937cb2a"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.tif",
      "@type": "File",
      "name": "example.tif",
      "alternateName": "09/09819a77eaad10e0b84d455ca7b2405c10126b70920d9782a23555ca767cb277c0cbe8b571bfc1817ebbcaed0440f613e8d4c8f9734916a6ba1d4953930f067e.tif",
      "contentSize": 678520,
      "sha256": "69ca1ba6fed2b3f44f12fcc8ce8d4f945fe42dc81675acbd894a430676ebdc2e"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pptx",
      "@type": "File",
      "name": "example.pptx",
      "alternateName": "03/0327174c00c55853918afb01d1ada259041d1e365c3c2771ed8146c9a10842744dfeca43fb188c74ed7d8cd867cc6c5df425ad36d616d76de8208e69f34659f7.pptx",
      "contentSize": 57375,
      "sha256": "4fc01c51e094f4410a56f05f513be829425f12e7b33b5296115126a84aba74e7"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.wav",
      "@type": "File",
      "name": "example.wav",
      "alternateName": "27/27b4aa4d823cbaed6771b32f2d465a94094a4ccbc639566ccd2278ae91885e9b8ab9312376229f8a985ff951760da7c917c911e0b4ad8449af5f3bebfefd6e9d.wav",
      "contentSize": 582030,
      "sha256": "6f14f15d5346da53c12c5452ff17b10d4c217deef6034c186ac3cd5c86d11844"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.mp4",
      "@type": "File",
      "name": "example.mp4",
      "alternateName": "23/23ea9195d0875d51e7f9b31128b1482336b7462f90c6f7bd1ecf4ac01e6415512d4a64b1801d61f8da8796da962a62584840aaf2c6471be7d49a98e96acaaf66.mp4",
      "contentSize": 86999,
      "sha256": "39478838a3f6460f63ce88e3e84df24a324a4945a00ac26d077fa40eee685f47"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.webm",
      "@type": "File",
      "name": "example.webm",
      "alternateName": "83/83b2cfabf6015ad48910808bdd9e623695f8b905632c900d922d1c55975e6a42874e8a8bf61ba0285fdd45f55d26788fba24c6f9ba63085dc79fdfde83060ddb.webm",
      "contentSize": 35344,
      "sha256": "7d9df0ee10817b92d9849592216a10f56277d0d932d8d8d026ca379bdf2dd72a"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.aac",
      "@type": "File",
      "name": "example.aac",
      "alternateName": "fc/fc3251979f5cf10bd6582f04ff25050f0d3dc3f5989b5d1355062057d3b2dfcdf4a0e0f9266e755a819aab8f9ee72c851b9582b5542c725e925f761529475acb.aac",
      "contentSize": 49862,
      "sha256": "d5625c25d68638813b198db5aef35c78754d87e7f3a533a10a08d8d9115e125d"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.mp3",
      "@type": "File",
      "name": "example.mp3",
      "alternateName": "7e/7e58477610e4087fef85dd30043a8c58b6c195191ab4840ad706aa30294d8ed91629f9ae14e16994bc64b6330ddc9610584ffdc91139c888ec2c2891a8c84d0f.mp3",
      "contentSize": 49388,
      "sha256": "97e1978a6ab500590075bb00202619830d31981ec7ee87951e732da74a35720b"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.ogg",
      "@type": "File",
      "name": "example.ogg",
      "alternateName": "9f/9f32600666f4ec1558a5f8be24d6e62701e68d8518a2a26e9b9540ebb8fe65efe53e384ea9b63511626d2aeb3dfde811109493d391ccf08d03eded4494932958.ogg",
      "contentSize": 38381,
      "sha256": "a57e9c643ccb5f754241e88f5fa94549969a247434fd40c97a937db86085a952"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.flac",
      "@type": "File",
      "name": "example.flac",
      "alternateName": "e0/e06dec2fef05d3433f87f5ef52cdb22d88cd31608436f7e63f41ff1c26a2f40b2c20a17f3332c17c9e6ddccb029ca1563d327f0c662d55d8aca9bc08d1e14c8b.flac",
      "contentSize": 206308,
      "sha256": "fb178f5b984db5db43fb65527121e30f95f0936d05d698e890ec7fdc144b6be2"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.ape",
      "@type": "File",
      "name": "example.ape",
      "alternateName": "c6/c6a8fb0328f66a3590e92ab6b863ce807c41883d4fb4ca199b9a583f6626a42559f52fd46a47d6a275663b179f78f6c5874a37afdd848a2ef01beddffd2d37b2.ape",
      "contentSize": 21104,
      "sha256": "11f50d056dbe2a73d6a516009be410fe26ea05481c8ddaaa0732daad2ac2c614"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.xyz",
      "@type": "File",
      "name": "example.xyz",
      "alternateName": "54/543d30bf47330736d576a4047a36f5421556a3e83c9431fb021dffc16e627685b3204bb71b17b683342775ea6c816967ea22a2dd598e67db03a1237c45ab5e48.xyz",
      "contentSize": 1079,
      "sha256": "99f6c504dad42fe09f6d7c2422f720a671384a0de47c6bbb24f6b895baa87aec"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.sdf",
      "@type": "File",
      "name": "example.sdf",
      "alternateName": "44/443e1b2525d36a54d67f02fa3b95e9f76b3de8436b2d29c81f59a83ad35cd13b1a8b9d8bb94ff4ddf1cb2c8c05a357ddead2a19a7441cfa8e5b137544861dfb4.sdf",
      "contentSize": 3782,
      "sha256": "f44f2e734602a5ac09f4692e111f2c386af5c88691488d4bc2a5ecbd507e4ad4"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.hevc",
      "@type": "File",
      "name": "example.hevc",
      "alternateName": "a4/a472e7289f3411311475611529d1ce82061a28c0ce5eb1cd78ee12b63f3949d479e8eea4369b3c5b45a8ae29bef841b6486782d333fd1637878dbb5239a5818d.hevc",
      "contentSize": 61598,
      "sha256": "c6caff9401753fe0e3ac304a7497870e9c2a1a25953029c0d7edb0b67b818c5a"
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/elabftw-logo.png",
      "@type": "File",
      "name": "elabftw-logo.png",
      "alternateName": "12/12944550ed1eb684f3f8d2d063e5287f238b50159725f0d76547bef30e0ee328cd065fb347baefbd6944c0da1ec5b06465e3da2d222e22ee858d317c9b22b8df.png",
      "contentSize": 7409,
      "sha256": "31ce1a37e125cb6a581059a7bf9aeb35d656797f017deb011207e82a1c998faa"
    },
    {
      "@id": "comment://da67bf031aa9176e3382e0991140f998f9c622cccd348f673b3a36caa086344d?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-11-17T03:01:58+01:00",
      "text": "Oh, how fascinating. I'm sure the groundbreaking discovery that water is wet will change the course of human history forever.",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      }
    },
    {
      "@id": "comment://21df88ad372de913f72d5a6ae3add04fda3c672ad68d3ebe74c9ee3aefe07468?hash_algo=sha256",
      "@type": "Comment",
      "dateCreated": "2024-11-17T03:01:58+01:00",
      "text": "Well, it's a relief to see that the scientific community is hard at work discovering what we already suspected: that the sky is indeed blue. I can't wait for their next groundbreaking revelation that grass is green.",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      }
    },
    {
      "@id": "#category-Project CRYPTO-COOL",
      "@type": "Thing",
      "name": "Project CRYPTO-COOL",
      "color": "745cb8"
    },
    {
      "@id": "./Project-CRYPTO-COOL - An-example-experiment - 7c69b55a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:01:58+01:00",
      "dateModified": "2024-11-17T03:01:58+01:00",
      "temporal": "2025-01-01T00:00:00+01:00",
      "name": "An example experiment",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=256",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://da67bf031aa9176e3382e0991140f998f9c622cccd348f673b3a36caa086344d?hash_algo=sha256"
        },
        {
          "@id": "comment://21df88ad372de913f72d5a6ae3add04fda3c672ad68d3ebe74c9ee3aefe07468?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Success",
      "identifier": "20241117-7c69b55a8dcc83df0c6c83ee96e8e888bc189061",
      "keywords": "example,demo",
      "text": "This is the content of the experiment",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-Default",
      "@type": "Thing",
      "name": "Default",
      "color": "29AEB9"
    },
    {
      "@id": "./Default - Ducimus-dolores-deserunt-beatae-aut-odit-vel - 27800bd8/",
      "@type": "Dataset",
      "author": {
        "@id": "person://c8bc7d581ea61b54c0a608a683b080162a45e6391e157c71fd0c38fe9a57ff2f?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:00:06+01:00",
      "dateModified": "2024-11-17T03:00:07+01:00",
      "temporal": "2021-09-26T00:00:00+02:00",
      "name": "Ducimus dolores deserunt beatae aut odit vel.",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/database.php.php?mode=view&id=50",
      "genre": "resource",
      "creativeWorkStatus": "Maintenance mode",
      "identifier": "20241117-27800bd83ac183935a76ac21e6b6054b88e4a719",
      "keywords": "spectroscopy,biotechnology,gene expression,FRET,statistical analysis",
      "text": "King, 'and don't look at them--'I wish they'd get the trial done,' she thought, 'till its ears have come, or at least one of the house opened, and a crash of broken glass. 'What a number of changes she had a head unless there was Mystery,' the Mock Turtle, 'Drive on, old fellow! Don't be all day about it!' Last came a rumbling of little pebbles came rattling in at all?' said Alice, in a large piece out of the shelves as she could, and soon found herself falling down a very short time the Mouse to tell me your history, she do.' 'I'll tell it her,' said the March Hare went 'Sh! sh!' and the procession came opposite to Alice, very much what would happen next. The first question of course you don't!' the Hatter began, in a large ring, with the game,' the Queen never left off when they liked, so that altogether, for the hedgehogs; and in despair she put it. She felt that it would be four thousand miles down, I think--' (for, you see, as she could. 'The Dormouse is asleep again,' said the.",
      "about": {
        "@id": "#category-Default"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - c686e77b/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:01:59+01:00",
      "dateModified": "2024-11-17T03:01:59+01:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=258",
      "genre": "experiment",
      "creativeWorkStatus": "Fail",
      "identifier": "20241117-c686e77bb6839af2531d0193575e91825656c039",
      "keywords": "synthesis,antimicrobial,chemistry",
      "mentions": [
        {
          "@id": "./Default - Ducimus-dolores-deserunt-beatae-aut-odit-vel - 27800bd8/"
        }
      ],
      "text": "<h1>Synthesis and Characterization of a Novel Organic Compound with Antimicrobial Properties</h1>\n<p>\nThe emergence of drug-resistant bacterial strains has become a major public health concern, highlighting the need for the development of new antimicrobial agents. In this study, we aimed to synthesize a novel organic compound with potential antimicrobial activity.\n</p>\n<h2>Experimental Design</h2>\n<p>\nThe compound was synthesized via a multi-step reaction scheme. The starting material, benzaldehyde, was reacted with aniline in the presence of an acid catalyst to form the intermediate product, N-phenylbenzamide. The intermediate product was then reacted with thionyl chloride to form the corresponding acid chloride. The acid chloride was then reacted with aminoguanidine in the presence of a base catalyst to form the final product, which was purified by recrystallization.\n</p>\n<h2>Characterization</h2>\n<p>\nThe synthesized compound was characterized using various spectroscopic techniques. The melting point of the compound was determined using a melting point apparatus and compared to the literature value. The IR spectrum of the compound was obtained using a Fourier transform infrared spectrometer and compared to the expected spectrum. The NMR spectrum of the compound was obtained using a nuclear magnetic resonance spectrometer and analyzed to confirm the structure of the compound.\n</p>\n<h2>Antimicrobial Activity</h2>\n<p>\nThe antimicrobial activity of the synthesized compound was evaluated against several bacterial strains using the disk diffusion method. The results showed that the compound exhibited significant antimicrobial activity against both Gram-positive and Gram-negative bacteria, suggesting its potential as a new antimicrobial agent.\n</p>\n",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null,
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 1,
        "reviewCount": 1
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - fcab150c/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:01:58+01:00",
      "dateModified": "2024-11-17T03:01:59+01:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Transfection of p103\u039412-22 into RPE-1 Actin-RFP",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=257",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20241117-fcab150c3e9fe4766f2d2a2fee2291c4903c2bf9",
      "keywords": "transfection,biocell,RPE-1",
      "text": "<h1>Goal</h1><p>Transfecting the plasmid p103\u039412-22 into the RPE-1 Actin-RFP cells and look at the death rate.</p>",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "./Default - Distinctio-consectetur-vero-quisquam-impedit - 36d0f66b/",
      "@type": "Dataset",
      "author": {
        "@id": "person://c8bc7d581ea61b54c0a608a683b080162a45e6391e157c71fd0c38fe9a57ff2f?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:00:07+01:00",
      "dateModified": "2024-11-17T03:00:07+01:00",
      "temporal": "2023-05-23T00:00:00+02:00",
      "name": "Distinctio consectetur vero quisquam impedit.",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/database.php.php?mode=view&id=51",
      "genre": "resource",
      "creativeWorkStatus": "Operational",
      "identifier": "20241117-36d0f66b03b4cb38b9ac354713d1e2cd0113831f",
      "keywords": "spectroscopy,Project X,genetics,Secret",
      "text": "I must go back by railway,' she said this, she was to get her head on her toes when they arrived, with a little animal (she couldn't guess of what work it would all come wrong, and she tried to get her head impatiently; and, turning to Alice, she went on 'And how many hours a day or two: wouldn't it be of very little use, as it lasted.) 'Then the words did not like to show you! A little bright-eyed terrier, you know, with oh, such long curly brown hair! And it'll fetch things when you have of putting things!' 'It's a Cheshire cat,' said the Lory, as soon as she spoke--fancy CURTSEYING as you're falling through the door, she walked on in these words: 'Yes, we went to school in the sky. Twinkle, twinkle--\"' Here the Queen added to one of its little eyes, but it was the Cat again, sitting on the look-out for serpents night and day! Why, I haven't had a large plate came skimming out, straight at the Gryphon said to Alice; and Alice rather unwillingly took the hookah into its face to see.",
      "about": {
        "@id": "#category-Default"
      }
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:02:01+01:00",
      "dateModified": "2024-11-17T15:10:07+01:00",
      "temporal": "2025-03-03T00:00:00+01:00",
      "name": "Testing the eLabFTW lab notebook",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=263",
      "genre": "experiment",
      "comment": [
        {
          "@id": "comment://4fb80877aeb18492a13ff6ae43049f5730b7846e97a9b99d70397f5ddaf5945d?hash_algo=sha256"
        }
      ],
      "creativeWorkStatus": "Running",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/README.md"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.avi"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.bmp"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.epub"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.gif"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.mol"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.json"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.jpg"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.jdx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.jcamp"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.gbk"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.docx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.dna"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.cdx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pdf"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.odp"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pdb"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.png"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pps"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.ppsx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.tif"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.pptx"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.wav"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.mp4"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.webm"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.aac"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.mp3"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.ogg"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.flac"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.ape"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.xyz"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.sdf"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/example.hevc"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/elabftw-logo.png"
        }
      ],
      "identifier": "20241117-62e3c0a3fd90123288ba4647878e36718153ed64",
      "keywords": "demo,test",
      "mentions": [
        {
          "@id": "./Project-CRYPTO-COOL - An-example-experiment - 7c69b55a/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - c686e77b/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - fcab150c/"
        },
        {
          "@id": "./Default - Ducimus-dolores-deserunt-beatae-aut-odit-vel - 27800bd8/"
        },
        {
          "@id": "./Default - Distinctio-consectetur-vero-quisquam-impedit - 36d0f66b/"
        }
      ],
      "text": "<h1>Goal</h1><p>Test the software.</p><h1>Procedure</h1><p>Click everywhere and explore everything.</p><h1>Results</h1><p>It's really nice, I think I'll adopt it for our lab.</p>",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": [
        {
          "propertyID": "elabftw_metadata",
          "description": "eLabFTW metadata JSON as string",
          "value": "{\"extra_fields\": {\"Raw data URL\": {\"type\": \"url\", \"value\": \"https://datalake.example.com/experiments/3921\"}, \"Annie, are you okay\": {\"type\": \"checkbox\", \"value\": \"\", \"description\": \"This is a checkbox custom input\"}, \"This is a custom list input\": {\"type\": \"select\", \"value\": \"Some choice\", \"options\": [\"Some choice\", \"Another choice\", \"A third choice\"], \"description\": \"The value is selected from a pre-defined list\"}}}"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Raw data URL",
          "valueReference": "url",
          "value": "https://datalake.example.com/experiments/3921"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "Annie, are you okay",
          "valueReference": "checkbox",
          "value": "",
          "description": "This is a checkbox custom input"
        },
        {
          "@type": "PropertyValue",
          "propertyID": "This is a custom list input",
          "valueReference": "select",
          "value": "Some choice",
          "description": "The value is selected from a pre-defined list"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 5,
        "reviewCount": 1
      }
    },
    {
      "@id": "#category-Project CASIMIR",
      "@type": "Thing",
      "name": "Project CASIMIR",
      "color": "82e49d"
    },
    {
      "@id": "./Project-CASIMIR - Synthesis-of-Aspirin - 6179cb6a/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:02:01+01:00",
      "dateModified": "2024-11-17T15:10:35+01:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Synthesis of Aspirin",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=262",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20241117-6179cb6a0c1f49df77c0b1c3e3663ff082d24edb",
      "keywords": "chemistry,has-mathjax",
      "text": "<h1>Introduction</h1>\n<p>\nAspirin is a widely used pain-relieving and anti-inflammatory drug. In this experiment, we aimed to synthesize aspirin from salicylic acid and acetic anhydride.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe mixed salicylic acid and acetic anhydride in the presence of a catalyst, sulfuric acid. The reaction produced aspirin and acetic acid, as shown in the following chemical equation:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nAfter the reaction, we purified the aspirin by recrystallization from hot water. The purity of the aspirin was confirmed using thin-layer chromatography (TLC) and melting point analysis.\n</p>\n<h2>Results</h2>\n<p>\nThe yield of aspirin was 80% based on the amount of salicylic acid used. The purity of the aspirin was confirmed using TLC, which showed a single spot corresponding to aspirin. The melting point of the aspirin was 135-136\u00b0C, which is consistent with the literature value of 135-136.5\u00b0C.\n</p>\n<p>\nThe chemical reaction involved in the synthesis of aspirin can be written as:\n</p>\n<p>\n$$\\ce{C7H6O3 + (CH3CO)2O -&gt;[\\text{H2SO4}] C9H8O4 + CH3COOH}$$\n</p>\n<p>\nThe theoretical yield of aspirin can be calculated using the stoichiometry of the reaction. Assuming that all the salicylic acid reacts and no aspirin is lost during the purification process, the theoretical yield is calculated as follows:\n</p>\n<p>\n$$\\text{Theoretical yield} = \\frac{\\text{moles of salicylic acid used}}{\\text{molar ratio of salicylic acid to aspirin}} \\times \\text{molar mass of aspirin}$$\n</p>\n<p>\nThe actual yield of aspirin can be calculated by dividing the mass of the purified aspirin by the mass of salicylic acid used and multiplying by 100%. The percent yield can be calculated by dividing the actual yield by the theoretical yield and multiplying by 100%.\n</p>\n",
      "about": {
        "@id": "#category-Project CASIMIR"
      },
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - Testing-relationship-between-acceleration-and-gravity - 57999445/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:02:00+01:00",
      "dateModified": "2024-11-17T03:02:00+01:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Testing relationship between acceleration and gravity",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=261",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20241117-5799944529c420616b467bb89feeec6205efb827",
      "keywords": "has-mathjax,physics",
      "text": "<h1>Determination of Acceleration Due to Gravity</h1>\n<p>\nThe acceleration due to gravity is a fundamental constant that determines the gravitational force between two objects. In this experiment, we aimed to determine the value of acceleration due to gravity using a simple pendulum.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe suspended a metal ball from a string and measured the time taken for one complete oscillation of the pendulum. We repeated this measurement for different lengths of the pendulum and recorded the corresponding times. Using the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$, where $T$ is the period of the pendulum, $L$ is the length of the pendulum, and $g$ is the acceleration due to gravity, we calculated the value of $g$. The period $T$ can also be expressed in terms of the frequency $f$ using the equation $T=\\frac{1}{f}$.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the value of acceleration due to gravity was $9.81 \\text{ m/s}^2$, which is consistent with the accepted value. We also found that the period of the pendulum increased with increasing length, as predicted by the formula $T=2\\pi\\sqrt{\\frac{L}{g}}$. The relationship between the length and period of the pendulum can be expressed as $T^2=\\frac{4\\pi^2}{g}L$, which is a linear relationship with a slope of $\\frac{4\\pi^2}{g}$.\n</p>\n",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "#category-Tests",
      "@type": "Thing",
      "name": "Tests",
      "color": "2a8ab3"
    },
    {
      "@id": "./Tests - Effect-of-temperature-on-enzyme-activity - ef2b8e07/",
      "@type": "Dataset",
      "author": {
        "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:02:00+01:00",
      "dateModified": "2024-11-17T15:10:40+01:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "Effect of temperature on enzyme activity",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=260",
      "genre": "experiment",
      "creativeWorkStatus": "Need to be redone",
      "identifier": "20241117-ef2b8e072da876b38cf252fa619af0b29e818631",
      "keywords": "enzymology,test,Project ENZYTEMP",
      "text": "<h1>Effect of Temperature on Enzyme Activity</h1>\n<p>\nEnzymes are biological molecules that catalyze chemical reactions in living organisms. In this experiment, we investigated the effect of temperature on the activity of the enzyme amylase, which catalyzes the hydrolysis of starch into glucose.\n</p>\n<h2>Experimental Design</h2>\n<p>\nWe prepared a solution of starch and added a small amount of amylase to the solution. We then incubated the solution at different temperatures, ranging from 4\u00b0C to 70\u00b0C, for 5 minutes. After the incubation period, we added iodine to the solution to detect the presence of starch. The disappearance of the blue-black color of the iodine indicated the breakdown of starch into glucose.\n</p>\n<h2>Results</h2>\n<p>\nThe results showed that the activity of amylase increased with increasing temperature up to 37\u00b0C, which is the optimum temperature for amylase activity. At temperatures above 37\u00b0C, the activity of amylase decreased rapidly, and at 70\u00b0C, the enzyme was completely denatured and lost its catalytic activity.\n</p>\n<p>\nThe relationship between temperature and enzyme activity can be described by the Arrhenius equation, which relates the rate constant of a reaction to the activation energy and temperature. The equation can be written as:\n</p>\n<p>\n$$k = Ae^{-E_a/RT}$$\n</p>\n<p>\nwhere k is the rate constant, A is the pre-exponential factor, E_a is the activation energy, R is the gas constant, and T is the absolute temperature. The activation energy is the energy required to break the bonds in the reactants and form the products. The rate constant increases with increasing temperature due to the increase in the number of reactant molecules with sufficient kinetic energy to overcome the activation energy barrier.\n</p>\n<p>\nThe effect of temperature on enzyme activity can also be described by the Q10 value, which is the ratio of the reaction rate at a given temperature to the reaction rate at a temperature 10\u00b0C lower. The Q10 value for most enzyme-catalyzed reactions is around 2-3, indicating that the reaction rate doubles or triples with each 10\u00b0C increase in temperature.\n</p>\n",
      "about": {
        "@id": "#category-Tests"
      },
      "variableMeasured": null
    },
    {
      "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - aaae41a1/",
      "@type": "Dataset",
      "author": {
        "@id": "person://c8bc7d581ea61b54c0a608a683b080162a45e6391e157c71fd0c38fe9a57ff2f?hash_algo=sha256"
      },
      "dateCreated": "2024-11-17T03:01:59+01:00",
      "dateModified": "2024-11-17T03:02:00+01:00",
      "temporal": "2025-01-02T00:00:00+01:00",
      "name": "\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76",
      "encodingFormat": "text/html",
      "url": "https://demo.elabftw.net/experiments.php.php?mode=view&id=259",
      "genre": "experiment",
      "creativeWorkStatus": "Success",
      "identifier": "20241117-aaae41a1bc8fd66ca3a829dcd5b2429ca9fd62b4",
      "keywords": "CJK,\u30b7\u30e7\u30a6\u30b8\u30e7\u30a6\u30d0\u30a8",
      "text": "<p>\u80cc\u666f\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u679c\u7269\u306e\u6210\u719f\u904e\u7a0b\u306b\u5927\u304d\u306a\u5f71\u97ff\u3092\u4e0e\u3048\u307e\u3059\u3002\u305d\u306e\u305f\u3081\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u3064\u3044\u3066\u7814\u7a76\u3059\u308b\u3053\u3068\u306f\u3001\u679c\u7269\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u610f\u7fa9\u3092\u6301\u3061\u307e\u3059\u3002</p>\n\n<p>\u76ee\u7684\uff1a \u3053\u306e\u7814\u7a76\u306e\u76ee\u7684\u306f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306e\u7a2e\u985e\u3092\u8abf\u3079\u308b\u3053\u3068\u3067\u3059\u3002</p>\n\n<p>\u65b9\u6cd5\uff1a \u307e\u305a\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u3092\u6355\u7372\u3057\u3001\u5b9f\u9a13\u5ba4\u3067\u98fc\u80b2\u3057\u307e\u3059\u3002\u6b21\u306b\u3001\u679c\u7269\u3092\u8907\u6570\u7528\u610f\u3057\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u3092\u8abf\u3079\u307e\u3059\u3002\u679c\u7269\u306f\u3001\u30ea\u30f3\u30b4\u3001\u30d0\u30ca\u30ca\u3001\u30aa\u30ec\u30f3\u30b8\u3001\u30ad\u30a6\u30a4\u30d5\u30eb\u30fc\u30c4\u3001\u30b0\u30ec\u30fc\u30d7\u30d5\u30eb\u30fc\u30c4\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3001\u30de\u30f3\u30b4\u30fc\u306e7\u7a2e\u985e\u3092\u7528\u610f\u3057\u307e\u3059\u3002\u5404\u679c\u7269\u30921\u3064\u305a\u3064\u30b1\u30fc\u30b8\u306e\u4e2d\u306b\u5165\u308c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u305f\u304b\u3069\u3046\u304b\u3092\u78ba\u8a8d\u3057\u307e\u3059\u3002\u679c\u7269\u306f\u6bce\u65e5\u4ea4\u63db\u3057\u3001\u540c\u3058\u679c\u7269\u304c\u9023\u7d9a\u3057\u3066\u5165\u308c\u3089\u308c\u306a\u3044\u3088\u3046\u306b\u3057\u307e\u3059\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u3082\u8abf\u3079\u307e\u3059\u3002</p>\n\n<p>\u7d50\u679c\uff1a \u5b9f\u9a13\u306e\u7d50\u679c\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u597d\u3093\u3067\u98df\u3079\u308b\u679c\u7269\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3067\u3042\u308b\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002\u307e\u305f\u3001\u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u304c\u679c\u7269\u3092\u98df\u3079\u308b\u6642\u9593\u5e2f\u306f\u3001\u5348\u524d\u4e2d\u304c\u591a\u3044\u3053\u3068\u304c\u308f\u304b\u308a\u307e\u3057\u305f\u3002</p>\n\n<p>\u7d50\u8ad6\uff1a \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306f\u3001\u30d0\u30ca\u30ca\u3001\u30de\u30f3\u30b4\u30fc\u3001\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb\u3092\u597d\u3093\u3067\u98df\u3079\u308b\u3053\u3068\u304c\u660e\u3089\u304b\u306b\u306a\u308a\u307e\u3057\u305f\u3002\u3053\u306e\u7d50\u679c\u306f\u3001\u679c\u7269\u751f\u7523\u696d\u306b\u3068\u3063\u3066\u91cd\u8981\u306a\u60c5\u5831\u3068\u306a\u308a\u307e\u3059\u3002</p>\n",
      "about": {
        "@id": "#category-Project CRYPTO-COOL"
      },
      "variableMeasured": null
    },
    {
      "@id": "./",
      "identifier": "c27e24b3-ea46-4378-b40b-e9a1868b8c67",
      "@type": "Dataset",
      "datePublished": "2024-11-17T15:10:44+01:00",
      "hasPart": [
        {
          "@id": "./Project-CRYPTO-COOL - Testing-the-eLabFTW-lab-notebook - 62e3c0a3/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - An-example-experiment - 7c69b55a/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Synthesis-and-Characterization-of-a-Novel-Organic-Compound-with-Antimicrobial- - c686e77b/"
        },
        {
          "@id": "./Default - Ducimus-dolores-deserunt-beatae-aut-odit-vel - 27800bd8/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Transfection-of-p103\u039412-22-into-RPE-1-Actin-RFP - fcab150c/"
        },
        {
          "@id": "./Default - Distinctio-consectetur-vero-quisquam-impedit - 36d0f66b/"
        },
        {
          "@id": "./Project-CASIMIR - Synthesis-of-Aspirin - 6179cb6a/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - Testing-relationship-between-acceleration-and-gravity - 57999445/"
        },
        {
          "@id": "./Tests - Effect-of-temperature-on-enzyme-activity - ef2b8e07/"
        },
        {
          "@id": "./Project-CRYPTO-COOL - \u30d5\u30eb\u30fc\u30c4\u30d5\u30e9\u30a4\u306e\u98df\u6027\u306b\u95a2\u3059\u308b\u7814\u7a76 - aaae41a1/"
        }
      ],
      "name": "eLabFTW export",
      "description": "This is a .eln export from eLabFTW",
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
      }
    },
    {
      "@id": "person://ea073eacfa5790381567e321ab1b1b245c0661a38830c3327dedb1b61dec498e?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Alf",
      "familyName": "Stoltenberg",
      "email": "demo@deltablot.email"
    },
    {
      "@id": "person://c8bc7d581ea61b54c0a608a683b080162a45e6391e157c71fd0c38fe9a57ff2f?hash_algo=sha256",
      "@type": "Person",
      "givenName": "Nicolas",
      "familyName": "CARPi",
      "email": "nico@deltablot.email"
    }
  ]
}
```
