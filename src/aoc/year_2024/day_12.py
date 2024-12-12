"""https://adventofcode.com/2024/day/12"""

from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "What is the total price of fencing all regions on your map?",  # noqa: E501
    "",  # noqa: E501
]

Coord = Tuple[int, int]
map: Dict[Coord, str] = {}
gardens: Dict[Coord, int] = {}
regions: List[Dict[str, Dict[str, int]]] = []
max_rlevel: int = 0


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    global map
    global gardens
    global regions

    map = _parse_raw_data(raw_data)
    gardens = {}
    regions = []

    for coord, plant in map.items():
        # determine region
        if coord not in gardens.keys():
            region = len(regions)
            gardens[coord] = region
            regions.append({plant: {"area": 0, "perimeter": 0}})
            LOG.debug(f"Created new {region=} for garden {coord} with {plant=}.")
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if map.get((coord[0] + dx, coord[1] + dy), "") == plant:
                    _set_region((coord[0] + dx, coord[1] + dy), region, 1)
        else:
            region = gardens[coord]

        # calculate region area
        regions[region][map[coord]]["area"] += 1

        # calculate perimeter
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if map.get((coord[0] + dx, coord[1] + dy), "") != map[coord]:
                regions[region][map[coord]]["perimeter"] += 1

    # some stats
    LOG.debug(f"Max recursion level: {max_rlevel}")
    LOG.debug(f"Max region area    : {max(rv['area'] for r in regions for rv in r.values())}")

    LOG.debug(regions)

    answer = sum(rv["area"] * rv["perimeter"] for r in regions for rv in r.values())

    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Dict[Coord, str]:
    return {
        (x, y): char for y, row in enumerate(raw_data.split("\n")) for x, char in enumerate(list(row)) if char != "."
    }


def _set_region(coord: Coord, region: int, rlevel: int) -> None:
    global map
    global gardens
    global max_rlevel

    max_rlevel = max(max_rlevel, rlevel)

    if coord not in gardens.keys():
        gardens[coord] = region
        LOG.debug(f"[L{rlevel:03d}] Added garden {coord} with plant '{map[coord]}' to {region=}.")

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if map.get((coord[0] + dx, coord[1] + dy), "") == map[coord]:
                _set_region((coord[0] + dx, coord[1] + dy), region, rlevel + 1)

    return
