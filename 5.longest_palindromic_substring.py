'''
5. Longest Palindromic Substring
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, return the longest

in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(l,r):
            while l>=0 and r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            return r-l-1

        start, end = 0,0

        for i in range(len(s)):
            odd = expand_around_center(i,i)
            even = expand_around_center(i,i+1)
            maxlen = max(odd,even)

            if maxlen > end-start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2

        return s[start:end+1]
