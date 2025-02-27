"""
Scenario: Library Management System
Let’s imagine a library system that handles different types of Media items (Books, DVDs, and AudioBooks). All media items share some common properties like title, author, and publication_year, but each media type has unique properties. For example, a DVD has a duration (length of the video), and an audiobook has a narrator.

We will create a base class Media with common attributes and methods, and then create derived classes Book, DVD, and Audiobook that extend the Media class.
"""

# Base class
class Media:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published Year: {self.year}")

# Derived class: Book (inherits from Media)
class Book(Media):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages
    
    def display_details(self):
        super().display_details()
        print(f"Pages: {self.pages}")

# Derived class: DVD (inherits from Media)
class DVD(Media):
    def __init__(self, title, author, year, duration):

        # Note : Should not include the self parameter explicitly, as super().__init__() automatically # # passes the self reference for you.
        super().__init__(title, author, year)
        self.duration = duration,

    def display_details(self):
        super().display_details()
        print(f"Duration: {self.duration}")

# Derived class: Audiobook (inherits from Media)
class AudioBook(Media):
    def __init__(self, title, author, year, narrator):
        super().__init__(title, author, year)
        self.narrator = narrator

    def display_details(self):
        super().display_details()
        print(f"Narrator: {self.narrator}")

# Create objects of each media type
book = Book("The Catcher in the Rye", "J.D. Salinger", 1951, 277)
dvd = DVD("Inception", "Christopher Nolan", 2010, 148)
audiobook = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, "Rob Inglis")

print("Book details")
book.display_details()

print("-" *50)

print("DVD details")
dvd.display_details()

print("-" *50)

print("AudioBook details")
audiobook.display_details()
