def check_member_can_borrow(member):
    if member["books_borrowed"] < 5:
        return True
    else:
        member_name = member["name"]
        print(f"{member_name} has already borrowed the maximum of 5 books")
        print("Please return before borrowing more.")
        return False
