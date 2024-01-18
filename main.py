from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def display_info(self):
        print(f"The shape '{type(self).__name__}' is of '{self.color}' color and it's area is '{self.area()}'.")

    def check_value(self, value):
        if value < 0 or not isinstance(value, (int,float)):
            raise ValueError("Value can't be negative or a string. Can only be int or float.")
        else:
            pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.check_value(radius)
        self.radius = radius


    def area(self):
        return "{:.3f}".format(pi*(self.radius**2))
        # return round(pi*(self.radius**2),3) # using round function


circle = Circle("blue", 4)
circle.display_info()

circle2 = Circle("yellow", 8)
circle2.display_info()


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.check_value(width)
        self.width = width
        self.check_value(width)
        self.height = height

    def area(self):
        return self.width*self.height


rect1 = Rectangle("white",5,6)
rect1.display_info()
rect2 = Rectangle("black",5.6,7.9)
rect2.display_info()


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.check_value(base)
        self.base=base
        self.check_value(height)
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

tri1 = Triangle("pink", 9,14.9)
tri1.display_info()




