from model import Library, Book


class MapValue:
    def __init__(self):
        self.total_books = None
        self.total_library = None
        self.total_scanning_day = None
        self.books = dict()
        self.libraries = dict()

    def set_infos(self, total_books: int, total_library: int, total_scanning_day: int):
        self.total_books = total_books
        self.total_library = total_library
        self.total_scanning_day = total_scanning_day

    def add_library(self, library: Library):
        self.libraries[library.id] = library

    def get_library(self, library_id: int):
        return self.libraries[library_id]


    def add_book(self, book: Book):
        self.books[book.id] = book

    def get_book(self, book_id: int):
        return self.books[book_id]
