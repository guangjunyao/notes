"""
ignore the 5th, 8th, 13th number in the all sequences.
the 5th, 6th, 7th fibonacci numbers.
0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
0, 1, 1, 2, 3, 5, 8, 13,21,...
"""

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# 相当于一个vector, pop up the previous mines.
print(fib(4)+fib(8-5-1)+fib(13-8-1)+fib(27-13-1))
