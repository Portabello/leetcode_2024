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
        hs = {}
        s = s.split(" ")
        #print(s)
        if len(s) != len(pattern):
            return False
        def existsInHash(x):
            for value in hs.values():
                if x == value:
                    return True
            return False

        for i,x in enumerate(list(pattern)):
            #print(hs)
            if x not in hs and existsInHash(s[i]):
                return False
            if x in hs and hs[x] != s[i]:
                return False
            hs[x] = s[i]
        return True
