# RSpace

- Home page: https://www.researchspace.com/

- Documentation: https://researchspace.helpdocs.io/article/s3j29if453-export-formats

### Structure of the RSpace example
This exported archive includes an RSpace document which has:
 - An embedded image from the RSpace 'Gallery'
 - A link to another RSpace document.
 - Links are generated as DataSets that have a composite id of 'linking doc/linked doc'. Links also contain an identifier attribute which gives the real ID of the linked document.



### Example export
```json
{
  "@context" : "https://w3id.org/ro/crate/1.1/context",
  "@graph" : [ {
    "name" : "user user_2023-12-07_16:20:48",
    "description" : "",
    "@id" : "./",
    "@type" : "Dataset",
    "identifier" : "http://localhost:8080",
    "datePublished" : "2023-12-07",
    "hasPart" : [ {
      "@id" : "./resources"
    }, {
      "@id" : "./schemas/formSchema.xsd"
    }, {
      "@id" : "./schemas/documentSchema.xsd"
    }, {
      "@id" : "./doc_Editable2-32"
    }, {
      "@id" : "./doc_Experiment-1-25"
    } ]
  }, {
    "about" : {
      "@id" : "./"
    },
    "conformsTo" : {
      "@id" : "https://w3id.org/ro/crate/1.1"
    },
    "sdPublisher" : {
      "@id" : "#RSpace"
    },
    "@id" : "ro-crate-metadata.json",
    "@type" : "CreativeWork"
  }, {
    "encodingFormat" : "application/xml",
    "sha256" : "8171e143737567e3fe352fedf774a348af0b5335e7b96bc92531441048270b9e",
    "additionalType" : "Experiment",
    "description" : "A Form used to create an RSpace Structured Document",
    "dateCreated" : "07:12:23:16:11:11",
    "dateModified" : "07:12:23:16:11:11",
    "@id" : "./doc_Experiment-1-25/doc_Experiment-1-25_form.xml",
    "@type" : "File"
  }, {
    "encodingFormat" : "application/xml",
    "sha256" : "99405c27462b93d17b77d7bae5be5065317df0fc0bad293072db5ab2288c378c",
    "additionalType" : "Selenium",
    "description" : "A Form used to create an RSpace Structured Document",
    "dateCreated" : "07:12:23:16:11:11",
    "dateModified" : "07:12:23:16:11:11",
    "@id" : "./doc_Editable2-32/doc_Editable2-32_form.xml",
    "@type" : "File"
  }, {
    "description" : "Common resources shared among exported data",
    "@id" : "./resources",
    "@type" : "Dataset"
  }, {
    "description" : "schema for RSpace forms",
    "encodingFormat" : "application/xml",
    "sha256" : "3381f83d983a75f49673659805599476f5cf507b36e402528fcf972848295a6c",
    "@id" : "./schemas/formSchema.xsd",
    "@type" : "File"
  }, {
    "sha256" : "cb51c02b436a3db4207193ca4d58dbb14143a376a16c61c44fcbd7c38ed196ee",
    "encodingFormat" : "image/x-png",
    "description" : "A file linked by an exported document or in a user Gallery",
    "dateCreated" : "07:12:23:16:11:12",
    "dateModified" : "07:12:23:16:11:12",
    "@id" : "./doc_Experiment-1-25/Picture1_1701965472094.png",
    "@type" : "File"
  }, {
    "encodingFormat" : "application/xml",
    "description" : "schema for RSpace documents",
    "sha256" : "429f05d9daf5d77ac8edac1aa0dd7b98e05e3103651463168ddc1ecd42a795f0",
    "@id" : "./schemas/documentSchema.xsd",
    "@type" : "File"
  }, {
    "sha256" : "200d2196966f89fc7f93a4a6aa1785c20c982b08fbdf828919881043504cfe7c",
    "encodingFormat" : "image/gif",
    "description" : "A file linked by an exported document or in a user Gallery",
    "dateCreated" : "07:12:23:16:11:13",
    "dateModified" : "07:12:23:16:11:13",
    "@id" : "./doc_Editable2-32/lemmings_1701965473304.gif",
    "@type" : "File"
  }, {
    "identifier" : "./doc_Experiment-1-25",
    "description" : "A file linked by an exported document or in a user Gallery",
    "@id" : "./doc_Editable2-32/doc_Experiment-1-25",
    "@type" : "Dataset"
  }, {
    "encodingFormat" : "application/xml",
    "sha256" : "0d81bf271c83852eaac7ab4462d8b00ccafed292b2862c00a453ccebffaf74ff",
    "description" : "An RSpace Structured Document",
    "dateCreated" : "07:12:23:16:11:12",
    "dateModified" : "07:12:23:16:11:12",
    "@id" : "./doc_Experiment-1-25/doc_Experiment-1-25.xml",
    "@type" : "File"
  }, {
    "@id" : "./doc_Editable2-32",
    "@type" : "Dataset",
    "keywords" : [ "red", "green", "todolist" ],
    "hasPart" : [ {
      "@id" : "./doc_Editable2-32/doc_Editable2-32_form.xml"
    }, {
      "@id" : "./doc_Editable2-32/lemmings_1701965473304.gif"
    }, {
      "@id" : "./doc_Editable2-32/doc_Experiment-1-25"
    }, {
      "@id" : "./doc_Editable2-32/doc_Editable2-32.xml"
    } ]
  }, {
    "encodingFormat" : "application/xml",
    "sha256" : "040155faf2f02cba3a75f30e8f37740f6af0e64b2a45c5f48169d519b0e24997",
    "description" : "An RSpace Structured Document",
    "dateCreated" : "07:12:23:16:11:13",
    "dateModified" : "07:12:23:16:19:53",
    "@id" : "./doc_Editable2-32/doc_Editable2-32.xml",
    "@type" : "File"
  }, {
    "@id" : "./doc_Experiment-1-25",
    "@type" : "Dataset",
    "keywords" : "exampleExperimentTag",
    "hasPart" : [ {
      "@id" : "./doc_Experiment-1-25/doc_Experiment-1-25_form.xml"
    }, {
      "@id" : "./doc_Experiment-1-25/Picture1_1701965472094.png"
    }, {
      "@id" : "./doc_Experiment-1-25/doc_Experiment-1-25.xml"
    } ]
  }, {
    "description" : "The RSpace user who exported this data",
    "@id" : "user user",
    "email" : "user@user.com",
    "givenName" : "user",
    "familyName" : "user",
    "@type" : "Person"
  }, {
    "name" : "RSpace",
    "url" : "https://www.researchspace.com/",
    "@id" : "#RSpace",
    "email" : "info@researchspace.com",
    "@type" : "Organization"
  } ]
}
```
