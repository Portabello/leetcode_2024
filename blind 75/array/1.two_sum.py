class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            if target-x in nums and nums.index(target-x)!=i:
                return [i,nums.index(target-x)]
#hash solu tion
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,x in enumerate(nums):
            if target-x in hashmap:
                return [i,hashmap[target-x]]
            hashmap[x] = i
