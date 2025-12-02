'''
221. Maximal Square
Attempted
Medium
Topics
premium lock iconCompanies

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.


'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0

        def is_valid(corners):
            for corner in corners:
                if corner[0]<0 or corner[0]>len(matrix)-1:
                    print('out of bound')
                    return False
                if corner[1]<0 or corner[1]>len(matrix[0])-1:
                    print('out of bound')
                    return False
            return True
        def check_square(corners, size):
            for i in range(corners[0][0], corners[0][0]+size):
                for j in range(corners[0][1], corners[0][1]+size):
                    print('checking ', i, j)
                    if matrix[i][j] == '0':
                        return False
            return True
        def expand_square(corners, size):
            nonlocal max_square
            new_size = size + 2
            new_corners = [[corners[0][0]-1, corners[0][1]-1], [corners[1][0]+1, corners[1][1]-1], [corners[2][0]-1, corners[2][1]+1], [corners[3][0]+1, corners[3][1]+1]]
            print('expanded corners ', new_corners)
            if is_valid(new_corners):
                if check_square(new_corners, new_size):
                    max_square = max(max_square, new_size**2)
                    expand_square(new_corners, new_size)
            return

        #1 square check
        for x in matrix:
            for y in x:
                if y=='1':
                    max_square = 1
                    break
        #check for 2x2 then expand
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                corners = [[i,j], [i+1,j], [i,j+1], [i+1,j+1]]
                print('validating corners ', corners)
                if is_valid(corners):
                    if check_square(corners, 2):
                        max_square = max(max_square, 4)
                        expand_square(corners, 2)
        return max_square
