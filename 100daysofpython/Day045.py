'''
Day 45: Polymorphism
Implement polymorphism with a shape area calculator.
'''
class Square():
  def __init__(self, side):
    self.sides = side
    self.area = self.side * self.side
  def __str__(self):
    return f'The area of its square is {self.area}'
class Triangle():
  def __init__(self, base, height):
    self.base = base
    self.height= height
    self.area = (height * base) / 2
  def __str__(self):
    return f'The area of your triangle is {self.area}'
class Circle():
  def __init__(self, radius):
    self.radius = radius
    self.pi = 3.14
    self.area = self.pi * self.radius ** 2
  def __str__(self):
    return f'The area of your circle is {self.area}'

square1 = Square(5)
triangle1 = Triangle(5,7)
circle1 = Circle(4)

for item in (square1,triangle1,circle1):
  print(item.__str__())