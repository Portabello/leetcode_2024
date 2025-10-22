'''
114. Flatten Binary Tree to Linked List
Solved
Medium
Topics
Companies
Hint

Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.



Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]



Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tree = []
        def r(node):
            if not node:
                return
            tree.append(node.val)
            r(node.left)
            r(node.right)
        r(root)
        if len(tree)==0:
            return None
        cur = root
        for i,x in enumerate(tree):
            cur.val = x
            cur.left = None
            if i!=len(tree)-1:
                cur.right = TreeNode()
                cur = cur.right
