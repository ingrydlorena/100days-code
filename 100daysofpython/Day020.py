'''
Day 20: Fibonacci sequence
Write a function to calculate the Fibonacci sequence up to a certain limit.
'''
def Fibonacci(quantity):
    sequence = []
    a, b = 0,1
    for x in range(quantity):
        sequence.append(a)
        a,b = b, a+b
    return sequence

fibonacci = Fibonacci(10)
print(f'Fibonacci sequence\n{fibonacci}')
    