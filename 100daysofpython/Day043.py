'''
Day 43: Encapsulation
Implement encapsulation in a class.
'''

class Protected:
    def __init__(self, name, age, adress):
        self.name = name
        self._age = age # _ determines whats is protected
        self._adress = adress
class Display(Protected):
    def display_information(self):
        return f'You name is {self.name} and your age is {self._age} and you live in {self._adress}'

obj = Display('Alon', 17, 'NY')
print(obj.display_information())

class Private:
    def __init__(self, salary):
        self.__salary = salary # __ determines whats is private
    def salary(self):
        return self.__salary # Acess through public method
    
private_obj = Private(7500)
print(private_obj.salary()) #Works
# print(private_obj.__salary) Raise AttributeError

