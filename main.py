import numpy as np
import argparse
from Parser import Parser
from Writer import Writer


def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(line[:-1])


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input", help="Input file")
    args = arg_parser .parse_args()
    return args.input


if __name__ == '__main__':
    show_banner()
    path_to_input_file = get_args()

    parser = Parser(path_to_input_file)
    parser.parse()
    # Parsing
    # Solving
    # Scoring

    # Write output
    writer = Writer()
    writer.write_out_put(path_to_input_file, "coucou")

