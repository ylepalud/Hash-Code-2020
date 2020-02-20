import io
from model.Map_values import MapValue
from model.Book import Book
from model.Library import Library


class Parser:
    def __init__(self, path_to_input_file):
        self.input_file = path_to_input_file

    def parse(self) -> MapValue:
        line_number = 0
        number_of_library = 0
        current_library = None
        map_value = MapValue()

        with io.open(self.input_file, "r", encoding="utf-8") as file:
            for line in file:
                line = [int(number) for number in line[:-1].split(" ")]

                if line_number == 0:
                    map_value.set_infos(line[0], line[1], line[2])

                elif line_number == 1:
                    for _id, score in enumerate(line):
                        book = Book(_id, score)
                        map_value.add_book(book)

                else:
                    if line_number % 2 == 0:
                        library = Library(number_of_library, line[0], line[2], line[1])
                        current_library = library
                        map_value.add_library(library)
                        number_of_library += 1

                    else:
                        for book_id in line:
                            current_library.add_book(map_value.get_book(book_id))
                        current_library.sort_books()

                line_number += 1

        return map_value
