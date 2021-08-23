# Using postinit function in data classes
# To convert a book class to a version that uses data class: import data class (only on python 3.7 and above)
from dataclasses import dataclass

@dataclass # to indicate that book class is a data class
class Book:
  title: str
  author: str
  pages: int
  price: float

  # TODO: the __post_init__ function lets us customize additional property
  # after the object has been initialized via built-in __init__
  def __post_init__(self):
    self.description = f"{self.title}, by {self.author}, {self.pages} pages"

# Create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in The Rye", "JD Salinger", 234, 29.95)


# TODO: use the description attribute
print(b1.description)
print(b2.description)