# write a function that computes x mod any power of 2 in constant time

# there's an analogy here to base 10. in base 10, any number mod 10 returns
# the last digit, and any number mod 100 gives the last two digits
# therefore in binary modding by any power of 2, ie 2 ** n, just requires
# returning the last n bits. the caveat is n == 0, which requires returning
# the number. but then for n = 1, return the rightmost bit. for n == 2
# it's number mod 4, return the last two bits. this can be done
# by using a n bit bitmask and anding. an n bit bitmask is obtained
# by 2^n - 1 (11 for 4, 111 for 8, 1111 for 16, etc).

def mod_power_of_two(x, power):
    if power == 0:
        return x
    else:
        mask = power - 1
        return x & mask

print(mod_power_of_two(77, 64))
print(mod_power_of_two(128, 64))
print(mod_power_of_two(8, 2))
print(mod_power_of_two(2, 8))
print(mod_power_of_two(12, 8))
