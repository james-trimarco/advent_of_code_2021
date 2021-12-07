from typing import List, Tuple
from pathlib import Path


def read_ints_sep_comma(file_path: Path) -> List[int]:
    try:
        with open(file_path, "r") as file:
            for line in file:
                ints = line.split("")
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return ints


def build_matrix(input: List[str]) -> List[List[int]]:
    matrix = []
    for bin_string in input:
        row = [int(x) for x in bin_string]
        matrix.append(row)
    return matrix


def handle_input(day_number: int, run_type: str):
    if run_type == "data":
        print("Running with full puzzle data.")
        return Path.cwd() / "src" / "advent21" / f"day_{day_number}" / "input.txt"
    else:
        print("Running with test data.")
        return Path.cwd() / "src" / "advent21" / f"day_{day_number}" / "test_input.txt"
