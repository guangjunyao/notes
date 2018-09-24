from functools import reduce
from math import ceil
a = [1, -2, 3, 10, -4, 7, 2, -5]


def max_sum_sub(a, from_, to_):
    if from_ == to_:
        return a[from_]
    middle = (from_ + to_) // 2
    #    middle = ceil((from_ + to_)/2)
    print('now', middle)
    m1 = max_sum_sub(a, from_, middle)
    m2 = max_sum_sub(a, middle + 1, to_)
    left = a[middle]
    now = a[middle]
    for i in range(from_, middle):
        now += a[i]
        left = max(now, left)
        print('left', i)
    right = a[middle + 1]
    now = a[middle + 1]
    for i in range(middle + 2, to_):
        now += a[i]
        right = max(now, right)
        print('right', i)
    m3 = left + right
    return max(m1, m2, m3)


print(max_sum_sub(a, 0, len(a) - 1))

# dynamic programming
result = a[0]
sum_ = a[0]
for i, value in enumerate(a):
    if sum_ > 0:
        sum_ += value
    else:
        sum_ = value
    if sum_ > result:
        result = sum_
print(result)
