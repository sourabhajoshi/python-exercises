"""
Exercise 4: Print multiplication table of a given number
Given:

num = 2
Expected output is:

2
4
6
8
10
12
14
16
18
20
"""

given_number = int(input("Enter a number : "))

for i in range(1, 11):
    print(given_number*i)