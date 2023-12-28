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
        b_x = str(bin(x)[2:])
        b_y = str(bin(y)[2:])
        if(len(b_x) > len(b_y)):
            pad_l = len(b_x) - len(b_y) 
            b_y = pad_l*"0" + str(b_y)
        elif(len(b_y) > len(b_x)):
            pad_l = len(b_y) - len(b_x) 
            b_x = pad_l*"0" + str(b_x)
        hamming_distance = 0
        for i,c in enumerate(b_x):
            if c != b_y[i]:
                hamming_distance += 1
        return hamming_distance

