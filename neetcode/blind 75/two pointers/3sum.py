class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = i
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0-(nums[i]+nums[j]) in counter:
                    k=counter[0-(nums[i]+nums[j])]
                    if i!=j and i!=k and j!=k:
                        t = [nums[i],nums[j],nums[k]]
                        t.sort()
                        if t not in ans:
                            ans.append(t)
        return ans
