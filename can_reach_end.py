# write a function that takes an array of nonnegative integers.
# each of these nonnegative integers denotes how far the player
# can move from that position. this function should output true
# if the player can get to the last position, and false otherwise

# this feels essentially like a dfs for an array..

def can_reach_end(array, start=0):
    if array[start] >= len(array) - start or len(array) == 1:
        return True
    for i in reversed(range(1, array[start] + 1)):
        if can_reach_end(array, i + start):
            return True
    return False

print(can_reach_end([1, 2, 0, 1]))
print(can_reach_end([1]))
print(can_reach_end([0]))
print(can_reach_end([0, 1]))
print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
print(can_reach_end([3, 2, 0, 0, 2, 0, 1]))


