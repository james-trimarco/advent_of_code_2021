import sys
from advent21.utils import handle_input, Timer
from advent21.day_9.utils import read_heightmap
from typing import List, Tuple, Set
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


def find_low_points(map: NDArray) -> List[Tuple[int, int]]:
    low_points, basins = [], []

    for ix, iy in np.ndindex(map.shape):
        point = map[ix, iy]
        neighbor_indices = find_neighbors(ix, iy, map.shape)
        neighbors = map[tuple(np.array(neighbor_indices).T)]
        if all(point < neighbors):
            starting_point = set([(ix, iy)])
            traversed = set()
            basin = find_basins(starting_point, map, traversed)
            basins.append(basin)
            low_points.append(point)
    return low_points, basins


def find_basins(
    basin_indices: set, map: NDArray, traversed: set
) -> List[Set[Tuple[int, int]]]:

    for point in basin_indices.difference(traversed):
        # print(f"traversing: {point}")
        traversed.add(point)
        # find all the neighbor points
        neighbor_indices = find_neighbors(point[0], point[1], map.shape)
        # remove neighbor points that are 9s
        neighbor_indices = [
            index for index in neighbor_indices if map[index[0], index[1]] < 9
        ]
        for point in neighbor_indices:
            basin_indices.add(point)
            basin_indices.union(find_basins(basin_indices, map, traversed))
    return basin_indices


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 9
    data_path = handle_input(day_number, sys.argv[1])
    map = read_heightmap(data_path)
    low_points, basins = find_low_points(map)
    basin_sizes = sorted([len(basin) for basin in basins], reverse=True)
    print(np.prod(basin_sizes[:3]))

    t.stop()
