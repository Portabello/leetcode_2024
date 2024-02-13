"""
1572. Matrix Diagonal Sum
Solved
Easy
Topics
Companies
Hint
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonals = set()
        #primary diagonal
        diagonals.add((0,0))
        last = [0,0]
        while True:
            if last[0]+1 < len(mat[0]) and last[1]+1 < len(mat):
                diagonals.add((last[0]+1, last[1]+1))
                last = [last[0]+1, last[1]+1]
            else:
                break
        #secondary diagonal
        diagonals.add((0, len(mat[0])-1))
        last = [0, len(mat[0])-1]
        while True:
            print([last[0]+1, last[1]-1])
            if last[0]+1 < len(mat[0]) and last[1]-1 >= 0:
                diagonals.add((last[0]+1, last[1]-1))
                last = [last[0]+1, last[1]-1]
            else:
                break
        sum = 0
        for x in diagonals:
            sum += mat[x[0]][x[1]]
        return sum