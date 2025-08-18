"""
257. Binary Tree Paths
Easy
6.3K
275
Companies
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.



Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]


Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def traverse(node, cur_path):
            if len(cur_path)==0:
                new_path = str(node.val)
            else:
                new_path = cur_path + '->' + str(node.val)
            if not node.left and not node.right:
                ans.append(new_path)
            if node.left:
                traverse(node.left, new_path)
            if node.right:
                traverse(node.right, new_path)
        traverse(root, "")
        return ans
