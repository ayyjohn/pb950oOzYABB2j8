import random
# write a function that takes an array
# and rearranges them so that they form an alternation
# ie that each number is either greater than both its
# neighbors or less than both its neighbors
# eg for an array b: b[0] < b[1] > b[2] < b[3]... etc.

# naive solution is to sort the array and then take
# the first half and interleave it with the second half

def alternation(array):
    array.sort()
    alternates = []
    for i in range(len(array)):
        if i % 2 == 0:
            alternates.append(array[i])
        else:
            alternates.append(array[-i])
    return alternates

print(alternation([1, 5, 2, 1, 3, 5, 7]))
print(alternation([1, 5, 2, 1, 3, 5, 7, 8]))

# another approach is to sort the array, and then swap the values
# at each pair (0, 1), (2, 3), (4, 5), etc.

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def alternation(array):
    array.sort()
    for i in range(1, len(array) - 1, 2):
        swap(array, i, i + 1)
    return array

print(alternation([1, 5, 2, 1, 3, 5, 7]))
print(alternation([1, 5, 2, 1, 3, 5, 7, 8]))

# the best approach is as follows: iterate over the array
# and swap when certain conditions are met. since the goal
# is for every even element to be less than its neighbors,
# and every odd element to be greater than its neighbors,
# then we can iterate over the array and swap each element with
# the next one if array[i] and array[i + 1] do not meet the conditions.
# ie if i is odd and array[i] < array[i + 1]
# or if i is even and array[i] > array[i + 1]

def alteration(array):
    for i in range(len(array)):
        array[i:i + 2] = sorted(array[i:i + 2], reverse = i % 2)

print(alternation([1, 5, 2, 1, 3, 5, 7]))
print(alternation([1, 5, 2, 1, 3, 5, 7, 8]))
