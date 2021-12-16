import sys
from advent21.utils import handle_input, Timer
from advent21.day_8.utils import read_words_sep_pipe
from typing import List


class Display:
    def __init__(self, pattern: List[str], output: List) -> None:
        self.uniques = self.read_uniques(pattern)
        self.decoder = self.create_decoder(self.uniques, pattern)
        self.result = self.decode_output(self.decoder, output)

    def read_uniques(self, pattern: List[str]) -> dict:
        lookup = {2: 1, 3: 7, 4: 4, 7: 8}
        uniques = {}
        for signal in pattern:
            if len(signal) in lookup.keys():
                uniques[lookup.get(len(signal))] = signal
        return uniques

    def create_decoder(self, uniques: dict, pattern: List[str]):
        segments = {}
        segments["A"] = tuple(set(uniques[7]).difference(set(uniques[1])))[0]
        nine = [
            word
            for word in pattern
            if len(word) == 6 and set(uniques[4]).issubset(set(word))
        ][0]
        six = [
            word
            for word in pattern
            if len(word) == 6 and not set(uniques[1]).issubset(set(word))
        ][0]
        zero = [word for word in pattern if len(word) == 6 and word not in (nine, six)][
            0
        ]
        uniques[9], uniques[6], uniques[0] = nine, six, zero
        segments["B"] = tuple(set(uniques[8]).difference(set(six)))[0]
        segments["C"] = [letter for letter in uniques[1] if letter != segments["B"]][0]
        segments["E"] = tuple(set(uniques[8]).difference(set(nine)))[0]
        segments["G"] = tuple(set(uniques[8]).difference(set(zero)))[0]
        two = [
            word
            for word in pattern
            if len(word) == 5 and segments["E"] in word and segments["C"] not in word
        ][0]
        three = [
            word
            for word in pattern
            if len(word) == 5 and segments["B"] in word and segments["E"] not in word
        ][0]
        five = [
            word
            for word in pattern
            if len(word) == 5
            and segments["B"] not in word
            and segments["E"] not in word
        ][0]
        uniques[2], uniques[5], uniques[3] = two, five, three
        decoder = {value: key for key, value in uniques.items()}  # reversing dict
        return decoder

    def decode_output(self, decoder: dict, output: List[str]) -> int:
        result = []
        for word in output:
            for code in decoder.keys():
                if set(word) == set(code):
                    result.append(decoder.get(code))
        return int("".join([str(x) for x in result]))


if __name__ == "__main__":
    t = Timer()
    t.start()

    day_number = 8
    data_path = handle_input(day_number, sys.argv[1])
    patterns, outputs = read_words_sep_pipe(data_path)
    results = []
    for pattern, output in list(zip(patterns, outputs)):
        display = Display(pattern, output)
        results.append(display.result)

    print(sum(results))
    t.stop()
