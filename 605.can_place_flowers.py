'''
605. Can Place Flowers
Solved
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        consecutive_zeros = 0
        for i,x in enumerate(flowerbed):
            # edge case len==1 flowerbed
            if len(flowerbed)==1:
                if n==0:
                    return True
                if x==0 and n==1:
                    return True
                return False
            #edge case i==0 or i==len(flowerbed)
            if x==0:
                if i==0:
                    #print('edge start')
                    if flowerbed[i+1] == 0:
                        n-=1
                        flowerbed[i] = 1
                elif i==len(flowerbed)-1:
                    #print('edge end')
                    if flowerbed[i-1] == 0:
                        n-=1
                        flowerbed[i] = 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
        if n<=0:
            return True
        return False
