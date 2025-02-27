"""
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
"""

f_name, l_name, country, age = input("Enter a f name, l name, country and age (with space) : ").split()
print(f_name, l_name, country, age)

f_name, l_name, country, age = input("Enter a f name, l name, country and age (with comma seperated) : ").split(",")
print(f_name, l_name, country, age)