'''
1925. Count Square Sum Triples
Solved
Easy
Topics
Companies
Hint

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.



Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).



Constraints:

    1 <= n <= 250

'''
import math
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1,n):
            for b in range(1,n):
                c = math.sqrt((a**2)+(b**2))
                if c.is_integer() and c<=n:
                    #print('found triple! ', a, '** + ',b, '** = ', c,'**')
                    ans += 1
        return ans
