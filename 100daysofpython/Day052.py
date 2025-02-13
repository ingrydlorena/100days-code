'''
Day 52: Hash Table
Implement a hash table.
'''
# This code is just to understand the process, python already has an implemented hashtable {dict}

class HashTable:
    def __init__(self,size):
        # Initialize the hash table with a given size
        self.size = size
        self.table = [[] for _ in range(size)] # Create a list of empty lists (buckets)

    def _hash(self, key):
        # Hash function to map the key to an index
        return hash(key) % self.size
    
    def insert(self, key, value):
        # Insert key-value pair into the hash table
        index = self._hash(key)
        # Check if the jey already exists, and update its value if it does
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return 
        # If the key doesn't exist, append a new key-value pair
        self.table[index].append((key,value))

    def search(self, key):
        # Search for a key in the hash table and return its value
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None #Return None if the key not found
    
    def delete(self, key):
        # Delete a key-value pair from the hash table
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False # Return False if key not found

# Example usage
hash_table = HashTable(10)

# Insert key-value pairs
hash_table.insert("banana", 2)
hash_table.insert("orange", 5)
hash_table.insert("melon", 3)
hash_table.insert("grape", 12)
print("banana:", hash_table.search("banana"))
print("orange", hash_table.search("orange"))
print("melon", hash_table.search("melon"))
print("grape:", hash_table.search("grape"))
print("apple:", hash_table.search("apple"))

hash_table.delete("banana")
print("banana after deletion:", hash_table.search("banana"))


'''Other way'''
def dicts(fruit):
    grocery = {}
    for x in fruit:
        value = input(f"What is the value for {x}: ")
        grocery[x] = value
    return grocery

fruits = ['banana', 'apple', 'mango']
print(dicts(fruits))