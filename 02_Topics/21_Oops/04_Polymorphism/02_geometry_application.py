"""
Imagine you're building a Geometry Application that helps users calculate the area of various shapes. This application allows users to input different shapes (like circles, rectangles, and triangles) along with their required parameters (radius, width/height, or base/height) to calculate and display the area of the shape.

In this application, we want to provide a simple interface that allows the user to enter any shape and then calculates the area, while the logic for calculating the area varies for each shape type.
"""

import math

# Base class
class Shape:
    def calculate_area(self):
        pass

# subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

# subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.height * self.width
    
# List of different shapes
shapes = [
    Circle(5),      # Circle with radius 5
    Rectangle(4, 6),  # Rectangle with width 4 and height 6
]

# Function to calculate and display area for all shapes
def display_areas(shapes):
    for shape in shapes:
        area = shape.calculate_area()
        print(f"The area of {shape.__class__.__name__} is: {area:.2f}")

# Call the function to display areas
display_areas(shapes)
    

