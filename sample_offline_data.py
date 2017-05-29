# write a function that takes an array of distinct elements
# and a size n less than the number of elements in the first
# array, and outputs a random sample of size n from the original
# array.

# to avoid repeats but also get fast time
# we can sample the original array at a random index, then
# swap that value with the end of the array, then array[-2], etc
# creating a partition of sampled elements without deleting them
import random

def random_sample(array, size):
    for i in range(size):
        sample_index = random.randint(0, len(array) - i - 1)
        array[sample_index], array[-1 - i] = array[-1 - i], array[sample_index]
    return array[:size]

print(random_sample(list(range(10)), 5))
print(random_sample(list(range(10)), 5))
print(random_sample(list(range(10)), 5))
print(random_sample(list(range(10)), 5))

# to not use extra memory, note that the end of the arrays in the previous
# example is the sampled arrays, so just remove the appending!

def random_sample(array, size):
    for i in range(size):
        r = random.randint(i, len(array) - i)
        array[i], array[r] = array[r], array[i]
    return array[:size]

# this can be further optimized by saying that if k > n / 2 then
# instead of sampling k elements we can delete n - k elements
# note that their implementation puts the sample at the start of the array
