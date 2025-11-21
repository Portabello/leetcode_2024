'''
179. Largest Number
Attempted
Medium
Topics
premium lock iconCompanies

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 109

'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_num = [0]
        def recurse(cur, nums):
            if len(nums)==0:
                max_num[0] = max(max_num[0], int(cur))
            for i,x in enumerate(nums):
                recurse(cur+str(x), nums[:i]+nums[i+1:])
        recurse("", nums)
        return str(max_num[0])
