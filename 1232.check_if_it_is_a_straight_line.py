"""
1232. Check If It Is a Straight Line
Solved
Easy
Topics
Companies
Hint
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #get equation of line from first 2 points
        i,j=coordinates[0][0], coordinates[0][1]
        for x in coordinates:
            if i != x[0]:
                i = None
            if j != x[1]:
                j = None
        if i != None or j != None:
            return True
        if coordinates[1][0]-coordinates[0][0] == 0:
            slope = 0
        else:
            slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        b = coordinates[0][1]-(slope*coordinates[0][0])
        for x in range(2,len(coordinates)):
            if coordinates[x][1] != slope*coordinates[x][0] + b:
                return False
        return True