import sys
from typing import List, Tuple
from pathlib import Path
from advent21.utils import handle_input
from advent21.day_2.utils import read_steps


class Submarine:
    def __init__(self, steps: List[Tuple]) -> None:
        self.h_position = 0
        self.depth = 0
        for step in steps:
            self.move(step)

    def move(self, step: Tuple):
        if step.direction == "forward":
            self.h_position += step.distance
        elif step.direction == "up":
            self.depth -= step.distance
        elif step.direction == "down":
            self.depth += step[1]

    def end(self):
        return self.h_position * self.depth


if __name__ == "__main__":
    day_number = 2
    data_path = handle_input(day_number, sys.argv[1])
    steps = read_steps(data_path)
    submarine = Submarine(steps)
    print(f"Submarine depth times horizontal position is {submarine.end()}")
