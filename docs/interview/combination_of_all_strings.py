"""
递归permutate all the elements in an array.
"""
a = [1, 2, 3, 4]


def permutation(li, from_, to_):
    if from_ == to_:
        print(li[0:to_])
    for i in range(from_, to_):
        print(i, from_)
        li[i], li[from_] = li[from_], li[i]
        permutation(a, from_ + 1, to_)
        li[from_], li[i] = li[i], li[from_]


permutation(a, 0, len(a))
