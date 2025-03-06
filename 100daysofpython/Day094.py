'''
Day 94: Decorators and descriptors
Experiment with decorators and descriptors.
'''
def my_decorator(func):
    def wrapper():
        print("Before running the function")
        func()
        print("After running the function")
    return wrapper

@my_decorator
def my_function():
    print("My function was been executed")

my_function()