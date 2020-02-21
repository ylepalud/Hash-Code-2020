from model.Book import Book


class Library:
    def __init__(self, id: int, number_of_books: int, books_per_day: int, sign_up_days: int):
        self.id = id
        self.number_of_books = number_of_books
        self.books_per_day = books_per_day
        self.sign_up_days = sign_up_days
        self.book_list = []
        self.efficiency = None
        self.send_books = []
        self.index_last_send_book = None

    def add_book(self, book: Book):
        self.book_list.append(book)

    def get_books(self):
        for book in self.book_list:
            yield book

    def remove_list_books(self, books: [Book]):
        for book in books:
            self.remove_book(book)

    def remove_book(self, book: Book):
        try:
            self.book_list.remove(book)
        except:
            pass

    def sort_books(self):
        self.book_list.sort(key=lambda x: x.score, reverse=True)

    def send_next_books(self):
        if self.index_last_send_book is None:
            self.index_last_send_book = 0
        next_send_book = self.send_books[self.index_last_send_book]

        for nb_book in range(self.books_per_day):
            self.send_books.append(next_send_book)
            self.index_last_send_book += 1

    def __str__(self):
        result = str(self.id) + " " + str(len(self.book_list)) + "\n"
        for book in self.book_list:
            result += str(book.id) + " "
        result += "\n"
        return result
