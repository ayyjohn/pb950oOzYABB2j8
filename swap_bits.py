# write a function that swaps the ith and jth bits of a
# binary number.

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        # this implies that the ith and jth bits are not the
        # same because we move the ith and jth bit to the
        # 0th position, and then flip all other bits away
        # with the & 1. thus, we'll swap them by
        # flipping their values. we can select the bits to flip
        # using the bit mask,
        bit_mask = (1 << i) | (1 << j)
        # this creates a number where the ith and jth bits are 1
        # we then xor this with x to swap both of them, since
        # xoring with 1 produces a 0 and xoring with 0 produces a 1
        x ^= bit_mask
    return x

print(swap_bits(150, 2, 3))
print(swap_bits(73, 1, 6))
