'''
504. Base 7
Solved
Easy
Topics
Companies
Given an integer num, return a string of its base 7 representation.



Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"


Constraints:

-107 <= num <= 107
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        neg = False
        if num == 0:
            return '0'
        if num < 0:
            neg = True
            num = abs(num)
        while num != 0:
            ans = str(num%7) + ans
            num = int(num/7)
        if neg:
            return '-'+ans
        return ans
