"""
Exercise 7: Print the following pattern
Write a Python program to print the reverse number pattern using a for loop.

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

number = int(input("Enter a number : "))

for i in range(number, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()