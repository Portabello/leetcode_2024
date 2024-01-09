"""
1584. Min Cost to Connect All Points
Medium
4.8K
117
Companies
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = []
        frontier = []
        cost = 0
        while len(visited) != len(points):
            if len(visited) == 0:
                visited.append(points[0])
            else:
                self.add_new_edges(visited, points, frontier)
                new_min = self.find_min_edge(frontier)
                visited.append(new_min[0])
                self.remove_from_frontier(frontier, new_min[0])
                cost += new_min[1]
        return cost

    def remove_from_frontier(self, frontier, point):
        for i,x in enumerate(frontier):
            if x[0] == point:
                frontier.pop(i)


    def find_min_edge(self, frontier):
        min_edge = None
        min_index = None
        for i,x in enumerate(frontier):
            
            if min_edge == None or x[1] < min_edge[1]:
                min_edge = x
                min_index = i
        return min_edge

    def add_new_edges(self, visited, points, frontier):
        last_visited = visited[-1]
        for x in points:
            if x not in visited:
                dist = self.manhattan_distance(last_visited, x)
                frontier.append([x,dist])

    def manhattan_distance(self, a: List[int], b: List[int]) -> int:
        return ((abs(a[0]-b[0]))+(abs(a[1]-b[1])))