from abc import ABC, abstractmethod

class Shape(ABC):

    # Abstract method to be implemented by every subclass
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    # Note : if i miss abstrct method draw() python will raise error message
    # TypeError: Can't instantiate abstract class Rectangle with abstract methods draw
    def draw(self):
        print("Drawing a Rectangle")


circle = Circle()
rectangle = Rectangle()

circle.draw()
rectangle.draw()
