# write a program that takes in an array, and an index i
# and reorders the array such that elements less than i
# come first, then elements equal to the pivot, then
# elements greater than the pivot.

# step 1 is to swap the first element with the pivot
# then, iterate over the array. if we hit an element
# greater than the pivot, just increment a counter
# which will tell us what part of the array
def partition(array, i):
    array[0], array[i] = array[i], array[0]
    less = 0
    for j in range(len(array)):
        if array[j] < array[less]:
            array[j], array[less] = array[less], array[j]
            less += 1
            array[less], array[j] = array[j], array[less]
    return array

print(partition([1, 5, 8, 3, 9, 0, 4], 3))

# this approach works but does not partition the 3s together
# to solve this trivially create 3 arrays, those equal, those
# greater, and those less than the value, the concat them.

def partition(array, i):
    less = []
    equal = []
    greater = []
    for j in array:
        if j < array[i]:
            less.append(j)
        elif j > array[i]:
            greater.append(j)
        else:
            equal.append(j)
    return less + equal + greater

print(partition([1, 5, 8, 3, 9, 0, 4, 3], 3))

# this can be done without using O(n) extra memory though
# by passing through the array twice, on the first pass
# grouping all elements less than the pivot to the left
# of the pivot, and then on the second pass grouping all
# elements greater than the pivot to the right

def partition(array, i):
    less = 0
    for j in range(len(array)):
        if array[j] < array[i]:
            array[less], array[j] = array[j], array[less]
            less += 1
    more = len(array) - 1
    for j in reversed(range(len(array))):
        if array[j] > array[i]:
            array[more], array[j] = array[j], array[more]
            more -= 1

    return array


print(partition([1, 5, 8, 3, 9, 0, 4, 3], 3))

def partition(array, i):
    pivot = array[i]
    smaller, equal, larger = 0, 0, len(array)

    while equal < larger:
        if array[equal] < pivot:
            array[smaller], array[equal] = array[equal], array[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif array[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            array[equal], array[larger] = array[larger], array[equal]
    return array
