import sys
from typing import List, Tuple
from pathlib import Path
from advent21.utils import handle_input
from advent21.day_4.utils import read_bingo_input
import numpy as np
from nptyping import NDArray


def process_number(number: int, boards: NDArray) -> NDArray:
    np.place(boards, boards == number, -1)
    return boards


def check_for_bingo(boards: NDArray, board_number: int) -> Tuple[bool, int]:
    columns = np.all(boards[board_number] == -1, axis=0)
    rows = np.all(boards[board_number] == -1, axis=1)
    if np.any(columns) or np.any(rows):
        return True, board_number
    else:
        return False, board_number


def find_last_board(numbers: List[int], boards: NDArray) -> int:
    board_ledger = []
    for number in numbers:
        boards = process_number(number, boards)
        for board_number in range(boards.shape[0]):
            bingo, board_number = check_for_bingo(boards, board_number)
            if bingo and board_number not in board_ledger:
                board_ledger.append(board_number)
            if len(board_ledger) == boards.shape[0]:
                board = boards[board_number]
                sum_unmarked = board[board != -1].sum()
                result = sum_unmarked * number
                return result


if __name__ == "__main__":
    day_number = 4
    data_path = handle_input(day_number, sys.argv[1])
    numbers, boards = read_bingo_input(data_path)
    result = find_last_board(numbers, boards)
    print(result)
