from utils.isbn_input import isbn_input
from print_functions import print_exit_library 

def reduce_book_count(library, isbn):
    if isbn not in library:
        return
    if library[isbn]["quantity"] > 0:
        library[isbn]["quantity"] -= 1
        print("1 copy of this book has successfully been removed!")
    else:
        print("No Copies Left.")
        print_exit_library(library)            