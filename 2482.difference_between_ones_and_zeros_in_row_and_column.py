'''
2482. Difference Between Ones and Zeros in Row and Column
Solved
Medium
Topics
Companies
Hint

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

    Let the number of ones in the ith row be onesRowi.
    Let the number of ones in the jth column be onesColj.
    Let the number of zeros in the ith row be zerosRowi.
    Let the number of zeros in the jth column be zerosColj.
    diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

Return the difference matrix diff.



Example 1:

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

Example 2:

Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 105
    1 <= m * n <= 105
    grid[i][j] is either 0 or 1.

'''
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r_one, r_zero = [0 for _ in range(len(grid))], [0 for _ in range(len(grid))]
        c_one, c_zero = [0 for _ in range(len(grid[0]))], [0 for _ in range(len(grid[0]))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    r_one[r] += 1
                    c_one[c] += 1
                else:
                    r_zero[r] += 1
                    c_zero[c] += 1
        #print(r_one, r_zero)
        #print(c_one, c_zero)
        dif = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        #print(dif)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                dif[r][c] = r_one[r] + c_one[c] - r_zero[r] - c_zero[c]
        return dif
