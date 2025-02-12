'''
Day 19: Maximum in List
Write a function to find the maximum element in a list.
'''
def maximum(list_elements):
    return max(list_elements, key=len)


list1 = maximum(['a', 'to','planet', 'grow', 'growth'])
print(f'The max element of your list is {list1}')
    