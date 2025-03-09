
cdef int add(int a, int b):
    return a + b

# Python-accessible function
def py_add(int a, int b):
    return add(a, b)

# Optimized factorial function
def factorial(int n):
    cdef int i, result = 1
    for i in range(1, n + 1):
        result *= i
    return result
