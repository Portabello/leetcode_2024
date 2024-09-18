'''
1137. N-th Tribonacci Number
Solved
Easy
Topics
Companies
Hint

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537



Constraints:

    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


'''
class Solution:
    def tribonacci(self, n: int) -> int:
        n1,n2,n3 = 0,0,0
        current = 0
        for i in range(n+1):
            if i == 0:
                pass
            if i == 1:
                current = 1
            if i == 2:
                current = 1
                n1 = 1
            else:
                n3 = n2
                n2 = n1
                n1 = current
                current = n1+n2+n3
        return current
