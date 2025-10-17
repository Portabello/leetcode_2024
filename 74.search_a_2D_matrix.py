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
        l,r=0,(len(matrix)*len(matrix[0]))-1

        while l<=r:
            m=(l+r)//2
            #print('row',m//len(matrix[0]))
            #print('col',m-(m//len(matrix[0])*len(matrix[0])))
            value = matrix[m//len(matrix[0])][m-(m//len(matrix[0])*len(matrix[0]))]
            #print('value ', value)
            if value==target:
                return True
            if value<target:
                l+=1
            else:
                r-=1
        return False
