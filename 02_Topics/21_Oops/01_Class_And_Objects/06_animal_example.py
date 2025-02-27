class Dog:

    species = "Canine" # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute

    """
    __str__ method in Python allows us to define a custom string representation of an object. By default, when we print an object or convert it to a string using str(), Python uses the default implementation, which returns a string
    """
    def __str__(self):
        return f"Dog name is {self.name} and age {self.age}."
    
dog = Dog("Rockey", 5)

print(dog) #Dog name is Rockey and age 5.
    

