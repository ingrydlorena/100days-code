'''
Day 26: Anagram strings
Write a function check if two strings are anagrams.
'''

def anagram(word1,word2):
    for x in word1:
        if x in word2:
            return f'Is a anagram'
        else:
            return f'Is not a anagram'
    

word_1 = 'listen'
word_2 = 'silent'
word_3, word_4 = 'Music', 'museum'
word_5, word_6 = 'heart', 'Earth'

print(anagram(word_1, word_2))
print(anagram(word_3,word_4))
print(anagram(word_5,word_6))