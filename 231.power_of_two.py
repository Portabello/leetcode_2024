"""
231. Power of Two
Easy
6.1K
392
Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false


Constraints:

-231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        l,r = 0,32
        while l<=r:
            m = (l+r)//2
            cur = 2**m
            if cur == n:
                return True
            elif cur < n:
                l=m+1
            else:
                r=m-1
        return False
