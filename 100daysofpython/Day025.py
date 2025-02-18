'''
Day 25: Words frequency
Write a function to count the frequency of words in a sentence.
'''
def frequency(phrase):
    word_frequency = {}
    new_phrase = phrase.lower().split()
    for word in new_phrase:
        # Remove punctuation from each word (optional, if you want cleaner words)
        word = ''.join(e for e in word if e.isalnum())
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

setence = "The dog chased the cat, and the cat ran away"
count = frequency(setence)
print(count)
