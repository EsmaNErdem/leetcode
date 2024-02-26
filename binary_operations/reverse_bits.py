# Reverse bits of a given 32 bits unsigned integer.

# Input: n = 00000010100101000001111010011100
# Output:    964176192

# Input: n = 11111111111111111111111111111101
# Output:   3221225471 

def reverse_bits(n):
    res = 0
    for i in range(32):
        bit = n >> i & 1
        res = bit << (31-i) | res

    return res
