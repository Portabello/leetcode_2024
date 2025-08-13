# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head:
            next_node = head.next
            head.next = last
            if not next_node:
                return head
            last = head
            head = next_node
        
