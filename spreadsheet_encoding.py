# write a function that takes in a string such as A, Q, Z, AA, AX, ZZ
# corresponding to a spreadsheet column header and outputs the
# integer mapping, eg for A it outputs 1, for D it outputs
# 4, for ZZ it outputs 702.

# at first glance this seems like it's just base 26?
# A => 1
# Z => 26
# AA => 27
# so at the top we have 1x26**1 + 1x26**0
# that would mean ZZ = 26x26**1 + 26x26**0
# which, yes, that equals 702!

# so a brute force approach is to map
# each value to its corresponding letter
# and then keep a running sum through the number

import string
import functools
def spreadsheet_column(s):
    total = 0
    for i in reversed(range(len(s))):
        total += (string.ascii_uppercase.index(s[i]) + 1) * 26**i
    return total

print(spreadsheet_column('ZZ'))
print(spreadsheet_column('AA'))
print(spreadsheet_column('A'))

# there's a better algorithm, though, that I remember from before
# where when building up the values we can do less multiplications
# essentially you traverse the string in order, multiplying by the base
# each time. so for base 10, and 314 we add 3, then multiply by 10.
# then we add 1, getting 31, then we multiply by 10 again.
# then we add 4.
# the general algorithm is initialize a partial to 0,
# then for partial value, multiply by 10 and add
# so partial = 0
# 0x10 + 3 = 3
# 3x10 + 1 = 31
# 31x10 + 4 = 314

def spreadsheet_column(col):
    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)

print(spreadsheet_column('ZZ'))
print(spreadsheet_column('AA'))
print(spreadsheet_column('A'))

