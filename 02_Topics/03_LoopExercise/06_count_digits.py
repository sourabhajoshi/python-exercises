"""
Exercise 6: Count the total number of digits in a number
Write a Python program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
"""

num = int(input("Enter a number : "))

if num < 0:
    print("Please enter a positive integer")
else:
    count_digits = 0
    while num > 0:
        num = num//10
        count_digits += 1

    print(count_digits)