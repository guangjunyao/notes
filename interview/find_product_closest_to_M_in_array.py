import random
import numpy as np
N = random.randint(2, 10000)
array = random.sample(range(1, 10000), N)
diff = np.inf
M = random.randint(2, 10000)
i = 0
l = N-1
while True:
    print(i,l)
    if np.abs(array[i]*array[l] - M) <= diff:
        diff = np.abs(array[i]*array[l] - M)
    elif array[i]*array[l] < M:
        i += 1
    else:
        l -= 1
