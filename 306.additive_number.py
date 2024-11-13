'''
306. Additive Number
Solved
Medium
Topics
Companies

An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation:
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:

Input: "199100199"
Output: true
Explanation:
The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199



Constraints:

    1 <= num.length <= 35
    num consists only of digits.



Follow up: How would you handle overflow for very large input integers?
'''
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def validNumber(x: str):
            if len(x) == 1:
                return True
            if x[0] == '0':
                return False
            return True


        res = [0]
        def rc(x,y,num):
            if len(num) == 0:
                res[0] = 1
                return
            #if num[0] == '0':
            #    return
            #if not validNumber(num):
                #return
            for i in range(1, len(num)+1):
                cur_sum = x + y
                z = int(num[0:i])
                #print('is ', x, ' + ', y, ' = ', z)
                if cur_sum == z and validNumber(num[0:i]):
                    rc(y,z,num[i:])





        for x in range(1,len(num)-1):
            for y in range(x+1,len(num)):
                #print(num[0:x], num[x:y], num[y:])
                if validNumber(num[0:x]) and validNumber(num[x:y]):
                    #print('valid found')
                    rc(int(num[0:x]), int(num[x:y]), num[y:])
                #else:
                    #print('leading zero found')
        if res[0] == 1:
            return True
        return False
