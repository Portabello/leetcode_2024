'''
875. Koko Eating Bananas
Solved
Medium
Topics
Companies

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23



Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValid(piles, h, k):
            t = 0
            for x in piles:
                if x<=k:
                    t+=1
                elif x%k==0:
                    t+=int(x/k)
                else:
                    t+=(1+int(x/k))
            return t<=h

        ans = max(piles)
        l,r = 1,ans
        while l<=r:
            m=(l+r)//2
            valid = isValid(piles, h, m)
            if valid:
                ans = min(ans,m)
                r=m-1
            else:
                l=m+1
        return ans
