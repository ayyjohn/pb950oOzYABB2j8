# in the trivial form of the knapsack problem
# we have an array of weights, an array of corresponding
# values to each of those weights, and finally a maximum
# capacity of our knapsack. the goal is to maximize the
# value taken while not going over our limit.
# we do this with a table building dynamic programming
# approach in which we see the maximum value at each
# incremental weight, and then use previous entries
# in such a table to determine next values.
# if we know the best answer for taking the first
# i items, then we know the best answer for taking
# the next item is the max value of taking it or not
# taking it (which is to take it if we can).
# note that this problem can be made harder by adding fractions

def knapsack(values, weights, capacity):
    matrix = [[0 for i in range(len(weights) + 1)] for j in range(capacity + 1)]
    for item in range(1, len(weights) + 1):
        for weight in range(1, capacity + 1):
            if weights[item - 1] > weight:
                value_if_take = -float('inf')
            else:
                value_if_take = matrix[item - 1][weight - weights[item - 1]] + values[item - 1]
            value_if_not_take = matrix[item - 1][weight]
            matrix[item][weight] = max(value_if_not_take, value_if_take)
    return matrix


print(knapsack([7, 6, 5], [2, 4, 1], 3))
