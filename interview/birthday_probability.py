import numpy as np
import random

random.seed(123)
youngest = []
for i in range(100000):
    if i % 10000 == 0:
        print(i)
    array = [random.randrange(1, 365) for x in range(4)]
    youngest.append(max(array))
print(sum(youngest) / len(youngest))
