"""
7. Reverse Integer
Medium
12.2K
13.2K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1


"""
class Solution:
    def reverse(self, x: int) -> int:
        negative = 1 if x<0 else 0
        x_reverse = str(abs(x))[::-1]
        if int(x_reverse) > (2**31)-1 or int(x_reverse) < (-2**31):
            return 0
        if negative:
            return int(x_reverse)*-1
        return int(x_reverse)
            return int(answer)* -1
