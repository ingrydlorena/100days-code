'''
Day 54: List comprehensions
Use list comprehensions to filter and transform lists.
'''

names = [
    "Alexander", "Olivia", "Benjamin", "Isabella", "William", 
    "Emma", "Noah", "Sophia", "Liam", "Ava", 
    "James", "Mia", "Oliver", "Charlotte", "Elijah", 
    "Amelia", "Lucas", "Harper", "Ethan", "Evelyn", "Bradley", "Brooke"
]

name_A = []
name_B = [name.capitalize() for name in names if name.lower()[0] == 'b']

for name in names:
    name = name.lower()
    if 'a' in name[0]:
        name_A.append(name.capitalize())

print(name_A)
print(name_B)