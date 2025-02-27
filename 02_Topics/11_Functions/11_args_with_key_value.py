"""
If we pass the arguments with key and value, the order of the arguments does not matter.
"""

def add_two_nums(x, y):
    print("x : ", x)
    print("y : ", y)
    print("x+y : ", x+y)

add_two_nums(y=10, x=5)


def print_fullname(f_name, l_name, city):
    print("First name : ", f_name, "last name : ", l_name, "City : ", city)

print_fullname(city="Bidar", l_name="Joshi", f_name="Sourabha")