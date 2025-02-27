import __main__
from my_modules import generate_full_name

fname = input("Enter first name : ")
lname = input("Enter last name : ")
# print("Full Name : ", generate_full_name(fname, lname))

# print(__name__) # __main__
# print(__main__) # <module '__main__' from 'c:\\Appl\\SelfLearning\\Python\\python-exercises\\02_Topics\\12_Modules\\01_simple_module_example.py'>

if __name__ == __main__:
    print("My module is running")
    generate_full_name(f_name="x", l_name="y")
else:
    print("My module is imported")