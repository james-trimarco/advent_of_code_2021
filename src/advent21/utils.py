from typing import List
from pathlib import Path


def read_ints(file_path: Path) -> List[int]:
    "Reads a list of ints from a filename."
    try:
        with open(file_path, "r") as file:
            ints = []
            for line in file:
                if line.strip().isnumeric():
                    ints.append(int(line))
                else:
                    continue
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return ints