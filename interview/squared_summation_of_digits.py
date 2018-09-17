import string
from functools import reduce

def is_squared_summation_digits(num):
    temp = str(num)
    summation = sum(map(lambda x:x**2,  [int(x) for x in temp]))
    if summation == 1.0:
        return True
    else:
        is_squared_summation_digits(summation)
    return True

n = 100
def get_count(n):
    counter = 0
    for num in range(n+1):
        try:
            if is_squared_summation_digits(num):
                counter += 1
        except:
            continue
    return counter
print(get_count(n))
