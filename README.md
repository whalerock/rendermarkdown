A simple CLI to preview markdown using GitHub's markdown API. By default, the document will render in your browser. Use `--no-browser` to only output HTML.

# Installing rendermarkdown

`pip install rendermarkdown`

## Examples

```
rendermarkdown README.md
rendermarkdown README.md --no-browser
```


## Testing

```
$ pip install -r dev-requirements.txt
$ tox
```
