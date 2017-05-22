# write a function that computes x / y

def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result

print(divide(9, 3))
print(divide(1, 1))
print(divide(5, 2))
print(divide(8, 2))
print(divide(99, 11))
