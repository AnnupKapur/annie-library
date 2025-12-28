def get_book(isbn, library):
    if isbn in library:
        book = library[isbn]
        return (True, book)
    else:
        return (False, False)

def print_book_list(book_dict):
    for isbn in book_dict.keys():
        book = book_dict[isbn]
        print(f"{isbn} :: {book['name']} - x {book['quantity']}")

def search_by_book_name(library):
    searched_name = input("Enter book name: ").strip().lower()
    books_found = {}

    for isbn in library.keys():
        book = library[isbn]
        if searched_name in book["name"].strip().lower():  
            books_found[isbn] = book

    if len(books_found.keys()) == 0:
        return False
    else:
        return books_found
