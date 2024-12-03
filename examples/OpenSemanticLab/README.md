[OpenSemanticLab](https://github.com/OpenSemanticLab) implementation is part of the [osw-python](https://github.com/OpenSemanticLab/osw-python) package.

It utilises the following schemas to populate the RO-Crate JSON-LD Graph:
- [osw:ElnEntry](https://opensemantic.world/id/Category-3AOSW0e7fab2262fb4427ad0fa454bc868a0d) -> [schema:Dataset](https://schema.org/Dataset)
- [osw:Organization](https://opensemantic.world/id/Category-3AOSW1969007d5acf40539642877659a02c23) -> [schema:Organization](https://schema.org/Organization)
- [osw:Person](https://opensemantic.world/id/Category-3AOSW44deaa5b806d41a2a88594f562b110e9) -> [schema:Person](https://schema.org/Person)
- [osw:Project](https://opensemantic.world/id/Category-3AOSWb2d7e6a2eff94c82b7f1f2699d5b0ee3) -> [schema:Project](https://schema.org/Project)
- [osw:Keyword](https://opensemantic.world/id/Category-3AOSW09f6cdd54bc54de786eafced5f675cbe) -> [schema:DefinedTerm](https://schema.org/DefinedTerm)
- [osw:Tool](https://opensemantic.world/id/Category-3AOSWe427aafafbac4262955b9f690a83405d) -> [schema:HowToTool](https://schema.org/HowToTool)
- [osw:File](https://opensemantic.world/id/Category-3AOSW11a53cdfbdc24524bf8ac435cbf65d9d) -> [schema:CreativeWork](https://schema.org/CreativeWork)

Currently the following additional mapping context is applied:

```json
"@context": [
    "https://w3id.org/ro/crate/1.1/context",
    {
        "type": {"@id": "schema:additionalType", "@type": "@id"},
        "rdf_type": "@type",
        "description": {"@id": "schema:description", "@context": {
            "text": "@value",
            "lang": "@lang",
        }},
        "about": {"@id": "schema:about", "@type": "@id"},
        "conforms_to": {"@id": "conformsTo", "@type": "@id"},
        "date_created": "dateCreated",
        "publisher": {"@id": "schema:sdPublisher", "@type": "@id"},
        "date_published": "schema:datePublished",
        "has_part": {"@id": "schema:hasPart", "@type": "@id", "@container": "@set"},
        "start_date_time": "schema:dateCreated",
        "creator": {"@id": "schema:author", "@type": "@id"},
        "website": "url",
    }
]
```