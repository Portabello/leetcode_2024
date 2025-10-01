'''
47. Permutations II
Solved
Medium
Topics
premium lock iconCompanies

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



Constraints:

    1 <= nums.length <= 8
    -10 <= nums[i] <= 10

'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        def recurse(cur_permutation, remaining_nums):
            if not remaining_nums:
                if cur_permutation not in all_permutations:
                    all_permutations.append(cur_permutation)
                return
            for i,num in enumerate(remaining_nums):
                recurse(cur_permutation+[num], remaining_nums[:i]+remaining_nums[i+1:])
        recurse([], nums)
        return all_permutations
