#check_for_member

def check_for_member(members):
    member_id = input("Enter Member ID: ")
    member = check_for_member(members, member_id)
    if member:
    print("You are:", member["name"])
    else:
    print("Membership does not exist.")