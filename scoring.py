from model import Library


def total_score_library(library : Library):
    total = 0
    for i in library.book_list:
        total += i.score
    return total


def efficiency_library(library):
    return total_score_library(library) / ((library.books_per_day * library.number_of_books) + library.signup_time)


def efficiency_remaining_days(days, library):
    days_of_scan = days-library.signup_time
    books_scanned = days_of_scan*library.books_per_day
