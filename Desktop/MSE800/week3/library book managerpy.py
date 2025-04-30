class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

# Main

lib = Library()
lib.add_book("Harry Potter", "J.K. Rowling")
lib.add_book("The Alchemist", "Paulo Coelho")

print("Books in library:")
lib.show_books()
