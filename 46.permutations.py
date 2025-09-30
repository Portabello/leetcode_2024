'''
46. Permutations
Solved
Medium
Topics
premium lock iconCompanies

Given an array nums of distinct integers, return all the possible

. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]



Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        def recurse(cur_permutation, remaining_nums):
            if not remaining_nums:
                all_permutations.append(cur_permutation)
                return
            for i,num in enumerate(remaining_nums):
                recurse(cur_permutation+[num], remaining_nums[:i]+remaining_nums[i+1:])
        recurse([], nums)
        return all_permutations
