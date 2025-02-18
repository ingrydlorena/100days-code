'''
Day 17: Number of vowels in a string
Write a function to count the number of vowels in a string.
'''
def vowels(word):
    the_word = word
    vowels = 0
    for x in the_word.lower():
        if x in 'AEIOUaeiou':
            vowels += 1
        else:
            pass
    return f'Your word have {vowels} vowels'

word1 = vowels('Car')
word2 = vowels('House')
word3 = vowels('Computer')
word4 = vowels('Crypt')
word5 = vowels('Towel')

print(f'{word1}\n{word2}\n{word3}\n{word4}\n{word5}')