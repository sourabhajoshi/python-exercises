# define a class
class Car:
    # Constructor method to initialize the object with make and model
    # Instance attribute
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Instance method to display car details
    def display(self):
        print(f"Car make : {self.make} and model is {self.model}")

# create an object
my_car = Car("Tata", "Tiago")
my_car.display()