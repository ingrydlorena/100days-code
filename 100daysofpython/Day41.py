'''
Day 41: Inheritance
Implement inheritance between classes.
'''
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def __str__(self):
        return f'Welcome {self.first_name}'

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def passed(self, score):
        self.studante_score = score
        if self.studante_score > 5:
            return f'You passed'
        else:
            return f'You not passed, you score is {self.studante_score}'
        

        
student1 = Student('Emily','Parker')
print(f'{student1.passed(6)}')
student2 = Student('Jaxon', 'Flynn')
print(f'{student2.passed(4)}')
student3 = Student('Olivia', 'Matthews')
print(f'{student3.passed(10)}')