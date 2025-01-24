'''
Day 40: Class hierarchy
Create a class hierarchy for different shapes (circle, square, triangle).
'''
class Shapes:
    def __init__(self, sides):
        self.sides = sides
        

    def __str__(self):
        if self.sides == 0:
            return f'You have a circle'
        elif self.sides == 4:
            return f'You have a square'
        elif self.sides == 3:
            return f'You have a Triangle'
        else:
            return 'Unknown shapes'
        
class Square(Shapes):
    def __init__(self,sides):
        super().__init__(sides)

    def area(self, side_size):
        self.area_square = side_size * side_size
        return f'The area of the Square is {self.area_square}'

class Triangle(Shapes):
    def __init__(self,sides):
        super().__init__(sides)
    
    def area(self, height, base):
        self.area_triangle = (height * base) / 2
        return f'The area of the Triangle is {self.area_triangle}'

class Circle(Shapes):
    def __init__(self,sides):
        super().__init__(sides)
    
    def area(self, radius):
        self.area_circle = 3.14 * radius ** 2
        return f'The area of the Circle is {self.area_circle}'
    
square = Square(4)
circle = Circle(0)
triangle = Triangle(3)
square1 = Square(8)


print(f'{square.area(3)}\n{triangle.area(5,8)}\n{circle.area(4)}\n{square1}')