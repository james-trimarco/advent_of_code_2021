import sys
from statistics import mean
from typing import List, Tuple
from pathlib import Path
from advent21.utils import handle_input, build_matrix


def read_ints_from_line(line: str, sep=","):
    return [int(x) for x in line.split(sep) if x.strip().isnumeric()]


def read_bingo_input(file_path: Path):
    try:
        with open(file_path, "r") as file:
            boards = []
            for index, line in enumerate(file):
                line = line.replace("  ", " ")
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
            return numbers, boards

    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    # return numbers


class Board:
    def __init__(self) -> None:
        self.new_method()

    def new_method(self):
        pass


if __name__ == "__main__":
    day_number = 4
    data_path = handle_input(day_number, sys.argv[1])
    numbers, boards = read_bingo_input(data_path)

    # matrix = build_matrix(boards[0])

    # print(f" {results[0] * results[1]}")
