"""
485. Max Consecutive Ones
Solved
Easy
Topics
Companies
Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxone = 0
        con = 0
        for x in nums:
            if x==1:
                con += 1
                maxone = max(maxone, con)
            else:
                con = 0
        return maxone