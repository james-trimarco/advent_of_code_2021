import sys
import numpy as np
from typing import List
from nptyping import NDArray
from pathlib import Path
from advent21.utils import read_ints_sep_comma, handle_input, Timer


def pass_one_day(fish: int):
    print(fish)
    if fish == 0:
        return 6
    else:
        return fish - 1


if __name__ == "__main__":
    t = Timer()
    # t.start()

    day_number = 6
    data_path = handle_input(day_number, sys.argv[1])
    fishes = read_ints_sep_comma(data_path)
    school = []

    for index, fish in enumerate(fishes):
        school.append(fish)

    for day in range(180):
        print(day)
        t.start()
        count_zeros = school.count(0)
        t.stop()
        t.start()
        school = [*map(lambda x: 6 if x == 0 else x - 1, school)]
        t.stop()

        t.start()
        school.extend([8] * count_zeros)
        t.stop()

    print(len(school))
    t.stop()
