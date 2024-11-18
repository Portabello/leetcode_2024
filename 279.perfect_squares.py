'''
279. Perfect Squares
Solved
Medium
Topics
Companies

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.



Constraints:

    1 <= n <= 104

'''
import math
class Solution:
    def numSquares(self, n: int) -> int:
        #gen all squares from 0,n
        squares = []
        i=1
        while (i*i) <= n:
            squares.append(i*i)
            i+=1
        #print(squares)
        '''
        res=[float('inf')]
        def rc(remaining, len):
            if remaining == 0:
                #print('solution found')
                res[0] = min(res[0], len)
            elif remaining < 0:
                return
            for x in squares:
                new_remaining = remaining - x
                rc(new_remaining, len+1)
        rc(n,0)
        return res[0]
        '''
        def min_elements_to_sum(arr, target):
            # Initialize dp array with a large value (infinity), and dp[0] = 0
            dp = [float('inf')] * (target + 1)
            dp[0] = 0  # It takes 0 elements to sum up to 0

            # Loop through all possible targets up to the given target
            for i in range(1, target + 1):
                for num in arr:
                    if i - num >= 0:
                        print('dp[',i,'] = min(dp[',i,']=',dp[i],' , dp[',i,'-',num,']=',dp[i-num],'+1')
                        dp[i] = min(dp[i], dp[i - num] + 1)

            # If dp[target] is still infinity, return -1, meaning it's not possible to reach the target
            return dp[target] if dp[target] != float('inf') else -1
        return min_elements_to_sum(squares, n)
