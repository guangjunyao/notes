initial_market_share = [.6, .4]
switch_probability = [[.8, .2], [.1, .9]]

#initial_market_share = [1]
#switch_probability= [[1]]
# output = [  0.3333, 0.6667]


def market_equilibrium(initial_market_share, switch_probability):

    if len(initial_market_share) == 1:
        return 1.0
    switch_probability = [x[-1] for x in switch_probability]
    switch_probability = switch_probability[::-1]
    for i in range(100):
        initial_market_share = [
            a * b for a, b in zip(initial_market_share, switch_probability)
        ]
        initial_market_share = [
            sum(initial_market_share), 1 - sum(initial_market_share)
        ]
    result = []
    for x in initial_market_share:
        result.append(round(x, 4))
    return result[::-1]


output = market_equilibrium(initial_market_share, switch_probability)
print(output)
