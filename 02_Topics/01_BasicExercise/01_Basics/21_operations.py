"""
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
"""

print("Check the data type of all your variables using type() built-in function")
a, b, c, d, e = 10, 15.254, 2+3j, "Joshi", [1, 2, 3]
print(f"type of a : {type(a)}, type of b : {type(b)}, type of c : {type(c)}, type of d : {type(d)}, type of e : {type(e)},")

print("Using the len() built-in function, find the length of your first name")
f_name = "Sourabha"
print("Length of name is ",len(f_name))

print("Compare the length of your first name and your last name")
f_name, l_name = "Sourabha", "Joshi"
print(f"Length of f_name {len(f_name)} and l_name {len(l_name)} ")
print(len(f_name) > len(l_name))