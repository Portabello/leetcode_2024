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



Example  1:


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
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node_sum = 2
                cur_node = grid[i][j]
                if cur_node ==0:
                    node_sum-=2
                #top
                if i==0:
                    node_sum += cur_node
                else:
                    if grid[i-1][j]<cur_node:
                        node_sum += cur_node - grid[i-1][j]
                #bottom
                if i == len(grid)-1:
                    node_sum += cur_node
                else:
                    if grid[i+1][j]<cur_node:
                        node_sum += cur_node - grid[i+1][j]
                #left
                if j == 0:
                    node_sum += cur_node
                else:
                    if grid[i][j-1]<cur_node:
                        node_sum += cur_node - grid[i][j-1]
                #right
                if j == len(grid[0])-1:
                    node_sum += cur_node
                else:
                    if grid[i][j+1]<cur_node:
                        node_sum += cur_node - grid[i][j+1]
                #print('[',i,',',j,'] node: ',cur_node, '  sum: ',node_sum)
                ans += node_sum
        return ans
