library = {
    "9780192833655": {"name": "The Picture of Dorian Gray", "quantity": 50},
    "9780060173227": {"name": "To Kill a Mockingbird", "quantity": 3},
    "9780140817744": {"name": "1984 - ed1", "quantity": 7},
    "9780192833983": {"name": "War and Peace", "quantity" : 10},
    "9780805210408": {"name": "The Trial", "quantity" : 15} 
}

def get_book_name(isbn):
    book = library[isbn]
    return book["name"]

# change this function to handle books we already have
def add_new_book_to_library():
    isbn = input("Enter the ISBN : ")
    if isbn in library:
        purchase_quantity_quantity = int(input("Enter the quantity(num): "))
        library[isbn]["quantity"] += purchase_quantity
    else:
        new_book_name = input("Enter the book name: ")
        new_quantity = int(input("Enter the quantity(num): "))
        library[isbn] = { "name": name, "quantity" : new_quantity }

