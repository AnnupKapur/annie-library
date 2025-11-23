library = {
    "9780192833655": {"name": "The Picture of Dorian Gray", "quantity": 50},
    "9780060173227": {"name": "To Kill a Mockingbird", "quantity": 3},
    "9780140817744": {"name": "1984 - ed1", "quantity": 7},
    "9780192833983": {"name": "War and Peace", "quantity" : 10},
    "9780805210408": {"name": "The Trial", "quantity" : 15} 
}

def isbn_input():
    isbn = input("Enter the ISBN : ")
    return isbn

def get_book(isbn):
    if isbn in library:
        book = library[isbn]
        return (True, book)
    else:
        return (False, False)

def add_new_book_to_library():
    isbn = isbn_input()
    book_exists = get_book(isbn)
    if book_exists[0] == True:
        purchase_quantity_quantity = int(input("Enter the quantity(num): "))
        library[isbn]["quantity"] += purchase_quantity
    else:
        new_book_name = input("Enter the book name: ")
        new_quantity = int(input("Enter the quantity(num): "))
        library[isbn] = { "name": new_book_name, "quantity" : new_quantity }

# CHANGE THIS FUNCTION
def remove_books():
    isbn = isbn_input()
    book_exists = get_book(isbn)
    if book_exists[0] == True:
        print(f"You are removing some of {book_exists[1]["name"]}")
        quantity_to_remove = int(input("Enter the quantity(num) to remove: "))
        library[isbn]["quantity"] -= quantity_to_remove
    else:
        print("Book not in library system")


# This is a helper function you can call to print out the current state of the library
def print_library():
    print("Here is the current library:")
    print("-----------------------------------")
    for book in library:
        qty = library[book]["quantity"]
        name = library[book]["name"]
        print(f"{qty:2}x {name}")
    print("-----------------------------------")
    print("")
    print("")


# you can run code here to test your stuff works
# e.g. I have printed the library
# print library
print_library()

# how to test your stuff
# print the library at the beginning
# call your function which you have worked on
# print the library again to test it worked
