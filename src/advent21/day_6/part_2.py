import sys
import numpy as np
from typing import List
from nptyping import NDArray
from pathlib import Path
from advent21.utils import read_ints_sep_comma, handle_input, Timer
from collections import Counter


def pass_one_day(school: Counter):
    t = Timer()
    t.start()

    for age, count in sorted(school.copy().items(), reverse=True):
        if age == 0:
            school[6] += count
            school[8] = count
        else:
            school[age - 1] = count
    return school


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 6
    data_path = handle_input(day_number, sys.argv[1])
    fishes = read_ints_sep_comma(data_path)

    school = Counter(fishes)
    for key in range(9):
        if key not in school.keys():
            school[key] = 0

    for day in range(1, 257):
        print(f"{day} Days")
        school = pass_one_day(school)

        print(sum(school.values()))
        print("\n")

    t.stop()
