# write a function that outputs n lines of pascal's triangle

def pascals_triangle(n):
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result

print(pascals_triangle(5))

# to compute the nth row in o(n) space, ie without computing the whole tree
# use the fact that the ith entry of the nth row = n choose i
# which has the formula n! / (n - k)!k!

import math

def choose(n, k):
    return int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))

def pascals_triangle(n):
    if n == 0:
        return [1]
    result = [0] * (n + 1)
    for i in range(n + 1):
        result[i] = choose(n, i)
    return result

print(pascals_triangle(0))
print(pascals_triangle(1))
print(pascals_triangle(2))
print(pascals_triangle(3))
print(pascals_triangle(4))
print(pascals_triangle(5))
