'''
643. Maximum Average Subarray I
Solved
Easy
Topics
Companies

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000



Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104

'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_avg = None
        max_avg = None
        for i in range(len(nums)-k+1):
            #print(nums[i:i+k])
            if cur_avg == None:
                cur_avg = sum(nums[i:i+k])/k
                max_avg = cur_avg
                #print('init to ', cur_avg)
            else:
                cur_avg = ((cur_avg*k)-nums[i-1]+nums[i+k-1])/k
                #print('removing ', nums[i-1], '  adding: ', nums[i+k-1])
                max_avg = max(max_avg, cur_avg)
        return max_avg
