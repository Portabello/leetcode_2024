"""
387. First Unique Character in a String
Easy
8.4K
270
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        tally = {}
        for c in s:
            if c in tally:
                tally[c] += 1
            else:
                tally[c] = 1
        for x in tally:
            if tally[x] == 1:
                return s.index(x)
        return -1
