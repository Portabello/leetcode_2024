'''
1382. Balance a Binary Search Tree
Solved
Medium
Topics
Companies
Hint

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def rc(root):
            if root == None:
                return
            arr.append(root.val)
            rc(root.left)
            rc(root.right)
        rc(root)
        arr.sort()
        print(arr)
        head = [None]
        def create(arr, parent):
            mid = arr[(len(arr)//2)]
            left = arr[:(len(arr)//2)]
            right = arr[(len(arr)//2)+1:]
            #print('iteration ', left, mid, right)
            new_parent = None

            if parent == None:
                #print('new head')
                new_parent = TreeNode(mid)
                head[0] = new_parent
            elif mid > parent.val:
                #print('new right parent')
                parent.right = TreeNode(mid)
                new_parent = parent.right
            else:
                #print('new left parent')
                parent.left = TreeNode(mid)
                new_parent = parent.left
            if len(left)>0:
                #print('create(', left, new_parent.val,')')
                create(left, new_parent)
            if len(right)>0:
                #print('create(', right, new_parent.val,')')
                create(right, new_parent)
        create(arr, None)
        return head[0]
