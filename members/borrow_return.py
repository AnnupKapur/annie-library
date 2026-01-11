def add_book_to_member(member, isbn):
    member_books = member["books_borrowed"]

    # Check if they already have borrowed that book

    # if yes, they can't borrow it again
    if isbn in member_books:
        print("Member has already borrowed this book.")
        return False
    # if no, then they can borrow it
    else:
        member_books.append(isbn)


def remove_book_from_member(member, isbn):
    member_books = member["books_borrowed"]

    # check if they have borrowed that book

    # if yes, they can return it
    if isbn in member_books:
        member_books.remove(isbn)
        print("Book returned successfully.")
        return True
    # if no, they cannot return a book they have not borrowed
    else:
        print("Member did not borrow this book.")
        return False
