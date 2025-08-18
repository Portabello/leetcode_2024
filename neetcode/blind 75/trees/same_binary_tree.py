# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans= [True]
        def traverse(p,q):
            if not p and q or not q and p:
                ans[0] = False
                return
            if not p and not q:
                return
            if p.val !=q.val:
                ans[0] = False
            if p.right and not q.right:
                ans[0] = False
            if p.left and not q.left:
                ans[0] = False
            if q.right and not p.right:
                ans[0] = False
            if q.left and not p.left:
                ans[0] = False
            if p.left and q.left:
                traverse(p.left,q.left)
            if p.right and q.right:
                traverse(p.right,q.right)

        traverse(p,q)
        return ans[0]
