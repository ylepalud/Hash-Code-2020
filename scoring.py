from model import Library


def total_score_library(library: Library):
    total = 0
    for i in library.book_list:
        total += i.score
    return total


def efficiency_library(library: Library, remaining_days_total):
    total_days_library = (library.books_per_day * library.number_of_books) + library.sign_up_days
    if total_days_library < remaining_days_total:
        return efficiency_remaining_days(remaining_days_total, library)
    else:
        return total_score_library(library) / total_days_library


def efficiency_remaining_days(days: int, library: Library):
    score = 0
    days_of_scan = days - library.sign_up_days
    books_scanned = days_of_scan * library.books_per_day
    list_books = library.book_list
    for i in range(books_scanned):
        if i < len(list_books):
            score += list_books[i].score
        else:
            return score


def efficiency_on_given_days(days: int, library: Library):
    return efficiency_remaining_days(days, library)
