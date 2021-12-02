import sys
from pathlib import Path
from typing import List
from advent21.utils import read_ints


if sys.argv[1] == "data":
    print("Running with full puzzle data.")
    data_path = Path.cwd() / "src" / "advent21" / "day_1" / "input.txt"
else:
    print("Running with test data.")
    data_path = Path.cwd() / "src" / "advent21" / "day_1" / "test_input.txt"


def detect_increasing_depth(data: List[int]):
    increases = 0
    previous_sweep = float("inf")
    for sweep in data:
        if sweep > previous_sweep:
            increases += 1
        previous_sweep = sweep
    return increases


if __name__ == "__main__":
    list_of_ints = read_ints(data_path)
    print(detect_increasing_depth(list_of_ints))
