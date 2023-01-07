import re
from typing import Any, Generator, Tuple

DISALLOWED_NOQA_REGEX = re.compile(r"# (noqa(?!(?:: (?:E501|F401|E402|W291)| isort:skip)\n).*)")


def _print(physical_line):
    match = DISALLOWED_NOQA_REGEX.search(physical_line)
    if match:
        yield match.start(), f"FOC100 {match.group(1)}"


def logical(physical_line: Any) -> Generator[Tuple[int, str], None, None]:
    yield from _print(physical_line)
