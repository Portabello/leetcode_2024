"""
1496. Path Crossing
Solved
Easy
Topics
Companies
Hint
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0,0))
        print(visited)
        cur_pos = (0,0)
        for x in path:
            if x=='N':
                cur_pos = (cur_pos[0], cur_pos[1]+1)
                if cur_pos in visited:
                    return True
                visited.add(cur_pos)
            elif x=='S':
                cur_pos = (cur_pos[0], cur_pos[1]-1)
                if cur_pos in visited:
                    return True
                visited.add(cur_pos)
            elif x=='E':
                cur_pos = (cur_pos[0]+1, cur_pos[1])
                if cur_pos in visited:
                    return True
                visited.add(cur_pos)
            elif x=='W':
                cur_pos = (cur_pos[0]-1, cur_pos[1])
                if cur_pos in visited:
                    return True
                visited.add(cur_pos)
            print(x, visited)
        return False