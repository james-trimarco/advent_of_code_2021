import sys
from typing import List
from advent21.day_1.utils import read_ints
from advent21.utils import handle_input


def detect_increasing_depth(data: List[int]):
    increases = 0
    previous_sweep = float("inf")
    for sweep in data:
        if sweep > previous_sweep:
            increases += 1
        previous_sweep = sweep
    return increases


if __name__ == "__main__":
    day_number = 1
    data_path = handle_input(day_number, sys.argv[1])
    list_of_ints = read_ints(data_path)
    print(detect_increasing_depth(list_of_ints))
