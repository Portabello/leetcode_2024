'''
783. Minimum Distance Between BST Nodes
Solved
Easy
Topics
Companies
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
elements = []
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global elements
        elements = []
        self.read(root)
        #print(elements)
        min_diff = None
        for i in range(0,len(elements)):
            for j in range(i+1, len(elements)):
                #print(i,j)
                if min_diff == None or abs(elements[i]-elements[j]) < min_diff:
                    min_diff = abs(elements[i]-elements[j])
        return min_diff


    def read(self, root):
        global elements
        elements.append(root.val)
        if root.left:
            self.read(root.left)
        if root.right:
            self.read(root.right)
