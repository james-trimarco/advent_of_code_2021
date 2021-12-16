import sys
from advent21.utils import handle_input, Timer
from advent21.day_9.utils import read_heightmap
from typing import List, Tuple
import numpy as np
from nptyping import NDArray


def find_potentials(ix: int, iy: int):
    return [(ix + 1, iy), (ix - 1, iy), (ix, iy + 1), (ix, iy - 1)]


def find_neighbors(ix: int, iy: int, map_shape: Tuple[int]) -> List[Tuple[int, int]]:
    neighbor_indices = [
        tup
        for tup in find_potentials(ix, iy)
        if tup[0] in range(map_shape[0]) and tup[1] in range(map_shape[1])
    ]
    return neighbor_indices


def find_low_points(map: NDArray) -> List[int]:
    low_points = []
    for ix, iy in np.ndindex(map.shape):
        point = map[ix, iy]
        neighbor_indices = find_neighbors(ix, iy, map.shape)
        neighbors = map[tuple(np.array(neighbor_indices).T)]
        if all(point < neighbors):
            low_points.append(point)
    return low_points


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 9
    data_path = handle_input(day_number, sys.argv[1])
    map = read_heightmap(data_path)
    low_points = find_low_points(map)
    sum_of_risks = sum(x + 1 for x in low_points)
    print(sum_of_risks)
    t.stop()
