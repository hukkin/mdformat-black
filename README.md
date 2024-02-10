[![Build Status](https://github.com/hukkinj1/mdformat-ruff/workflows/Tests/badge.svg?branch=master)](<https://github.com/hukkinj1/mdformat-ruff/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![PyPI version](https://badge.fury.io/py/mdformat-ruff.svg)](<https://badge.fury.io/py/mdformat-ruff>)

# mdformat-ruff
> Mdformat plugin to ruffen Python code blocks

## Description
mdformat-ruff is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format Python code blocks with [ruff](https://github.com/psf/ruff).
## Usage
Install with:
```bash
pip install mdformat-ruff
```
You may pin ruff dependency for formatting stability:
```bash
pip install mdformat-ruff ruff==22.1.0
```

When using mdformat on the command line, ruff formatting will be automatically enabled after install.

When using mdformat Python API, code formatting for Python will have to be enabled explicitly:
````python
import mdformat

unformatted = "```python\n'''ruff converts quotes'''\n```\n"
formatted = mdformat.text(unformatted, codeformatters={"python"})
assert formatted == '```python\n"""ruff converts quotes"""\n```\n'
````

## Usage as a [pre-commit](https://pre-commit.com) hook

Add the following to your `.pre-commit-config.yaml`:
```yaml
- repo: https://github.com/executablebooks/mdformat
  rev: 0.7.13  # Use the ref you want to point at
  hooks:
    - id: mdformat
      additional_dependencies:
        - mdformat-ruff
        - ruff==22.1.0  # Pinning ruff here is optional
```
