'''
62. Unique Paths
Solved
Medium
Topics
Companies

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

|cffffffffTinterface/ICONS/Inv_holiday_beerfestsausage02:50:50:0:-1|cfffffffft

Constraints:

    1 <= m, n <= 100

'''
class Solution:
    # O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for x in range(n)] for y in range(m)]
        table[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                t=0
                if i!=0:
                    t+=table[i-1][j]
                if j!=0:
                    t+=table[i][j-1]
                table[i][j]=t
        return table[m-1][n-1]
