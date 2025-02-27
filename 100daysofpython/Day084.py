'''
Day 84: GUI using Tkinter
Build a calculator app with a GUI using Tkinter.
'''
import tkinter as tk


def calculate(operation):
    global expression

    if operation == 'C':
        expression = ''
    elif operation == '<-':
        expression = expression[:-1]
    else:
        if expression == '' and operation in ['+', '-', '*', '/']:
            return
        expression += operation
    
    label_text.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        label_text.set(result)
        expression = result
    except:
        label_text.set("Error")
        expression = ""

root = tk.Tk()
root.title("Calculator")

expression = ''
label_text = tk.StringVar()

label = tk.Label(root, textvariable=label_text, font=("Arial", 30), bg="white", width=15, height=2)
label.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("C", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("<-", 4, 2), ("*", 4, 3),
    ("/", 5, 0), ("=", 5, 1)
]

for text, row, col in buttons:
    if text == '=':
        button = tk.Button(root, text=text, command=action, font=("Arial", 30), width=5, height=2)
    else:
        action = lambda x=text: calculate(x) 
        button = tk.Button(root, text=text, command=action, font=("Arial", 30), width=5, height=2)
    button.grid(row=row, column=col)


button = tk.Button(root, text='=', command=evaluate, font=("Arial", 30), width=11, height=2)
button.grid(row=5, column=1, columnspan=2)


root.mainloop()
