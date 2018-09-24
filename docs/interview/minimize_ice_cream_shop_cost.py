"""
An ice cream shop is looking to minimize their operation costs, under the given constraints:

They are faced with costs of purchasing ice cream from a local distributor, where each order has a (potentially large) fixed delivery cost shipping _ cost as well as the price price for each pint

to minimize delivery costs, they can buy more ice cream than needed for a given day, and keep it stored it in their freezer overnight

their freezer can store max capacity pints of ice cream at any time (includes both the shipment as well as any pints stored overnight)

However, storing extra ice cream overnight is not free, and it costs them overnight cost dollars per pint (per night) to keep any additional ice cream frozen if they buy in advance

Given a list of daily demand (in pints) of ice cream for the next num_days days, what is the minimum cost for the shop to be stocked up ready to meet their demands each day?

Inputs

An integer num _ days , for the number of days

A list of n integers demands, separated by a space, for the pints of ice cream demanded each day

An integer max _ capacity , for the max capacity of their freezer

An integer shipping _ cost , for the fixed cost of each shipment taken

An integer price, for the price they pay for each pint of ice cream

An integer overnight_cost, the cost of storing a pint of ice cream for a day
"""
"""
minCost[n] = the minimize cost on the nth day.

iceCream[n] = the pints of ice cream demanded on the nth day

the whole price of ice cream should be the sum of pints * price, it will never change.

on day 1, the shop must pay shipping fee. minCost[0] = shipping_cost.

if the remaining ice cream cannot satisfy the demand on that day, the shop has to ship more, cost = shipping_cost + overnight_cost, so they should avoid this situation. Therefore, we only compare shipping_cost with overnight_cost.

minCost[n] = min { shipping_cost + minCost[n-1], overnight_cost * iceCream[n] + minCost[n-1] }

however, when max_capacity is not big enough, the remaining ice cream cannot satisfy the demand on next day, they have to ship.

if( ( max_capacity - iceCream[n-1] ) < iceCream[n] )

minCost[n] = shipping_cost + minCost[n-1]
"""


def min_cost(num_days, demands, max_capacity, shipping_cost, price,
             overnight_cost):
    count_ice_cream = float('inf')
    count_day = 1
    cost1 = []

    for i in demands:
        storage_cost = i * count_day * overnight_cost

        if count_ice_cream + i <= max_capacity and storage_cost < shipping_cost:
            cost1.append(storage_cost)
            count_ice_cream += i
            count_day += 1
        else:
            cost1.append(shipping_cost)
            count_ice_cream = i
            count_day = 1

    demands.reverse()
    count_ice_cream = float('inf')
    cost2 = []

    for i in demands:
        storage_cost += count_ice_cream * overnight_cost

        if count_ice_cream + i <= max_capacity and storage_cost < shipping_cost:
            cost2.append(storage_cost)
            count_ice_cream += i
        else:
            cost2.append(shipping_cost)
            storage_cost = 0
            count_ice_cream = i

    cost1.insert(0, 0)
    cost2.insert(0, 0)

    def accumu(lis):
        total = 0
        for x in lis:
            total += x
            yield total

    accum_cost1 = list(accumu(cost1))
    accum_cost2 = list(accumu(cost2))
    accum_cost2.reverse()

    accum_cost = [a + b for a, b in zip(accum_cost1, accum_cost2)]

    shipping_storage = min(accum_cost)
    total_cost = shipping_storage + sum(demands) * price

    return total_cost


num_days = 3
demands = [1, 1, 1]
max_capacity = 5
shipping_cost = 3
price = 2
overnight_cost = 1
print(
    min_cost(num_days, demands, max_capacity, shipping_cost, price,
             overnight_cost))
