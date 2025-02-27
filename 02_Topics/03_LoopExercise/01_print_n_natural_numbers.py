"""
Exercise 1: Print first "n" natural numbers using while loop
Help: while loop in Python

Expected output:

1
2
3
4
5
6
7
8
9
10
"""

num = int(input("Enter a number : "))

if num < 0:
    print("Please entewr a positive integer value")
else:
    i = 1
    while i <= num:
        print(i)
        i += 1 
