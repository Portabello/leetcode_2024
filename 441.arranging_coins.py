"""
441. Arranging Coins
Solved
Easy
Topics
Companies
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.



Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1+2+3+...+n = n(n+1)/2
        for x in range(n+2):
            calc = (x*(x+1))/2
            if calc > n:
                return x-1
