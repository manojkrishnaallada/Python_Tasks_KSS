"""A graphics application needs to calculate the area of different shapes. Create classes 
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate 
polymorphism by calling the same method for different objects. """

class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

class Rectangle:
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w

class Triangle:
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h

for shape in [Circle(5), Rectangle(4, 6), Triangle(3, 8)]:
    print(type(shape).__name__, "area =", shape.area())
