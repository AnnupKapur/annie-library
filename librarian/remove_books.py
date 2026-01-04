from print_functions.print_exit_library import print_exit_library
from utils.helper import print_library 
from utils.comms import isbn_input
from utils.get_book import get_book

def remove_books(library):
    isbn = isbn_input(library)
    book_exists = get_book(isbn, library)

    if book_exists[0] == True:
        name_of_book = book_exists[1]["name"]
        confirmation = input(f"Are you sure you want to remove {name_of_book}?' yes/no: ").strip().lower()

        if confirmation == "yes":
            quantity_to_remove = int(input("Enter the quantity(num) to remove: "))
            library[isbn]["quantity"] -= quantity_to_remove
            print (f"{quantity_to_remove} copies of {name_of_book} have been removed") 
            go_again = input("Would you like to remove any more books? yes/no: ").strip().lower()

            if go_again == "yes":
                return remove_books(library)

            else:
                print_exit_library(library)
                print_library(library)
    else:
        print("Book not in library system")
        try_again = input("Would you like to try again? yes/no: ").strip().lower()

        if try_again == "yes":
            return remove_books(library)

        else:
            print_exit_library(library)
