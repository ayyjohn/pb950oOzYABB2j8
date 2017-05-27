# write a function that takes an array as input, where each
# number represents the price of a stock on a given day.
# the function should output the maximum profit that can
# be made by buying and selling one share of that stock
# one time, note that the sale must come after the buy.

# the trivial solution is to try every combination and
# then output the maximum. IE iterate over the array twice
# at the same time, storing the first value as the buy
# and each subsequent value as the sale, and tabulating
# a running max.

def buy_and_sell_once(array):
    current_max = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] - array[i] > current_max:
                current_max = array[j] - array[i]
    return current_max

print(buy_and_sell_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

# this solution is O(n**2) which is not great. this problem seems
# similar to the window problem where the window is the length
# of the array...
# what if we tracked the min value and the max value that we'd encountered
# throughout the array, and only updated them if they were a valid pair?
# for example 310 is both min and max, then 310 is min, and since 315 comes
# after then 315 is the max. then we find 275, and we set that to the min
# but we don't update the max difference of 5 because the pair is not valid yet
# then we see 295 and we update this to the max, and update the max difference to
# 20. then we see 260 and we update the min, but nothing else. then we see 270
# and do nothing, then we see 290 and update the max difference to 30 and the
# max value to 290. then we see 230 and update the min to 230. then we see 255
# and do nothing, then we see 250 and do nothing

def buy_and_sell_once(array):
    max_sale, min_price, = 0, array[0]
    for i in array:
        if i < min_price:
            min_price = i
        elif i - min_price > max_sale:
            max_sale = i - min_price
    return max_sale

print(buy_and_sell_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

def buy_and_sell_once(array):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in array:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

print(buy_and_sell_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

# variant: write a function that takes an array as input and returns the length
# of the longest sequence inside the array for which elements are the same
# eg for [1, 3, 3, 5, 8, 5, 5] it should return 2

def longest_same_subarray(array):
    longest_sequence, current, current_sequence = 1, None, 0
    if not array:
        return 0
    for i in array:
        if i == current:
            current_sequence += 1
            longest_sequence = max(current_sequence, longest_sequence)
        else:
            current = i
            current_sequence = 1
    return longest_sequence

print(longest_same_subarray([1, 3, 3, 5, 7, 5, 5, 5]))
print(longest_same_subarray([1, 3, 3, 5, 7, 5, 5]))
print(longest_same_subarray([1, 3, 3, 3, 5, 3, 3, 5, 5]))
print(longest_same_subarray([1]))
print(longest_same_subarray([1, 1]))
print(longest_same_subarray([1, 2, 3, 4, 5]))
print(longest_same_subarray([]))
