# write a function that takes an array of numbers that represent
# the prices of a stock on a day and outputs the highest
# value that can be made from buying and selling the stock
# two different times where the second buy occurs after the
# first sale

# there is a brute force approach similar to the last one
# where we iterate over the entire array, this time 4 times
# and try all possible combinations of 4 values to ensure
# that we: 1. maximize the profit over 2 sales, and 2,
# stick to the constraints of when we can buy and sell
# however this is O(n**4), and we can only improve this
# using this approach to O(n**2) by using the previous
# one pass algorithm twice

# the solution is to use previous information, ie
# knowledge of the best sale/buy combination going forward
# can be used backwards to solve this problem.

def buy_and_sell_twice(array):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(array)
    #calculate the maximum profit if we sell on day i
    for i, price in enumerate(array):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # for each day, find the maximum profit if we make the second buy on
    # that day by going backwards
    for i, price in reversed(list(enumerate(array[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i - 1])
    return max_total_profit
