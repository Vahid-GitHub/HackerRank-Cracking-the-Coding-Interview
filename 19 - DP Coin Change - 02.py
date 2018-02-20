def make_change(coins, n):
    if (len(coins) == 1):
        reminder = n % coins[0]
        if (reminder == 0):
            return([[n / coins[0]]])
        else:
            return([])
    wList = []
    coin = coins[0]
    maxCoin = (n // coin) + 1
    for i in range(maxCoin):
        reminder = n - i * coin
        tails = make_change(coins[1:], reminder)
        if (tails != []):
            for tail in tails:
                wList.append([i] + tail)
    return(wList)

n = 100
coins = [1, 2, 3]
m = len(coins)
print(len(make_change(coins, n)))