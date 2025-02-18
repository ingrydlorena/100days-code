'''
Day 6: Functions and Code Reusability
Functions are reusable blocks of code that make programs easier to read, debug, and maintain. Learn how to define, call, and use functions effectively.

Simple Function
Define and call a simple function greet_user which takes name as a parameter. The function should print 'Hello, name' to the console.
'''
def greet_user(name):
    return f'Hello, {name}'

print(greet_user('Ingryd'))
'''
Default and Keyword Arguments
Update the greet_user function by adding a default value 'Guest' for the name parameter. When the function is called without an argument it should print 'Hello, Guest' to the console.
'''
def greet_user(name='Guest'):
    return f'Hello, {name}'

print(greet_user())
'''
Function with Return Values
Write a function that calculates and returns the area of a rectangle. The function should take length and breadth as the arguments.
'''
def rectangle(length, breadth):
    area = length * breadth
    return f'The area is {area}'

print(rectangle(5,6))
'''
Variable Scope
To understand the difference between local and global variables, follow these steps:
1. Define a global variable and print its value.
2. Write a function and assign a new value to the same varible inside the function and then print it.
3. Print the variable again outside the function again to observe that its value didn't change.
4. Write another function that access the global variable using the global keyword and then update its value.
5. Print the variable again outside the function. Verify that it's value now got updated.
'''

var_global = 'This is a global variable'
def example():
    var_global = 'This is a local variable'
    return f'{var_global}'

def another_example():
    global var_global
    var_global = 'now var_global is me'
print(var_global)
print(f"The local variable don't change the global variable: {example()}")
another_example()
print(f"Unless we call the global variable inside the function: {var_global}")

