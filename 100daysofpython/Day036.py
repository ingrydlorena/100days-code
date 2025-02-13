'''
Day 36: Handle Exceptions I
Handle exceptions for division by zero.
'''
def division(num1, num2):
    try:
        div = num1 / num2 
        return f'{div}'
    except ZeroDivisionError:
        return 'An integer is not divisible by zero'
    
count1 = division(5,2)
count2 = division(4,2)
count3 = division(6,0)

print(f'{count1}\n{count2}\n{count3}')