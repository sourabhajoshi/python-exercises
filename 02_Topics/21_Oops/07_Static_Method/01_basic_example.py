"""
Static Method:
Definition: A static method does not take a reference to the class or instance (cls or self). It behaves like a regular function that belongs to the class's namespace.
Usage: Static methods are used to perform a task that is related to the class but doesn't need access to the class or instance attributes. They are isolated and don’t modify the class or instance state.

Note : 
Used for utility functions that belong to the class logically, but don’t need access to class or instance data.
"""

class Calculator:

    @staticmethod
    def addition(a, b):
        return a+b
    
    @staticmethod
    def subtraction(a, b):
        return a-b
    
    @staticmethod
    def multiplication(a, b):
        return a*b
    
    @staticmethod
    def division(a, b):
        return a/b
    
print(Calculator.addition(2, 5))
print(Calculator.subtraction(5, 2))
print(Calculator.multiplication(2, 2))
print(Calculator.division(10, 2))