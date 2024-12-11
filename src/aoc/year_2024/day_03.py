"""https://adventofcode.com/2024/day/3"""

import re
from doctest import debug
from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What do you get if you add up all of the results of the multiplications?",  # noqa: E501
    "What do you get if you add up all of the results of just the enabled multiplications?",  # noqa: E501
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    matches = re.findall(r"mul\((\d+),(\d+)\)", raw_data)
    answer = sum(int(i) * int(j) for i, j in matches)
    LOG.debug(f"{matches=}")

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    search_string = raw_data
    matches = re.findall(r"don't\(\).*do\(\)", search_string)
    search_string = search_string.replace(matches[-1], "---")

    matches = re.findall(r"mul\((\d+),(\d+)\)", search_string)
    answer = sum(int(i) * int(j) for i, j in matches)
    LOG.debug(f"{search_string=}\n{matches=}")

    return questions[1], answer
