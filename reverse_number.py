# write a function which takes an integer and returns
# the input in reverse order, eg 42 => 24, -314 => -413

# naive approach is to split and reverse, keeping a
# flag for negative

def reverse(num):
    negative = False
    if num < 0:
        negative = True
        num *= -1
    result = ''.join(list(str(num))[::-1])
    return '-' + result if negative else result

print(reverse(-314))
print(reverse(42))

# better approach

def reverse(x):
    result, remainder = 0, abs(x)
    while remainder:
        result = result * 10 + remainder % 10
        remainder //= 10
    return -result if x < 0 else result

print(reverse(-314))
print(reverse(42))

