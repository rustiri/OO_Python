# Using data classes to represent data objects
# To convert a book class to a version that uses data class: import data class (only on python 3.7 and above)
from dataclasses import dataclass

@dataclass # to indicate that book class is a data class
class Book:
  title: str
  author: str
  pages: int
  price: float

  def bookInfo(self):
    return f"{self.title}, by {self.author}"

# Create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in The Rye", "JD Salinger", 234, 29.95)


# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)

# TODO: change some fields
b1.title = "Anna Karenina"
b1.pages = 864

print(b1.bookInfo())