"""
Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
"""

given_number = int(input("Enter a number : "))
orignal_number = given_number

while given_number > 0:
    reminder = given_number % 10
    given_number = given_number//10
    print(reminder, end=" ")