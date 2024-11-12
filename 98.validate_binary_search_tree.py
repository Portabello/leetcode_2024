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
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = [1]
        def rc(root, l, r, parents):
            if root == None:
                #print('end reached, returning')
                return

            #print('examining node: ', root.val, ' to its parents ')
            for parent, side in parents:
                #print('looking at parent...', parent.val, 'from side', side)
                if side == 'L':
                    if root.val >= parent.val:
                        ans[0] = 0
                elif side == 'R':
                    if root.val <= parent.val:
                        ans[0] = 0

            new_parents = parents + [(root, 'L')]
            rc(root.left, True, False, new_parents)
            new_parents = parents + [(root, 'R')]
            rc(root.right, False, True, new_parents)
        rc(root, False, False, [])
        if ans[0]:
            return True
        return False
