'''
Day 57: Search algorithms
Implement searching algorithms (e.g., binary search).
'''

def binary_search(list, item):
    lower = 0
    high = len(list) - 1

    while lower <= high:
        middle = int((lower + high) / 2)
        guess = list[middle]
        if guess == item:
            return middle
        elif guess > item:
            high = middle - 1
        else:
            lower = middle + 1
    return None

my_list = [5, 9, 13, 23, 42, 58, 76, 77, 89, 101]
print (binary_search(my_list, 89))
print(binary_search(my_list, 2))
