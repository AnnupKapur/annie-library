from utils.get_book import get_book

def dob_format(dob):
    dob_formatted = str(dob["day"]) + " / " + str(dob["month"]) + " / " + str(dob["year"])
    return dob_formatted


# This is a helper function you can call to print out the current state of the library
def print_library(library):
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
def print_members(members, library):
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
            book = get_book(isbn, library)
            if book[0] == True:
                print(f"   {isbn} :: {book[1]['name']}")
        print("===================================")
