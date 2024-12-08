"""https://adventofcode.com/2024/day/8"""

from typing import Any, Dict, List, Tuple

from adventofcode import LOG

questions: List[str] = [
    "How many unique locations within the bounds of the map contain an antinode?",  # noqa: E501
    "How many unique locations within the bounds of the map contain an antinode?",  # noqa: E501
]

Coord = Tuple[int, int]


def part_one(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_one({raw_data=}, {kwargs=})")
    answer: int = 0
    antennas, width, heigth = _parse_raw_data(raw_data)
    antinodes: List[Coord] = []
    handled_coords: List[Tuple[Coord, Coord]] = []

    for coord, frequency in antennas.items():
        LOG.debug(f"Antenna with {frequency=} @{coord=}")
        for other_coord, _ in [
            fd
            for fd in antennas.items()
            if fd[0] != coord and (coord, fd[0]) not in handled_coords and fd[1] == frequency
        ]:
            # Delta zwischen Antennen berechnen
            dx = other_coord[0] - coord[0]
            dy = other_coord[1] - coord[1]
            LOG.debug(f"Found other antenna with same frequency @{other_coord=}. ∆={(dx,dy)}")

            # Antinodes berechnen
            antinodes.append((coord[0] - dx, coord[1] - dy))
            antinodes.append((other_coord[0] + dx, other_coord[1] + dy))

            handled_coords.append((other_coord, coord))

    answer = len(
        set(coord for coord in antinodes if coord[0] >= 0 and coord[0] < width and coord[1] >= 0 and coord[1] < heigth)
    )
    LOG.debug(f"{len(handled_coords)} handled antenna combinations.")
    return questions[0], answer


def part_two(raw_data: str, **kwargs: Dict[str, Any]) -> Tuple[str, int]:
    LOG.debug(f"part_two({raw_data=}, {kwargs=})")
    answer: int = 0
    antennas, width, heigth = _parse_raw_data(raw_data)
    antinodes: List[Coord] = []
    handled_coords: List[Tuple[Coord, Coord]] = []

    LOG.debug(_print_map(antinodes, antennas, width, heigth))
    for coord, frequency in antennas.items():
        LOG.debug(f"Antenna with {frequency=} @{coord=}")
        for other_coord, _ in [
            fd
            for fd in antennas.items()
            if fd[0] != coord and (coord, fd[0]) not in handled_coords and fd[1] == frequency
        ]:
            # Delta zwischen Antennen berechnen
            dx = other_coord[0] - coord[0]
            dy = other_coord[1] - coord[1]
            LOG.debug(f"Found other antenna with same frequency @{other_coord=}. ∆={(dx,dy)}")

            # Antinodes berechnen
            antinode_coord = (coord[0] - dx, coord[1] - dy)
            while (
                antinode_coord[0] >= 0
                and antinode_coord[0] < width
                and antinode_coord[1] >= 0
                and antinode_coord[1] < heigth
            ):
                antinodes.append(antinode_coord)
                LOG.debug(f"Added antinode @{antinode_coord}")
                antinode_coord = (antinode_coord[0] - dx, antinode_coord[1] - dy)

            antinode_coord = (other_coord[0] + dx, other_coord[1] + dy)
            while (
                antinode_coord[0] >= 0
                and antinode_coord[0] < width
                and antinode_coord[1] >= 0
                and antinode_coord[1] < heigth
            ):
                antinodes.append(antinode_coord)
                LOG.debug(f"Added antinode @{antinode_coord}")
                antinode_coord = (antinode_coord[0] + dx, antinode_coord[1] + dy)

            handled_coords.append((other_coord, coord))

    answer = len(set([*antinodes, *antennas.keys()]))
    LOG.debug(f"{len(handled_coords)} handled antenna combinations.")

    LOG.debug(_print_map(antinodes, antennas, width, heigth))
    return questions[1], answer


def _parse_raw_data(raw_data: str) -> Tuple[Dict[Coord, str], int, int]:
    return (
        {
            (x, y): char
            for y, row in enumerate(raw_data.split("\n"))
            for x, char in enumerate(list(row))
            if char != "."
        },
        len(raw_data.splitlines()[0]),
        len(raw_data.splitlines()),
    )


def _print_map(antinodes: List[Coord], antennas: Dict[Coord, str], width: int, heigth: int) -> str:
    map: List[str] = [f"   {''.join(str(i % 10) for i in range(width))}"]
    for y in range(heigth):
        row: List[str] = [f"{y:2d} "]
        for x in range(width):
            row.append("#" if (x, y) in antinodes else antennas.get((x, y), "."))
        map.append("".join(row))

    return "\n".join(map)
