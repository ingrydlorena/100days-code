'''
Day 34: File operations: Append
Append data to an existing text file.
'''
file = open("file.txt", 'a')
file.write("##This text is new, don't existint in the old file")

file = open("file.txt", 'r')
print(file.read())