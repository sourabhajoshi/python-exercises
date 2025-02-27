"""
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
"""

floor_div = 7//3
int_val = int(2.7)
is_equal = floor_div == int_val

print("is if the floor division of 7 by 3 is equal to the int converted value of 2.7? ", is_equal)

print("Check if type of '10' is equal to type of 10? ", type(10) == type("10"))

print("Check if int('9.8') is equal to 10? ", int(float('9.8'))==10 )