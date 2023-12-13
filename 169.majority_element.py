class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictn = {}
        for n in nums:
            if n not in dictn:
                dictn[n] = 1
            else:
                dictn[n] += 1
        for element in dictn:
            if dictn[element] > (len(nums)/2):
                return element