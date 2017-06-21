# given a string containing a set of words separated by whitespace, transform
# it into a sentence where all the words appear in reverse order

# this can be done by first reversing the entire string, then
# reversing each individual word

def reverse_words(s):

    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end += 1

    start = 0
    while 1:
        end = s.find(b' ', start)
        if end < 0:
            break
        reverse_range(s, start, end - 1)
        start = end + 1
    reverse_range(s, start, len(s) - 1)
