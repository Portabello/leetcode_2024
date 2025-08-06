class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        bucket = [[] for x in range(len(nums))]
        for x in num_counter:
            bucket[num_counter[x]-1].append(x)
        ans = []
        k_left = k
        for i in range(len(bucket)-1,-1,-1):
            for x in bucket[i]:
                ans.append(x)
                k_left -=1
                if k_left == 0:
                    return ans
