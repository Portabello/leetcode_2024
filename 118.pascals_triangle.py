"""
118. Pascal's Triangle
Easy
12.2K
395
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
testing
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        while numRows > 1:
            numRows -= 1
            t = []
            if ans[-1] == [1]:
                ans.append([1,1])
            else:
                for i in range(len(ans[-1])-1):
                    t.append(ans[-1][i] + ans[-1][i+1])
                t.insert(0, 1)
                t.append(1)
                ans.append(t)
        return ans
