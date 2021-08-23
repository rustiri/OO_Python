# This is an example of composition to create a complex object simpler
# Composition: build object out of another object, so it has relationship

# Define parent class
class Book:
  def __init__(self, title, price, author=None):
      self.title = title
      self.price = price

      self.author = author

      self.chapters = [] # To hold the chapter list information

  def addChapter(self, chapter):
    self.chapters.append(chapter) # Add chapter to the collections of chapters

  # method to calculate book page: the book can calculate its own count
  def getBookPageCount(self):
    result = 0
    # iterate each chapter
    for ch in self.chapters:
      result += ch.pageCount

    return result


# Define class Author to extracting author data
class Author:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  # define author string representation
  def __str__(self):
    return f"{self.fname} {self.lname}"

# Define class Chapter
class Chapter:
  def __init__(self, name, pageCount):
    self.name = name
    self.pageCount = pageCount



# Run the program
auth = Author("Leo", "Tolstoy")
b1 = Book("War And Peace", 39.0, auth)

b1.addChapter(Chapter("Chapter 1", 125))
b1.addChapter(Chapter("Chapter 2", 97))
b1.addChapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getBookPageCount())