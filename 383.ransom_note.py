"""
383. Ransom Note
Easy
4.7K
482
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hs = {}
        for x in magazine:
            if x not in hs:
                hs[x] = 1
            else:
                hs[x] += 1
        for x in ransomNote:
            if x in hs:
                if hs[x] == 0:
                    return False
                else:
                    hs[x] -= 1
            else:
                return False
        return True
