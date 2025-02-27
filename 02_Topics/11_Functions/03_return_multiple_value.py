"""
Exercise 3: Return multiple values from a function
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

Given:

def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Expected Output

50, 30
"""

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

addition, subtraction, multiplication, division = calculation(40, 10)
print(f"Addition of two nums : {addition}")
print(f"Subtraction of two nums : {subtraction}")
print(f"Multiplication of two nums : {multiplication}")
print(f"Division of two nums : {division}")
