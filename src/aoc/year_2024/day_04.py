"""https://adventofcode.com/2024/day/4"""

from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "How many times does XMAS appear?",
    "How many times does an X-MAS appear?",
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    array, length, width = _parse_raw_data(raw_data)

    answer = sum(
        int(_check(x, y, *direction, "XMAS", array))
        for y in range(length)
        for x in range(width)
        for direction in [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
    )

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    array, length, width = _parse_raw_data(raw_data)

    answer = sum(
        int(
            (_check(x, y, 1, 1, "SAM", array) or _check(x, y, 1, 1, "MAS", array))
            and (_check(x + 2, y, -1, 1, "SAM", array) or _check(x + 2, y, -1, 1, "MAS", array))
        )
        for y in range(length)
        for x in range(width)
    )

    return questions[1], answer


def _parse_raw_data(raw_data: str):
    return (
        {(x, y): char for y, row in enumerate(raw_data.split("\n")) for x, char in enumerate(list(row))},  # array
        len(raw_data.split("\n")),  # length
        max([len(row) for row in raw_data.split("\n")]),  # width
    )


def _check(x, y, dx, dy, word, array) -> bool:
    for i, char in enumerate(word):
        if char != array.get((x + i * dx, y + i * dy), "."):
            return False
    LOG.debug(f"{word} found @({x:3d},{y:3d}) in direction ({dx:2d},{dy:2d})")
    return True
