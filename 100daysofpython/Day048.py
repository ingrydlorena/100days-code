'''
Day 48: Queues
Implement a queue data structure.
'''
class Queue:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def empty(self):
        return len(self.items) == 0
    def first(self):
        if not self.empty():
            return self.items[0]
        else:
            return f'Queue empty!'
    def pop(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            return f'Queue empty!'
    def lenght(self):
        if not self.empty():
            return len(self.items)
        else:
            return f'Queue empty'

queue = Queue()
queue.add(5)
queue.add(8)
queue.add(9)
queue.add(7)
queue.add(2)

print(f'Top of the queue: {queue.first()}')
print(f'Removing an item from the queue: {queue.pop()}')
print(f'Current top of queue: {queue.first()}')
print(f'The queue is empty? {queue.empty()}')
print(f'The lenght of the queue is {queue.lenght()}')