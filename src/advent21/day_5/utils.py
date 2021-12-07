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
