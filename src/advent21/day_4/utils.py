from typing import List
from pathlib import Path


def convert_bin_to_decimal(bin_strings: List[str]) -> List[int]:
    return [int(bin_string, 2) for bin_string in bin_strings]


def read_bin_strings(file_path: Path) -> List[str]:
    "Reads a list of binary strings from a filename."
    try:
        with open(file_path, "r") as file:
            bin_strings = []
            for line in file:
                if line.strip().isnumeric():
                    bin_strings.append(str(line.rstrip()))
                else:
                    continue
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return bin_strings
