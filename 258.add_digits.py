"""
258. Add Digits
Easy
4.6K
1.9K
Companies
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 231 - 1

 """
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            t = 0
            for x in str(num):
                t += int(x)
            num = t
        return num
