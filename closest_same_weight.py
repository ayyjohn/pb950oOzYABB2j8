# write a function that takes an integer x and returns
# the nearest (|y - x| is minimized) value y such that
# x and y have the same weight, where weight is defined
# as the number of bits that are 1 in the number.

# if the number is even then the result is to set the last
# bit to 1, and then change the next closest value that is a 1 to
# a 0. the reverse is true if the number is odd, set the last bit to 0
# and then set the next nearest value to 1.

# this is almost correct. it doesn't work for 7, for example, for which
# this would return 1110 instead of 1011 (14 is further than 11 from 7).

# suppose we flip the bit at index k1 and the bit at index k2, where k1 > k2
# then the absolute value of the difference between the original integer and
# the new one is 2**k1 - 2**k2. To minimize this we need to make k1 as small
# as possible and have k2 as close to k1 as possible. this means that the bit
# at k1 needs to be different than k2 to preserve the weight, so the rightmost bit
# that's different from the least significant bit is k1, and the next bit is k2.
# ie the two rightmost bits that are different should be swapped.
# this works on the example 0111 for which k1 = 2, and k2 = 3. so 1011 is the answer.

def closet_same_bit_weight(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        # if the bits at the indices are different,
        # swap them.
        if (x >> i) & 1 != (x >> (i - 1) & 1):
            x ^= (1 << i) | (1 << (i + 1))
            return x
    raise ValueError('All bits are 0 or 1') #can't find an answer

# this can be done in O(1) time and space by using bit tricks to find
# the rightmost set bit of x, and the second lowest unset bit, then swapping them.

def closet_same_bit_weight(x):
    rightmost_set = x & ~(x - 1)
    second_lowest_not_set = ~x & (x + 1)
    return x ^ rightmost_set | second_lowest_not_set

print(closet_same_bit_weight(6))
