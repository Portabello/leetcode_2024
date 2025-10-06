'''
59. Spiral Matrix II
Solved
Medium
Topics
premium lock iconCompanies

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]



Constraints:

    1 <= n <= 20

'''
import itertools
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for x in range(n)]for x in range(n)]
        direction_cycler = itertools.cycle(['right', 'down', 'left', 'up'])
        direction = next(direction_cycler)
        x,y,e=0,0,1
        seen = set()
        for i in range(n*n):
            ans[x][y]=e
            e+=1
            seen.add((x,y))
            if direction=='right':
                if (y==n-1 or (x,y+1) in seen):
                    direction=next(direction_cycler)
                    x+=1
                else:
                    y+=1
            elif direction=='down':
                if (x==n-1 or (x+1,y) in seen):
                    direction=next(direction_cycler)
                    y-=1
                else:
                    x+=1
            elif direction=='left':
                if (y==0 or (x,y-1) in seen):
                    direction=next(direction_cycler)
                    x-=1
                else:
                    y-=1
            elif direction=='up':
                if (x==0 or (x-1,y) in seen):
                    direction=next(direction_cycler)
                    y+=1
                else:
                    x-=1
        return ans
