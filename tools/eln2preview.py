#!/usr/bin/env python3
"""Create and embed a minimal RO-Crate HTML preview in an .eln archive."""
import argparse
import html
import json
import os
import sys
import tempfile
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile

METADATA_FILE = 'ro-crate-metadata.json'
PREVIEW_FILE = 'ro-crate-preview.html'
SHOW_FIELDS = (('Name', 'name'), ('ID', '@id'), ('Type', '@type'), ('Description', 'description'))

def _text(value):
    """Helper: return a readable plain-text representation of a metadata value."""
    if isinstance(value, list):
        return ', '.join(_text(item) for item in value)
    if isinstance(value, dict):
        if '@id' in value:
            return str(value['@id'])
        return ', '.join(f'{key}: {_text(item)}' for key, item in value.items())
    return str(value)


def create_preview(metadata):
    """Create static HTML for an RO-Crate metadata document."""
    graph = metadata.get('@graph')
    nodes_by_id = {node.get('@id'): node for node in graph if isinstance(node, dict) and isinstance(node.get('@id'), str)}
    nodes = []
    visited = set()

    def visit(node_id):
        """Visit each node"""
        if node_id in visited or node_id not in nodes_by_id:
            return
        visited.add(node_id)
        node = nodes_by_id[node_id]
        nodes.append(node)
        for part in node.get('hasPart', []):
            visit(part['@id'])

    visit('./')
    for node in graph:
        if isinstance(node, dict):
            visit(node.get('@id'))
    anchors = {node['@id']: f'node-{index}' for index, node in enumerate(nodes)}
    root = nodes[0]
    title = _text(root.get('name', 'RO-Crate preview'))
    root_fields = ''.join(
        f'<dt>{html.escape(label)}</dt><dd>{html.escape(_text(root[key]))}</dd>'
        for label, key in SHOW_FIELDS if key in root
    )

    items = []
    for node in nodes:
        node_id = node['@id']
        fields = ''.join(
            f'<dt>{html.escape(label)}</dt><dd>{html.escape(_text(node[key]))}</dd>'
            for label, key in SHOW_FIELDS if key in node
        )
        part_items = [
            f'<li><a href="#{anchors[part["@id"]]}">{html.escape(part["@id"])}</a></li>'
            for part in node.get('hasPart', [])
        ]
        if part_items:
            fields += '<dt>Has part</dt><dd><ul>' + ''.join(part_items) + '</ul></dd>'
        items.append(
            f'<article id="{anchors[node_id]}">'
            f'<h2>{html.escape(_text(node.get("name", node_id)))}</h2>'
            f'<dl>{fields}</dl></article>'
        )

    return (
        '<!doctype html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '  <meta charset="utf-8">\n'
        f'  <title>{html.escape(title)}</title>\n'
        '</head>\n'
        '<body>\n'
        '  <header>\n'
        f'    <h1>{html.escape(title)}</h1>\n'
        f'    <dl>{root_fields}</dl>\n'
        '  </header>\n'
        '  <main>\n'
        '    <h2>RO-Crate nodes</h2>\n'
        f'    {"".join(items)}\n'
        '  </main>\n'
        '</body>\n'
        '</html>\n'
    )


def update_archive(archive_path):
    """Generate a preview and add it to an .eln archive."""
    archive_path = Path(archive_path)
    temporary_path = None
    try:
        with ZipFile(archive_path, 'r') as source:
            names = source.namelist()
            roots = {PurePosixPath(name).parts[0] for name in names if PurePosixPath(name).parts}
            root = next(iter(roots))
            metadata_path = f'{root}/{METADATA_FILE}'
            preview_path = f'{root}/{PREVIEW_FILE}'
            if preview_path in names:
                if not sys.stdin.isatty():
                    print(
                        'Existing preview found; refusing to replace it '
                        'without interactive confirmation.'
                    )
                    print('Archive was not changed.')
                    return False
                try:
                    answer = input(f'Existing {PREVIEW_FILE} found. Replace it? [y/N]: ')
                except EOFError:
                    answer = ''
                if answer.strip().lower() not in {'y', 'yes'}:
                    print('Archive was not changed.')
                    return False
            metadata = json.loads(source.read(metadata_path))
            preview = create_preview(metadata).encode('utf-8')
            with tempfile.NamedTemporaryFile(dir=archive_path.parent, prefix=f'.{archive_path.name}.',
                                             suffix='.tmp', delete=False) as temporary:
                temporary_path = Path(temporary.name)
            with ZipFile(temporary_path, 'w', compression=ZIP_DEFLATED) as target:
                for info in source.infolist():
                    if info.filename != preview_path:
                        target.writestr(info, source.read(info.filename))
                target.writestr(preview_path, preview)
        os.replace(temporary_path, archive_path)
        print(f'Embedded {PREVIEW_FILE} in {archive_path}')
        return True
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate and embed a minimal RO-Crate HTML preview.')
    parser.add_argument('archive', type=Path, help='path to the .eln archive')
    arguments = parser.parse_args()
    try:
        update_archive(arguments.archive)
    except (OSError, ValueError, KeyError, TypeError, UnicodeDecodeError) as error:
        parser.error(f'could not create preview: {error}')
