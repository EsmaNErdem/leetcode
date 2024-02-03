# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Input: m = 3, n = 7
# Output: 28

# Input: m = 3, n = 2
# Output: 3

def unique_paths(m,n):
    # filling initilized list to map out to board
    dp = [[1 for _ in range(n)]for _ in range(m)]

    for r in range(1, m):
        for c in range(1, n):
            # there are two way we arrive to current cell from up cell and left cell since the robot can only move down and right
            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[m-1][n-1]

print(unique_paths(3, 7) == 28)
print(unique_paths(3, 2) == 3)