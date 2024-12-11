"""https://adventofcode.com/2024/day/6"""

from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "How many distinct positions will the guard visit before leaving the mapped area?",  # noqa: E501
    "How many different positions could you choose for this obstruction?",  # noqa: E501
]

Coord = Tuple[int, int]
Map = Dict[Coord, str]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0

    guardian_directions = "^>v<"
    map: Map = _parse_raw_data(raw_data)
    guardian_positions = []

    start, guardian_direction = [(coord, map[coord]) for coord in map.keys() if map[coord] in guardian_directions][0]

    x, y = start
    guardian_positions.append(start)
    dx, dy = _get_guardian_vector(guardian_direction)

    while (x + dx, y + dy) in map.keys():
        if map[(x + dx, y + dy)] == "#":
            guardian_direction = guardian_directions[(guardian_directions.find(guardian_direction) + 1) % 4]
            dx, dy = _get_guardian_vector(guardian_direction)
        else:
            x, y = x + dx, y + dy
            guardian_positions.append((x, y))

    answer = len(set(guardian_positions))
    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0

    guardian_directions: str = "^>v<"

    start_map: Map = _parse_raw_data(raw_data)
    map_width = len(raw_data.splitlines())
    map_heigth = len(raw_data.splitlines()[0])

    start, start_guardian_direction = [
        (coord, start_map[coord]) for coord in start_map.keys() if start_map[coord] in guardian_directions
    ][0]

    for row in range(map_heigth):
        for col in range(map_width):
            map = start_map.copy()
            guardian_path: Map = {}
            guardian_direction = start_guardian_direction
            if map[(col, row)] != "#":
                map[(col, row)] = "#"
                x, y = start
                guardian_path[start] = guardian_direction
                dx, dy = _get_guardian_vector(guardian_direction)
                while (x + dx, y + dy) in map.keys() and guardian_path.get((x + dx, y + dy), "") != guardian_direction:
                    if map[(x + dx, y + dy)] == "#":
                        guardian_direction = guardian_directions[
                            (guardian_directions.find(guardian_direction) + 1) % 4
                        ]
                        dx, dy = _get_guardian_vector(guardian_direction)
                    else:
                        x, y = x + dx, y + dy
                        guardian_path[(x, y)] = guardian_direction

                if guardian_path.get((x + dx, y + dy), "") == guardian_direction:
                    # _draw_map(map, guardian_path, map_width, map_heigth)
                    answer += 1
                    LOG.debug(
                        f"Loop #{answer:04d} detected mit additional obstacle @{(col,row)} with pathlength of {len(guardian_path)}"
                    )

    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Map:
    return {(x, y): char for y, row in enumerate(raw_data.split("\n")) for x, char in enumerate(list(row))}


def _get_guardian_vector(guardian: str) -> Tuple[int, int]:
    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }
    return directions.get(guardian, (0, 0))


def _draw_map(map: Dict, path: Dict, width, heigth):
    drawing: str = ""
    for y in range(heigth):
        row = ""
        for x in range(width):
            row += path[(x, y)] if (x, y) in path else map.get((x, y), "")
        drawing += f"{row}\n"
    LOG.debug(drawing)
