# write a function that takes 3 inputs, a string, an integer b1, and
# an integer b2. the string is in base b1 and the output should be
# that number in base b2 as a string

def base_convert(s, b1, b2):
    x = -1
    val = int(s)
    output = ""
    x = -1
    while 2**(x + 1) <= val:
        x += 1
    for i in reversed(range(x + 1)):
        print(i)
        if val >= 2**i:
            output += '1'
            val -= 2**i
        else:
            output += '0'
    return output
print(base_convert(15, 0, 0))
print(base_convert(8, 0, 0))
