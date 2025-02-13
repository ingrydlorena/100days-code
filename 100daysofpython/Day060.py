'''
Day 60: Tower of Hanoi
Solve the Tower of Hanoi problem.
'''

def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    tower_of_hanoi(n-1, aux_rod, to_rod,from_rod)

N = 3

tower_of_hanoi(N, 'Tower1', 'Tower2', 'Tower3')