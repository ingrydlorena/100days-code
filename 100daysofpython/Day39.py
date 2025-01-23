'''
Day 39: Class Object
Create a class for a simple car with methods like start and stop.
'''
class Car:
    def __init__(self, km_start, km_final, speed):
        self.speed = speed
        self.speed_limit = 60
        self.start = km_start
        self.end = km_final
    def begin(self):
        if self.speed <= self.speed_limit:
            return f'Safe speed'
        else:
            return f'You need calm down the speed limit is {self.speed_limit}'
    def stop(self):
        if self.start == self.end:
            return 'You did! Welcome to your destine'
        elif self.start > self.end:
            return 'You passed your destin, come back'
        else:
            return "You didn't reach your destination"

car1 = Car(25,120,25)
print(car1.begin())
print(car1.stop())
car2 = Car(120,120,50)
print(car2.begin())
print(car2.stop())
car3 = Car(200,160,65)
print(car3.begin())
print(car3.stop())
