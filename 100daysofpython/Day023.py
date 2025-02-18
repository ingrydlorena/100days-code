'''
Day 23: List intersection
Write a function to find the intersection of two lists.
'''
def intersection(list1, list2):
    new_list = list(set(list1) & set(list2))
    return new_list

list1 = [1, 2, 3, 4, 5, 8, 7, 3]
list2 = [4, 5, 6, 7, 8, 4, 2, 8]
result = intersection(list1,list2)
print(f'The result is {result}')