"""
119. Pascal's Triangle II
Solved
Easy
Topics
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #if rowIndex==0:
        #    return [1]
        #if rowIndex==1:
        #    return [1,1]
        ans = []
        for x in range(rowIndex+1):
            #print(x)
            if x == 0:
                ans = [1]
                continue
            if x == 1:
                ans = [1,1]
                continue
            nextans = [1]*(len(ans)+1)
            #print(x, nextans)
            for i in range(1,len(nextans)-1):
                nextans[i] = ans[i-1]+ans[i]
                #print(i)
            ans = nextans
        return ans