import os

from flake8.main.cli import main


def test_module(capsys):
    assert main((os.path.join("tests", "fixtures", "noqa.py"),)) == 1

    assert capsys.readouterr().out == """\
tests/fixtures/noqa.py:11:27: FOC100 noqa: F401,E402 isort:skip
tests/fixtures/noqa.py:19:6: FOC100 noqa: E201
"""

    # Note: flake8 skips the bare "noqa".
