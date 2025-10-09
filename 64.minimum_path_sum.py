'''
64. Minimum Path Sum
Medium
Topics
Companies

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200

'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ans = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    ans[i][j]=grid[i][j]
                    continue
                t=99999999
                if i!=0:
                    t=min(ans[i-1][j], t)
                if j!=0:
                    t=min(ans[i][j-1], t)
                ans[i][j] = t + grid[i][j]
        #print(ans)
        return ans[len(grid)-1][len(grid[0])-1]
