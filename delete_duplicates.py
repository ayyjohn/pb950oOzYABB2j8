# write a function that takes an array in sorted order
# as input and alters that array with all the
# duplicates filtered out and all correct values shifted
# over to the left. then return the number of valid
# elements left in the array. there is an O(n) time and
# O(1) space solution.

# iterate over the array. store a value that partitions the
# array into unique values and non unique values. also
# store the current value, when you encounter a new value
# set that to current and swap it with the nearest value of
# current.

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def unique_in_sorted_array(array):
    current = None
    unique = 0
    i = 0
    while i < len(array):
        if array[i] != current:
            current = array[i]
            swap(array, unique, i)
            unique += 1
        i += 1

    return array, unique

print(unique_in_sorted_array([2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 11, 11, 13]))

# their solution

def delete_duplicates(array):
    if not array:
        return 0

    write_index = 1
    for i in range(1, len(array)):
        if array[write_index - 1] != array[i]:
            array[write_index] = array[i]
            write_index += 1
    return write_index

# write a function that takes in an array and a key and returns
# the array with the key deleted and the values shifted over
# where the key used to be, also return the number of non key
# elements. there are no specifications for the array after
# the non key elements
def delete_specific_key(array, key):
    not_key = 0
    for i in range(len(array)):
        if array[i] != key:
            swap(array, not_key, i)
            not_key += 1
    return array, not_key

print(delete_specific_key([2, 3, 2, 2, 3, 3, 3, 5, 5, 7, 3, 11, 13], 3))
