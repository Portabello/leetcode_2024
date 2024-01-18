"""
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        for x in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one
        
        
    """    o(n^2)
        ans = self.r_f(0,n)
        return ans
    def r_f(self, x, n):
        if x>n:
            return 0
        if x==n:
            return 1
        if x<n:
            return self.r_f(x+1, n) + self.r_f(x+2, n)
    """