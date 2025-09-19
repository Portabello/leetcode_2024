"""
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None
        while list1 or list2:
            if list1 and not list2:
                if head == None:
                    head = list1
                    cur = list1
                else:
                    cur.next = list1
                    cur = cur.next
                list1 = list1.next
            elif list2 and not list1:
                if head == None:
                    head = list2
                    cur = list2
                else:
                    cur.next = list2
                    cur = cur.next
                list2 = list2.next
            elif list1 and list2:
                if list1.val<list2.val:
                    next_node = list1
                    list1 = list1.next
                else:
                    next_node = list2
                    list2 = list2.next
                if head == None:
                    head = next_node
                    cur = next_node
                else:
                    cur.next = next_node
                    cur = cur.next
        return head
