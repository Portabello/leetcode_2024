"""
463. Island Perimeter
Easy
6.1K
315
Companies
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #a land block can either be the following conifgurations...

        # perimeter = 3 - only connected to 1 other land

        # perimeter = 2 - only connected to 2 other land 

        # perimeter = 1 - only connected to 3 other land

        # perimeter = 0 - land locked
        perimeter = 0
        print(grid)
        for x_i,x in enumerate(grid):
            for y_i,y in enumerate(x):
                print(x_i,y_i," - ",y)
                if(grid[x_i][y_i] == 1):
                    land_sides = 0
                    if(x_i-1 >= 0):
                        if(grid[x_i-1][y_i] == 1):
                            land_sides += 1
                    if(y_i-1 >= 0):
                        if(grid[x_i][y_i-1] == 1):
                            land_sides += 1
                    if(x_i+1 < len(grid)):
                        if(grid[x_i+1][y_i] == 1):
                            land_sides += 1
                    if(y_i+1 < len(x)):
                        if(grid[x_i][y_i+1] == 1):
                            land_sides += 1
                    print("landsides ",land_sides)
                    if(land_sides == 0):
                        perimeter += 4
                    if(land_sides == 1):
                        perimeter += 3
                    if(land_sides == 2):
                        perimeter += 2
                    if(land_sides == 3):
                        perimeter += 1
        return perimeter
