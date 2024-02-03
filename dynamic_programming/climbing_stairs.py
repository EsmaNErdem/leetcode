# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Input: n = 2
# Output: 2

# Input: n = 3
# Output: 3

def climbing_stairs(n):
    prev1 = 1 
    prev2 = 1
    curr = 1
    for _ in range(1, n):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return curr

print(climbing_stairs(2) == 2)
print(climbing_stairs(3) == 3)

