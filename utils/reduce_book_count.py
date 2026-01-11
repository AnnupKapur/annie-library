from utils.isbn_input import isbn_input
from print_functions import print_exit_library 

def reduce_book_count(library, isbn):
    if isbn not in library:
        print("Book Not Found")
        return

    if library[isbn]["quantity"] > 0:
        library[isbn]["quantity"] -= 1
        book_name = library[isbn]["name"]
        print(f"Removed 1 copy of {book_name}")
    else:
        print("No Copies Left.")
