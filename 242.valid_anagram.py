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
        hash_table = {}
        for x in s:
            if x in hash_table:
                hash_table[x] += 1
            else:
                hash_table[x] = 1
        
        for x in t:
            if x not in hash_table:
                return False
            if x in hash_table:
                if hash_table[x] == 1:
                    del(hash_table[x])
                else:
                    hash_table[x] -= 1
        if(len(hash_table) != 0):
            return False
        return True
