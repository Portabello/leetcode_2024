# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        l=0
        while cur:
            l+=1
            cur = cur.next
        print(l, head.val)
        node_to_remove = l-n
        i=0
        cur = head
        last = None
        while cur:
            next_node = cur.next
            if i==node_to_remove:
                if last == None:
                    head = head.next
                    cur = cur.next
                else:
                    last.next = next_node
                    last = cur
                    cur = next_node
            else:
                last = cur
                cur = cur.next
            i+=1
        return head
