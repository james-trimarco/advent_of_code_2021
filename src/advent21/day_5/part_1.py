import sys
from typing import List
from pathlib import Path
from advent21.utils import handle_input
from advent21.day_5.utils import read_vent_lines
import numpy as np
from nptyping import NDArray


def interpolate(map: List[List[List[int]]]):
    for index in range(len(map)):
        line = map[index]
        if line[0][0] == line[1][0]:
            # vertical
            if line[1][1] < line[0][1]:
                line[1][1], line[0][1] = line[0][1], line[1][1]  # swap
            for i in range(1, line[1][1] - line[0][1]):
                new_point = list([line[0][0], line[0][1] + i])
                line.insert(i, new_point)
            map[index] = line
        elif line[0][1] == line[1][1]:
            # horizontal
            if line[1][0] < line[0][0]:
                line[1][0], line[0][0] = line[0][0], line[1][0]  # swap
            for i in range(1, line[1][0] - line[0][0]):
                new_point = list([line[0][0] + i, line[1][1]])
                line.insert(i, new_point)
            map[index] = line
        else:
            # delete nonstraight line
            map[index] = []
    return map


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


if __name__ == "__main__":
    day_number = 5
    data_path = handle_input(day_number, sys.argv[1])
    lines_raw = read_vent_lines(data_path)
    lines = interpolate(lines_raw)
    map = draw_lines(lines)
    print(map.T)
    print(f"Number of overlaps: {len(map[map > 1])}")
