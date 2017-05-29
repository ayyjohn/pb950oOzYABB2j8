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
# array[j], then reverse the array starting at i + 1
# up to the end of the array

def next_permutation(array):
    i = 'flag'
    for idx in range(len(array) - 1):
        if array[idx] < array[idx + 1]:
            i = idx
    if i == 'flag':
        return []
    for k in range(i + 1, len(array)):
        if array[k] > array[i]:
            j = k
    array[i], array[j] = array[j], array[i]
    return array[:i + 1] + list(reversed(array[i + 1:]))

print(next_permutation([0, 3, 2, 1]))
print(next_permutation([2, 3, 0, 1]))
print(next_permutation([1, 3, 0, 2]))
print(next_permutation([3, 2, 1, 0]))

# better because it iterates backwards both times since we're looking for the rightmost instance
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

# write a function that finds the previous permutation, or if
# the input is the first permutation in dictionary order return []

# in the version where we find the next permutation we first find the
# rightmost place where a number is less than the next number.
# this signifies that everything after this index is in decreasing order
# and thus cannot be increased. if this is the entire array
# than the permutation has no next value, eg [3, 2, 1, 0].
# once this is found, it makes sense to swap this value with the
# smallest possible value in the suffix for which array[j] > array[i]
# because this will minimize the increase. it's like incrementing
# the value on a spedometer, but since we don't necessarily have all
# values available we'll take the smallest one we do. by iterating
# over the values backwards, since they're in descending order, we guarantee
# that the first value found is the smallest one that is greater than array[i].
# once we swap these values, we've made the smallest possible increase to the prefix
# that we can, because we replaced its last value with the next possible value.
# all that's left is to reverse the suffix because it's in descending order, ie
# in its maximal state, and we want it to change to its smallest. think of it
# like when your spedometer reads 199, the next value for the smallest value that
# can increase is 2, and then we reset all the rightmost values. in this case we don't
# have an unlimited number of zeros, so we make the suffix as small as possible by reversing it.

# to find the previous permutation, let's consider the same thing.
# the base case is an array that is in sorted order, because this has
# no value smaller. so we must search for the rightmost value that is
# greater than the value next to it, ie array[i] > array[i + 1]. we want
# to switch this with the largest value that is less than this value, because
# we ordinarily would just subtract 1, but we may not have 1 available, so we'll take
# the closest thing to it. by searching in reverse order through all values to the right
# of i, we will guarantee finding one such of these values because array[i + 1] is less
# than array[i]. once we have found this value we can swap them, and then we have the smallest
# change to the suffix possible. the right side is now still in increasing order so we maximize
# it by reversing it.

def previous_permutation(perm):
    inflection = len(perm) - 2
    # find the first point at which perm is not increasing
    while inflection >= 0 and perm[inflection] < perm[inflection + 1]:
        inflection -= 1
    # if there is no such point we will go through the whole array
    # and thus there is no previous permutation so we return []
    if inflection == -1:
        return []
    # next, find the largest number right of inflection
    # for which perm[j] < perm[inflection]
    # since the right side of the array is in sorted
    # order ascending, the first value from the right
    # will be the largest possible
    for i in reversed(range(inflection + 1, len(perm))):
        if perm[i] < perm[inflection]:
            perm[i], perm[inflection] = perm[inflection], perm[i]
            break
    # now we have minimized the decrease of the prefix, and we should
    # maximize the suffix.
    perm[inflection + 1:] = reversed(perm[inflection + 1:])
    return perm

print(previous_permutation([0, 3, 2, 1]))
print(previous_permutation([2, 3, 0, 1]))
print(previous_permutation([1, 3, 0, 2]))
print(previous_permutation([3, 2, 1, 0]))
print(previous_permutation([0, 1, 2, 3]))
