import numpy as np
import argparse


def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(line[:-1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()
    path_to_input_file = args.input

    show_banner()
    # Parsing
    # Solving
    # Scoring
    # Write output
