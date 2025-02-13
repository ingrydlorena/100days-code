'''
100 Days of Python challenges
Day 49: Binary Search Tree
Implement a binary search tree.
'''
class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value is not None:
            self.left = None
            self.right = None
        else:
            self.left = None
            self.right = None

    def empty(self):
        return self.value is None
      
      
    def add(self, data):
        if self.empty():
            self.value = data
            self.left = None
            self.right = None

        # If the data is smaller, go to the left
        elif data < self.value:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.add(data)
        
        # If the data is greater, go to the right
        elif data > self.value:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.add(data)
    def traversal(self):
        values = []
        if self.left is not None:
            values += self.left.traversal()
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            values += self.right.traversal()
        return values


# Create a tree with root value 15       
root = Tree(25)

# Insert some values into the tree
root.add(5)
root.add(8)
root.add(15)
root.add(25)
root.add(55)

print(root.traversal())