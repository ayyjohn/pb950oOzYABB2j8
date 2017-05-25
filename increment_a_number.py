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

print(increment([8, 8, 9]))
print(increment([8, 8, 0]))
print(increment([8, 8, 7]))
print(increment([8, 9, 9]))
print(increment([9, 9, 9]))
print(increment([0]))

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

# i think mine might be technically faster, but shrug
