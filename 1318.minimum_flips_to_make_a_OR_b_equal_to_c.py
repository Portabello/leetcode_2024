'''
1318. Minimum Flips to Make a OR b Equal to c
Solved
Medium
Topics
Companies
Hint

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.



Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:

Input: a = 4, b = 2, c = 7
Output: 1

Example 3:

Input: a = 1, b = 2, c = 3
Output: 0



Constraints:

    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        # fill shorter binary representation with leading 0's
        maxlen = max(len(a), len(b), len(c))
        a = '0'*(maxlen - len(a)) + a
        b = '0'*(maxlen - len(b)) + b
        c = '0'*(maxlen - len(c)) + c

        a = list(a)
        b = list(b)
        c = list(c)

        flips = 0

        for i in range(len(a)):
            # if we need to flip bit
            if (int(a[i]) | int(b[i])) != int(c[i]):
                # if c == 0 make both a and b zero
                if c[i] == '0':
                    if a[i]=='1':
                        flips += 1
                    if b[i] == '1':
                        flips += 1
                # if c == 1 make at least 1 a or b == 1
                else:
                    flips += 1

        return flips
