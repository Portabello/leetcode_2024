"""
1763. Longest Nice Substring
Solved
Easy
Topics
Companies
Hint
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        #test every substring
        s_len = 1
        longest_string = ""
        longest_len = -1
        def is_nice(s):
            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for c in s:
                #if lower
                if c in lower:
                    if c.upper() not in s:
                        return False
                #if upper
                if c in upper:
                    if c.lower() not in s:
                        return False
            return True

        while s_len <= len(s):
            for i in range(len(s)-s_len+1):
                #print(s[i:i+s_len])
                t = s[i:i+s_len]
                if is_nice(t):
                    if len(t) > longest_len:
                        longest_len = len(t)
                        longest_string = t
            s_len += 1
        return longest_string