# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longest_consecutive_sequence(nums):

    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if not num - 1 in nums_set:
            sequence  = 0 
            while num in nums_set:
                sequence += 1
                num += 1

            longest = max(longest, sequence)

    return longest

print(longest_consecutive_sequence([100,4,200,1,3,2]) == 4)
print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]) == 9)
