import sys
from advent21.utils import handle_input, Timer
from typing import List


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 9
    data_path = handle_input(day_number, sys.argv[1])

    t.stop()
