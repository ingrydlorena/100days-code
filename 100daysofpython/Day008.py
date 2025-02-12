'''
Day 8: Simple Calculator
Create a simple calculator program that can add, subtract, multiply, and divide two integers
'''
def calculator(num1,num2, sign):
    if sign == '+' :
        add = num1 + num2
        return f'The result is {add}'
    elif sign == "-":
        subtract = num1 - num2
        return f'The result is {subtract}'
    elif sign == '*':
        multiply  = num1 * num2
        return f'The result is {multiply}'
    elif sign == '/':
        divide = num1 // num2
        return f'The result is {divide}'
formula1 = calculator(5,8,'+')
formula2 = calculator(6,4,'-')
formula3 = calculator(2,6,'*')
formula4 = calculator(9,7,'/')
print(f'{formula1}\n{formula2}\n{formula3}\n{formula4}')
