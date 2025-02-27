"""
Exercise: Book Details

Write a Python program that defines a Book class. Each book has two attributes: title and author. Create an object of the Book class, initialize it with a book title and author, and then display the details of the book.
"""

# Create a class
class Book:
    """
        A class to represent a book
        Attributes : 
            title (str) : title of book
            author (str) : author of the book
    """
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book title is {self.title} and author is {self.author}")

# create an object
my_book = Book("Nakutanti", "D.R.Bendre")
my_book.display()
        