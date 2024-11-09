'''
82. Remove Duplicates from Sorted List II
Medium
Topics
Companies

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]



Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        og_head = head
        while head:
            if head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                break
        return og_head
        '''
        occured_once = []
        duplicates = []
        iterator = head
        while iterator:
            if iterator.val not in occured_once:
                occured_once.append(iterator.val)
            elif iterator.val in occured_once and iterator.val not in duplicates:
                duplicates.append(iterator.val)
            iterator = iterator.next
        print(duplicates)


        iterator = head
        prev = None
        while iterator:
            if iterator.val in duplicates:
                if prev:
                    #t = iterator
                    prev.next = iterator.next
                    iterator = iterator.next
                else:
                    iterator = iterator.next
                    head = iterator
            else:
                prev = iterator
                iterator = iterator.next
        return head
        
