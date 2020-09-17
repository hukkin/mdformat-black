import mdformat_black


def test_format_python():
    assert mdformat_black.format_python("print(\n''\n)") == 'print("")\n'
