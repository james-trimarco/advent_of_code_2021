import numpy as np
from typing import List, Tuple
from pathlib import Path


def read_ints_from_line(line: str, sep=",") -> List[int]:
    return [int(x) for x in line.replace("  ", " ").split(sep) if x.strip().isnumeric()]


def read_bingo_input(file_path: Path) -> Tuple[List[int], np.array]:
    try:
        with open(file_path, "r") as file:
            boards = []
            for index, line in enumerate(file):
                if index == 0:
                    numbers = read_ints_from_line(line)
                else:
                    row = read_ints_from_line(line, sep=" ")
                    if len(row) < 1:
                        board = []
                    else:
                        board.append(row)
                        if len(board) == 5:
                            boards.append(board)
            boards = np.array(boards)
            return numbers, boards
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
