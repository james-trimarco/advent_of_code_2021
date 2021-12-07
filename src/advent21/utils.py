from typing import List, Tuple
from pathlib import Path
import time


def read_ints_sep_comma(file_path: Path) -> List[int]:
    try:
        with open(file_path, "r") as file:
            for line in file:
                ints = [int(x.strip()) for x in line.split(",")]
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


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.3f} seconds")
