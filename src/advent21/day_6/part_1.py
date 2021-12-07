import sys
import numpy as np
from nptyping import NDArray
from pathlib import Path
from advent21.utils import read_ints_sep_comma, handle_input, Timer


def pass_one_day(fish: int):
    if fish == 0:
        fish = 6
        school.append(9)
    else:
        fish -= 1
    return fish


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 6
    data_path = handle_input(day_number, sys.argv[1])
    fishes = read_ints_sep_comma(data_path)
    school = []

    for fish in fishes:
        school.append(fish)

    for day in range(80):
        school = [pass_one_day(x) for x in school if isinstance(fish, int)]
        print(f"Day {day}: {len(school)} lanternfish")

    t.stop()
