# write a function that takes in a 64 bit number
# and outputs the number with the bits
# in reverse order.

# naive approach is to perform the previous function
# on each of the first half and last half, ie go through
# half of the number and swap each bit with the -1 - ith bit.

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

def reverse_bits(x):
    for i in range(len(x) >> 1):
        x = format(swap_bits(int(x, 2), i, len(x) -1 - i), f"0{ len(x) }b")
    return x

print(reverse_bits('11001011'))
print(reverse_bits('0'))
print(reverse_bits('1'))
print(reverse_bits('10110111'))
print(reverse_bits('0110111'))

# if we're going to do this many times, we can store 2^16
# cached values since reversing is commutative, eg we can
# reverse y3, y2, y1, y0 to rev(y0), rev(y1), rev(y2), rev(y3)
# where the rev(yn) values are stored in an array. 
