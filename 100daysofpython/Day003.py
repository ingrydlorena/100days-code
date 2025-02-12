# Day 3 - Input and Output

'''
Basic Input and Output:
Write a program that reads a single input from the user and prints it to the console. For example, if the user enters their name, the program should output: ""Hello, {name}""

Handling Different Data Types:
Extend the program to read and print different types of inputs. Ensure the inputs are properly converted to their respective types and then printed. The program should ask the user to enter:

A string
An integer
A floating-point number
'''
name = input("What's your name? ")
age = int(input("What year you born? "))
height = input("What's your height? ")

print(f'Welcome {name} you have {2024 - age} years old')