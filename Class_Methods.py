class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self):
        Book.total_books += 1  # Increment the book count whenever a new book is created

# Example
book1 = Book()  # Creating a new book
book2 = Book()  # Creating another book

print("Total Books:", Book.total_books)  # Display total books count
