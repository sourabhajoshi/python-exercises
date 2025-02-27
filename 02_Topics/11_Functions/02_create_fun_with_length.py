"""
Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

Read: variable length of arguments in functions

Function call:

# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
"""

def func1(*args):
    ''' which take n no. of arguments '''
    print("Printing values")
    for item in args:
        print(item)

func1(20, 40, 60)
func1(80, 100)