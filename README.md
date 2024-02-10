# mdformat-ruff

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/mdformat-ruff/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/mdformat-ruff/main)
[![github/workflow](https://github.com/Freed-Wu/mdformat-ruff/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/mdformat-ruff/actions)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/mdformat-ruff/total)](https://github.com/Freed-Wu/mdformat-ruff/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/mdformat-ruff/latest/total)](https://github.com/Freed-Wu/mdformat-ruff/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff)
[![github/v](https://shields.io/github/v/release/Freed-Wu/mdformat-ruff)](https://github.com/Freed-Wu/mdformat-ruff)

[![pypi/status](https://shields.io/pypi/status/mdformat-ruff)](https://pypi.org/project/mdformat-ruff/#description)
[![pypi/v](https://shields.io/pypi/v/mdformat-ruff)](https://pypi.org/project/mdformat-ruff/#history)
[![pypi/downloads](https://shields.io/pypi/dd/mdformat-ruff)](https://pypi.org/project/mdformat-ruff/#files)
[![pypi/format](https://shields.io/pypi/format/mdformat-ruff)](https://pypi.org/project/mdformat-ruff/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/mdformat-ruff)](https://pypi.org/project/mdformat-ruff/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/mdformat-ruff)](https://pypi.org/project/mdformat-ruff/#files)

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

When using mdformat on the command line, ruff formatting will be automatically
enabled after install.

When using mdformat Python API, code formatting for Python will have to be
enabled explicitly:

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
    rev: 0.7.13 # Use the ref you want to point at
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-ruff
          - ruff==22.1.0 # Pinning ruff here is optional
```
