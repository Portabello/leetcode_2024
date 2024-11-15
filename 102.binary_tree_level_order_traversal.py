'''
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
Companies

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        levels = [0]
        hs = {}

        def rc(root, level):
            if root == None:
                return
            levels[0] = max(levels[0], level)
            if level in hs:
                hs[level].append(root.val)
            else:
                hs[level] = [root.val]
            rc(root.left, level+1)
            rc(root.right, level+1)

        rc(root, 0)
        #print(levels)
        #print(hs)
        ans = [[] for _ in range(levels[0]+1)]
        for i,x in enumerate(ans):
            if i in hs:
                ans[i] = hs[i]
        return ans
