# write a function that takes an array of characters
# and removes every b and replaces each a by two ds
# so for example on the array [a c d b b c a]
# we would come out with      [d d c d d c d d]

# so with n extra space we could build an array
# the quickest, with O(n) time, by just iterating over
# when we see an 'a' push on two ds, and when we
# see a b do nothing, otherwise push on whatever character
# we're at.

def remove_and_replace(a):
    result = []
    for i in a:
        if i == 'b':
            pass
        elif i == 'a':
            result.append('d')
            result.append('d')
        else:
            result.append(i)
    return result

print(remove_and_replace(['a', 'c', 'd', 'b', 'c', 'a']))

# the problem statement says we don't have to worry about
# preserving subsequent entries, as in if we're given
# an array of length 5, but we're told the length is 4,
# then we just return an array of length 4, with the first
# 4 parts of the original array operated upon

# inserting and deleting are slow but we can do it in n time
# so technically there's the n time and n space solution
# where we just iterate over and perform all those shifts
# in place

# the hint is to pass over the array multiple times.
# how about on the first pass we can delete all b's
# simply by storing where "we" are in the array
# and writing to that spot. then on a second pass
# we can count the size of the full array by
# taking the original length minus the number of bs
# plus one for each a because we'll be adding in
# two d's.
# actually this can be done in 1 pass.
# the final step is to build the array. we can do this
# by and building backwards
# for example we now have an array, after removing
# bs of [a, c, d, c, a, _, _]. we can start at the rightmost
# 'a', adding 2 ds to the end of the array giving us
# [a, c, d, c, a, d, d]. then we add a c
# [a, c, d, c, c, d, d], then a d
# [a, c, d, d, c, d, d], then a c
# [a, c, c, d, c, d, d], then finally
# two more ds
# [d, d, c, d, c, d, d]
# this entire algorithm is sort of based around us having extra space
# at the end of the array

def replace_and_remove(s, size):
    

print(replace_and_remove(['c', 'd', 'b', 'c', 'a', 'b'], 4))
