def print_book_list(book_dict):
    for isbn in book_dict.keys():
        book = book_dict[isbn]
        print(f"{isbn} :: {book['name']} - x {book['quantity']}")
