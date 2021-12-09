import sys
from advent21.utils import handle_input, Timer
from advent21.day_8.utils import read_words_sep_pipe

if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 8
    data_path = handle_input(day_number, sys.argv[1])
    patterns, output = read_words_sep_pipe(data_path)
    print(output)
    t.stop()
