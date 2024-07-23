'''
812. Largest Triangle Area
Solved
Easy
Topics
Companies
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.



Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000


Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
'''
import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        for x in range(0, len(points)):
            for y in range(x+1, len(points)):
                for z in range(y+1, len(points)):
                    #print(x,y,z)
                    max_area = max(self.area_of_triangle(points[x], points[y], points[z]), max_area)
        return max_area

    def area_of_triangle(self,x,y,z):
        #a = x-y
        a = math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
        #b = y-z
        b = math.sqrt((y[0]-z[0])**2+(y[1]-z[1])**2)
        #c = z-x
        c = math.sqrt((z[0]-x[0])**2+(z[1]-x[1])**2)
        s = (a+b+c)/2
        t = s*(s-a)*(s-b)*(s-c)
        if t>0:
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        else:
            return 0
        return area
