"""
2. Add Two Numbers
Medium
29.5K
5.7K
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_s = self.r_f(l1)
        l2_s = self.r_f(l2)
        int_ans =  int(l1_s[::-1]) + int(l2_s[::-1])
        int_ans = str(int_ans)[::-1] 
        ans = ListNode(None, None)
        current = ans
        for i,x in enumerate(int_ans):
            current.val = int(x)
            if(i<len(str(int_ans))-1):
                current.next = ListNode(None,None)
                current = current.next
        return ans
    def r_f(self, l):
        if l:
            return str(l.val) + self.r_f(l.next)
        return ""
