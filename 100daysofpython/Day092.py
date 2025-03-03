'''
Day 92: Design patterns
Study and implement design patterns in Python.
'''

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        return None
    

class EuropeanPlug:
    def voltage(self):
        return '220v'

class USPlug:
    def voltage(self):
        return '110v'
    

class Adapter:
    def __init__(self, plug):
        self.plug = plug
    def voltage(self):
        return f"Converted: {self.plug.voltage()}"

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observers in self._observers:
            observers.update(message)

class Observer:
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"Email: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"SMS: {message}")

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print("Singleton Test:", s1 is s2)

    animal = AnimalFactory.get_animal("dog")
    print("Factory Test:", animal.speak())

    plug = EuropeanPlug()
    adapter = Adapter(plug)
    print("Adapter Test:", adapter.voltage())

    subject = Subject()
    subject.attach(EmailNotifier())
    subject.attach(SMSNotifier())

    subject.notify("New update available!")
