import sys
import numpy as np
from nptyping import NDArray
from pathlib import Path
from advent21.utils import handle_input, Timer, read_ints_sep_comma


def find_min_fuel(crabs: NDArray) -> int:
    min = np.inf
    for index in range(crabs.size):
        sum = np.sum(np.abs(crabs[index] - crabs))
        if sum < min:
            min = sum
    return min


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 7
    data_path = handle_input(day_number, sys.argv[1])
    crabs = read_ints_sep_comma(data_path)
    crabs = np.asarray(crabs, dtype=np.int32)
    print(find_min_fuel(crabs))

    t.stop()
