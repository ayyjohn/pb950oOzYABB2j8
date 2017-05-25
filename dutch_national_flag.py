# write a program that takes in an array, and an index i
# and reorders the array such that elements less than i
# come first, then elements equal to the pivot, then
# elements greater than the pivot.

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
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, i):
    less = 0
    for j in range(len(array)):
        if array[j] < array[i]:
            swap(array, less, j)
            less += 1
    more = len(array) - 1
    for j in reversed(range(len(array))):
        if array[j] > array[i]:
            swap(array, more, j)
            more -= 1

    return array


print(partition([1, 5, 8, 3, 9, 0, 4, 3], 3))

# iterate through the array, the iterator is named equal.
# if we encounter a smaller element than the pivot, we
# swap that element with the rightmost element that is smaller
# than the pivot. if we encounter an element equal to the pivot
# we continue. if we encounter an element greater than the pivot we
# swap it with the smallest unclassified element, because we still
# need to operate on the unclassified element, but now we know
# that that element should go to the right side of the list.
# note that in this case we do NOT increment the equal value
# because otherwise we'd skip the value that got swapped.

def partition(array, i):
    pivot = array[i]
    smaller, equal, larger = 0, 0, len(array)

    while equal < larger:
        if array[equal] < pivot:
            swap(array, smaller, equal)
            smaller += 1
            equal += 1
        elif array[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            swap(array, equal, larger)
    return array

print(partition([1, 5, 8, 3, 9, 0, 4, 3], 3))
