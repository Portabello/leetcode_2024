"""
11. Container With Most Water
Solved
Medium
Topics
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        left_ptr = [height[0], 0]
        right_ptr = [height[len(height)-1], len(height)-1]
        #max_area = self.calc_area(left_ptr, right_ptr)
        max_area = 0
        while left_ptr[1] != right_ptr[1]:
            tmp_area = self.calc_area(left_ptr, right_ptr)
            max_area = max(max_area, tmp_area)
            min_side = self.min_side(left_ptr, right_ptr)
            if min_side == "left":
                left_ptr = [height[left_ptr[1]+1], left_ptr[1]+1]
            else:
                right_ptr = [height[right_ptr[1]-1], right_ptr[1]-1]
        return max_area

    def min_side(self, a, b):
        if(a[0]<b[0]):
            return "left"
        return "right"


    def calc_area(self, a, b):
        height = min(a[0], b[0])
        length = abs(a[1]-b[1])
        return int(length*height)