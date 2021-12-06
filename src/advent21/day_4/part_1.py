import sys
from statistics import mean
from typing import List, Tuple
from pathlib import Path
from advent21.utils import handle_input
from advent21.day_4.utils import read_bingo_input
import numpy as np
from nptyping import NDArray


def process_number(number: int, boards: NDArray) -> NDArray:
    np.place(boards, boards == number, -1)
    return boards


def check_for_bingo(boards: NDArray) -> Tuple[bool, int]:
    for board_number in range(boards.shape[0]):
        columns = np.all(boards[board_number] == -1, axis=0)
        rows = np.all(boards[board_number] == -1, axis=1)
        if np.any(columns) or np.any(rows):
            return True, board_number
    return False, board_number


if __name__ == "__main__":
    day_number = 4
    data_path = handle_input(day_number, sys.argv[1])
    numbers, boards = read_bingo_input(data_path)

    for number in numbers:
        boards = process_number(number, boards)
        check, board_number = check_for_bingo(boards)
        if check:
            board = boards[board_number]
            sum_unmarked = board[board != -1].sum()
            result = sum_unmarked * number
            print(result)
            break
