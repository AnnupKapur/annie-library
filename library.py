from utils.get_book import get_book
from utils.get_book import search_by_book_name
from utils.comms import isbn_input
from utils.comms import print_exit_library
from utils.helper import print_members
from utils.helper import print_library 
from utils.helper import dob_format

library = {
    "9780192833655": {"name": "The Picture of Dorian Gray", "quantity": 50, "genre": "Gothic Horror"},
    "9780060173227": {"name": "To Kill a Mockingbird", "quantity": 3, "genre": "Southern Gothic"},
    "9780140817744": {"name": "1984", "quantity": 7, "genre": "Dystopian Fiction"},
    "9780192833983": {"name": "War and Peace", "quantity" : 10, "genre": "Historical Fiction"},
    "9780805210408": {"name": "The Trial", "quantity" : 15, "genre": "Dystopian Fiction"},
    "9780141040349": {"name": "Pride and Prejudice", "quantity": 25, "genre": "Romance Fiction"},
    "9780141439556": {"name": "Wuthering Heights", "quantity": 30, "genre": "Gothic Fiction"},
    "9780198840824": {"name": "Frankenstein", "quantity": 2, "genre": "Science Fiction"},
    "9780140449242": {"name": "The Brothers Karamazov", "quantity": 5, "genre": "Philosophical Fiction"},
    "9780140449174": {"name": "Anna Karenina", "quantity": 8, "genre": "Romantic Fiction"}
}

members = {
    "0001": { 
        "name": "Annika",
        "dob": { "day": 25, "month": 1, "year": 1996 },
        "address": "84 Broadway North, Walsall, WS1 2QF",
        "books_borrowed": [ "9780192833655", "9780141040349", "9780805210408" ]
    }
}

def get_next_id():
    current = len(members)
    new = current + 1
    return f"{new:04}"

def add_members():
    name = input("Enter your name: ")
    print("Enter you DOB:")
    day = int(input(" - Day: "))
    month = int(input(" - Month: "))
    year = int(input(" - Year: "))
    address  = input("Enter your address: ")
    new_id = get_next_id()
    members[new_id] = {
        "name": name,
        "dob": {
            "day": day,
            "month": month,
            "year": year,
        },
        "address": address,
        "books_borrowed": [],
    }
    return new_id

def create_member_flow(members):
    new_member_id = add_members()
    print("Welcome")
    name = members[new_member_id]["name"]
    dob = dob_format(members[new_member_id]["dob"])
    address = members[new_member_id]["address"]
    print(f"{name} : {dob}")
    print(f"{address}")
    print("-----------------------------")
    return new_member_id

def add_new_book_to_library():
    while True:
        isbn = isbn_input()
        book_exists = get_book(isbn, library)

        if book_exists[0] == True: 
            purchase_quantity = int(input("Enter the quantity(num): "))
            library[isbn]["quantity"] += purchase_quantity
            print(f"You have added {purchase_quantity} copies of this book to the library")
        else: 
            new_book_name = input("Enter the book name: ")
            new_quantity = int(input("Enter the quantity(num): "))
            library[isbn] = {"name": new_book_name, "quantity": new_quantity}
            print(f"You have added '{new_book_name}' with {new_quantity} copies to the library")

        add_more = input("Are there more books to add? yes/no: ").strip().lower()
        if add_more != "yes":
            break 
    print_library()  
    print_exit_library()
 
def remove_books():
    isbn = isbn_input()
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
                return remove_books()

            else:
                print_exit_library()
                print_library()
    else:
        print("Book not in library system")
        try_again = input("Would you like to try again? yes/no: ").strip().lower()

        if try_again == "yes":
            return remove_books ()

        else:
            print_exit_library()



# you can run code here to test your stuff works
# e.g. I have printed the library
# print library
print_members(members, library)
print_library(library)
# how to test your stuff
# print the library at the beginning
# call your function which you have worked on
# print the library again to test it worked
