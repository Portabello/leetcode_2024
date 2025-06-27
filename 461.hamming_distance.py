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
        x,y = bin(x)[2:], bin(y)[2:]
        def pad_zeros(x,y):
            maxlen = max(len(x), len(y))
            if len(x)!=maxlen:
                x = (maxlen-len(x))*'0' + x
            else:
                y = (maxlen-len(y))*'0' + y
            return x,y
        x,y = pad_zeros(x,y)
        hamming_distance = 0
        for i in range(len(x)):
            if x[i]!=y[i]:
                hamming_distance += 1
        return hamming_distance
