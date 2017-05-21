# write a function that returns true for a value x if x is a power of 2
# ie returns true for 1, 2, 4, 8, in constant time.

# in binary, all powers of two contain exactly 1 1.
# eg 0001 is 1, 0010 is 2, 0100 is 4, 1000 is 8.
# so if this statement is true, then the number is a power of two.

# in the naive approach we need to check the binary representation
# and count the number of 1s, which means checking logbase2(n) + 1
# numbers.
def power_of_two(x):
    return list(bin(x)).count('1') == 1

print(power_of_two(1))
print(power_of_two(2))
print(power_of_two(4))
print(power_of_two(8))
print(power_of_two(16))
print(power_of_two(3))
print(power_of_two(5))
print(power_of_two(0))

# that's decent but we want constant time
# since x & (x - 1) erases the lowest bit, and a power of
# two should only have one 1, if x & (x - 1) == 0 and x != 0
# then this is true

def power_of_two(x):
    return x & (x - 1) == 0 and x != 0

print(power_of_two(1))
print(power_of_two(2))
print(power_of_two(4))
print(power_of_two(8))
print(power_of_two(16))
print(power_of_two(3))
print(power_of_two(5))
print(power_of_two(0))
