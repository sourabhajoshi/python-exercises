"""
Exercise 5: Display numbers from a list using a loop
Write a Python program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:

75
150
145
"""

numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)
    