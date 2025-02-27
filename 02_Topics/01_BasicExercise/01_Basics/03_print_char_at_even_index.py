"""
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  PYnative
Printing only even index chars
P
n
t
v
"""

orig_str = input("Enter a string : ")

print(f"Original string is : {orig_str}")
print("Characters present at an even index numbers : ")
for index, ch in enumerate(orig_str):
    if(index % 2 == 0):
        print(ch)