'''
844. Backspace String Compare
Solved
Easy
Topics
Companies
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        print(self.text_in_editor(s))
        print(self.text_in_editor(t))
        if self.text_in_editor(s) == self.text_in_editor(t):
            return True
        return False

    def text_in_editor(self, s):
        ans = ""
        for c in s:
            if c=='#' and len(ans)!= 0:
                ans = ans[:-1]
            elif c=='#' and len(ans)==0:
                continue
            else:
                ans = ans + c
        return ans
