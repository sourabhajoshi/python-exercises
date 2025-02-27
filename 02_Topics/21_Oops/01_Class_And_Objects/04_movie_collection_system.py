"""
Creating a simple Movie Collection Management System for a movie enthusiast or a movie library. The goal is to store and manage a collection of movies, with each movie having a title, a director, and the release year. You want to be able to display all the movies in your collection.

In this scenario:

The Movie: Each movie has details like:
Title (e.g., "Inception")
Director (e.g., "Christopher Nolan")
Release year (e.g., "2010")

The Movie Collection: A collection (or library) of movies is where you can store multiple Movie objects. This collection can be thought of as a movie library, where each entry represents one movie.
"""

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = director
    
    def display(self):
        print(f"Movie name {self.title}, Director {self.director} and releaseed year {self.year}")

class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        if not self.movies:
            print("No movies")
        else:
            for movie in self.movies:
                movie.display()


# Create movie objects
movie1 = Movie("Inception", "Christopher Nolan", 2010)
movie2 = Movie("The Dark Knight", "Christopher Nolan", 2008)
movie3 = Movie("Interstellar", "Christopher Nolan", 2014)

# create movie collection
my_movie_collection = MovieCollection()

# Add movies 
my_movie_collection.add_movie(movie1)

my_movie_collection.display_movies()