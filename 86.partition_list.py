'''
86. Partition List
Solved
Medium
Topics
Companies

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]



Constraints:

    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #make 2 new LLs a under and over
        '''
        mid = None
        under = None
        under_head = None
        over = None
        over_head = None
        over_count = 0
        under_count = 0
        while head:
            print('loop', head.val)
            #print('under',under)
            #print('over',over)
            if head.val == x and mid == None:
                mid = x
            elif head.val < x:
                under_count += 1
                if under_head == None:
                    under_head = head
                    under = head
                    #under.next = None
                else:
                    under.next = head
                    under = under.next
                    #under.next = None
            elif head.val >= x:
                over_count += 1
                if over_head == None:
                    over_head = head
                    over = head
                    #over.next = None
                else:
                    over.next = head
                    over = over.next
                    #over.next = None
            head = head.next
        #under.next = None
        #over.next = None
        print(mid)
        print(under_head)
        print(under_count)
        print(over_head)
        print(over_count)
        '''
        if head == None or head.next == None:
            return head
        #make 2 new LLs a under and over
        under = None
        under_head = None
        over = None
        over_head = None
        over_count = 0
        under_count = 0
        while head:
            #print('loop', head.val)
            #print('under',under)
            #print('over',over)
            if head.val < x:
                under_count += 1
                if under_head == None:
                    under_head = ListNode(head.val)
                    under = under_head
                    #under.next = None
                else:
                    under.next = ListNode(head.val)
                    under = under.next
                    #under.next = None
            elif head.val >= x:
                over_count += 1
                if over_head == None:
                    over_head = ListNode(head.val)
                    over = over_head
                    #over.next = None
                else:
                    over.next = ListNode(head.val)
                    over = over.next
                    #over.next = None
            head = head.next
        #under.next = None
        #over.next = None
        #print(mid)
        #print(under_head)
        #print(under_count)
        #print(over_head)
        #print(over_count)
        if under:
            under.next = over_head
            return under_head
        return over_head
