# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Input: nums = [2,3,-2,4]
# Output: 6

# Input: nums = [-2,0,-1]
# Output: 0

def max_product_subarray(nums):
    dp = [1] * len(nums)
    dp[0] = nums[0]
    max_product = dp[0]
    min_product = dp[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            dp[i] = max(nums[i], nums[i] * min_product)
            min_product = min(nums[i], dp[i-1] * nums[i])

        else:
            dp[i] = max(nums[i], dp[i-1] * nums[i])
            min_product = min(nums[i], min_product * nums[i])

        max_product = max(dp[i], max_product)

    return max_product

print(max_product_subarray([2,3,-2,4]))
print(max_product_subarray([-2,0,-1]))