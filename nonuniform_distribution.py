# write a function that takes in an array of values
# and an array of probabilities that sum to one, each
# of which should correspond to the chance that we pick
# the number at the same index in the original array.
# we can use a random number generator
# that produces a random number in [0, 1]

# by decomposing the probabilities into ranges by summing
# the previous values we can create ranges between which
# correspond to choosing any given value

# in the example there are 3, 5, 7, and 11
# and the probabilities are 9/18, 6/18, 2/18, and 1/18 respectively.

# the trivial solution is to generate an array of values
# full of these numbers and then pick a random number between 0 and
# 18. but we can do this without generating such an array by just
# multiplying a random number between 0 and 1 by 18, and then seeing
# if it's between 0 and 9, between 9 and 15, 15 and 17, and 17 and 18
# etc. the better solution does this without multiplication
import itertools
import bisect
import random

def nonuniform_random_number(values, probabilities):
    prefix_sum_of_probabilities = (
        [0.0] + list(itertools.accumulate(probabilities)))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random()) - 1
    return values[interval_idx]

print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
print(nonuniform_random_number([3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]))
