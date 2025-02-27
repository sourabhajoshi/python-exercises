"""
Scenario:
You are building a software system to manage different types of vehicles in a fleet management system. The system needs to calculate the fuel efficiency (miles per gallon, MPG) for different vehicle types.

Car – The fuel efficiency of a car depends on its engine size and type.
Truck – The fuel efficiency of a truck depends on its weight and load capacity.
Motorcycle – The fuel efficiency of a motorcycle depends on the type of engine it has and the number of cylinders.
All vehicles have common properties like fuel tank capacity and mileage.

Task:
Define an abstract class Vehicle with an abstract method fuel_efficiency().
Implement concrete classes for Car, Truck, and Motorcycle that extend Vehicle and provide specific implementations for the fuel_efficiency() method.
The goal is to ensure that each class calculates fuel efficiency in its own way while keeping a common interface for all vehicles.
"""

from abc import ABC, abstractmethod

class Vehical(ABC):

    def __init__(self, fuel_tank_capacity, mileage):
        super().__init__()
        self.fuel_tank_capacity = fuel_tank_capacity
        self.mileage = mileage

    @abstractmethod
    def get_fuel_efficiancy():
        pass

class Car(Vehical):
    def __init__(self, fuel_tank_capacity, mileage, engine_size):
        super().__init__(fuel_tank_capacity, mileage) 
        self.engine_size = engine_size

    def get_fuel_efficiancy(self):
        return self.mileage/self.engine_size
    
class Truck(Vehical):
    def __init__(self, fuel_tank_capacity, mileage, weight, load_capacity):
        super().__init__(fuel_tank_capacity, mileage)
        self.weight = weight
        self.load_capacity = load_capacity

    def get_fuel_efficiancy(self):
        return self.mileage / (self.weight + self.load_capacity)
    
class Motorcycle(Vehical):
    def __init__(self, fuel_tank_capacity, mileage, num_cylinders):
        super().__init__(fuel_tank_capacity, mileage)
        self.num_cylinders = num_cylinders

    def get_fuel_efficiancy(self):
        return self.mileage / (self.num_cylinders * 2)
    
# Creating a Car object
car = Car(fuel_tank_capacity=15, mileage=25, engine_size=4)
print(car.get_fuel_efficiancy())

# Creating a Truck object
truck = Truck(fuel_tank_capacity=40, mileage=12, weight=5000, load_capacity=2000)
print(f"Truck fuel efficiency: {truck.get_fuel_efficiancy()} MPG")

# Creating a Motorcycle object
motorcycle = Motorcycle(fuel_tank_capacity=5, mileage=60, num_cylinders=2)
print(f"Motorcycle fuel efficiency: {motorcycle.get_fuel_efficiancy()} MPG")

