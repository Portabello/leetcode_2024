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
        maxAverage = None
        tsum = None
        for i in range(0,len(nums)-k+1):
            if tsum == None:
                tsum = sum(nums[0:k])
            else:
                tsum -= nums[i-1]
                tsum += nums[i+k-1]
                #print('removing ', nums[i-1], 'adding ',nums[i+k-1])
            #print(tsum)

            taverage = tsum/k
            if maxAverage == None or taverage > maxAverage:
                maxAverage = taverage
        return maxAverage