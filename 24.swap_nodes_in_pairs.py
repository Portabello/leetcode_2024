'''
24. Swap Nodes in Pairs
Solved
Medium
Topics
Companies

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]



Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return_head = None
        if head == None:
            return head
        if head:
            if head.next:
                return_head = head.next
            else:
                return head
        current = head
        last = None
        while current:
            if current.next:
                t = current.next
                current.next = t.next
                t.next = current
                if last:
                    last.next = t
                last = t.next
                current = current.next
            else:
                break
            #print(current)
            #print(last)
        return return_head
