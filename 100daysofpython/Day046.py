'''
Day 46: Class decorators
Use class decorators in Python.
'''
def my_decorator(cls):
  def __str__(self):
    return f'Welcome, {self.name} how cool you are {self.age}'

  cls.__str__ = __str__

  return cls


@my_decorator
class Person():
  def __init__(self,name,age):
    self.name = name
    self.age = age

obj = Person('Ingryd', 18)

print(obj)