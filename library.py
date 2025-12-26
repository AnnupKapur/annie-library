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

def access_id_number():
    user_id_input = input("Enter your ID number: ").strip().lower()
    if user_id_input in members:
        print(f'Are you {members[user_id_input]["name"]}?')
        user_choice = input("yes/no ").strip().lower()
        if user_choice == "yes":
            print (f"Welcome to your library service!")
        else:
            print("Do you need to create a library account?")
            user_choice_two = input("yes/no ").strip().lower()
            if user_choice_two == "yes":
                return add_members()
            else:
                print("There is a problem with the service, please go to the desk to resolve the issue.")
    else:
        print("Member does not exist. Do you need to create a new membership")
        user_choice_two = input("yes/no ").strip().lower()
        if user_choice_two == "yes":
            return add_members()
        else:
            print("Exiting library service")

def borrow_books():
    member_id = input("Enter your member ID: ").strip()
    if member_id not in members:
        print("Member not found.")
        return access_id_number()

    member = members[member_id]
    book_name_input = input("Enter the name of the book you would like to borrow: ").strip().lower()

    for isbn, book_in_stock in library.items():
        if book_in_stock["name"].strip().lower() == book_name_input:
            print(f"Before borrowing, quantity: {book_in_stock['quantity']}")
            if book_in_stock["quantity"] > 0:
                library[isbn]["quantity"] -= 1
                member["books_borrowed"].append(isbn)
                print(f"{member['name']} has borrowed '{book_in_stock['name']}' (ISBN: {isbn})")
                print(f"After borrowing, quantity: {library[isbn]['quantity']}")
                print("Would you like to borrow another book?")
                borrow_another_book = input("yes/no: ").strip().lower()
                if borrow_another_book == "yes":
                    return borrow_books() 
                else:
                    return print_exit_library()
            else:
                print(f"Sorry, '{book_in_stock['name']}' is currently out of stock.")
                print("Would you like to check the library for a different book?")
                check_a_different_book = input("yes/no: ").strip().lower()
                if check_a_different_book == "yes":
                    return borrow_books()
                else:
                    return print_exit_library()  

    print("Book not found in library.")
    print("Would you like to try again?")
    try_again = input("yes/no ")
    if try_again == "yes":
        return borrow_books()
    else:
        return print_exit_library() 


def return_books():
    member_id = input("Enter your member ID: ").strip()
    if member_id not in members:
        print("Member not found.")
        return access_id_number()
    
    member = members[member_id]
    book_name_input = input("Enter the name of the book you would like to return: ").strip().lower()

    for isbn, book_in_returns in library.items():
        if book_in_returns["name"].strip().lower() == book_name_input:
            print(f"Before returning, quantity: {book_in_returns['quantity']}")
        if book_in_returns["name"] == library[isbn]["name"]: 
                library[isbn]["quantity"] += 1
                member["books_borrowed"].remove(isbn)
                print(f"{member['name']} has returned '{book_in_returns['name']}' (ISBN: {isbn})")
                print(f"After returning, quantity: {library[isbn]['quantity']}")
                print("Would you like to return another book?")
                return_another_book = input("yes/no: ").strip().lower()
                if return_another_book == "yes":
                    return return_books() 
                else:
                    return print_exit_library()













def isbn_input():
    isbn = input("Enter the ISBN : ")
    return isbn

def get_book(isbn):
    if isbn in library:
        book = library[isbn]
        return (True, book)
    else:
        return (False, False)

def print_exit_library():
    print ("--------------------------------")
    print ("Exiting library system")
    print ("--------------------------------")

def add_new_book_to_library():
    while True:
        isbn = isbn_input()
        book_exists = get_book(isbn)

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
    book_exists = get_book(isbn)

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

def search_by_book_name():
    while True:
        searched_name = input("Enter book name: ").strip().lower()
        if_its_found = False

        for isbn in library.keys():
            book = library[isbn]
            if searched_name in book["name"].strip().lower():  
                print(f"{isbn} :: {book['name']} - x {book['quantity']}")
                if_its_found = True

        if not if_its_found:
            print("Book not found in the library.")

        go_again = input("Would you like to search for another book? yes/no: ").strip().lower()
        if go_again != "yes":
            print_exit_library()
            break

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

# This is a helper function you can call to print out the current state of the members 
def print_members():
    print("Here is the current library members")
    print("===================================")
    for memberId in members:
        member = members[memberId]
        name = member["name"]
        dob = member["dob"]
        dob_formatted = str(dob["day"]) + str(dob["month"]) + str(dob["year"])
        address = member["address"]
        print(f"name: {name}")
        print(f"dob: {dob_formatted}")
        print(f"address: {address}")
        print("-----------------------------------")
        print("books: ")
        for isbn in member["books_borrowed"]:
            book = get_book(isbn)
            if book[0] == True:
                print(f"   {isbn} :: {book[1]['name']}")
        print("===================================")


# you can run code here to test your stuff works
# e.g. I have printed the library
# print library
return_books()
print_library()
# how to test your stuff
# print the library at the beginning
# call your function which you have worked on
# print the library again to test it worked
