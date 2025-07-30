'''
543. Diameter of Binary Tree
Solved
Easy
Topics
Companies

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        node_diameter = [0, 0]
        def diameterOfNode(node, side, cur_diameter):
            if side=='root':
                #if not node.left and not node.right:
                #    node_diameter[0] = max(node_diameter[0], cur_diameter+1)
                #    node_diameter[1] = max(node_diameter[1], cur_diameter+1)
                if node.left:
                    diameterOfNode(node.left, 'left', 1)
                if node.right:
                    diameterOfNode(node.right, 'right', 1)
            else:
                if not node.left and not node.right:
                    if side=='left':
                        node_diameter[0] = max(node_diameter[0], cur_diameter)
                    if side=='right':
                        node_diameter[1] = max(node_diameter[1], cur_diameter)
                if node.left:
                    diameterOfNode(node.left, side, cur_diameter+1)
                if node.right:
                    diameterOfNode(node.right, side, cur_diameter+1)
        max_diameter = [0]
        def traverse(node):
            node_diameter[0] = 0
            node_diameter[1] = 0
            diameterOfNode(node, 'root', 0)
            #print(node.val, node_diameter)
            max_diameter[0] = max(max_diameter[0], (node_diameter[0]+node_diameter[1]))
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(root)
        return max_diameter[0]
