'''
90. Subsets II
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums that may contain duplicates, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]



Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        def recurse(cur, arr):
            if len(arr)==0:
                cur.sort()
                if cur not in ans:
                    ans.append(cur)
                return
            recurse(cur, arr[1:])
            recurse(cur+[arr[0]], arr[1:])
        recurse([], nums)
        return ans
