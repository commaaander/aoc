"""https://adventofcode.com/2025/day/6"""

import re
from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What is the grand total found by adding together all of the answers to the individual problems?",  # noqa: E501
    "What is the grand total found by adding together all of the answers to the individual problems?",  # noqa: E501
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")

    answer: int = 0
    individual_problems = list(
        map(
            list,
            zip(*[re.split(r"\s+", value.strip()) for value in [line for line in raw_data.splitlines()]]),
        )
    )
    answer = sum(
        eval(individual_problem[-1].join(individual_problem[0:-1])) for individual_problem in individual_problems
    )
    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0
    transposed_data = list(map(list, zip(*[value[::1] for value in [line for line in raw_data.splitlines()]])))
    individual_problems = []
    numbers = []
    operator = ""
    for line in transposed_data:
        if not all(" " == i for i in line[:-1]):
            numbers.append("".join(line[:-1]))
            operator += line[-1]
        else:
            individual_problems.append((numbers, operator))
            numbers = []
            operator = ""
    individual_problems.append((numbers, operator))

    for numbers, operator in individual_problems:
        individual_problem = operator.join(numbers)
        answer += eval(individual_problem)

    return questions[1], answer
