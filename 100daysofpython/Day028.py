'''
Day 28: Reverse words
Reverse words in a sentence.
'''
word1 = 'The sun dipped below the horizon casting a warm glow across the quiet beach'

def reverse(setence):
    new_setence = ''
    old_setence = setence.split()
    for x in old_setence:
        new_word = x[::-1]
        new_setence += new_word + ' '
    return new_setence
        

print(reverse(word1))