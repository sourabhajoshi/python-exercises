"""
In this scenario, we'll demonstrate encapsulation in an employee management system. We'll create a class Employee that encapsulates employee details like salary, name, and position. We will use getter and setter methods to access and modify the private details of the employee.

The system will ensure that salary can only be modified in a controlled manner, and that it follows certain constraints, such as not allowing a salary increase if it's below a certain threshold.
"""

class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary # Private variable to store the salary (encapsulated)

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount < 3000:
            print("Salary increase must be at least $3000.")
        else:
            self.__salary = amount
            print(f"Salary updated to ${self.__salary}.")

    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.__salary}")


# Creating an employee object
employee1 = Employee("Sourabha", "Software Engineer", 5000)

# Display employee details
employee1.display_details()

# Trying to set an invalid salary (less than $3000)
employee1.set_salary(2500)

# Updating the salary with a valid amount
employee1.set_salary(8000)

# Display updated employee details
employee1.display_details()

# Accessing salary using the getter method
print(f"Employee's salary (using getter): ${employee1.get_salary()}")

