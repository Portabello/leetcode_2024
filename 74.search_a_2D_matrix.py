'''
74. Search a 2D Matrix
Solved
Medium
Topics
Companies

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for row
        def binarySearchRow(matrix, target):
            l,r = 0,len(matrix)-1
            while l<=r:
                m = (l+r)//2
                if target >= matrix[m][0] and target <= matrix[m][len(matrix[0])-1]:
                    return m
                elif target > matrix[m][len(matrix[0])-1]:
                    l = m+1
                else:
                    r = m-1
            return -1
        target_row = binarySearchRow(matrix, target)
        #print(target_row)
        if target_row == -1:
            return False
        # binary search for col
        def binarySearchColumn(row, target):
            l,r = 0,len(row)
            while l<=r:
                m = (l+r)//2
                if row[m] == target:
                    return m
                elif target < row[m]:
                    r = m-1
                else:
                    l = m+1
            return -1

        target_col = binarySearchColumn(matrix[target_row], target)
        #print(target_col)
        if target_col == -1:
            return False
        return True
