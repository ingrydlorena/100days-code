'''
Day 55: Iterable class.
Implement a custom iterable class.
'''

class Numbers:
    def __init__(self,start):
        if start % 2 != 0:
            start += 1
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 50:
            x = self.current
            self.current += 2
            return x
        else:
            raise StopIteration
        
mynumbers = Numbers(2)
for number in mynumbers:
    print(number)