# write a function which takes an array of digits
# encoding a decimal integer D and updates the array to represent
# D + 1. This should work in languages that have finite precision
# arithmetic.

def increment(array):
    if array[-1] != 9:
        array[-1] += 1
    elif all(i == 9 for i in array):
        array[0] = 1
        for i in range(1, len(array)):
            array[i] = 0
            array.append(0)
    else:
        non_zero = len(array) - 1
        for i in range(len(array) - 1, -1, -1):
            if array[i] != 9:
                non_zero = i
                break
        array[non_zero] += 1
        for i in range(non_zero + 1, len(array)):
            array[i] = 0
    return array

# print(increment([8, 8, 9]))
# print(increment([8, 8, 0]))
# print(increment([8, 8, 7]))
# print(increment([8, 9, 9]))
# print(increment([9, 9, 9]))
# print(increment([0]))

# solution version

def plus_one(array):
    array[-1] += 1
    for i in reversed(range(1, len(array))):
        if array[i] != 10:
            break
        array[i] = 0
        array[i - 1] += 1
    if array[0] == 10:
        array[0] = 0
        array.insert(0, 1)
    return array

# now take two arrays that represent binary numbers and add them

# I think this can be done by working backwards over both arrays
# simultaneously, if both are 1, set the value of carry to true
# and basically implement a full adder

def half_adder(a, b):
    return [a ^ b, a & b]

# print(half_adder(0, 0))
# print(half_adder(1, 0))
# print(half_adder(0, 1))
# print(half_adder(1, 1))

def full_adder(a, b, c):
    s1, c1 = half_adder(a, b)
    s_out, c2 = half_adder(s1, c)
    c_out = c1 | c2
    return [s_out, c_out]

def binary_add(array1, array2):
    # pad both arrays to be the same length
    l1, l2 = len(array1), len(array2)
    while len(array1) < l2:
        array1.insert(0, 0)
    while len(array2) < l1:
        array2.insert(0, 0)
    c = 0
    total = []
    for i in range(len(array1) - 1, -1, -1):
        s, c = full_adder(array1[i], array2[i], c)
        total.append(s)
    if c == 1:
        total.append(1)
    return total[::-1]


print(binary_add([1, 0, 1, 0], [0, 1]))
print(binary_add([1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1]))
print(binary_add([1, 0, 1, 0], [0, 1, 0, 1, 1]))
print(binary_add([1, 1, 1, 1], [0, 1]))

def decimal_add(string1, string2):
    string1 = string1.zfill(len(string2))
    string2 = string2.zfill(len(string1))
    total = ''
    carry = 0
    for i in range(len(string1) -1, -1, -1):
        add = int(string1[i]) + int(string2[i]) + carry
        if add >= 10:
            carry = 1
            add %= 10
        else:
            carry = 0
        total += str(add)
    if carry:
        total += str(carry)
    return total[::-1]

print(decimal_add('100', '50'))
print(decimal_add('99', '3'))
print(decimal_add('19', '16'))

