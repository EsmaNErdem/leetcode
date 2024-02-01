# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false


def is_valid_bst(root):
    def valid(left, node, right):
        if not node:
            return True
        
        if not(left < node.val and node.val < right):
            return False
        
        return is_valid_bst(left, node.left, node.val) and is_valid_bst(node.val, node.right, right)
    
    return valid(float("-inf"), root, float("inf"))