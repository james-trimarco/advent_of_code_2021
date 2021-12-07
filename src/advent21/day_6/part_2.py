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
    school = np.array([], dtype=np.uint8)  # start with 100 million spaces in the array
    print(school.shape)

    for index, fish in enumerate(fishes):
        school = np.append(school, [fish], 0)

    for day in range(256):
        print(day)
        t.start()
        count_zeros = school.size - np.count_nonzero(school)
        t.stop()

        t.start()
        school = np.where(school == 0, 6, school - 1)
        t.stop()

        t.start()
        school = np.concatenate([school, np.repeat(8, count_zeros)])
        t.stop()

    print(school.size)
    # t.stop()
