"""https://adventofcode.com/2024/day/4"""

from doctest import debug
from typing import Any, Dict, List, Tuple

import numpy as np

from adventofcode import LOG

questions: List[str] = [
    "How many times does XMAS appear?",
    "How many times does an X-MAS appear?",
]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    word_search_array = _parse_raw_data(raw_data)
    length, width = word_search_array.shape
    word_found_array = np.zeros((length, width), dtype=int)
    xmas_found: int = 0
    deltas = {
        "East": [("X", 0, 0), ("M", 0, 1), ("A", 0, 2), ("S", 0, 3)],
        "West": [("X", 0, 0), ("M", 0, -1), ("A", 0, -2), ("S", 0, -3)],
        "South": [("X", 0, 0), ("M", 1, 0), ("A", 2, 0), ("S", 3, 0)],
        "North": [("X", 0, 0), ("M", -1, 0), ("A", -2, 0), ("S", -3, 0)],
        "Southeast": [("X", 0, 0), ("M", 1, 1), ("A", 2, 2), ("S", 3, 3)],
        "Southwest": [("X", 0, 0), ("M", 1, -1), ("A", 2, -2), ("S", 3, -3)],
        "Northeast": [("X", 0, 0), ("M", -1, 1), ("A", -2, 2), ("S", -3, 3)],
        "Northwest": [("X", 0, 0), ("M", -1, -1), ("A", -2, -2), ("S", -3, -3)],
    }

    for y in range(length):
        for x in range(width):
            for direction in deltas.keys():
                if _check_word_search_array(word_search_array, (y, x), deltas[direction]):
                    _set_word_found_array_values(word_found_array, (y, x), deltas[direction])
                    xmas_found += 1
                    LOG.debug(f"XMAS nr. {xmas_found:2d} found @({x+1:3d},{y+1:3d}) in direction {direction}")
                    pass

    result: str = ""
    for y in range(length):
        for x in range(width):
            result += word_search_array[y, x] if word_found_array[y, x] == 1 else "."
        result += "\n"

    print(result)

    answer = xmas_found
    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    word_search_array = _parse_raw_data(raw_data)
    length, width = word_search_array.shape
    word_found_array = np.zeros((length, width), dtype=int)
    xmas_found: int = 0
    deltas = {
        "masXmas": [("M", -1, -1), ("A", 0, 0), ("S", 1, 1), ("M", 1, -1), ("A", 0, 0), ("S", -1, 1)],
        "samXmas": [("S", -1, -1), ("A", 0, 0), ("M", 1, 1), ("M", 1, -1), ("A", 0, 0), ("S", -1, 1)],
        "masXsam": [("M", -1, -1), ("A", 0, 0), ("S", 1, 1), ("S", 1, -1), ("A", 0, 0), ("M", -1, 1)],
        "samXsam": [("S", -1, -1), ("A", 0, 0), ("M", 1, 1), ("S", 1, -1), ("A", 0, 0), ("M", -1, 1)],
    }

    for y in range(length):
        for x in range(width):
            for direction in deltas.keys():
                if _check_word_search_array(word_search_array, (y, x), deltas[direction]):
                    _set_word_found_array_values(word_found_array, (y, x), deltas[direction])
                    xmas_found += 1
                    LOG.debug(f"XMAS nr. {xmas_found:2d} found @({x+1:3d},{y+1:3d}) in direction {direction}")
                    pass

    result: str = ""
    for y in range(length):
        for x in range(width):
            result += word_search_array[y, x] if word_found_array[y, x] == 1 else "."
        result += "\n"

    print(result)

    answer = xmas_found
    return questions[1], answer


def _parse_raw_data(raw_data: str):
    ret_val: List[List[str]] = []

    for row in raw_data.split("\n"):
        ret_val.append(list(row))

    return np.array(ret_val)


def _check_word_search_array(word_search_array, start, coords) -> bool:
    y, x = start
    length, width = word_search_array.shape

    try:
        for letter, dy, dx in coords:
            if y + dy < 0 or y + dy >= length or x + dx < 0 or x + dx >= width:
                return False
            if word_search_array[y + dy, x + dx] != letter:
                return False
    except:  # noqa: E722
        return False
    return True


def _set_word_found_array_values(word_found_array, start, coords):
    y, x = start

    for _, dy, dx in coords:
        word_found_array[y + dy, x + dx] = 1
