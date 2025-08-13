# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = None
        cur = None
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    if new_head==None:
                        cur,new_head = list1, list1
                        list1 = list1.next
                    else:
                        cur.next = list1
                        cur, list1 = cur.next, list1.next
                else:
                    if new_head==None:
                        cur,new_head = list2, list2
                        list2 = list2.next
                    else:
                        cur.next = list2
                        cur, list2 = cur.next, list2.next
            if list1 and not list2:
                if new_head==None:
                    cur,new_head = list1, list1
                    list1 = list1.next
                else:
                    cur.next = list1
                    cur, list1 = cur.next, list1.next
            if not list1 and list2:
                if new_head==None:
                    cur,new_head = list2, list2
                    list2 = list2.next
                else:
                    cur.next = list2
                    cur, list2 = cur.next, list2.next
        return new_head
