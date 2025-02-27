"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
"""

given_number = int(input("Enter a number : "))
orignal_number = given_number
reversed_number = 0
while given_number > 0:
    reminder = given_number%10
    reversed_number = (reversed_number * 10) + reminder
    given_number = given_number//10

print(reversed_number)

if orignal_number == reversed_number:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")
