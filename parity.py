"""Compute the parity of a 64 bit word"""

# brute force: check each bit, then divide the number by two (bit-wise right
# shift is equal to dividing by 2). We only need to know whether the current
# parity is even or odd since it flips from 0 to one so result = result ^ (x & 1)
# and x & 1 will be 0 if x is even, 1 if it's odd. Finally return the result.

def parity(n):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# improvements can be made based on this: x & (x -1) equals x with its lowest
# bit erased. EG: if x = 00101100 then x - 1 = 00101011 and so x & (x - 1)
# = 00101100 & 00101011 which is equal to 00101000. Note that the last 1 is gone.
# Thus the time complexity can be reduced to the number of bits which are one
# since we can do k operations to remove k instances of the number 1 and find the
# parity.

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

# note another neat trick is that x & ~(x - 1) isolates the lowest bit that is
# one in x. (~ is the bitwise complement operator)

# further improvements can be made by caching, based on the fact that
# decomposing a 64 bit number into 4 16 bit numbers, and caching all 2^16
# 16 bit parities is not that hard at all; and then the parity of
# the entire number is the parity of the 4 16 bit numbers

# in addition, xor provides another amazing improvement. By splitting
# a 64 bit binary number in half, and xor-ing the two halves together,
# the parity can be produced. This can then be repeated down to 0 bits
# and a result can be extracted. To exemplify:
# the parity of 11010111 is the same as the parity of 1101 xor 0111
# which is 1010. the parity of 1010 is the same as the parity of 10 xor 10
# which is 00. the final result is 0 xor 0 which is 0.

def parity(x):
    nums = [32, 16, 8, 4, 3, 1]
    for i in nums:
        x ^= x >> i
    return x & 0x1

# note that this can be combined with the 16 bit caching.
# this time complexity is O(log(n))
