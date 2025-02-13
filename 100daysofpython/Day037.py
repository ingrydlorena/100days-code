'''
Day 37: Handle Exceptions II
Handle exceptions for file not found.
'''
def read(file):
    try:
        not_found = open(file, 'r')
        print(not_found.read())
    except FileNotFoundError:
        print("File Not Found!")

test = read('new_file.txt')
teste = read("100daysofpython/file.txt")