'''
2937. Make Three Strings Equal
Solved
Easy
Topics
Companies
Hint

You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string.

Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal, return -1.



Example 1:

Input: s1 = "abc", s2 = "abb", s3 = "ab"

Output: 2

Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

Example 2:

Input: s1 = "dac", s2 = "bac", s3 = "cac"

Output: -1

Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.



Constraints:

    1 <= s1.length, s2.length, s3.length <= 100
    s1, s2 and s3 consist only of lowercase English letters.

'''
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_len = min(len(s1), len(s2), len(s3))
        for i in range(min_len, 0, -1):
            sub1, sub2, sub3 = s1[:i], s2[:i], s3[:i]
            if sub1 == sub2 and sub1 == sub3 and sub2 == sub3:
                return (len(s1) - i) + (len(s2) - i) + (len(s3) - i)
        return -1
