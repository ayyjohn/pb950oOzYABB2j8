"""Write a program to count the number of bits that are set to one in a positive integer"""

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print(count_bits(9))
print(count_bits(2))
print(count_bits(8))
