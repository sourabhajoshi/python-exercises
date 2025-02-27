"""
Scenario: Vehicle Management System
Let’s imagine a vehicle management system where we need to manage different types of vehicles. All vehicles have common attributes like make, model, year, and color, but each type of vehicle also has some unique attributes. For example, a Car has the number of doors, a Bike has the type of handlebar, and a Truck has the cargo capacity.

We will create a base class Vehicle with common attributes and then create derived classes Car, Bike, and Truck that extend the base class and add unique properties for each type of vehicle.

In this updated version, we’ll include:
Car: Checks if the number of doors is valid (between 2 and 5).
Truck: Converts cargo capacity from tons to kilograms when displaying details.
Bike: Determines if the bike is suitable for long-distance rides based on the handlebar type.
"""

class Vehical:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_detailes(self):
        print(f"make : {self.make}")
        print(f"model : {self.model}")
        print(f"year : {self.year}")
        print(f"color : {self.color}")
    

class Bike(Vehical):
    def __init__(self, make, model, year, color, handlebar):
        super().__init__(make, model, year, color)    
        self.handlebar = handlebar


    def is_suitable_for_long_distance(self):
        """Determines if the bike is suitable for long-distance rides."""
        suitable_handlebars = ["Drop", "Touring"]
        if self.handlebar in suitable_handlebars:
            return True
        else:
            return False
        
    def display(self):
        super().display_detailes()
        print(f"handlebar : {self.handlebar} and sutable for long drive : {self.is_suitable_for_long_distance()}")
   
class Car(Vehical):
    def __init__(self, make, model, year, color, no_of_doors):
        super().__init__(make, model, year, color)    
        self.no_of_doors = no_of_doors

    def display(self):
        super().display_detailes()
        print(f"no_of_doors : {self.no_of_doors}")
        if self.is_number_of_doors_valid():
            print("valid doors")
        else:
            print("Not valid doors")

    def is_number_of_doors_valid(self):
        """ return true if no of doors are 2 to 5"""
        if self.no_of_doors > 1 and self.no_of_doors < 6:
            return True
        else:
            return False

class Truck(Vehical):
    def __init__(self, make, model, year, color, cargo_capacity):
        super().__init__(make, model, year, color)    
        self.cargo_capacity = cargo_capacity

    def convert_ton_to_kg(self):
        return (self.cargo_capacity * 1000)

    def display(self):
        super().display_detailes()
        print(f"cargo_capacity : {self.cargo_capacity} tonn or {self.convert_ton_to_kg()} kg")


# create an object instance

print("Bike Details : ")
bike = Bike("Honda", "Deo", "2016", "Black-White", "Flat")
bike.display()
print("-" * 60)

print("Car Details : ")
car = Car("Honda", "City", "2016", "Red", 4)
car.display()
print("-" * 60)

print("Truck Details : ")
truck = Truck("Tata", "Heavy-Truck", "2022", "Orange", 5)
truck.display()