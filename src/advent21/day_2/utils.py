from typing import List
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
