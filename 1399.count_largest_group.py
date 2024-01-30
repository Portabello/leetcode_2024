"""
1399. Count Largest Group
Solved
Easy
Topics
Companies
Hint
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
"""
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for x in range(n):
            if len(str(x+1)) == 1:
                if x+1 in dic:
                    dic[x+1]+=1
                else:
                    dic[x+1]=1
            else:
                t = 0
                for y in str(x+1):
                    t+= int(y)
                if t in dic:
                    dic[t] += 1
                else:
                    dic[t] = 1
        max_sum = 0
        max_count = 0
        for x in dic:
            if dic[x]>max_sum:
                max_sum = dic[x]
                max_count = 1
            elif dic[x]==max_sum:
                max_count += 1
        return max_count
