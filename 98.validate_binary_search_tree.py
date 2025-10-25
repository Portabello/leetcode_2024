'''
98. Validate Binary Search Tree
Solved
Medium
Topics
Companies

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = [True]
        def recurse(node, left_bound, right_bound, side):
            #root node
            #if parent==None and side == None:
            if not node:
                return
            if not (left_bound < node.val < right_bound):
                valid[0]=False
                return
            if node.left:
                recurse(node.left, left_bound, min(node.val, right_bound), 'left')
            if node.right:
                recurse(node.right, max(left_bound, node.val), right_bound, 'right')
        recurse(root, -float(inf), float(inf), None)
        return valid[0]
