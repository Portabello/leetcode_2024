'''
704. Binary Search
Solved
Easy
Topics
Companies
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print('sss')
        ans =  self.binary_search(nums, target, nums)
        print(ans)
        return ans
    def binary_search(self, nums, target, og):
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                print('found1')
                return og.index(target)
            print('notfound')
            return -1
        if len(nums)==2:
            mid = nums[1]
        else:
            mid = nums[int(len(nums)/2)]

        if mid == target:
            print('found')
            return og.index(mid)
        elif mid>target:
            #go left
            print('mid:', mid, 'going left: ', nums[:int(len(nums)/2)])
            return self.binary_search(nums[:int(len(nums)/2)], target, og)
        else:
            #go right
            print('mid:', mid, 'going right: ', nums[int(len(nums)/2)+1:])
            return self.binary_search(nums[int(len(nums)/2)+1:], target, og)
