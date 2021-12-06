import numpy as np
from typing import List
from pathlib import Path


def read_vent_lines(file_path: Path) -> List[List[List[int]]]:
    try:
        with open(file_path, "r") as file:
            map = []
            for line in file:
                points = line.split("->")
                points = [list(int(i) for i in i.strip().split(",")) for i in points]
                map.append(points)

    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return map
