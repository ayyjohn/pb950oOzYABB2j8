# write a function that creates a random permutation of length n.

# this can be done by using the same random sampling technique
# for the offline sampling problem, just on an array of [0, 1, 2, .. n - 1]
# and having a sample size of n
# we iterate over the array, swapping with a random number, and then
# shrinking the range we're choosing from to avoid repeats
import random

def random_permutation(n):
    permutation = list(range(n))
    for i in range(n):
        r = random.randint(i, n - 1)
        permutation[r], permutation[i] = permutation[i], permutation[r]
    return permutation

print(random_permutation(4))
print(random_permutation(4))
print(random_permutation(4))
print(random_permutation(4))
print(random_permutation(4))
