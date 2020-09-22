import mdformat

import mdformat_black


def test_format_python():
    assert mdformat_black.format_python("print(\n''\n)") == 'print("")\n'


def test_mdformat_integration():
    unformatted_md = """```python
def hello():
    print(
        'Hello world!'
    )
```
"""
    formatted_md = """~~~python
def hello():
    print("Hello world!")
~~~
"""
    assert mdformat.text(unformatted_md, codeformatters={"python"}) == formatted_md
