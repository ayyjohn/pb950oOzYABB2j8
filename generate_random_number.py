import random
# write a function that generates a random number between
# a and b inclusive given a random number generator that
# produces 0 and 1 with equal likelihood. all values
# should be equally likely

# to simulate a 3 sided die, flip 2 coins, and treat
# each flip as a bit, ie the possible results are
# 00, 01, 10, and 11, in binary, which equate to
# 0, 1, 2, and 3. if the result is 0, try again
# otherwise, return 1, 2, or 3. 1, 2, and 3 were all
# equally likely.

def three_sided_die():
    choice = 0
    while not choice:
        choice = random.choice([0, 1, 2, 3])
    return choice

def six_sided_die():
    choice = 8
    while choice > 5:
        choice = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
    return choice + 1

rolls = []
for i in range(100000):
    rolls.append(six_sided_die())

print(rolls.count(1))
print(rolls.count(2))
print(rolls.count(3))
print(rolls.count(4))
print(rolls.count(5))
print(rolls.count(6))

def random_number(a, b):
    num_range = b - a + 1
    while True:
        result, i = 0, 0
        while (1 << i) < num_range:
            result = (result << 1) | random.choice([0, 1])
            i += 1
        if result < num_range:
            break
    return result + b
