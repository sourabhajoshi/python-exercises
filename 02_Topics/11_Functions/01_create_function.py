"""
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, and print their value.
"""

def printUserInfo(name, age):
    print(name, age)

name = input("Enter a name : ")
age = int(input("Enter a age : "))

printUserInfo(name, age)