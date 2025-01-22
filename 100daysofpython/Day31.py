'''
Day 31: Merge dictionaries.
Merge two dictionaries.
'''

name_students_A = {'Ingryd': 15, 
                   'Alon': 23, 
                   'Kiko': 54, 
                   'Joan': 12
                   }
name_students_B = {"Alice": 29,
                   "Bob": 34,
                   "Charlie": 25,
                    "Diana": 40
                    }
name_students_A.update(name_students_B)
new_dict = name_students_A,name_students_B.copy()

print(name_students_A)
print("Another way")
print(new_dict)