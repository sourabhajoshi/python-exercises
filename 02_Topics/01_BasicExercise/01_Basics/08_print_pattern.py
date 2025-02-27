"""
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

number = int(input("Enter a number : "))

for i in range(1, number+1):
    for j in range(i):
        print(i, end="")
    print()