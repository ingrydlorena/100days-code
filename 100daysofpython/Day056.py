'''
Day 56: Sorting algorithms
Implement sorting algorithms (e.g., bubble sort, merge sort).
'''
def partition(array,low,high):
    pivot = array[high] # choose the pivot element
    lower = low - 1 # pointer for the smaller element

    # Traverse through all elements, compare each with pivot
    for num in range(low,high):
        if array[num] <= pivot: # if current element is smaller or equal to pivot
            lower += 1 # increment the smaller element index
            array[lower], array[num] = array[num], array[lower] # swap elements

    # place the pivot element in the correct position
    array[lower+1], array[high] = array[high], array[lower+1]
    return lower+1 # return pivot's final position

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) -1 # set high to the last index if not provided

    if low < high:
        pivot_index = partition(array, low, high)  # partition the array
        quicksort(array,low ,pivot_index-1) # sort the left part
        quicksort(array, pivot_index+1, high) # sort the right part
        
my_array = [8, 15, 3, 12, 6, 19, 1, 9, 5, 13, 10, 18, 2, 14, 17, 4, 7, 11, 16, 20]
quicksort(my_array)
print(my_array)