'''
Day 74: Natural language processing
Perform natural language processing tasks (e.g., sentiment analysis).
'''

from deep_translator import GoogleTranslator

origin = "auto"
destiny = 'en'

text = input("Write a texto to translate: ")

translation = GoogleTranslator(source=origin, target=destiny).translate(text)

print(f"Translation: {translation}")