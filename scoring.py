from model import Library


def total_score_library(library: Library):
    total = 0
    for i in library.book_list:
        total += i.score
    return total


def efficiency_library(library: Library):
    return total_score_library(library) / ((library.books_per_day * library.number_of_books) + library.signup_time)


def efficiency_remaining_days(days: int, library: Library):
    score = 0
    days_of_scan = days - library.sign_up_days
    books_scanned = days_of_scan * library.books_per_day
    list_books = library.get_books()
    for i in range(books_scanned):
        score += list_books[i].score
    return score


def efficiency_on_given_days(days: int, library: Library):
    return efficiency_remaining_days(days, library)
