"""
1784. Check if Binary String Has at Most One Segment of Ones
Solved
Easy
Topics
Companies
Hint
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
"""
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        first_seg = -1
        for c in s:
            if c == "1" and first_seg == -1:
                first_seg = 0
            elif c == "0" and first_seg == 0:
                first_seg = 1
            elif c == "1" and first_seg == 1:
                return False
        return True
