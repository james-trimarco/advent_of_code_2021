import sys
from statistics import mean
from typing import List, Tuple
from pathlib import Path
from advent21.utils import handle_input, build_matrix
from advent21.day_3.utils import read_bin_strings, convert_bin_to_decimal


def compute_gamma_epsilon(matrix: List[List]) -> Tuple[str, str]:
    matrix = build_matrix(input)
    gamma, epsilon = "", ""
    for index in range(len(matrix[0])):
        col = [row[index] for row in matrix]
        gamma += str(round(mean(col)))
        epsilon += str(0 if mean(col) > 0.5 else 1)
    return gamma, epsilon


if __name__ == "__main__":
    day_number = 3
    data_path = handle_input(day_number, sys.argv[1])
    bin_strings = read_bin_strings(data_path)
    matrix = build_matrix(bin_strings)
    gamma, epsilon = compute_gamma_epsilon(matrix)
    results = convert_bin_to_decimal([gamma, epsilon])
    print(f"The power consumption of the sub is {results[0] * results[1]}")
