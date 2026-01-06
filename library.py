from utils.helper import print_members
from utils.helper import print_library 
from members.remove_member import delete_member_flow
from members.can_member_borrow import can_member_borrow_a_book 


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


# you can run code here to test your stuff works
# e.g. I have printed the library
# print library
print_members(members, library)
print_library(library)
can_member_borrow_a_book(members,library) 
# how to test your stuff
# print the library at the beginning
# call your function which you have worked on
# print the library again to test it worked
