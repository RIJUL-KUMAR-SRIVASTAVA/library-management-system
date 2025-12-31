class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
