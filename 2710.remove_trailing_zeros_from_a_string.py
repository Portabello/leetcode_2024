'''
2710. Remove Trailing Zeros From a String
Solved
Easy
Topics
Companies
Hint

Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.



Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".



Constraints:

    1 <= num.length <= 1000
    num consists of only digits.
    num doesn't have any leading zeros.

'''
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        trailing = 0
        for i in range(len(num)-1,-1,-1):
            if num[i]=='0':
                trailing += 1
            else:
                break
        num = num[:len(num)-trailing]
        return num
