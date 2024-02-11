"""
1556. Thousand Separator
Solved
Easy
Topics
Companies
Hint
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1
"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        r_n = str(n)[::-1]
        print(r_n)
        count = 0
        ans = ""
        for i,c in enumerate(r_n):
            ans = ans + c
            count += 1
            if count == 3 and i != len(r_n)-1:
                count = 0
                ans  = ans + "."
        return ans[::-1]