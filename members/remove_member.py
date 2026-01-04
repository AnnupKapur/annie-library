from print_functions.print_member_books import print_member_books
from print_functions.print_exit_library import print_exit_library
from members.check_for_member import check_member_by_id

def delete_member(member_id, members, library):
    if member_id in members:
        member = members[member_id]
        member_books = member["books_borrowed"]
        if len(member_books) > 0 :
            print("You have these books:")
            print_member_books(member_id, members, library)
            print("Cannot delete membership until all books are returned")
        else:
            del members[member_id]
            print(f"{member["name"]} successfully deleted")
            print_exit_library()
    else:
        print("That is not a valid member id")

def delete_member_flow(members, library):
    member_check = check_member_by_id(members)
    if member_check == False:
        print("Member does not exist")
        print_exit_library(library)
        return;

    print_member_books(member_check[0], members, library)
    confirmation = input("Is this you (y/n) ?").strip().lower()

    if confirmation == "y":
        delete_member(member_check[0], members, library)
    else:
        try_again = input("Would you like to try again? yes/no: ").strip().lower()

        if try_again == "yes":
            return delete_member_flow(members, library)

        else:
            print_exit_library(library)
            return
