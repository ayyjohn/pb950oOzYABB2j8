# write a function that takes in a positive integer n and another positive
# integer k <= n and outputs a k sized subset as an array. all subsets
# should be equally likely, and all permutations of the subset
# should be equally likely.
import random

def subset(n, k):
    changed_elements = {}
    for i in range(k):
        # generate a random index between i and n - 1, inclusive
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]
