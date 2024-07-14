'''
530. Minimum Absolute Difference in BST
Easy
Topics
Companies
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
nodes = []
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global nodes
        nodes = []
        self.traverse_tree(root)
        print(nodes)
        min_abs_distance = 99999999999
        for i,x in enumerate(nodes):
            for j,y in enumerate(nodes):
                if i!=j:
                    min_abs_distance = min(min_abs_distance, abs(x-y))
        return min_abs_distance

    def traverse_tree(self, root):
        global nodes
        nodes.append(root.val)
        if root.left:
            self.traverse_tree(root.left)
        if root.right:
            self.traverse_tree(root.right)
