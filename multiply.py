# write a function that takes two arrays representing integers
# and returns an integer representation of their product.
# if one is negative than the result should be negative

def multiply(array1, array2):
    sign = -1 if (array1[0] < 0) ^ (array2[0] < 0) else 1
    array1[0], array2[0] = abs(array1[0]), abs(array2[0])

    result = [0] * (len(array1) + len(array2))
    for i in reversed(range(len(array1))):
        for j in reversed(range(len(array2))):
            result[i + j + 1] += array1[i] * array2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
