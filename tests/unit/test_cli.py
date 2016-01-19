"""Tests for CLI."""
import unittest
import mock
import rendermarkdown
from click.testing import CliRunner
from rendermarkdown import cli


class TestCli(unittest.TestCase):

    """Test methods on cli."""

    @mock.patch.object(cli, 'render_html')
    @mock.patch.object(cli, 'readfile', return_value='hello')
    @mock.patch.object(cli, 'html_from_markdown', return_value='<p>hello</p>')
    def test_cli(self, markdown, readfile, render_html):
        """Test the ability to render a .MD from the CLI."""
        runner = CliRunner()
        results = runner.invoke(rendermarkdown.cli.cli, ['README.md'])
        assert results.exit_code == 0
        assert results.output == '<p>hello</p>\n'
        readfile.assert_called_once_with('README.md')
        markdown.assert_called_once_with('hello')
        render_html.assert_called_once_with('<p>hello</p>')
