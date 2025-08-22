"""
283. Move Zeroes
Easy
15.9K
411
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end_index = len(nums)-1
        def moveToEnd(i, end_index, nums):
            t = nums.pop(i)
            nums.insert(end_index, t)
            return nums
        i = 0
        while i<=end_index:
            if nums[i] == 0:
                moveToEnd(i,end_index,nums)
                i-=1
                end_index -=1
            i+=1
        return nums
