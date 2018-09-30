bag = [1, 2, 3, 4, 5]
weight = 10


def knap(weight, bag, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap(weight - bag[n - 1], bag, n - 1):
        print("item ", str(n), ": ", bag[n - 1])
        return True
    if knap(weight, bag, n - 1):
        return True
    else:
        return False


print(knap(weight, bag, 5))
