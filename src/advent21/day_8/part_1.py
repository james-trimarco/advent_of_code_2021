import sys
from advent21.utils import handle_input, Timer
from advent21.day_8.utils import read_words_sep_pipe
from typing import List


def count_uniques(output: List[str]) -> int:
    counter = 0
    UNIQUES = (2, 3, 4, 7)
    for signal in output:
        if len(signal) in UNIQUES:
            counter += 1
    return counter


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 8
    data_path = handle_input(day_number, sys.argv[1])
    _, output = read_words_sep_pipe(data_path)
    counter = count_uniques(output)
    print(f"Count: {counter}")

    t.stop()
