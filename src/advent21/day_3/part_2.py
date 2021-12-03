import sys
from statistics import mean
from typing import List
from pathlib import Path
from advent21.utils import handle_input
from advent21.day_3.utils import read_bin_strings, build_matrix, convert_bin_to_decimal


def compute_oxygen_or_carbon(matrix: List[List], type: str) -> str:
    for index in range(len(matrix[0])):
        col = [row[index] for row in matrix]
        if type == "oxygen":
            keeper = 1 if mean(col) >= 0.5 else 0
        elif type == "carbon":
            keeper = 0 if mean(col) >= 0.5 else 1
        matrix = [row for row in matrix if row[index] == keeper]
        if len(matrix) == 1:
            result = "".join([str(x) for x in matrix[0]])
            return result
    print("No answer was detected.")
    return None


if __name__ == "__main__":
    day_number = 3
    data_path = handle_input(day_number, sys.argv[1])
    binary_strings = read_bin_strings(data_path)
    matrix = build_matrix(binary_strings)
    oxygen = compute_oxygen_or_carbon(matrix, type="oxygen")
    carbon = compute_oxygen_or_carbon(matrix, type="carbon")
    results = convert_bin_to_decimal([oxygen, carbon])
    print(f"The life support rating of the sub is {results[0] * results[1]}")
