import random
import numpy as np
N = random.randint(2, 10000)
array = sorted(random.sample(range(1, 10000), N))
diff = np.Inf
M = random.randint(2, 10000)
i = 0
l = N-1
# while True:
#     print(i,l)
#     if np.abs(array[i]*array[l] - M) <= diff:
#         diff = np.abs(array[i]*array[l] - M)
#     elif array[i]*array[l] < M:
#         i += 1
#     else:
#         l -= 1
for i in range(N-1):
    current = np.abs(array[i]*array[i+1] - M)
    if current <= diff:
        diff = current
        print(i)
        print('array near M', array[i-2: i+2])
print("N", N)
print('M', M)
print('minimum difference', diff)
