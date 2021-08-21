# Using Abstract Base Classes to enforce class constrains

# Example of creating drawing program that let's the user create different kind 2D shape
# We want the program to be extensible to that new shape type can be added
# Use ABC module from standard library
from abc import ABC, abstractmethod

# Define Base/Parent class
class GraphicShape(ABC):
  def __init__(self):
    super().__init__()

  # use abstractmethod decorator that indicates that calArea method is an abstract method
  # this tells python that there's no implementation base class 
  # and each sub class has to override this method
  @abstractmethod 
  def calcArea(self):
    pass


# Define sub class that inherits parent class
class Circle(GraphicShape):
  def __init__(self, radius):
    self.radius = radius

  def calcArea(self):
    # circle area =  pie times radius square
    return 3.14 * (self.radius ** 2)

# Define another sub class that inherits parent class
class Square(GraphicShape):
  def __init__(self, side):
    self.side = side
  
  def calcArea(self):
    # Square = length * width
    return self.side * self.side

# Run the program
c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
