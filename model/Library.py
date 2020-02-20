from model.Book import Book


class Library:
    def __init__(self, id: int, number_of_books: int, books_per_day: int):
        self.id = id
        self.number_of_books = number_of_books
        self.books_per_day = books_per_day
        self.book_list = []

    def add_book(self, book: Book):
        self.book_list.append(book)

    def sort_books(self):
        self.book_list.sort(key=lambda x: x.score, reverse=False)

    def __str__(self):
        # TODO pour simplifier le write
        pass
