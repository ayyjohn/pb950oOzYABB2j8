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

# there's also an iterative approach. starting with the first
# element, track the farthest element that we can reach. the farthest
# element that we can reach is at i + array[i], and if at any time
# i surpasses that value then we can't get to the end of the array

def can_reach_end(array):
    furthest_so_far, last_index = 0, len(array) - 1
    i = 0

    while i <= furthest_so_far and furthest_so_far < last_index:
        furthest_so_far = max(furthest_so_far, array[i] + i)
        i += 1
    return furthest_so_far >= last_index
