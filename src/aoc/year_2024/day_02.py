"""https://adventofcode.com/2024/day/2"""

from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = ["How many reports are safe?", "How many reports are now safe?"]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0
    parsed_data = _parse_raw_data(raw_data)

    answer = sum(1 for report in parsed_data if _report_is_safe(report))

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0
    parsed_data = _parse_raw_data(raw_data)

    answer = sum(1 for report in parsed_data if _report_is_safe(report=report, use_problem_dampener=True))

    return questions[1], answer


def _parse_raw_data(raw_data: str) -> List[List[int]]:
    return [[int(level) for level in report.split()] for report in raw_data.split("\n")]


def _report_is_safe(report: List[int], use_problem_dampener: bool = False) -> bool:
    bad_level_count: int = 0
    is_bad_level: bool = False
    deltas: List[int] = [0]
    for idx in range(1, len(report)):
        delta: int = report[idx] - report[idx - 1]
        deltas.append(delta)
        if delta == 0 or abs(delta) > 3:
            is_bad_level = True
        if idx > 2:
            old_delta: int = report[idx - 1] - report[idx - 2]
            if _sign(delta) != _sign(old_delta):
                is_bad_level = True
        if is_bad_level:
            bad_level_count += 1

    if use_problem_dampener:
        bad_level_count -= 1
    report_is_safe: bool = bool(bad_level_count < 1)
    LOG.debug(f"{report=} with {deltas=} is {report_is_safe=}. {bad_level_count=}")
    return report_is_safe


def _sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
