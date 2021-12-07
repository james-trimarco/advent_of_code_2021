import sys
import numpy as np
from typing import List
from nptyping import NDArray
from pathlib import Path
from advent21.utils import read_ints_sep_comma, handle_input, Timer


class LanternFish:
    # __slots__ = ["age", "school", "pass_one_day", "reproduce"]  # <-- allowed attributes

    def __init__(self, age: int, school: list) -> None:
        self.age = age
        self.school = school

    def pass_one_day(self):
        if self.age == 0:
            self.age = 6
            # self.reproduce()
        else:
            self.age -= 1

    def reproduce(self):
        self.school.append(LanternFish(8, self.school))


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 6
    data_path = handle_input(day_number, sys.argv[1])
    fishes = read_ints_sep_comma(data_path)
    school = []
    for age in fishes:
        school.append(LanternFish(age, school))

    print([type(x) for x in school])
    print([x.age for x in school])

    for day in range(18):
        school = [x.pass_one_day() for x in school if isinstance(x, LanternFish)]
        print(len(school))
        # fishes = [x.age for x in school]
        # print(f"After {day} days:{fishes}")

    t.stop()
