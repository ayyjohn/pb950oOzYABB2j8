# write an expression that right-propagates the rightmost set bit in x
# eg turns 01010000 into 01011111 (the rightmost 1 turns the rest of the
# numbers into ones) in constant time.

# x & (x - 1) removes the last set bit. xoring the original value with that
# value gives us that isolated bit, and subtracting 1 from that gives
# us the rest of the values as 1s. Adding that final number to the
# original number produces the result.
import math
def right_propagate(x):
    return format(x + (x & (x - 1) ^ x - 1), f"0{ math.floor(math.log(x, 2) + 1) }b")

print(right_propagate(0b01010000))
print(right_propagate(0b0001000))
