"""https://adventofcode.com/2025/day/4"""

from typing import Any, Dict, List, Set, Tuple

from adventofcode import LOG

questions: List[str] = [
    "How many rolls of paper can be accessed by a forklift?",  # noqa: E501
    "How many rolls of paper in total can be removed by the Elves and their forklifts?",  # noqa: E501
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    paper_roll_coords = parse_raw_data(raw_data)

    for coord in paper_roll_coords:
        neighbors = count_paper_rolls_around(*coord, paper_roll_coords)
        if len(neighbors) < 4:
            LOG.debug(f"Found accesible role at {coord} with {len(neighbors)} neighbors")
            answer += 1

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    paper_roll_coords = parse_raw_data(raw_data)
    removed_paper_roll_coords = set()

    while True:
        removed_paper_rolls = 0
        round = 0

        for coord in paper_roll_coords:
            neighbors = count_paper_rolls_around(*coord, paper_roll_coords)
            if neighbors < 4:
                # LOG.debug(f"Found accesible role at {coord} with {neighbors} neighbors")
                removed_paper_roll_coords.add(coord)
                removed_paper_rolls += 1

        # paper_roll_coords = [coord for coord in paper_roll_coords if coord not in removed_paper_roll_coords]
        paper_roll_coords = paper_roll_coords - removed_paper_roll_coords

        if removed_paper_rolls == 0:
            break
        round += 1
        LOG.debug(f"{round=:03} Removed {removed_paper_rolls} paper rolls, {len(paper_roll_coords)} remain")

    answer = len(removed_paper_roll_coords)

    return questions[1], answer


def parse_raw_data(raw_data: str) -> Set[Tuple[int, int]]:
    return set(
        (line, column)
        for line, row in enumerate(raw_data.splitlines())
        for column, char in enumerate(row)
        if char == "@"
    )


def count_paper_rolls_around(x: int, y: int, paper_roll_coords: Set[Tuple[int, int]]) -> int:
    paper_roll_coords = paper_roll_coords.copy() - {(x, y)}
    paper_rolls_around = set((x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2))
    return paper_roll_coords & paper_rolls_around
