'''
Day 61: Dynamic Programming
Implement dynamic programming for Fibonacci.
'''

def Fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = Fibonacci(n - 1, memo) + Fibonacci(n-2, memo)
    return memo[n]

fibonacci = Fibonacci(15)
print(f'Fibonacci sequence\n{fibonacci}')
