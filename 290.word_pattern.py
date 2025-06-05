"""
290. Word Pattern
Easy
7K
907
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        pattern = list(pattern)
        #print(s,pattern)
        if len(s) != len(pattern):
            return False
        hs = {}
        for i in range(len(pattern)):
            #print(s[i],pattern[i])
            if pattern[i] in hs:
                if hs[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in hs.values():
                    return False
                else:
                    hs[pattern[i]] = s[i]
        return True
