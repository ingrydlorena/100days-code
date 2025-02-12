'''
Day 22: List duplicates
Write a function to remove duplicates from a list.
'''
def remove_duplicates(list_elements):
    new_list = set(list_elements)
    return new_list

list1 = remove_duplicates(['apple', 'banana', 'grape', 'apple', 'orange', 'grape', 'mango', 'banana'])
print(f'Your list without duplicates {list1}')