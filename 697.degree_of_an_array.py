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
        degree = {}
        max_degree_count = 0
        max_degree = None
        for x in nums:
            if x in degree:
                degree[x]+=1
            else:
                degree[x]=1
            if degree[x]>max_degree_count:
                    max_degree_count = degree[x]
                    max_degree = x
        #print(degree)
        #print(max_degree, ' : ', max_degree_count)
        if max_degree_count == 1:
            return 1


        #check for other max_degrees
        all_max_degree = []
        for x in degree:
            if degree[x] == max_degree_count:
                all_max_degree.append(x)
        #print(all_max_degree)
        min_subarray = None
        for d in all_max_degree:
            first_index = None
            last_index = None
            for i,x in enumerate(nums):
                if x == d and first_index == None:
                    first_index = i
                elif x == d and first_index != None:
                    last_index = i
            if min_subarray == None:
                min_subarray = last_index - first_index + 1
            else:
                min_subarray = min(min_subarray, (last_index - first_index + 1))

            #print(d, 'firstindex', first_index)
            #print(d, 'lastindex', last_index)
        return min_subarray
