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
        l,r = 0,0
        min_subarray_len = None
        cur_sum = 0
        while l < len(nums):
            #print(l,r,nums[l:r], sum(nums[l:r]), '?=', cur_sum)
            #cur_sum = sum(nums[l:r])
            if cur_sum < target:
                if r >= len(nums):
                    cur_sum -= nums[l]
                    l+=1

                else:

                    r += 1
                    if r <= len(nums):
                        cur_sum += nums[r-1]
            else:
                if min_subarray_len == None or r-l < min_subarray_len:
                    #print('updating : ', l,r,r-l)
                    min_subarray_len = r-l
                cur_sum -= nums[l]
                l += 1
        return 0 if not min_subarray_len else min_subarray_len
