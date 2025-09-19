'''
19. Remove Nth Node From End of List
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]



Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz



Follow up: Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr,l = head, 0
        while itr:
            l+=1
            itr = itr.next
        index=0
        cur, last = head, None
        while cur:
            if index == (l-n):
                if last == None:
                    if cur.next == None:
                        return None
                    else:
                        return cur.next
                else:
                    last.next = cur.next
                    break
            else:
                last = cur
                cur = cur.next
                index += 1
        return head
