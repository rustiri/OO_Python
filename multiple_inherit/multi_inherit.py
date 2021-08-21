# Explore how multiple inheritance works
# It will print the first order in the argument
# for example, if first arg in class C (B, A) => print out B first
# use print(C.__mro__) to inspect them

class A:
  def __init__(self):
      super().__init__()
      self.foo = "foo"
      self.name = "Class A"

class B:
  def __init__(self):
      super().__init__()
      self.bar = "bar"
      self.name = "Class B"


class C(A, B):
  def __init__(self):
    super().__init__()

  def showProps(self):
    print(self.foo)
    print(self.bar)
    print(self.name)


c = C()
c.showProps()
print(C.__mro__)
