"""
Exercise 14: Print a downward half-pyramid pattern of stars
* * * * *  
* * * *  
* * *  
* *  
*
"""

number = int(input("Enter a number : "))

for i in range(number+1, 0, -1):
    for j in range(0, i-1):
        print("*", end=" ")
    print()