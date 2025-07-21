"""
242. Valid Anagram
Easy
11.6K
365
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        for c in t:
            if c not in s_counter:
                return False
            if s_counter[c]==1:
                del s_counter[c]
            else:
                s_counter[c]-=1
        if len(s_counter)==0:
            return True
        return False
