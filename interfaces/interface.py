# This is an example to use a combination of multiple inheritance and abstract base classes
# to implement a type of programming feature called interface (kinda promise)
# For example if we want our concrete shape object to be able to present themselve as json, we need
# to create another base class jsonify 

# Using Abstract Base Classes to enforce class constrains

# Example of creating drawing program that let's the user create different kind 2D shape
# We want the program to be extensible to that new shape type can be added
# Use ABC module from standard library
from abc import ABC, abstractmethod

# Define Base/Parent class
class JSONify(ABC):
  # define a single abstract method to json
  @abstractmethod
  def toJSON(self):
    pass

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


# Define sub class that inherits multiple parent class
class Circle(GraphicShape, JSONify):
  def __init__(self, radius):
    self.radius = radius

  def calcArea(self):
    # circle area =  pie times radius square
    return 3.14 * (self.radius ** 2)

  # override method to provide a string that represent json format
  def toJSON(self):
    return f"{{\"Circle\" : {str(self.calcArea())} }}"

# Run the program
c = Circle(10)
print(c.calcArea())
print(c.toJSON())
