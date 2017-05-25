# 1. write a function that takes an array full of objects that
# have keys that take on one of 3 values and partitions the array
# such that objects with the same key appear together in O(n) time
# with O(1) additional space

# for example [{1: True}, {2: True}, {1: True}, {3: True}, {1: True}, {2: True}]
# should return [{1: True}, {1: True}, {1: True}, {3: True}, {2: True}, {2: True}]
# order does not matter within sub arrays, ie 3 can come before 2.

# there is a trivial solution with n time and n extra space, we iterate through
# the array and store 3 arrays containing the different keys, then return
# the arrays at the end, concatenated

def object_partition_1(array, key1, key2, key3):
    first, second, third = [], [], []
    for i in array:
        if list(i) == [key1]:
            first.append(i)
        elif list(i) == [key2]:
            second.append(i)
        else:
            third.append(i)
    return first + second + third

# the next approach is to treat one element like the pivot from
# the previous problem, (dutch flag partition), and do a similar iteration
# in which we keep middle, start, end, and unchecked partitions
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def object_partition_2(array, key1, key2, key3):
    group1, group2, group3 = 0, 0, len(array)

    while group2 < group3:
        if list(array[group2]) == [key1]:
            swap(array, group2, group1)
            group1 += 1
            group2 += 1
        elif list(array[group2]) == [key2]:
            group2 += 1
        else:
            group3 -= 1
            swap(array, group2, group3)
    return array

print(object_partition_2([{1: True}, {3: True}, {3: True}, {1: True}, {2: True}, {1: True}, {3: True}, {1: True}, {2: True}], 1, 2, 3))

# given an array of n objects with boolean keys reorder the array
# such that objects with they key false appear first in O(n) time and
# O(1) space

def object_partition_3(array):
    true = len(array) - 1

    index = 0
    while index < true:
        if list(array[index])[0]:
            swap(array, index, true)
            true -= 1
        else:
            index += 1

        print(array)
    return array

print(object_partition_3([{True: 7}, {False: 3}, {False: 38}, {True: 9}, {False: 0}, {True: 0}]))

# do the previous problem without changing the relative position of the true elements.
# this can be accomplished by doing something of a selection sort operation.
# whenever you find a false key, move it to the start of the array, and continue

def object_partition_4(array):
    for i in range(len(array)):
        if not list(array[i])[0]:
            array.insert(0, array.pop(i))
    return array

print(object_partition_4([{True: 7}, {False: 3}, {False: 38}, {True: 9}, {False: 0}, {True: 0}]))
