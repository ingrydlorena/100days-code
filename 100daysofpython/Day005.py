'''
Conditional Statements and Loops
If-else Statements
Write a program that takes an integer as input and checks if it's even or odd.
'''
number = int(input('Enter a number to see if is even or odd '))
# The calculation to find the remainder of the division
rest = number % 2
if rest == 0:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')
'''
Write a program that takes an age as input and determines if the person is a child, teenager, adult, or senior citizen.
'''
age = int(input('Enter your age: '))
if age <= 12:
    print('Your are a child')
elif age <= 19:
    print('You are a teenager')
elif age <= 64:
    print('You are a adult')
elif age >= 65:
    print('You are a senior citizen')
else:
    print('Enter a valid age')
'''

Nested If-else Statements
Using nested if-else, write a program that takes three numbers as input and determines the largest among them.
'''
num1 = int(input('Enter the number one: '))
num2 = int(input('Enter the number two: '))
num3 = int(input('Enter the number three: '))

if num1 >= num2:
    if num1 >= num3:
        print(f'The number: {num1} is the largest among them')
    else: 
        print(f'The number: {num3} is the largest among them')
else:
    if num2 >= num3:
        print(f'The number {num2} is the largest among them')
    else:
        print(f'The number: {num3} is largest among them')
'''
For Loop
Write a program to calculate the sum of all numbers up to the given input number.
'''
num1 = int(input('Enter the number: '))
sum = 0
for num in range(1,num1 + 1):
    sum += num
print(f'The sum is: {sum}')
'''
While Loop
Write a program to calculate the factorial of a given number.
'''
num1 = int(input(f'Enter the number: '))
result = 1
while num1 > 1:
    result *= num1
    num1 -= 1
print(f'The factorial is: {result}')
