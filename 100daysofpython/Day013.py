'''
Day 13: Largest of three numbers.
Write a program to find the largest of three numbers.
'''

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter a third number: '))

if num1 > num2 and num1 > num3:
    print(f'Number one is the largest ({num1})')
elif num2 > num1 and num2 > num3:
    print(f'Number two is the largest ({num2})')
elif num3 > num1 and num3 > num2:
    print(f'The number three is the largest ({num3})')
else:
    print("Don't have a largest number")