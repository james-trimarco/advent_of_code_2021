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


def rolling_sum_of_three(data: List[int]) -> List[int]:
    sums = []
    for index in range(len(data)):
        try:
            first, second, third, = (
                data[index],
                data[index + 1],
                data[index + 2],
            )
            sums.append(sum([first, second, third]))
        except IndexError as e:
            print(f"Full set of three sweeps not available: {e}")
    return sums


def detect_increasing_depth(data: List[int]) -> List[int]:
    increases = 0
    previous_sweep = float("inf")
    for sweep in data:
        if sweep > previous_sweep:
            increases += 1
        previous_sweep = sweep
    return increases


if __name__ == "__main__":
    list_of_ints = read_ints(data_path)
    rolling_sums = rolling_sum_of_three(list_of_ints)
    increase_count = detect_increasing_depth(rolling_sums)
    print(f"A total of {increase_count} increases were detected.")
