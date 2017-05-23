import math
# write a function that takes an integer and returns
# true if it's a palindrome, otherwise false


# hint: it's easy to find the least significant bit
# how would you find the most significant bit?

# naive approach: convert the number to a string
# and check the first n / 2 numbers to make sure that
# they match, if not, break and return false.

def palindrome(num):
    num = str(num)
    for i in range(len(num) // 2):
        left = num[i]
        right = num[-1 - i]
        if left != right:
            return False
    return True

print(palindrome(14241))
print(palindrome(1))
print(palindrome(14244))

# another approach is to chop off the last
# digit and the first digit using math!
# the last digit is available by % 10
# the first digit is available by x / 10 ** (n - 1)
# where n is logbase10(x) + 1

def palindrome(x):
    if x < 0:
        return False

    num_digits = math.floor(math.log10(x)) + 1
    most_significant = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // most_significant != x % 10:
            return False
        x %= most_significant
        x //= 10
        most_significant //= 100
    return True

print(palindrome(14241))
print(palindrome(1))
print(palindrome(14244))

# and the final approach is to reverse the number
# using the optimal reverse with divmod and then
# check if they're the same number

def reverse(x):
    result, remainder = 0, abs(x)
    while remainder:
        result = result * 10 + remainder % 10
        remainder //= 10
    return -result if x < 0 else result

def palindrome(num):
    rev = reverse(num)
    return rev == num

print(palindrome(14241))
print(palindrome(1))
print(palindrome(14244))
