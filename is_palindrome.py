# write a function that takes in a string
# and returns true if the string is
# palindromic

def is_palindrome(string):
    # note that ~i = -i - 1
    return all(string[i] == string[~i] for i in range(len(string) // 2))
