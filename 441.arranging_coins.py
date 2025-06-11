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
        if n==1 or n==2:
            return 1
       # if n==3:
            #return 2
        def triangular_number(x):
            return (x*(x+1))/2
        l,r= 0,n
        while l<=r:
            m=(l+r)//2
            tn = triangular_number(m)
            #print('iteration l=',l,' m=',m,' r=',r)
            #print('testing ', tn)
            if tn>=n:
                #print('1')
                #check layer below
                if tn == n:
                    return m
                tnn = triangular_number(m-1)
                if tnn < n:
                    return m-1
            if tn>=n:
                #print('2')
                r=m
            else:
                #print('3')
                l=m
        return -1
