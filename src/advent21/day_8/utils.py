from pathlib import Path
from typing import Tuple, List


def read_words_sep_pipe(file_path: Path) -> Tuple[List[str], List[str]]:
    try:
        with open(file_path, "r") as file:
            patterns, output = [], []
            for line in file:
                patterns_raw, output_raw = line.split("|")[0], line.split("|")[1]
                patterns.append([word.strip() for word in patterns_raw.split()])
                output.append([word.strip() for word in output_raw.split()])
    except FileNotFoundError as e:
        print(f"File not found {e}")
        raise
    return patterns, output
