# write a function that takes 3 inputs, a string, an integer b1, and
# an integer b2. the string is in base b1 and the output should be
# that number in base b2 as a string

def to_binary(s):
    if s == "0":
        return 0
    x = -1
    val = int(s)
    output = ""
    while 2**(x + 1) <= val:
        x += 1
    for i in reversed(range(x + 1)):
        if val >= 2**i:
            output += '1'
            val -= 2**i
        else:
            output += '0'
    return output
print(to_binary("15"))
print(to_binary("8"))
print(to_binary("9"))
print(to_binary("0"))

import string
import functools

def convert_base(num_as_string, base1, base2):
    def construct_from_base(num_as_int, base):
        if num_as_int == 0:
            return ''
        else:
            result = ''
            while num_as_int:
                result += string.hexdigits[num_as_int % base].upper()
                num_as_int = num_as_int // base
        return result[::-1]

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(lambda x, c: x * base1 + string.hexdigits.index(c.lower()),
                                  num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, base2))

print(convert_base('59', 10, 2))
print(convert_base('59', 8, 10))
def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))
print(convert_base('59', 10, 2))
print(convert_base('59', 8, 10))

# first, we find whether or not the number is negative
# then we use the previous algorithm of adding and multiplying
# leftwards down a string to convert a string of any base
# to an int in base 10. then we use construct from base
# to do the canonical divmod to get the value in another base
# from the original int.
