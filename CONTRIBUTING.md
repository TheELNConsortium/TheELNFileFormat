# Contributing to the eln file format

Contributions to this repository are welcome. Use GitHub issues or Discussions to report issues or suggest improvements.

## Testing locally

~~~bash
uv sync --group test
uv run --group test pytest
~~~

## Adding an example file

Once you have your .eln, create a folder in `examples/` with your application name, and add the .eln in there.

Add a file `README_TEMPLATE.md` which will be the header of the final `README.md` file.

Then run:

~~~bash
python tools/eln2md.py -d examples/<your folder>
~~~

This will generate a `README.md` file with the `ro-crate-metadata.json`.
