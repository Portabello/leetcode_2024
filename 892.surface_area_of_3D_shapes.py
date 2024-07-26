'''
892. Surface Area of 3D Shapes
Solved
Easy
Topics
Companies
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.



Example 1:


Input: grid = [[1,2],[3,4]]
Output: 34
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 3:


Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Constraints:

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
'''
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        sum = 0
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                #print(y)
                #bottom and top
                if y!= 0:
                    sum += 2
                #up
                if i == 0:
                    sum += y
                elif y>grid[i-1][j]:
                    sum += y-grid[i-1][j]
                #down
                if i == len(grid)-1:
                    sum += y
                elif y>grid[i+1][j]:
                    sum += y-grid[i+1][j]
                #left
                if j==0:
                    sum += y
                elif y>grid[i][j-1]:
                    sum += y-grid[i][j-1]
                #right
                if j==len(x)-1:
                    sum += y
                elif y>grid[i][j+1]:
                    sum+= y-grid[i][j+1]
                print(y, " : ", sum)
        return sum
