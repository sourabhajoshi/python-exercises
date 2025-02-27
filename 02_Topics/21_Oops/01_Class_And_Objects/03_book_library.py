"""
Scenario:
You are building a system to manage a collection of books in a library. You will define a Book class with the following attributes:

title: The title of the book.
author: The author of the book.
year: The year the book was published.

Additionally, you will define a Library class that:

Can add books to the library.
Can display all books in the library.
Can find a book by its title.
"""

class Book:
    """
        a class to represent the book
        attributes : title (str), author (str) and year (int)
    """

    def __init__(self, title, author, year):
        """ Initializes the Book object with a title, author, and year of publication. """
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        """ Display details of book """
        print(f"Book title is {self.title}, author is {self.author} and publication year {self.year}")

class Library:
    """
        A class represent a library which contain collection of books
    """

    def __init__(self):
        """ initilize library with empty list of books """
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        """ display all the books """
        if not self.books:
            print("No books in library")
        else:
            for book in self.books:
                book.display()

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book    
        return None
    

book1 = Book("The Alchemist", "Paulo Coelho", 1988)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Create an instance of the Library class
my_library = Library()

my_library.display_books() #No books in library

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.display_books() #No books in library

# Find a book by its title
search_title = "1984"
found_book = my_library.find_book_by_title(search_title)

if found_book:
    print(f"\nFound book with title '{search_title}':")
    found_book.display()
else:
    print(f"\nNo book found with title '{search_title}'")