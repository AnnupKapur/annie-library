#add_new_book

def add_new_book_to_library(library):
    while True:
        isbn = isbn_input(library)
        book_exists = get_book(isbn, library)

        if book_exists[0] == True: 
            purchase_quantity = int(input("Enter the quantity(num): "))
            library[isbn]["quantity"] += purchase_quantity
            print(f"You have added {purchase_quantity} copies of this book to the library")
        else: 
            new_book_name = input("Enter the book name: ")
            new_quantity = int(input("Enter the quantity(num): "))
            library[isbn] = {"name": new_book_name, "quantity": new_quantity}
            print(f"You have added '{new_book_name}' with {new_quantity} copies to the library")

        add_more = input("Are there more books to add? yes/no: ").strip().lower()
        if add_more != "yes":
            break 
    print_library(library)  
    print_exit_library(library)