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
