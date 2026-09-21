## Editing, building, and publishing extension documentation


[Sphinx](https://www.sphinx-doc.org/en/master/index.html#) is used for document generation.

### Local testing
To build the documentation locally:

```
uv run --group docs make -C docs html
```

Navigate to `docs/build/html/` and open `index.html`.
