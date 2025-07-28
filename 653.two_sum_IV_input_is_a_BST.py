'''
653. Two Sum IV - Input is a BST
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.



Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hs = {}
        ans = [False]
        def traverse(node):
            if k-node.val in hs:
                ans[0] = True
            hs[node.val] = 1
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(root)
        return ans[0]
