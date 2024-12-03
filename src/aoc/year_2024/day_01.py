"""https://adventofcode.com/2024/day/1"""

from collections import Counter
from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What is the total distance between your lists?",  # noqa: E501
    "What is their similarity score?",  # noqa: E501
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0
    a1, a2 = _parse_raw_data(raw_data)
    for idx in range(len(a1)):
        answer += abs(a1[idx] - a2[idx])

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0
    a1, a2 = _parse_raw_data(raw_data)
    a2_counts = Counter(a2)
    for i in a1:
        answer += i * a2_counts.get(i, 0)
    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Tuple[List[int], List[int]]:
    a1: List[int] = []
    a2: List[int] = []
    for line in raw_data.split("\n"):
        l1, l2 = line.split()
        a1.append(int(l1))
        a2.append(int(l2))
    return sorted(a1), sorted(a2)
