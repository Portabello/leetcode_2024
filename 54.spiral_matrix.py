'''
54. Spiral Matrix
Solved
Medium
Topics
Companies
Hint

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        total_matrix_length = len(matrix)*len(matrix[0])
        ans = []


        while not self.is_empty(matrix):
            print('matrix - ',matrix)

            end_found = False
            #top side
            for i in range(0,len(matrix[0])):
                if matrix[0][i]==None:
                    end_found = True
                    break
                ans.append(matrix[0][i])
                print('top appending ', matrix[0][i])
                matrix[0][i] = None
            #right side
            if end_found == False:
                for i in range(1,len(matrix)):
                    if matrix[i][len(matrix[0])-1]==None:
                        end_found = True
                        break
                    ans.append(matrix[i][len(matrix[0])-1])
                    print('right appending ', matrix[i][len(matrix[0])-1])
                    matrix[i][len(matrix[0])-1] = None
            #bottom side
            if end_found == False:
                for i in range(len(matrix[0])-2,-1,-1):
                    if matrix[len(matrix)-1][i]==None:
                        end_found = True
                        break
                    ans.append(matrix[len(matrix)-1][i])
                    print('bottom appending ', matrix[len(matrix)-1][i])
                    matrix[len(matrix)-1][i] = None
            #left side
            if end_found == False:
                for i in range(len(matrix)-2,-1,-1):
                    print(i)
                    if matrix[i][0]==None:
                        end_found = True
                        break
                    ans.append(matrix[i][0])
                    print('left appending ', matrix[i][0])
                    matrix[i][0] = None
            print('ans - ', ans)
            print('------------')
            matrix = self.remove_perimeter(matrix)
        return ans

    def remove_perimeter(self, matrix):
        return [row[1:-1] for row in matrix[1:-1]]
    def is_empty(self,matrix):
        return not matrix or not matrix[0]
