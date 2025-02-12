'''
Day 7: Temparature Conversion
1. Write a program to convert temperature from Celsius to Fahrenheit. 2. Write a program to convert temperature from Fahrenheit to Celsius
'''
Celsius = float(input('What is the temperature in celsius: '))
formula = Celsius * (9/5) + 32
print(f'The Fahrenheit is {formula: .2f}')