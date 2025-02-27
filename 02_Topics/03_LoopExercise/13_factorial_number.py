"""
Exercise 13: Find the factorial of a given number
Write a Python program to use for loop to find the factorial of a given number.

The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.

For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120

Expected output:

120
"""

number = int(input("Enter a number : "))

if number < 0:
    print("Enter a positive integer")
elif number == 0:
    print("factorial of 0 is 1")
else:
    factorial_num = 1
    for i in range(1, number+1):
        factorial_num = (factorial_num*i)
    print(factorial_num)