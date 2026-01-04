#add_members

def add_members(members):
    name = input("Enter your name: ")
    print("Enter you DOB:")
    day = int(input(" - Day: "))
    month = int(input(" - Month: "))
    year = int(input(" - Year: "))
    address  = input("Enter your address: ")
    new_id = get_next_id(members)
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