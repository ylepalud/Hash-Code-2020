import argparse
from Parser import Parser
from model.result_values import ResultValue
import scoring


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
    print("Parsing solution from file ", path_to_input_file)
    parser = Parser(path_to_input_file)
    map_value = parser.parse()

    # Solving
    print("Solving solution for ", path_to_input_file.split(".")[0])
    result_value = ResultValue()
    libraries = map_value.libraries.values()
    remaining_days_before_next_library_submission = 0
    last_elected_library = None
    submited_libraries = []

    for day_number in range(map_value.total_scanning_day):
        # Si on peut soumettre une nouvelle library
        if remaining_days_before_next_library_submission == 0:
            # On recalcule efficiency pour chaque library et on trie les library
            for library in libraries:
                library.efficiency = scoring.efficiency_library(library, map_value.total_scanning_day - day_number)
            libraries.sort(key=lambda x: x.efficiency, reverse=False)

            last_elected_library = libraries[0]
            remaining_days_before_next_library_submission = last_elected_library.sign_up_days
            libraries = libraries[1:]

            for library in libraries:
                library.remove_list_books(last_elected_library.book_list)

        remaining_days_before_next_library_submission -= 1

    # Write output
    result_value.write_result(path_to_input_file)


