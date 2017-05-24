# write a function that takes an array of numbers as an input
# and returns the array with all of the even elements
# appear before the first odd element. do this without
# allocating extra space, ie in place

def even_odd(array):
    next_even, next_odd = 0, len(array) - 1
    while next_even < next_odd:
        if array[next_even] % 2 == 0:
            next_even += 1
        else:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -= 1
    return array

print(even_odd([1, 5, 3, 9, 3, 2, 1, 5, 4, 7]))
