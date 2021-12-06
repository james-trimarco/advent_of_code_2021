from typing import List, Tuple
from pathlib import Path


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
