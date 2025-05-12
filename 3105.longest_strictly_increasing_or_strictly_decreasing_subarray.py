'''
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Solved
Easy
Topics
Companies

You are given an array of integers nums. Return the length of the longest
subarray
of nums which is either
strictly increasing
or
strictly decreasing
.



Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.


Constraints:

    1 <= nums.length <= 50
    1 <= nums[i] <= 50

'''
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        largest_increasing = 0
        increasing = 0
        last = None
        for x in nums:
            if last == None:
                last = x
                increasing = 1
            elif x > last:
                increasing += 1
                last = x
            elif x <= last:
                increasing = 1
                last = x
            largest_increasing = max(increasing, largest_increasing)
        #print(largest_increasing)

        largest_decreasing = 0
        decreasing = 0
        last = None
        for x in nums:
            if last == None:
                last = x
                decreasing = 1
            elif x < last:
                decreasing += 1
                last = x
            elif x >= last:
                decreasing = 1
                last = x
            largest_decreasing = max(decreasing, largest_decreasing)
        #print(largest_decreasing)
        return max(largest_decreasing, largest_increasing)
