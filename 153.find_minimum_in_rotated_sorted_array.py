"""
153. Find Minimum in Rotated Sorted Array
Solved
Medium
Topics
Companies
Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r,m = 0,len(nums)-1, int((len(nums)-1)/2)
        min_val = nums[m]
        #min = min(min, nums[m])
        #print(nums[l], nums[m], nums[r])
        while l<=r:
            if(nums[l]<nums[r]):
                min_val = min(min_val, nums[l])
            min_val = min(min_val, nums[m])
            if nums[m] >= nums[l]:
                #print("search right")
                #search right
                #move l to m+1, keep r, recalc m
                l = m+1
                m = int((r+l)/2)
                #print(nums[l], nums[m], nums[r])
            else:
                #print("search left")
                #search left
                #move r to m-1, keep l, recalc m
                r = m-1
                m = int((r+l)/2)
                #print(nums[l], nums[m], nums[r])
        return min_val