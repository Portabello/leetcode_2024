'''
1886. Determine Whether Matrix Can Be Obtained By Rotation
Solved
Easy
Topics
Companies
Hint
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.



Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.


Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        #cw
        for x in range(4):
            mat = self.rotate_clockwise(mat)
            if mat == target:
                return True
        #ccw
        for x in range(4):
            mat = self.rotate_counterclockwise(mat)
            if mat == target:
                return True
        return False
    def rotate_clockwise(self, mat):
        transposed_matrix = list(zip(*mat))
        # Reverse the rows to get the rotated matrix
        rotated_matrix = [list(row)[::-1] for row in transposed_matrix]
        return rotated_matrix
    def rotate_counterclockwise(self, mat):
        # Reverse the rows
        reversed_rows = mat[::-1]
        # Transpose the matrix
        rotated_matrix = list(zip(*reversed_rows))
        return rotated_matrix
