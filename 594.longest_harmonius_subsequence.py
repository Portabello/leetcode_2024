'''
594. Longest Harmonious Subsequence
Easy
Topics
Companies
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            t_len_up = 0
            up_valid = False
            t_len_down = 0
            down_valid = False
            for y in nums:
                if y==x or y==x+1:
                    #print(x, ':', y)
                    if y==x+1:
                        up_valid = True
                    t_len_up += 1
                if y==x or y==x-1:
                    if y==x-1:
                        down_valid = True
                    t_len_down += 1
            #print('final: ', t_len)
            #print(x, t_len)
            if up_valid:
                ans = max(t_len_up, ans)
            if down_valid:
                ans = max(t_len_down, ans)
            #ans = max(t_len_up, t_len_down, ans)
            t_len_up = 0
            t_len_down = 0

        return ans
