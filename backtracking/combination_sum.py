# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Input: candidates = [2], target = 1
# Output: []

def combination_sum(arr, target):
    res = []

    # dfs through the list to try out different combinations
    def dfs(i, combinations, total):
        # backtracking-try
        if total == target:
            res.append(combinations[:])
            return
        # backtracking-base
        if i >= len(arr) or total > target:
            return

        # backtracking-decision
        combinations.append(arr[i])
        dfs(i, combinations, total+arr[i])

        # backtracking-backtrack
        combinations.pop()

        # backtracking-move forward
        dfs(i+1, combinations, total)

    dfs(0, [], 0)

    return res

print(combination_sum([2, 3, 6, 7], 7) == [[2,2,3],[7]])
print(combination_sum([2, 3, 5], 8) == [[2,2,2,2],[2,3,3],[3,5]])