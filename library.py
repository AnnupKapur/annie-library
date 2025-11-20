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
    name = input("Enter the book name: ")
    quantity = int(input("Enter the quantity(num): "))
    library[isbn] = { "name": name, "quantity" : quantity }

#if the title is already in the library, it needs to be added to the quantity
#if/else to check for title 
#if it is in the library, add it to the quantity that is already there
#else, create a new entry in the dictionary (square brackets)
#the new entry (else) will be = and not += because it is a new entry

def add_new_book_to_library (library, title, quantity): 
    if title in library:
        library[title]+=quantity
    else:
        library[title] = quantity 
    return library 
