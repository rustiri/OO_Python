# Example on how to use attribute access method


class Book:
  def __init__(self, title, author, price):
      super().__init__()
      self.title = title
      self.author = author
      self.price = price
      self.discount = 0.1

  # The __str__ function is used to return a user-friendly string
  # representation of the object
  def __str__(self):
    return f"The book title: {self.title} by {self.author}, costs {self.price}"

  # TODO: __getattribute__ called when an attr is retrieved. Don't directly access
  # the attr name otherwise a recursive loop is created
  def __getattribute__(self, name):
    # automatically apply the discount whenever the price attribut is retrieved
    if name == "price":
      # get the value of current price by calling super class version of get attribute
      p = super().__getattribute__("price")
      d = super().__getattribute__("discount")
      return p - (p * d)

    return super().__getattribute__(name)

  # TODO: __setattr__ called when an attribute value is set.
  # Don't set it directly here otherwise a recursive loop cause a crash 
  def __setattr__(self, name, value):
    if name == "price":
      if type(value) is not float:
        raise ValueError("The price attr must be a float")

    return super().__setattr__(name, value)

  # TODO: __getattr__ called when __getattribute__ lookup fails (i.e. doesn't exist or throw an exception). 
  # pretty much generate attribute on the fly with this method
  def __getattr__(self, name):
    return name + " is not here!"

b1 = Book("War And Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in The Rye", "JD Salinger", 29.95)
b3 = Book("To Kill a Monkingbird", "Harper Lee", 24.95)
b4 = Book("War And Peace", "Leo Tolstoy", 39.95)

b1.price = 38.95
print(b1)

b2.price = float(40)
print(b2)

print(b1.randomprop)