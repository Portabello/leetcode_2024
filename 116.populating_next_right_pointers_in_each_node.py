'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nodes_at_level = [root]
        if root == None:
            return
        while True:
            #print(nodes_at_level)
            for i,x in enumerate(nodes_at_level):
                if i==len(nodes_at_level)-1:
                    x.next=None
                else:
                    x.next=nodes_at_level[i+1]
            if nodes_at_level[0].left==None:
                break
            t=[]
            for x in nodes_at_level:
                t.append(x.left)
                t.append(x.right)
            nodes_at_level = t
        return root

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nodes_at_level = [root]
        if root == None:
            return
        while True:
            #print(nodes_at_level)
            for i,x in enumerate(nodes_at_level):
                if i==len(nodes_at_level)-1:
                    x.next=None
                else:
                    x.next=nodes_at_level[i+1]
            if nodes_at_level[0].left==None:
                break
            t=[]
            for x in nodes_at_level:
                t.append(x.left)
                t.append(x.right)
            nodes_at_level = t
        return root
