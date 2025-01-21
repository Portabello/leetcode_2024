'''
3174. Clear Digits
Solved
Easy
Topics
Companies
Hint

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.



Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".



Constraints:

    1 <= s.length <= 100
    s consists only of lowercase English letters and digits.
    The input is generated such that it is possible to delete all digits.

'''
class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        while True:
            found = False
            digit = None
            char = None
            for i,c in enumerate(s):
                if c.isdigit():
                    found = True
                    digit = i
                    print('found digit ', c, ' at ', i)
                    for y in range(i-1, -1, -1):
                        print('to left ', y, s[y])
                        if s[y].isalpha():
                            char = y
                            break
                    break

            #delete now
            if found:
                s.pop(digit)
                s.pop(char)
            else:
                break
        return ''.join(s)
