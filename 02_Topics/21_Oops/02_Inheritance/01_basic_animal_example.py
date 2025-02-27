"""
Scenario: Animals
Let's say we have a base class Animal and two derived classes: Dog and Cat. Both Dog and Cat will inherit properties and methods from the base class Animal, but they can also have their own unique properties and methods.
"""

# Base class : Animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} make sound")

# Derived class: Dog (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Derived class : Cat (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Create objects of Dog and Cat and call instance method
dog = Dog("Buddy")
dog.speak()

cat = Cat("Rockey")
cat.speak()

animal = Animal("dummy")
animal.speak()

