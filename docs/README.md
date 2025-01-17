## Editing, building, and publishing extension documentation


[Sphinx](https://www.sphinx-doc.org/en/master/index.html#) is used for document generation.

### Local testing

```
pip install sphinx sphinx_rtd_theme
```

Then build the documentation locally:

```
make -C docs html
```

Navigate to `docs/build/` and open `index.html`.
