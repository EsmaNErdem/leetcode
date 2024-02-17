# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Input: root = [1,2,3]
# Output: 6

# Input: root = [-10,9,20,null,null,15,7]
# Output: 42

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_Sum(root):
    res = [float('-inf')]

    def dfs_max(node):
        if not node:
            return 0
        
        right = dfs_max(node.right)
        left = dfs_max(node.left)

        res[0] = max(left + node.val + right, res[0])

        return max(0, node.val + right, node.val + left)
    
    dfs_max(root)

    return res[0]