class Animal:
    def speak(self):
        print("Animal speak..!")

class Dog(Animal):
    def speak(self):
        print("Dog bark..!")

class Cat(Animal):
    def speak(self):
        print("Cat meow..!")

animals = [ Dog(), Cat()]

for animal in animals:
    animal.speak()