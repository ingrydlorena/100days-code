'''
Day 50: Linked List
Implement a linked list.
'''
class Node:
    def __init__(self,data):
        self.data = data #Store data
        self.next = None # Pointer to the next node

class Linkedlist:
    def __init__(self):
        self.head = None # create an empty list
        
    def add(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next: # Traverse to the last node
                last = last.next
            last.next = new_node # Link the new node

    def remove(self,key):
        current = self.head

        if current and current.data == key:
            self.head = current.next #move the head to the next node
        
        # Search for the node to remove
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # is the key was not found
        if current is None:
            print(f'Node with value {key} not found')
            return
        
        # Remove the node by updating the ´revious node's next
        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end= " -> ")
            current = current.next
        print("None")

lk = Linkedlist()
lk.add(15)
lk.add(75)
lk.add(23)
lk.add(72)
lk.add(12)
lk.add(3)
print(f'Original list:')
lk.display()
lk.remove(75)
print(f'List after removing 75:')
lk.display()
print(f'search error:')
lk.remove(1)
lk.display()