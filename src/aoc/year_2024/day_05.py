"""https://adventofcode.com/2024/day/5"""

from functools import cmp_to_key
from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What do you get if you add up the middle page number from those correctly-ordered updates?",  # noqa: E501
    "What do you get if you add up the middle page numbers after correctly ordering just those updates?",  # noqa: E501
]


rules = {}


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    global rules

    rules, updates = _parse_raw_data(raw_data)
    answer = sum(update[len(update) // 2] for update in updates if _update_is_correct(update, rules))

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    global rules

    rules, updates = _parse_raw_data(raw_data)

    fixed_updates = []
    for update in updates:
        if not _update_is_correct(update, rules):
            update.sort(key=cmp_to_key(_sort))
            fixed_updates.append(update)

    answer = sum(update[len(update) // 2] for update in fixed_updates)
    return questions[1], answer


def _parse_raw_data(raw_data: str):
    raw_rules, raw_updates = raw_data.split("\n\n")

    return (
        [(int(i), int(j)) for rule in raw_rules.split("\n") for i, j in [rule.split("|")]],  # rules
        [[int(page) for page in pages.split(",")] for pages in raw_updates.split("\n")],  # updates
    )


def _update_is_correct(update, rules) -> bool:
    for idx, page in enumerate(update[:-1]):
        for other_page in update[idx + 1 :]:
            if (other_page, page) in rules:
                LOG.warning(f"Inorrect {update=} @ {idx=}, {page=} with {other_page=}")
                return False
    for idx, page in enumerate(update[1:]):
        for other_page in update[: idx + 1]:
            if (page, other_page) in rules:
                LOG.warning(f"Inorrect {update=} @ {idx=}, {page=} with {other_page=}")
                return False
    LOG.debug(f"Correct {update=}")
    return True


def _sort(a, b):
    if (a, b) not in rules:
        return 0
    return -1 if (a, b) in rules else 1
