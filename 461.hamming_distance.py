"""
461. Hamming Distance
Easy
3.8K
216
Companies
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1


Constraints:

0 <= x, y <= 231 - 1
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_b,y_b = bin(x)[2:], bin(y)[2:]
        def pad_zeros(x,y):
            xlen,ylen = len(x),len(y)
            maxlen = max(xlen,ylen)
            if xlen!=maxlen:
                pad = maxlen-xlen
                x = pad*'0' + x
            if ylen!=maxlen:
                pad = maxlen-ylen
                y = pad*'0' + y
            return x,y
        x_b,y_b = pad_zeros(x_b,y_b)
        hamming_distance = 0
        for i in range(len(x_b)):
            if x_b[i] != y_b[i]:
                hamming_distance += 1
        return hamming_distance
