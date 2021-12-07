import sys
import numpy as np
from typing import List
from nptyping import NDArray
from pathlib import Path
from advent21.utils import read_ints_sep_comma, handle_input, Timer


class LanternFish:
    def __init__(self, age: int) -> None:
        self.just_hatched = False
        self.age = age

    def pass_one_day(self, age):
        self.age -= 1


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 6
    data_path = handle_input(day_number, sys.argv[1])
    fish = read_ints_sep_comma(data_path)

    t.stop()
