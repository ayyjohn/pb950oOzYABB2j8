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
