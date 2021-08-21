# Example of inheritance in Object Oriented Python

# Define parent class
class Publication:
  def __init__(self, title, price):
      self.title = title
      self.price = price

# Define class that inherits from parent class
class Periodical(Publication):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price) # initialize super class
    self.period = period
    self.publisher = publisher

# Define Book class that inherits from Publication parent class
class Book(Publication):
  def __init__(self, title, author, pages, price):
    super().__init__(title, price)
    self.author = author
    self.pages = pages

# Define Magazine class that inherit from Periodical class
class Magazine(Periodical):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price, period, publisher)

# Define Newspaper class that inherit from Periodical class
class Newspaper(Periodical):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price, period, publisher)
    

# Run python
b1 = Book("When Ghost Speak", "Mary Ann Winkowski", 300, 39.18)
n1 = Newspaper("NY Times", 6.0, "Daily", "New York Times Company")
m1 = Magazine("Scientific American", 5.99, "Monthly", "Springer Nature")

print(b1.author)
print(n1.publisher)
print(b1.price, n1.price, m1.price)
