'''
73. Set Matrix Zeroes
Solved
Medium
Topics
Companies
Hint

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]



Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1



Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerod_cols, zerod_rows = set(), set()
        def zero_col(col, matrix):
            for j in range(len(matrix[0])):
                matrix[col][j]=0
        def zero_row(row, matrix):
            for i in range(len(matrix)):
                matrix[i][row]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zerod_cols.add(i)
                    zerod_rows.add(j)
        print(zerod_cols, zerod_rows)
        for i in zerod_cols:
            zero_col(i, matrix)
        for j in zerod_rows:
            zero_row(j, matrix)
        
