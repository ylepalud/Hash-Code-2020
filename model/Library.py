from model.Book import Book


class Library:
    def __init__(self, id: int, number_of_books: int, books_per_day: int, sign_up_days: int):
        self.id = id
        self.number_of_books = number_of_books
        self.books_per_day = books_per_day
        self.sign_up_days = sign_up_days
        self.book_list = []

    def add_book(self, book: Book):
        self.book_list.append(book)

    def get_books(self):
        for book in self.book_list:
            yield book

    def sort_books(self):
        self.book_list.sort(key=lambda x: x.score, reverse=False)

    def __str__(self):
        result = str(self.id) + " " + str(self.number_of_books) + "\n"
        for book in self.book_list:
            result += str(book.id) + " "
        result += "\n"
        return result
