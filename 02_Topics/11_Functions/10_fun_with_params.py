"""
Functions with params
"""

def add_two_nums(a, b):
    return a+b

print(add_two_nums(2, 5))

def greetings(wishes):
    return wishes

print(greetings("Good morning"))

def full_details(id, name, age, city):
    return id, name, age, city

id, name, age, city = full_details(1, "Sourabha", 25, "Bidar")
print(id, name, age, city)