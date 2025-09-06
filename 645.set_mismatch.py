'''
645. Set Mismatch
Solved
Easy
Topics
Companies
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hs = Counter(nums)
        ans = [0,0]
        for x in range(1,len(nums)+1):
            if x not in hs:
                ans[1]=x
            else:
                if hs[x]==2:
                    ans[0]=x
        return ans
