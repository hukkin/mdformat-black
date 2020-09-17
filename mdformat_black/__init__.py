import black

__version__ = "0.0.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_python(unformatted: str) -> str:
    return black.format_str(unformatted, mode=black.Mode())
