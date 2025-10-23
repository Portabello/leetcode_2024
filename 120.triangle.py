'''
120. Triangle
Solved
Medium
Topics
Companies

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10



Constraints:

    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        min_path = [float(inf)]
        def recurse(i, row, cursum):
            cursum += triangle[row][i]
            if row == len(triangle)-1:
                min_path[0] = min(cursum, min_path[0])
                return
            recurse(i, row+1, cursum)
            recurse(i+1, row+1, cursum)
        recurse(0, 0, 0)
        return min_path[0]
        '''
        dp = [row[:] for row in triangle]
        #print(dp)
        for i,row in enumerate(triangle):
            if i!=0:
                for x in range(len(row)):
                    #print("dp[",i,"][",x,"] = ", dp[i-1][max(0,x-1)], ' - ', dp[i-1][min(x, len(dp[i-1])-1)])
                    dp[i][x] = dp[i][x] + min(dp[i-1][max(0,x-1)], dp[i-1][min(x, len(dp[i-1])-1)])
        #print(dp)
        return min(dp[-1])
