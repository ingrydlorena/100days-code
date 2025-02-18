'''
Day 15: Factorial
Write a function to calculate the factorial of a number.
'''

def factorial(num):
    result = 1
    for x in range(1,num +1):
        result *= x
    return result
print(f'The factorial is {factorial(5)}')
