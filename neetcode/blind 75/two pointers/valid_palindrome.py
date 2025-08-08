class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_format = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                s_format = s_format + c.lower()
        return s_format == s_format[::-1]
