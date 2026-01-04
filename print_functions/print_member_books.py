from utils.get_book import get_book

def print_member_books(member_id, members, library):
    member = members[member_id]
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
