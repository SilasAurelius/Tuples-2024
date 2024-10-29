# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists. 
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    book_name = input("Enter book name: ").title()
    book_author = input("Enter book author: ").title()
    if (book_name, book_author) in library:
        print("Book already in library.")
    else:
        library.append((book_name, book_author))
        print("Book added to library!")
        
def view_library():
    library.sort()
    for book, name in library:
        print(f"\n{book} by {name}")

while True:
    print("\n===MENU===")
    print("1. Add book\n2. View all books\n3. Quit")
    try:
        user_input = int(input("Enter selection: "))
        if user_input == 1:
            add_book()
        elif user_input == 2:
            view_library()
        else:
            print("Thanks for using the library! Goodbye")
            break
    except ValueError:
        print("Enter valid number.")