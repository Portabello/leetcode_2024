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
        direction = 'right'
        seen = set()
        matrix_len = len(matrix[0])*len(matrix)
        #print(matrix_len)
        i,j=0,0
        ans = []
        while len(seen)<matrix_len:
            #print(direction, i,j)
            #print('seen', seen)
            ans.append(matrix[i][j])
            seen.add((i,j))
            if direction=='right':
                if j==len(matrix[0])-1 or (i,j+1) in seen:
                    direction='down'
                    i+=1
                else:
                    j+=1
            elif direction=='down':
                if i==len(matrix)-1 or (i+1,j) in seen:
                    direction='left'
                    j-=1
                else:
                    i+=1
            elif direction=='left':
                if j==0 or (i,j-1) in seen:
                    direction='up'
                    i-=1
                else:
                    j-=1
            elif direction=='up':
                if i==0 or (i-1,j) in seen:
                    direction='right'
                    j+=1
                else:
                    i-=1
        #print(ans)
        return ans
