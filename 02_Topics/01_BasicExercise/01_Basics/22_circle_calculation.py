"""
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.

Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

import math

print("With given radius ")
rad_of_circle = 30
area_of_circle = math.pi * (rad_of_circle ** 2)
circum_of_circle = 2 * math.pi * rad_of_circle

print("Area of circle pi*r^2: ", round(area_of_circle, 2))
print("circumference of circle 2*pi*r: ", round(circum_of_circle, 2))

print("-" * 50)

rad = int(input("Enter radius : "))
print("Area of circle : ", math.pi*(rad**2))