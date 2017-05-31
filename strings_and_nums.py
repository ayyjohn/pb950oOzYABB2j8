# write a function that converts a string to a number
# and works on negative numbers without using the int()
# function.

# the easiest way to do this is to create a hashmap
# of strings that map to numbers, and then
# iterate over the string backwards, adding n x 10**i
# to the result as we go.
NUMS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def string_to_num(string):
    negative = string[0] == '-'
    if negative:
        string = string[1:]
    total = 0
    for i, num in enumerate(reversed(string)):
        total += NUMS[num] * 10 ** i
    return -1 * total if negative else total

print(string_to_num('-1000'))
print(string_to_num('5000'))
print(string_to_num('0'))

STRS = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}
# the easiest way to do this is to divmod off values
# and add the stringified value to a running string
def num_to_string(num):
    if num == 0:
        return '0'
    negative = num < 0
    num = abs(num)
    string = ""
    while num:
        string += STRS[num % 10]
        num //= 10
    string = string[::-1]
    return '-' + string if negative else string

print(num_to_string(1000))
print(num_to_string(-5000))
print(num_to_string(0))
