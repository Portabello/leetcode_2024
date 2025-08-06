class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for x in counter.values():
            if x>1:
                return True
        return False
