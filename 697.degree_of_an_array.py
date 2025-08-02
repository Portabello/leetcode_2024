'''
697. Degree of an Array
Solved
Easy
Topics
Companies
Hint
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.



Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.


Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        num_with_max_degree = []
        hs = Counter(nums)
        for x in hs:
            if hs[x] == degree:
                num_with_max_degree.append(x)
            if hs[x] > degree:
                num_with_max_degree = [x]
                degree = hs[x]

        #print(degree, num_with_max_degree)
        subarray_len = len(nums)
        for x in num_with_max_degree:
            first, last = None, None
            for i,y in enumerate(nums):
                if y == x:
                    if first == None:
                        first = i
                    last = i
            #print('first at ',first,' last at ', last)
            subarray_len = min(last-first+1, subarray_len)
        return subarray_len
