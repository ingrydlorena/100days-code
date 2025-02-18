'''
Day 24: Words to sentence.
Write a function to convert a list of words into a sentence.
'''
def convert(list):
    phrase = ''
    for x in list:
        phrase += ' '+ x
    return phrase
list = ['Python', 'is', 'a', 'powerful', 'programming', 'language']
result = convert(list)
print(f'{result}')