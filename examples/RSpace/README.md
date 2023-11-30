# RSpace

- Home page: https://www.researchspace.com/

- Documentation: https://researchspace.helpdocs.io/article/s3j29if453-export-formats
 
### Example export
```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "name": "user user_2023-11-29_15:55:04",
      "description": "testrocrate",
      "@id": "./",
      "@type": "Dataset",
      "identifier": "http://localhost:8080",
      "datePublished": "2023-11-29",
      "hasPart": [
        {
          "@id": "./documentSchema.xsd"
        },
        {
          "@id": "./resources"
        },
        {
          "@id": "./formSchema.xsd"
        },
        {
          "@id": "./doc_Editable2-32"
        }
      ]
    },
    {
      "about": {
        "@id": "./"
      },
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "sdPublisher": {
        "@id": "#RSpace"
      },
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork"
    },
    {
      "encodingFormat": "application/xml",
      "description": "schema for RSpace documents",
      "@id": "./documentSchema.xsd",
      "@type": "File"
    },
    {
      "encodingFormat": "application/xml",
      "additionalType": "Selenium",
      "description": "A Form used to create an RSpace Structured Document",
      "dateCreated": "29:11:23:14:34:25",
      "dateModified": "29:11:23:14:34:24",
      "@id": "./doc_Editable2-32/doc_Editable2-32_form.xml",
      "@type": "File"
    },
    {
      "description": "Common resources shared among exported data",
      "@id": "./resources",
      "@type": "Dataset"
    },
    {
      "description": "schema for RSpace forms",
      "encodingFormat": "application/xml",
      "@id": "./formSchema.xsd",
      "@type": "File"
    },
    {
      "@id": "./doc_Editable2-32",
      "@type": "Dataset",
      "keywords": "'help'",
      "hasPart": [
        {
          "@id": "./doc_Editable2-32/doc_Editable2-32_form.xml"
        },
        {
          "@id": "./doc_Editable2-32/doc_Editable2-32.xml"
        }
      ]
    },
    {
      "encodingFormat": "application/xml",
      "description": "An RSpace Structured Document",
      "dateCreated": "29:11:23:14:34:26",
      "dateModified": "29:11:23:15:54:45",
      "@id": "./doc_Editable2-32/doc_Editable2-32.xml",
      "@type": "File"
    },
    {
      "description": "The RSpace user who exported this data",
      "@id": "user user",
      "email": "user@user.com",
      "givenName": "user",
      "familyName": "user",
      "@type": "Person"
    },
    {
      "name": "RSpace",
      "url": "https://www.researchspace.com/",
      "@id": "#RSpace",
      "email": "info@researchspace.com",
      "@type": "Organization"
    }
  ]
}
```
