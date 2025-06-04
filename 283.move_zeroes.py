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
        def movezero(i,n):
            #print('moving zero@', i, 'to', n)
            #print('before')
            #print(nums)
            for x in range(i,n):
                #print()
                t = nums[x+1]
                nums[x+1] = nums[x]
                nums[x] = t
            #print('after')
            #print(nums)
            #print('........')

        n = len(nums)-1
        while True:
            zerofound = False
            #print('exploring 0 to',n, nums)
            for i in range(0,n):
                if nums[i]==0:
                    zerofound = True
                    #print('found @', i, nums[i])
                    movezero(i,n)
                    n -= 1
                    break
            if zerofound == False:
                #print('exiting')
                break
