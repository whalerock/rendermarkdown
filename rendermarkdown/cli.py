"""CLI for rendering markdown."""
import os
import tempfile
import webbrowser

import click
import requests


@click.command()
@click.argument(
    'filename'
)
@click.option(
    '--browser/--no-browser',
    default=True
)
def cli(filename, browser):
    """
    Render a markdown file as html.

    Examples:

    rendermarkdown README.md
    """
    file_contents = readfile(filename)
    html = html_from_markdown(file_contents)
    click.echo(html)
    if browser:
        render_html(html)
    return


def readfile(filename):
    """Read the contents of a file."""
    with open(filename) as fh:
        contents = fh.read()
    return contents


def render_html(html):
    """Render HTML in browser."""
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp_file:
        tmp_file.write(html)
        path = os.path.realpath(tmp_file.name)
        abs_path_to_file = 'file://{}'.format(path)
        webbrowser.open(abs_path_to_file, 2)

    return True


def html_from_markdown(text):
    """Return markdown in html format."""
    url = 'https://api.github.com/markdown/raw'
    headers = {
        'Content-Type': 'text/plain'
    }
    response = requests.post(url, data=text, headers=headers)
    response.raise_for_status()
    return response.content
