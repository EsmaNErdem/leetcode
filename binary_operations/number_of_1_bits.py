# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Input: n = 00000000000000000000000000001011
# Output: 3

# Input: n = 00000000000000000000000010000000
# Output: 1

# Input: n = 11111111111111111111111111111101
# Output: 31

def hamming_weight(n):
    count = 0 
    while n:
        if n & 1:
            count += 1
        n >> 1

    return count