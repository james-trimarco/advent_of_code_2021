from pathlib import Path
from typing import Tuple
import numpy as np
from nptyping import NDArray


def read_heightmap(file_path: Path) -> NDArray:
    try:
        map = []
        with open(file_path, "r") as file:
            for line in file:
                line = [int(num.strip()) for num in line if num.isnumeric()]
                map.append(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return np.array(map)
