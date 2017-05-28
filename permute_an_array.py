# write a function that takes in an array and a permutation set
# and applies that permutation set to the array.
# this implies that, for example, applying the permutation
# <2, 0, 1, 3> to the array [a, b, c, d] creates
# [b, c, a, d] because the element at position 0 is mapped to
# position 2, the element at position 1 is mapped to position
# 0, the element at position 2 is mapped to position 1, and
# the element at position 3 is mapped to position 3.

#if we use n extra space we can just do this easily.

def permute(array, permutation):
    new_array = [0] * len(array)
    for i in range(len(permutation)):
        new_array[permutation[i]] = array[i]
    return new_array

print(permute(['a', 'b', 'c', 'd'], [2, 0, 1, 3]))

# if we recognize that permutations are cyclic we can
# remove the need for the n extra space by doing this
# in place, using the initial array to store values
# as they're moved, and the permutation array
# to store a pseudo boolean value to show whether
# or not that specific cycle has been finished

# permutations of an array are cyclic because
# if you apply them some repeated number of times you will get back the original
# array
# if you apply this to the permutation <3, 2, 1, 0>, the first move swaps
# the elements at 3 and 0, and the elements at 2 and 1. this means if we apply
# this permutation twice we get back the original result.
# for the permutation <2, 0, 1, 3> we have two cycles, the element
# at position 3 will always be in the same place since it swaps with itself.
# the other 3 elements will swap with each other, and if we do it two more times
# we will be at the beginning again. we can thus track whether we're inside
# a cycle using the permutation array and compute the permutation in place
# only proceeding to the next cycle once the current one is complete
