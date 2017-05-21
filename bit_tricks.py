# test if even
def even(x):
    if x == 0:
        return False
    else:
        return not bool(x & 1)

def nth_bit_set(x, n):
    return bool(x & (1 << n))

def set_nth_bit(x, n):
    return x | (1 << n)

def unset_nth_bit(x, n):
    return x & ~(1 << n)

