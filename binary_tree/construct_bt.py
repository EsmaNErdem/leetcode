# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(preorder, inorder):

    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    ind = inorder.index(preorder[0])

    root.left = construct_binary_tree(preorder[1: ind+1], inorder[:ind])
    root.right = construct_binary_tree(preorder[ind+1:], inorder[ind+1:])

    return root


print(construct_binary_tree([3,9,20,15,7], [9,3,15,20,7]))
