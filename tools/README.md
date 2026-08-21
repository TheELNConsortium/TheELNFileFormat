# Tools

Helper scripts for working with `.eln` files.

## `eln2md.py`

Generates the `README.md` of an example folder from its
`ro-crate-metadata.json`:

~~~bash
python tools/eln2md.py -d examples/<your folder>
~~~

## `eln2preview.py`

Generates and embeds a minimal static `ro-crate-preview.html` in one `.eln`
archive:

~~~bash
python tools/eln2preview.py examples/<your archive>.eln
~~~

If the archive already contains a preview, the command asks for explicit
confirmation before replacing it.

## `checkELN.py`

A [Streamlit](https://streamlit.io) page that verifies and previews an
uploaded `.eln` file.

~~~bash
uv run --group tools streamlit run tools/checkELN.py
~~~

The page then opens on <http://localhost:8501>.

### What it does

Upload a `.eln` file and the **Verify** tab runs the same five checks the test
suite runs, reporting each one separately:

| Check | Question it answers |
|---|---|
| Archive structure | Does the ZIP have a safe single-root layout and sensible resource limits? |
| Parameters metadata json | Are mandatory keys present and well formed? |
| Schema | Does the metadata match `tests/schema.json`? |
| Validator | Does `roc-validator` accept the crate? |
| Pypi RO-Crate | Can the `rocrate` package parse the crate? |

The **Preview** tab renders the `ro-crate-preview.html` that the producing
software embedded in the file.

It shares code with the tests deliberately, such that streamlit app and CI can never
drift into disagreeing.
