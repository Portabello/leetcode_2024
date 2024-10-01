'''
43. Multiply Strings
Solved
Medium
Topics
Companies

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"



Constraints:

    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.

'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'


        t1 = 0
        for x in num1:
            t1 = t1*10 + (ord(x)-ord('0'))

        t2 = 0
        for x in num2:
            t2 = t2*10 + (ord(x)-ord('0'))
        #print(t1,' : ',t2)

        ans = ""
        for x in str(t1*t2):
            ans = ans + x

        return ans
