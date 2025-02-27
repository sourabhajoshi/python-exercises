"""
Class Method:
Definition: A class method is a method that is bound to the class and not the instance of the class. It takes the class itself as the first argument (usually named cls), not the instance (self).
Usage: Class methods are used to operate on the class state or to create alternative constructors for the class.
Key Points:
Defined using the @classmethod decorator.
Takes cls (the class) as the first argument.
Can modify class-level variables or access other class methods.
"""

class World:
    population = 0

    def __init__(self, country_name):
        self.country_name = country_name
        World.increment_population() # increment population when new country created

    @classmethod
    def increment_population(cls):
        cls.population += 1

    @classmethod
    def get_population(cls):
        return cls.population
    
# create instnce

country1 = World("India")
print(country1.get_population())


country2 = World("USA")
print(country2.get_population())