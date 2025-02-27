"""
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
"""

a, b, c = input("Enter 3 sides of parameters seperated by comma : ").split(",")

per_of_triangle = int(a) + int(b) + int(c)

print(f"The perimeter of the triangle is {per_of_triangle}")