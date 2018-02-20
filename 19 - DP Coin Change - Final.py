# This program solve the problem, but I don't like it because of global variable I used in that. Changing it to local variable would need another helper function, I think.
subStates = {}
def make_change(coins, n):
    if (len(coins) == 1):
        if ((n % coins[0]) == 0):
            return(1)
        else:
            return(0)
    change_counter = 0
    maxCoin = (n // coins[0]) + 1
    for i in range(maxCoin):
        reminder = n - i * coins[0]
        if (not((len(coins[1:]), reminder) in subStates)):
            subStates[(len(coins[1:]), reminder)] = make_change(coins[1:], reminder)
        change_counter += subStates[(len(coins[1:]), reminder)]
    return(change_counter)

n = 100
coins = [2, 5, 3, 6]
m = len(coins)
print(make_change(coins, n))