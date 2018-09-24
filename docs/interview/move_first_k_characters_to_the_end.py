"""
move the first k characters in a list to the end.
(X'Y')' = YX
"""


def rotate(li, from_, to_):
    while from_ < to_:
        temp = li[from_]
        li[from_] = li[to_]
        li[to_] = temp
        from_ += 1
        to_ -= 1
    return li


a = [1, 2, 3, 4, 5]
# rotate the first k to the end
k = 1
a_temp = rotate(a, k, len(a) - 1)
a_temp = rotate(a, 0, k - 1)
a_temp = rotate(a, 0, len(a) - 1)
print(a_temp)
# rotate the end k to the front
k = 1
k = len(a) - 1 - 1
a_temp = rotate(a, k, len(a) - 1)
a_temp = rotate(a, 0, k - 1)
a_temp = rotate(a, 0, len(a) - 1)
print(a_temp)
