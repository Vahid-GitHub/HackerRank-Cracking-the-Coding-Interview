import math

def make_change(coins, n):
    coins.sort(reverse = True)
    LC = len(coins)
    weight = []
    wList = []
    base = n // min(coins) + 1
    counter = 1
    while (counter < (base ** LC)):
        weight = num_base(counter, base)
        weight += ([0] * (LC - len(weight)))
        wC = [x * y for (x, y) in zip(weight, coins)]
        sumWC = sum(wC)
        if (sumWC == n):
            print([counter, weight])
            wList.append(weight)
        counter += 1
    return(len(wList))

def num_base(num, base):
    Ln = int(math.log(num, base)) + 1
    n = [0] * Ln
    for i in range(Ln - 1, -1, -1):
        digitWeight = base ** i
        n[i] = num // digitWeight
        num -= ( n[i] * digitWeight)
    return(n)
n = 10
coins = [1, 2, 3]
m = len(coins)
print(make_change(coins, n))