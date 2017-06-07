# write a function that takes in an array of coins and an amount
# and returns the smallest number of coins that make the amount

# base case:
# return infinity if the amount is less than 0 (inf is used because it's always worse)
# return 0 if the amount is 0 (vacuous case)

# recursive case:
# iterate through the coins
# let temp = make_change(coins, amount - coin)
# keep track of the minimum amount so far
# and if temp < min so far, temp = min so far
# and then once we're done, return min so far + 1

def make_change(coins, amount):
    if amount < 0:
        return float('inf')
    elif amount == 0:
        return 0
    else:
        min_so_far = float('inf')
        for coin in coins:
            temp = make_change(coins, amount - coin) + 1
            if temp < min_so_far:
                min_so_far = temp
    return min_so_far

print(make_change([1, 7, 10], 14))

# to add dynamic programming to this, let's create a cache, which can replace one of the base cases
# specifically the if amount == 0, return 0, we can do cache = {0: 0}, and then each time we find a
# value, let's check the cache first to make sure we don't know it.

CACHE = {0: 0}

def make_change(coins, amount):
    if amount < 0:
        return float('inf')
    elif amount in CACHE:
        return CACHE[amount]
    else:
        min_so_far = float('inf')
        for coin in coins:
            temp = make_change(coins, amount - coin) + 1
            if temp < min_so_far:
                min_so_far = temp
            CACHE[amount] = min_so_far
    return min_so_far

print(make_change([1, 7, 10], 14))
print(make_change([1], 0))

# the previous is the bottom up solution
# let's do the top down version, which is essentially iterative
# we start with the base case, 0 outputs 0, and then for every value
# from 1 up to amount we try each coin and see if it's better
# so for 1, we try 1 and get 1, then we try 7 and get inf, then we try
# 10 and get inf, 1 is the smallest so results[1] = 1

# the time complexity is as follows; the outer loop runs amount times,
# and the inner list comprehension runs coins times so the overall
# complexity is coins*amount, and the cache has to store amount values

def make_change_table(coins, amount):
    if amount < 0:
        return "you can't make change for less than 0 coins"
    results = {0:0}
    for i in range(1, amount + 1):
        results[i] = min([results.get(i-coin, float('inf')) + 1 for coin in coins])
    return results[amount]
print(make_change_table([1, 7, 10], 14))
print(make_change_table([1, 7, 10], 15))
print(make_change_table([1, 7, 10], 0))
