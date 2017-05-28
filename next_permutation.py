# write a function that takes in an array
# of values representing a permutation
# and returns the dictionary defined "next"
# permutation. A permutation by definition
# will be n length containing the numbers
# range(n), ie 0 to n - 1. The dictionary definition
# of permutations states that one permutation is greater
# than another if at the first place that they differ
# the greater permutation is larger. ie <2, 0, 1> is
# less than <2, 1, 0>.
# the smallest permutation is <0, 1, 2> and the largest
# is <2, 1, 0> for a 3 length array.

# for a 3 length permutation the options, in sorted order
# <0, 1, 2>
# <0, 2, 1>
# <1, 0, 2>
# <1, 2, 0>
# <2, 0, 1>
# <2, 1, 0>

# for a length 2 permutation
# <0, 1>
# <1, 0>

# for a length 4 permutation
# <0, 1, 2, 3>
# <0, 1, 3, 2>
# <0, 2, 1, 3>
# <0, 2, 3, 1>
# <0, 3, 1, 2>
# <0, 3, 2, 1>
# <1, 0, 2, 3>
# <1, 0, 3, 2>
# <1, 2, 0, 3>
# <1, 2, 3, 0>
# <1, 3, 0, 2>
# <1, 3, 2, 0>

# the algorithm is to find the rightmost element that
# has array[i] < array[i + 1], and the rightmost
# element greater than i for which array[j] > array[i]
# which must exist if the array is not in the
# largest order (ie reverse order). swap array[i] and
# array[j], then reverse the array starting at i
# up to the end of the array

def next_permutation(array):
    i = 'flag'
    for idx in range(len(array) - 1):
        if array[idx] < array[idx + 1]:
            i = idx
    if i == 'flag':
        return []
    for k in range(i, len(array)):
        if array[k] > array[i]:
            j = k
    array[i], array[j] = array[j], array[i]
    return array[:i + 1] + list(reversed(array[i + 1:]))

print(next_permutation([0, 3, 2, 1]))
print(next_permutation([2, 3, 0, 1]))
print(next_permutation([1, 3, 0, 2]))
print(next_permutation([3, 2, 1, 0]))

def next_permutation(array):
    inversion_point = len(array) - 2
    while(inversion_point >= 0 and array[inversion_point] >= array[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []
    for i in reversed(range(inversion_point + 1, len(array))):
        if array[i] > array[inversion_point]:
            array[inversion_point], array[i] = array[i], array[inversion_point]
            break
    array[inversion_point + 1:] = reversed(array[inversion_point + 1:])
    return array

print(next_permutation([0, 3, 2, 1]))
print(next_permutation([2, 3, 0, 1]))
print(next_permutation([1, 3, 0, 2]))
print(next_permutation([3, 2, 1, 0]))

