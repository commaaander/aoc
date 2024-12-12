"""https://adventofcode.com/2024/day/9"""

from collections import deque
from typing import Any, Deque, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What is the resulting filesystem checksum?",  # noqa: E501
    "",  # noqa: E501
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    disk_map = _parse_raw_data(raw_data)
    compacted_disk_map: Deque[int] = deque()

    while True:
        try:
            if (block := disk_map.popleft()) != -1:
                compacted_disk_map.append(block)
            else:
                while (end_block := disk_map.pop()) == -1:
                    pass
                compacted_disk_map.append(end_block)
        except IndexError:
            break

    answer = sum(idx * id for idx, id in enumerate(compacted_disk_map))

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Deque[int]:
    disk_map: Deque[int] = deque()

    for file_id, idx in enumerate(range(0, len(raw_data), 2)):
        block: str = raw_data[idx : idx + 2]
        for _ in range(int(block[0])):
            disk_map.append(file_id)
        for i in range(int(block[1]) if len(block) == 2 else 0):
            disk_map.append(-1)

    return disk_map
