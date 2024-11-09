'''
200. Number of Islands
Solved
Medium
Topics
Companies

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        grid = grid[::]

        def recursive_island_cleaner(i,j):
            grid[i][j] = 0
            #up
            if i != 0:
                if grid[i-1][j] == '1':
                    recursive_island_cleaner(i-1, j)
            #down
            if i != len(grid)-1:
                if grid[i+1][j] == '1':
                    recursive_island_cleaner(i+1, j)
            #left
            if j != 0:
                if grid[i][j-1] == '1':
                    recursive_island_cleaner(i, j-1)
            #right
            if j != len(grid[0])-1:
                if grid[i][j+1] == '1':
                    recursive_island_cleaner(i, j+1)
            return


        island_found_flag = False
        #find next 1 in grid if it exists:
        while True:
            island_found_flag = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        #print('island start found @ [',i,',',j,']')
                        island_count += 1
                        #clean island from grid
                        recursive_island_cleaner(i,j)
                        #print(grid)
                        island_found_flag = True
            if island_found_flag == False:
                return island_count
        return island_count
