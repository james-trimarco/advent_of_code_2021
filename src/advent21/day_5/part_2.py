import sys
from typing import List
from pathlib import Path
from advent21.utils import handle_input
from advent21.day_5.utils import (
    find_direction,
    read_vent_lines,
    find_step,
    Point,
    draw_lines,
)
import numpy as np
from nptyping import NDArray


def interpolate(map: List[List[Point]]) -> List[List[Point]]:
    for index in range(len(map)):
        line = map[index]
        dir = find_direction(line[0], line[1])
        for i in range(1, abs(max(dir, key=abs))):
            new_point = Point(
                line[0].x + (i * find_step(dir[0])),
                line[0].y + (i * find_step(dir[1])),
            )
            line.insert(i, new_point)
        map[index] = line
    return map


if __name__ == "__main__":
    day_number = 5
    data_path = handle_input(day_number, sys.argv[1])
    lines_raw = read_vent_lines(data_path)
    lines = interpolate(lines_raw)
    map = draw_lines(lines)
    print(map.T)
    print(f"Number of overlaps: {len(map[map > 1])}")
