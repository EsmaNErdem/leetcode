# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [1,2,3,1]
# Output: 4

# Input: nums = [2,7,9,3,1]
# Output: 12

def house_robber(nums):

    length = len(nums)

    if length == 0: return 0
    if length == 1: return nums[0]
    if length == 2: return max(nums[0], nums[1])


    dp = [0] * length
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, length):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    return dp[length-1]

print(house_robber([1,2,3,1]) == 4)
print(house_robber([2,7,9,3,1]) == 12)
