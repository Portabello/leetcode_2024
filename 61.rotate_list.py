'''
61. Rotate List
Solved
Medium
Topics
Companies

Given the head of a linked list, rotate the list to the right by k places.



Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]



Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or k==0:
            return head
        if head.next==None:
            return head
        list_length = 0
        t=head
        while t:
            list_length+=1
            t=t.next
        print(list_length)
        rotated_head = head
        if (list_length - (k%list_length))==0:
            return head
        for i in range(list_length - (k%list_length)):
            rotated_head = rotated_head.next
        print(rotated_head)
        if rotated_head==None:
            return head

        last=None
        second_half=head
        for x in range(list_length):
            if head==rotated_head:
                print('found element', head)
                last.next=None
            last=head
            head=head.next
        print(second_half)

        t=rotated_head
        while True:
            if t.next==None:
                t.next=second_half
                break
            t=t.next
        return rotated_head
