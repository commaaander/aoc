"""https://adventofcode.com/2024/day/11"""

from collections import deque
from typing import Any, Deque, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "",  # noqa: E501
    "",  # noqa: E501
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    blinks = 75
    stones: Deque[int] = deque(map(int, raw_data.split()))

    for i in range(blinks):
        new_stones: Deque[int] = deque([])
        try:
            while (stone := stones.popleft()) >= 0:
                if stone == 0:
                    new_stones.append(1)
                elif len(str(stone)) % 2 == 0:
                    s_stone = str(stone)
                    half_size = len(s_stone) // 2
                    new_stones.append(int(s_stone[:half_size]))
                    new_stones.append(int(s_stone[half_size:]))
                else:
                    new_stones.append(stone * 2024)
        except IndexError:
            pass
        stones = new_stones.copy()
        LOG.debug(f"{i+1:2d}. blink, {len(stones)} stones")

    answer = len(stones)

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    blinks: int = 75
    stones: Deque[int] = deque(map(int, raw_data.split()))

    for i in range(blinks):
        new_stones: Deque[int] = deque([])
        try:
            while (stone := stones.popleft()) >= 0:
                new_stones.extend(_execute_rules(stone))
        except IndexError:
            pass
        stones = new_stones.copy()
        LOG.debug(f"{i+1:2d}. blink, {len(stones)} stones")

    answer = len(stones)

    return questions[1], answer


def _execute_rules(stone: int) -> Deque[int]:
    stones: Deque[int] = deque()
    if stone == 0:
        stones.append(1)
    elif len(str(stone)) % 2 == 0:
        s_stone = str(stone)
        half_size = len(s_stone) // 2
        stones.append(int(s_stone[:half_size]))
        stones.append(int(s_stone[half_size:]))
    else:
        stones.append(stone * 2024)
    return stones
