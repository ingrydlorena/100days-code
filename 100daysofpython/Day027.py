'''
Day 27: Longest word
Find the longest word in a sentence.
'''
def longest(setence):
    setence_clean = setence.split()
    longest_word = max(setence_clean, key= len)
    return longest_word
        

setence1 = "Bright stars illuminated the quiet night sky"
setence2 = "She danced gracefully under the glowing moonlight"

print(f'The longest word in setence one is: {longest(setence1)}')
print(f'The longest word in setence two is: {longest(setence2)}')