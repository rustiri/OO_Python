# Example of using __eq__ and __lt__ magic methods


class Book:
  def __init__(self, title, author, price):
      super().__init__()
      self.title = title
      self.author = author
      self.price = price

  # TODO: use the __eq__ method to check for equality between two objects
  def __eq__(self, value):
    # throw an exception if we pass an object that it's not a book to compare against
    if not isinstance(value, Book):
      raise ValueError("Can't compare book to a non-book")

    return(self.title == value.title and self.author == value.author and self.price == value.price)

  # TODO: use the __ge__ method to establish >= relationship with another objects
  def __ge__(self, value):
    # throw an exception if we pass an object that it's not a book to compare against
    if not isinstance(value, Book):
      raise ValueError("Can't compare book to a non-book")

    return self.price >= value.price

  # TODO: use the __lt__ method to establish <= relationship with another objects
  def __lt__(self, value):
    # throw an exception if we pass an object that it's not a book to compare against
    if not isinstance(value, Book):
      raise ValueError("Can't compare book to a non-book")

    return self.price <= value.price


b1 = Book("War And Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in The Rye", "JD Salinger", 29.95)
b3 = Book("To Kill a Monkingbird", "Harper Lee", 24.95)
b4 = Book("War And Peace", "Leo Tolstoy", 39.95)

# TODO: check for equality
print(b1 == b4)
print(b1 == b2)

# TODO: check for greater and lesser value
print(b2 >= b1)
print(b2 <= b1)

# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
books.sort()
print([book.title for book in books])