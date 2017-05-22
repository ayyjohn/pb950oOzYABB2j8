# write a function that adds two numbers without using
# arithmetic operations

def add(x, y):
    while y > 0:
        carry = x & y
        x ^= y
        y = carry << 1
    return x

print(add(1, 4))
print(add(7, 4))
print(add(1, 0))
print(add(11, 22))
print(add(19, 41))
