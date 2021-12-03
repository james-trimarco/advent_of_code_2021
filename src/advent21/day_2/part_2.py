import sys
from typing import List, Tuple
from advent21.utils import handle_input
from pathlib import Path
from collections import namedtuple

Step = namedtuple("Step", "direction distance")


def read_steps(file_path: Path) -> List[Step]:
    try:
        with open(file_path, "r") as file:
            steps = []
            for line in file:
                parts = line.split()
                direction = parts[0]
                distance = int(parts[1])
                steps.append(Step(direction, distance))
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return steps


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
    print(submarine.end())
