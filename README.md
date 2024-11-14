[![Build Status](https://github.com/hukkin/mdformat-black/actions/workflows/tests.yaml/badge.svg?branch=master)](<https://github.com/hukkin/mdformat-black/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![PyPI version](https://badge.fury.io/py/mdformat-black.svg)](<https://badge.fury.io/py/mdformat-black>)

# mdformat-black
> Mdformat plugin to Blacken Python code blocks

## Description
mdformat-black is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format Python code blocks with [Black](https://github.com/psf/black).
## Usage
Install with:
```bash
pip install mdformat-black
```
You may pin Black dependency for formatting stability:
```bash
pip install mdformat-black black==22.1.0
```

When using mdformat on the command line, Black formatting will be automatically enabled after install.

When using mdformat Python API, code formatting for Python will have to be enabled explicitly:
````python
import mdformat

unformatted = "```python\n'''black converts quotes'''\n```\n"
formatted = mdformat.text(unformatted, codeformatters={"python"})
assert formatted == '```python\n"""black converts quotes"""\n```\n'
````

## Usage as a [pre-commit](https://pre-commit.com) hook

Add the following to your `.pre-commit-config.yaml`:
```yaml
- repo: https://github.com/executablebooks/mdformat
  rev: 0.7.13  # Use the ref you want to point at
  hooks:
    - id: mdformat
      additional_dependencies:
        - mdformat-black
        - black==22.1.0  # Pinning black here is optional
```
