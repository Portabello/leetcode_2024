"""
896. Monotonic Array
Solved
Easy
Topics
Companies
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.



Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false


Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = -1, -1
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if inc == -1:
                if nums[i] < nums[i+1]:
                    inc, dec = 1, 0
                if nums[i] > nums[i+1]:
                    inc, dec = 0, 1
            if inc == 1:
                if nums[i] > nums[i+1]:
                    return False
            if dec == 1:
                if nums[i] < nums[i+1]:
                    return False
        return True
