'''
Day 35: File operations
Calculate the average of numbers in a text file.

For this challenge you need create a file .txt with numbers
'''

def average(file_path):
    file = open(file_path, 'r')
    numbers = []

    for line in file:
        for word in line.split():
            try:
                num = float(word)
                numbers.append(num)
            except ValueError:
                continue
    
    file.close()

    if numbers:
        total = sum(numbers)
        count = len(numbers)
        average_value = total / count
        return average_value
    else:
        return "No numbers found in the file"

file = 'numbers.txt'
calculate_average = average(file)
print(f"The average is: {calculate_average}")
            
