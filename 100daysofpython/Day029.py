'''
Day 29: Words frequency
Create a dictionary of words and their frequencies.
'''

def frequency(setence):
    dictionary = {}
    for word in setence.split():
        if  word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

word1 = 'The cat chased the mouse but the mouse escaped quickly'

print(frequency(word1))
