# write a function that only uses assignment and bitwise operators
# and maybe loops to compute the product of two nonnegative integers
# x and y

# a brute force approach is to initialize a value at 0 and then
# add one number x to the running sum y times.

def bitwise_multiply(x, y):
    def bitwise_add(a, b):
        while b > 0:
            carry = a & b
            a ^= b
            b = carry << 1
        return a

    running_sum = 0
    while x:
        if x & 1:
            running_sum = bitwise_add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

print(bitwise_multiply(5, 12))
print(bitwise_multiply(0, 12))
print(bitwise_multiply(1, 12))
