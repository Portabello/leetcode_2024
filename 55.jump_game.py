'''
55. Jump Game
Solved
Medium
Topics
Companies

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105

'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = [False for _ in range(len(nums))]
        t[-1] = True
        for i in range(len(nums)-1, -1, -1):
            for y in range(i+1, min(len(nums), i+nums[i]+1)):
                if t[y]==True:
                    t[i]=True
                    break
        if t[0]==True:
            return True
        return False
