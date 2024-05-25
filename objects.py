class Shape:
    def area(self):
        pass # this is an placeholder that allows us to create empty code
                #without causing errors.

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
    
import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
    
square = Square(5)
print("Area of the square", square.area())
circle = Circle(3)
print("Area of the circle ",circle.area())
triangle = Triangle(4,5)
print("Area of the triangle is ", triangle.area())