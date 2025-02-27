"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

"""

num1 = int(input("Enter a num1 : "))
num2 = int(input("Enter a num2 : "))

product_of_two_nums = num1*num2

if(product_of_two_nums <= 1000):
    print("Product of two numbers : ", product_of_two_nums)
else: 
    print("Sum of two numbers : ", num1 + num2)