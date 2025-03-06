'''
Day 93: Code Optimization
Optimize code for performance (e.g., profiling, optimization techniques).
'''

# profiling com cprofile
import cProfile
def your_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

cProfile.run('your_function()')

# laços aninhados ineficientes

data = [1,2,3,4,5]
seen = set()
for item in data:
    if item in seen:
        print("Found match")
    seen.add(item)
