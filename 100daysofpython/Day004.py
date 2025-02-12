# Day 4 - Basic Operators and Expressions
'''
Write a program to perform the following arithmetic operations using two numbers:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulus (%)
Exponentiation (**)
''' 

# use the function int() to turn input str to float
num1 = float(input('Number one: ')) 
num2 = float(input('Number two: '))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
int_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

 # use the string format modifier :.0f to remove the cases after the comma
print(f'the result of addition is: {addition: .0f}')
print(f'the result of subtraction is: {subtraction: .0f}')
print(f'the result of multiplication is: {multiplication: .0f}')
print(f'the result of divison is: {division}')
print(f'the result of integer division is: {int_division: .0f}')
print(f'the result of modulus is: {modulus: .0f}')
print(f'the result of exponentiation is: {exponentiation: .0f}')


'''
Write a program to compare two numbers using the following operators:
Equal to (==)
Not equal to (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)
'''
num1 = int(input('Input the first integer: '))
num2 = int(input('Input the second integer: '))

print(f'Number one is equal to number two? {num1 == num2}')
print(f'Number one is greater than number two? {num1 > num2}')
print(f'Number one is less than number two? {num1 < num2}')
print(f'Number one is not equal to number two? {num1 != num2}')


'''
Write a program that evaluates the following between 2 booleans(True or False):
Logical AND (and)
Logical OR (or)
Logical NOT (not)
'''

numbers = [0, 5, 8, 6, 7, 2]

print(f'have the number 7 AND the number 4? {7 and 4 in numbers}')
print(f'Select the number 5 or the number 8? {5 or 8 in numbers}')
print(f'not have the number one in the list of numbers? {1 not in numbers}')  