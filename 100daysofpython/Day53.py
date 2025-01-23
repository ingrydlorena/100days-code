'''
Day 53: Set Operations
Perform various operations on sets (union, intersection, etc.).
'''

set1 = {"a", "b", "d", "e"}
set2 = {"e", "f", "g", "h"}
set3 = {1, 6, 3, 7, 5, 4}
set4 = {8, 6, 4, 3, 89, 2}

union = set1 | set2
intersection = set3 & set4
difference = set1.difference(set2)
join = set1 - set2
symmetric_difference = set3 ^ set4

print(f"union:{union}\nintersection:{intersection}\ndifference:{difference}\njoin:{join}\nsymmetric difference:{symmetric_difference}")


