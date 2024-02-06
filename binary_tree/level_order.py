# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Input: root = [1]
# Output: [[1]]

# Input: root = []
# Output: []
from collections import deque 

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    q = deque()
    q.append(root)
    res = []

    while q:
        q_length = len(q)
        level = []
        for _ in range(q_length):
            node = q.popleft()
            if node:
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        if level: res.append(level)

    
    return res
