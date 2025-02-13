'''
Day 16: Palindrome String
Write a function to check if a given string is a palindrome.
'''
def palindrome(word):
    the_word = word
    if the_word.upper() == the_word[::-1].upper():
        return f"It's a palindrome"
    else:
        return f'Not a palindrome'

word1 = palindrome('Civic')
word2 = palindrome('Mom')
word3 = palindrome('Place')
word4 = palindrome('Deified')
word5 = palindrome('Level')

print(f'{word1}\n{word2}\n{word3}\n{word4}\n{word5}')