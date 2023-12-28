"""
205. Isomorphic Strings
Easy
7.9K
1.9K
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictc = {}
        for i,x in enumerate(s):
            dictc[s[i]] = t[i]
        check_ans = ""
        for x in s:
            check_ans += dictc[x]
        print(check_ans)
        check_duplicate = []
        for key in dictc:
            if dictc[key] in check_duplicate:
                return False
            check_duplicate.append(dictc[key])
        if check_ans == t:
            return True
        return False