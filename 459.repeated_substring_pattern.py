"""
459. Repeated Substring Pattern
Solved
Easy
Topics
Companies
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len = len(s)
        sub = ""
        sub_l = 0
        for c in s:
            sub = sub+c
            sub_l += 1
            if sub_l*2 > s_len:
                return False
            multiply_length = int(s_len/sub_l)
            if sub*multiply_length == s:
                return True
        return False