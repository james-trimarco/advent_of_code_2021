from typing import Tuple
from pathlib import Path


def handle_input(day_number: int, run_type: str):
    if run_type == "data":
        print("Running with full puzzle data.")
        return Path.cwd() / "src" / "advent21" / f"day_{day_number}" / "input.txt"
    else:
        print("Running with test data.")
        return Path.cwd() / "src" / "advent21" / f"day_{day_number}" / "test_input.txt"
