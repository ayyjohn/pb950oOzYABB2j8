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
