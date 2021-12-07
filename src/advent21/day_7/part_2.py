import sys
import numpy as np
from nptyping import NDArray
from advent21.utils import handle_input, Timer, read_ints_sep_comma


def find_distances(crabs: NDArray) -> int:
    min = np.inf
    for index in range(crabs.size):
        distances = np.array(np.abs(crabs[index] - crabs), dtype=np.int32)
        partial_sums = [partial_sum(x) for x in distances]
        sum = np.sum(partial_sums)
        if sum < min:
            min = sum
    return int(min)


def partial_sum(nth_partial: int) -> int:
    return int((nth_partial * (nth_partial + 1)) / 2)


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 7
    data_path = handle_input(day_number, sys.argv[1])
    crabs = read_ints_sep_comma(data_path)
    crabs = np.asarray(crabs, dtype=np.int32)
    minimum_fuel = find_distances(crabs)
    print(minimum_fuel)

    t.stop()
