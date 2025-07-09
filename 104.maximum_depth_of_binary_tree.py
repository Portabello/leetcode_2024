"""
104. Maximum Depth of Binary Tree
Easy
12.2K
203
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxdepth = [0]
        def traverse(node, depth):
            newdepth = depth + 1
            if not node.left and not node.right and newdepth>maxdepth[0]:
                maxdepth[0] = newdepth
            if node.left:
                traverse(node.left, newdepth)
            if node.right:
                traverse(node.right, newdepth)
        traverse(root, 0)
        return maxdepth[0]
