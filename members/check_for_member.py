def check_member_by_id(members):
    member_id = input("Enter Member ID: ")
    if member_id in members:
        return (member_id, members[member_id])
    else:
        return False
