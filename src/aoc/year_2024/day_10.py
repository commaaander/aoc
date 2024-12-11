"""https://adventofcode.com/2024/day/10"""

from calendar import c
from typing import Any, Dict, List, Tuple

from rich import print

from adventofcode import LOG

questions: List[str] = [
    "What is the sum of the scores of all trailheads on your topographic map?",  # noqa: E501
    "",  # noqa: E501
]

Coord = Tuple[int, int]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    map = _parse_raw_data(raw_data)
    trails: Dict[Coord, List[Coord]] = {}
    LOG.debug(_print_map(map))
    for coord, heigth in map.items():
        if heigth == 0:
            LOG.debug(f"Found trailhead @{coord}.")
            trails[coord] = []
            _find_trail(map, coord, [], trails)

    filtered_trails = _filter_trails(trails)
    answer = sum(len(i) for i in filtered_trails.values())

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    map = _parse_raw_data(raw_data)
    trails: Dict[Coord, List[Coord]] = {}
    LOG.debug(_print_map(map))
    for coord, heigth in map.items():
        if heigth == 0:
            LOG.debug(f"Found trailhead @{coord}.")
            trails[coord] = []
            _find_trail(map, coord, [], trails)

    answer = sum(len(i) for i in trails.values())

    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Dict[Coord, int]:
    return {(x, y): int(heigth) for y, row in enumerate(raw_data.split("\n")) for x, heigth in enumerate(list(row))}


def _print_map(map: Dict[Coord, int]) -> str:
    width = max(coord[0] for coord in map.keys())
    heigth = max(coord[1] for coord in map.keys())
    string_map: List[str] = [f"   {''.join(str(i % 10) for i in range(width))}"]

    for y in range(heigth):
        row: List[str] = [f"{y:2d} "]
        for x in range(width):
            row.append(str(map.get((x, y), " ")))
        string_map.append("".join(row))

    return "\n".join(string_map)


def _print_trail(map: Dict[Coord, int], trail: List[Coord]) -> str:
    width = max(coord[0] for coord in map.keys()) + 1
    heigth = max(coord[1] for coord in map.keys()) + 1
    string_map: List[str] = [f"   {''.join(str(i % 10) for i in range(width))}"]
    for y in range(heigth):
        row: List[str] = [f"{y:2d} "]
        for x in range(width):
            row.append(
                f"[{'white' if (x, y) in trail else 'grey'}]{map[(x,y)]}[/{'white' if (x, y) in trail else 'grey'}]"
            )
        string_map.append("".join(row))

    return "\n".join(string_map)


def _find_trail(
    map: Dict[Coord, int],
    coord: Coord,
    current_trail: List[Coord],
    trails: Dict[Coord, List[Coord]],
) -> bool:
    current_trail.append(coord)
    # LOG.debug(f"Added {coord} with heigth={map[coord]} to current trail {current_trail}.")

    if map.get(coord) == 9:
        LOG.debug(f"Trail completed: {current_trail}")
        # print(_print_trail(map, current_trail))
        trails[current_trail[0]].append(current_trail)
        return True

    x, y = coord
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if map.get((x + dx, y + dy), -1) == map[coord] + 1:
            _find_trail(map, (x + dx, y + dy), current_trail.copy(), trails)
    return False


def _filter_trails(trails: Dict[Coord, List[Coord]]) -> Dict[Coord, List[Coord]]:
    filtered_trails: Dict[Coord, List[Coord]] = {}
    for trailhead in trails:
        filtered_trails[trailhead] = []
        for trail in trails[trailhead]:
            if [trail[0], trail[-1]] not in filtered_trails[trailhead]:
                filtered_trails[trailhead].append([trail[0], trail[-1]])

    return filtered_trails
