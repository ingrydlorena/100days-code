'''
Day 95: Metaclasses
Explore advanced topics like metaclasses.
'''

class MyGoalClass(type):
    def __new__(cls, name, bases, dct):
        dct['atributo_adicionado'] = "Valor Automático"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyGoalClass):
    pass

obj = MyClass()
print(obj.atributo_adicionado)