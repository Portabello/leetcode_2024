'''
111. Minimum Depth of Binary Tree
Solved
Easy
Topics
premium lock iconCompanies

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5



Constraints:

    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = [2**31]
        if not root:
            return 0
        def traverse(node, depth):
            new_depth = depth + 1
            if not node.left and not node.right:
                min_depth[0] = min(new_depth, min_depth[0])
            if node.left:
                traverse(node.left, new_depth)
            if node.right:
                traverse(node.right, new_depth)
        traverse(root, 0)
        return min_depth[0]
