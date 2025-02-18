'''
Day 44: Class definition
Create a class for a book with attributes like title and author.
'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self._year = year
    def __str__(self):
        return f'Title book: {self.title}\nAuthor: {self.author}\nYear: {self._year}'

mybook1 = Book('1984','George Orwell', 1949)
mybook2 = Book('To kill a mockingbird', 'Harper Lee', 1960)

print(f'{mybook1}\n{mybook2}')