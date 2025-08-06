class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i,num in enumerate(nums):
            if target-num in hs:
                return [hs[target-num],i]
            hs[num] = i
