'''
Day 14: Leap Year
Write a program that checks if a given input year is a leap year or not
'''
year = int(input('Input the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The year {year} is leap')
        else: 
            print(f'The year {year} is not leap')
    else:
        print(f'The year {year} is leap')
else:
    print(f'The year {year} is not leap')