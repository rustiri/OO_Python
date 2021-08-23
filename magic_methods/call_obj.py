# Example of using __call__  magic methods


class Book:
  def __init__(self, title, author, price):
      super().__init__()
      self.title = title
      self.author = author
      self.price = price

  # TODO: use the __str__ method to return a string, intended to display to the user
  def __str__(self):
    return f"{self.title} by {self.author}, costs {self.price}"

  # TODO: the __call__ method can be used to call the object like a function
  def __call__(self, title, author, price):
      self.title = title
      self.author = author
      self.price = price


b1 = Book("War And Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in The Rye", "JD Salinger", 29.95)

# TODO: call the object as if it were a function
print(b1)
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)