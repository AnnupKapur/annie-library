def create_member_flow(members):
    new_member_id = add_members(members)
    print("Welcome")
    name = members[new_member_id]["name"]
    dob = dob_format(members[new_member_id]["dob"])
    address = members[new_member_id]["address"]
    print(f"{name} : {dob}")
    print(f"{address}")
    print("-----------------------------")
    return new_member_id
