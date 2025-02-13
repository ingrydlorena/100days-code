'''
Day 70: Numerical computing
Use NumPy for numerical computing.
'''

import numpy as np

numpy_test1 = np.zeros(3)
print(f'TEST 1\nAn Array of zeros with three elements:\n{numpy_test1}')

numpy_test2 = np.ones(5)
print(f'TESTE 2\nAn Array of ones with five elements\n{numpy_test2}')

numpy_test3 = np.linspace(2, 10, 5)
print(f'TESTE 3\nFrom 2 to 10 with 5 elements:\n{numpy_test3}')
print(f'The second element of an array: {numpy_test3[2]}')

list_of_numbers = [12,3,4,8,9]
numpy_test4 = np.array(list_of_numbers)
print(f'TEST 4\nCreate an array with a list:\n{numpy_test4}')

np.random.seed(0)
numpy_test5 = np.random.randint(10, size = 6)
print(f'TEST 5\nCreate an array with method random with six elements:\n{numpy_test5}')
print(f'The random array on the contrary: {numpy_test5[::-1]}')