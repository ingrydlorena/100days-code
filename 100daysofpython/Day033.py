'''
Day 33: File operations: Write
Write data to a text file.
'''
another_file = open("another_file.txt", 'w')
another_file.write("Hello World! \nThis is another file, you can read the file one yet")

another_file = open("another_file.txt", 'r')
print(another_file.read())