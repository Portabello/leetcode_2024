'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sum = ""
        carry = 0
        while num1 or num2:
            if len(num1) == 0 and len(num2) != 0:
                t=str(int(num2[-1])+ carry)
                carry = 0
                if int(t)>=10:
                    carry = 1
                    t = str(int(t)-10)
                sum = t + sum
                num2=num2[:-1]
            elif len(num2) == 0 and len(num1) != 0:
                t=str(int(num1[-1])+ carry)
                carry = 0
                if int(t)>=10:
                    carry = 1
                    t = str(int(t)-10)
                sum = t + sum
                num1=num1[:-1]
            else:
                t=str(int(num1[-1])+int(num2[-1])+ carry)
                carry = 0
                if int(t)>=10:
                    carry = 1
                    t = str(int(t)-10)
                sum = t + sum
                num1=num1[:-1]
                num2=num2[:-1]
        print(sum)
        if carry == 1:
            return "1"+sum
        return sum
