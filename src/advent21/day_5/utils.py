import numpy as np
from typing import List, Tuple
from pathlib import Path
from collections import namedtuple

Point = namedtuple("Point", "x y")


def find_step(input: int) -> int:
    if input > 0:
        return 1
    elif input < 0:
        return -1
    else:
        return 0


def find_direction(point_1, point_2) -> Tuple[int]:
    return ((point_2.x - point_1.x), (point_2.y - point_1.y))


def find_max(lines, index):
    return max([point[index] for line in lines if len(line) > 0 for point in line])


def draw_lines(lines):
    height = find_max(lines, 0)
    width = find_max(lines, 1)
    map = np.zeros((width + 1, height + 1), dtype=np.int16)
    for line in lines:
        if len(line) > 0:
            for point in line:
                map[point[0], point[1]] += 1
    return map


def read_vent_lines(file_path: Path) -> List[List[List[int]]]:
    try:
        with open(file_path, "r") as file:
            map = []
            for line in file:
                points = line.split("->")
                points = [tuple(int(i) for i in i.strip().split(",")) for i in points]
                points = [Point(x, y) for (x, y) in points]
                map.append(points)

    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return map
