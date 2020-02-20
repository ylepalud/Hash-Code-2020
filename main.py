import numpy as np
import argparse
from Parser import Parser
from Writer import Writer
from model.result_values import ResultValue


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

    # Parsing
    parser = Parser(path_to_input_file)
    map_value = parser.parse()

    # Solving
    result_value = ResultValue()
    result_value.add_library(map_value.get_library(0))
    result_value.add_library(map_value.get_library(1))

    # Scoring

    # Write output
    result_value.write_result(path_to_input_file)

