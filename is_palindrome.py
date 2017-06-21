# write a function that takes in a string
# and returns true if the string is
# palindromic

def is_palindrome(string):
    # note that ~i = -i - 1
    return all(string[i] == string[~i] for i in range(len(string) // 2))

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+ 1, j - 1
    return True
