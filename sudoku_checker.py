# write a function that takes in a 9x9 array
# of a sudoku, partially solved, and outputs
# whether or not it is incorrect so far
import math
import collections
def is_valid_sudoku(partial_solution):

    # returns false if an input array has a duplicate
    # first by filtering out unfilled squares (zeros),
    # then by checking whether the lengths are equal
    # of the remainder and a set of values 1-9
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_solution)
    # check row and column constraints
    if any(
            has_duplicate([partial_solution[i][j] for j in range(n)]) or
            has_duplicate([partial_solution[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # check region constraints
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_solution[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))

# a pythonic version using list comprehensions

def is_valid_sudoku(partial_solution):
    region_size = int(math.sqrt(len(partial_solution)))
    return max(collections.Counter(
        k for i, row in enumerate(partial_solution) for j, c in enumerate(row)
        if c != 0
        for k in ((i, str(c)), (str(c), j
                               ), (i / region_size, j / region_size, str(c)))).values(), default=0) <= 1
