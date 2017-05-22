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

def toggle_nth_bit(x, n):
    return x ^ (1 << n)

def turn_off_rightmost_one_bit(x):
    return x & (x - 1)

def isolate_rightmost_one_bit(x):
    # -x == ~(x + 1)
    return x & ~(x + 1)

def right_propagate_rightmost_set_bit(x):
    # doesn't work on 0
    return x | (x - 1)

def isolate_rightmost_zero_bit(x):
    return ~x & (x + 1)

def turn_on_rightmost_zero_bit(x):
    return x | (x + 1)

def int_to_bin(x, bits=8):
    result = ''
    while bits:
        result = ('1' if x & 1 else '0') + result
        bits -=1
        x >>= 1
    return result

print(int_to_bin(8))
print(int_to_bin(15))
print(int_to_bin(9))
