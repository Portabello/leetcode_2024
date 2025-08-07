class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)
        starter = []
        for x in nums:
            if x-1 not in counter:
                starter.append(x)
        ans = 0
        for x in starter:
            sequence_length = 1
            sequence = x
            while sequence+1 in counter:
                sequence_length += 1
                sequence += 1
            ans = max(ans, sequence_length)
        return ans
