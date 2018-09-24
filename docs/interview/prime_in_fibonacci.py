import math
def fib(n):
    # find the fibonacci sequence
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

def prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
n = 5            
fib_seq = map(fib, range(0, n))
num = sum(map(prime, fib_seq))       
