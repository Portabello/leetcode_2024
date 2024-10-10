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
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0:
            return head
        if head.next == None:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
            print(tail.val)
        print('L',length, 'tail', tail.val)
        if k%length == 0:
            return head
        rotate_axis = length - (k%length)
        print('rotate_axis', rotate_axis)
        i = 1
        tmp = head
        new_head = None
        while tmp.next:
            if i == rotate_axis:
                print('rotate found ', tmp.val)
                new_head = tmp.next
                tmp.next = None
                break
            tmp = tmp.next
            i+=1
        print('----')
        print(head)
        print(new_head)
        tail.next = head
        print(new_head)
        return new_head
