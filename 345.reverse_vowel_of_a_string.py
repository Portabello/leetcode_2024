"""
345. Reverse Vowels of a String
Easy
4.2K
2.7K
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        t = []
        s = list(s)
        for x in s:
            if x in vowels:
                t.append(x)
        for i,x in enumerate(s):
            if x in vowels:
                s[i] = t.pop()
        return "".join(s)
