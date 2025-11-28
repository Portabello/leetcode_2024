'''
209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0



Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        sum=nums[0]
        if sum>=target:
            return 1
        min_size = float(inf)
        while r<len(nums):
            #print(l,r)
            sum =0
            for i in range(l,r+1):
                sum+=nums[i]
            #print('sum:',sum)
            if sum>=target:
                #print('found!', r-l+1)
                min_size = min(min_size, r-l+1)
            if sum<target:
                r+=1
            else:
                l+=1
        if min_size == float(inf):
            return 0
        return min_size
