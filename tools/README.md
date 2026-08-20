# Tools

Helper scripts for working with `.eln` files.

## `eln2md.py`

Generates the `README.md` of an example folder from its
`ro-crate-metadata.json`:

~~~bash
python tools/eln2md.py -d examples/<your folder>
~~~

## `checkELN.py`

A [Streamlit](https://streamlit.io) page that verifies and previews an
uploaded `.eln` file.

~~~bash
python -m venv venv
source venv/bin/activate
pip install -r tools/requirements.txt
streamlit run tools/checkELN.py
~~~

The page then opens on <http://localhost:8501>.

### What it does

Upload a `.eln` file and the **Verify** tab runs the same five checks the test
suite runs, reporting each one separately:

| Check | Question it answers |
|---|---|
| Archive structure | Does the ZIP contain exactly one root folder? |
| Pypi RO-Crate | Can the `rocrate` package parse the crate? |
| Parameters metadata json | Are mandatory keys present and well formed? |
| Schema | Does the metadata match `tests/schema.json`? |
| Validator | Does `roc-validator` accept the crate? |

The **Preview** tab renders the `ro-crate-preview.html` that the producing
software embedded in the file. That preview is supplied by the file, not
generated here, and a file without one is still valid.

### Why it shares code with the tests

`checkELN.py` deliberately contains no validation logic. It imports
`checkUploadedFile` from `tests/checks.py`, so the web page and CI can never
drift into disagreeing about what a valid `.eln` file is. Adding a check to
`tests/checks.py` and listing it in `ALL_CHECKS` makes it appear on the page
automatically.

A web upload arrives as an in-memory object rather than a file on disk, and
`checkValidator` needs a real path. `checkUploadedFile` therefore writes the
upload to one temporary file, runs every check against that same path, and
deletes it afterwards. A check that raises on a damaged file is reported as a
failure instead of breaking the page, because reporting on damaged files is
the point of the tool.

### Deploying

The page is a single stateless script with no server-side storage: uploads
live only in the temporary file created for the duration of one request. It
can be deployed on any host that can run `streamlit run tools/checkELN.py`
with `tools/requirements.txt` installed, including Streamlit Community Cloud
with `tools/checkELN.py` as the entry point.
