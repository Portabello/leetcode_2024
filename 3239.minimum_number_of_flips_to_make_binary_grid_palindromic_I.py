'''
3239. Minimum Number of Flips to Make Binary Grid Palindromic I
Solved
Medium
Topics
Companies
Hint

You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.



Example 1:

Input: grid = [[1,0,0],[0,0,0],[0,0,1]]

Output: 2

Explanation:

Flipping the highlighted cells makes all the rows palindromic.

Example 2:

Input: grid = [[0,1],[0,1],[0,0]]

Output: 1

Explanation:

Flipping the highlighted cell makes all the columns palindromic.

Example 3:

Input: grid = [[1],[0]]

Output: 0

Explanation:

All rows are already palindromic.



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m * n <= 2 * 105
    0 <= grid[i][j] <= 1

'''
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def minChanges(arr):
            changes = 0
            n=(len(arr)//2)
            y = len(arr)-1
            #print(n)
            for x in range(n):
                if arr[x] != arr[y]:
                    changes += 1
                y -= 1
            #print(arr, 'needs ', changes, ' changes to be palindromic')
            return changes

        col_changes=0
        for c in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][c])
                #print(i,c)
            #print(col)
            changes = minChanges(col)
            col_changes += changes

        row_changes=0
        for r in grid:
            row_changes += minChanges(r)
        return min(row_changes, col_changes)
