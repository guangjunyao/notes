import random
import numpy as np
N = random.randint(2, 10)
array = sorted(random.sample(range(1, 10), N))
diff = np.Inf
M = random.randint(2, 9)

a = array[M:] + array[:M]
def find_minimum(a):
    low = 0
    high = len(a)-1
    while low < high:
        middle = (low+high)//2
        if array[low] < array[high]:
            high = middle
        elif array[middle] > array[high]:
            low = middle + 1
    return array[low]
print('rotation point', M)
print('original array ', array)
print('rotation array ', a)
print('minimum after rotation, ', find_minimum(a))
