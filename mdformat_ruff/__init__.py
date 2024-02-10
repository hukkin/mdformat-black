import subprocess

from ruff.__main__ import find_ruff_bin

__version__ = (
    "0.1.1"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT
)


def format_python(unformatted: str, _info_str: str) -> str:
    r"""Format python.

    :param unformatted:
    :type unformatted: str
    :param _info_str:
    :type _info_str: str
    :rtype: str
    """
    ps = subprocess.run(
        [find_ruff_bin(), "format", "-"],
        input=unformatted.encode(),
        capture_output=True,
    )
    if ps.returncode == 0:
        return ps.stdout.decode()
    return unformatted
