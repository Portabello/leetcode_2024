'''
143. Reorder List
Solved
Medium
Topics
Companies

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]



Constraints:

    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        if head.next == None:
            return head

        length = 0
        t=head
        while t:
            length += 1
            t = t.next

        first_half = None
        #second_half = None
        first_head = None
        second_head = None

        for i in range(length//2):
            if first_head == None:
                first_head = head
                first_half = first_head
            else:
                first_half = first_half.next
        second_head = first_half.next
        first_half.next = None


        def reverse(LL):
            t=None
            prev = None
            while LL:
                if LL.next == None:
                    LL.next = prev
                    return LL
                t = LL.next
                LL.next = prev
                prev = LL
                LL = t
        second_head = reverse(second_head)
        #print(first_head)
        #print(second_head)
        new = None
        ans = None
        for i in range(length):
            if i%2==0:
                if new == None:
                    new = first_head
                    ans = new
                    first_head = first_head.next
                else:
                    if first_head:
                        new.next = first_head
                        new = new.next
                        first_head = first_head.next
            else:
                if second_head:
                    new.next = second_head
                    new = new.next
                    second_head = second_head.next
            #print(i, ans)
        return ans
