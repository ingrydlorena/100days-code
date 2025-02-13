'''
Day 30: Sort a list
Sort a list of numbers in ascending order.
'''
def sort(numbers_list):
    numbers_list.sort()
    return numbers_list

numbers = [42, 7, 19, 53, 3, 88, 21, 14, 65, 30]
print(sort(numbers))