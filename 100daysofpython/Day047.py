'''
Day 47: Stacks
Implement a stack data structure.
'''
class Stack():
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)

  def empty(self):
    return len(self.items) == 0

  def top(self):
    if not self.empty():
      return self.items[-1]
    else:
      return 'empty stack!'

  def pop(self):
    if not self.empty():
      return self.items.pop()
    else:
      return 'empty stack!'
  def lenght(self):
    if not self.empty():
      return len(self.items)
    else:
      return f'stack empty'



stack = Stack()

stack.push(5)
stack.push(9)
stack.push(4)
stack.push(3)
stack.push(7)
stack.push(1)

print(f'Top of the stack: {stack.top()}')
print(f'Removing an item from the stack: {stack.pop()}')
print(f'Current top of the stack: {stack.top()}')
print(f'The stack is empty? {stack.empty()}')
print(f'The lenght of the queue is {stack.lenght()}')
