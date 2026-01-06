def can_member_borrow_a_book(members,library):
    member_id = input("Enter Member ID: ")
    if member_id in members:
        if len(members[member_id]["books_borrowed"]) < 5:
            return True
        else:
            return False
    else:
        print("Member Not Found") 

