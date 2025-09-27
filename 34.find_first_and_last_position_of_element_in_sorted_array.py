'''
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
Companies

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        lowerbound = -1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                if m==0:
                    lowerbound=0
                    break
                if nums[m-1]==target:
                    r=m-1
                else:
                    lowerbound=m
                    break
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1

        l,r=0,len(nums)-1
        upperbound = -1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                if m==len(nums)-1:
                    upperbound=m
                    break
                if nums[m+1]==target:
                    l=m+1
                else:
                    upperbound=m
                    break
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        #print('lowerbound', lowerbound)
        #print('upperbound', upperbound)
        return [lowerbound, upperbound]
